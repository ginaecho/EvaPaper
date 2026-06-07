#!/usr/bin/env python3
"""
Parse the local paper report into a structured corpus for retrieval.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, List, Optional
from workspace_config import DEFAULT_WORKSPACE


ROOT = DEFAULT_WORKSPACE.root
DEFAULT_REPORT = DEFAULT_WORKSPACE.report_md
DEFAULT_INDEX = DEFAULT_WORKSPACE.corpus_index
DEFAULT_SCOUT_LOG = DEFAULT_WORKSPACE.scout_log


FIELD_HEADERS = {
    "Abstract": "abstract",
    "Abstract/Summary": "abstract",
    "Why I recommend this paper": "why_recommend",
    "Why I recommend this": "why_recommend",
    "Relevance to our topic": "relevance",
    "Recommendation reason": "recommendation_reason",
}

FOCUS_DIMENSIONS = ("static", "runtime", "behavioral", "landscape")

FOCUS_KEYWORDS = {
    "static": [
        "skill markdown", "specification", "schema", "validation", "validator", "contract",
        "contractual", "static", "declarative", "well-formed", "format", "lint", "compile",
        "pre-execution", "permissions", "boundaries", "approval points", "manifest",
    ],
    "runtime": [
        "runtime", "sandbox", "intent verification", "audit logging", "execution-layer",
        "policy enforcement", "authorization", "mcp", "threat taxonomy", "infrastructure",
        "agent execution", "tool invocation",
    ],
    "behavioral": [
        "benchmark", "evaluation", "trustworthiness", "behavioral safety", "task completion",
        "real-world tasks", "red teaming", "policy adherence", "agent behavior", "safely",
    ],
    "landscape": [
        "taxonomy", "framework", "state of the art", "industry standard", "comprehensive",
        "full lifecycle", "all three layers", "risk taxonomy", "governance stack",
    ],
}

FOCUS_OVERRIDES = {
    "Skilldex": {"static": 10, "runtime": 2, "behavioral": 0, "landscape": 1},
    "GovernSpec / Contractual Skills": {"static": 10, "runtime": 4, "behavioral": 1, "landscape": 2},
    "OWASP Top 10 for Agentic Skills (AST10)": {"static": 9, "runtime": 3, "behavioral": 0, "landscape": 3},
    "Layered Governance Architecture (LGA)": {"static": 1, "runtime": 10, "behavioral": 2, "landscape": 2},
    "IBM Sovereign Core — Governance Policy at Infrastructure Runtime": {"static": 0, "runtime": 10, "behavioral": 0, "landscape": 2},
    "Tencent AI-Infra-Guard — Full-Stack AI Red Teaming Platform": {"static": 4, "runtime": 8, "behavioral": 6, "landscape": 3},
    "BeSafe-Bench (BSB)": {"static": 0, "runtime": 1, "behavioral": 10, "landscape": 1},
    "ST-WebAgentBench": {"static": 4, "runtime": 2, "behavioral": 9, "landscape": 2},
    "ClawBench — Real-World Web Agent Benchmark": {"static": 0, "runtime": 1, "behavioral": 10, "landscape": 1},
    "Agent Evaluation Guide (Quality-Focused Frameworks)": {"static": 0, "runtime": 2, "behavioral": 8, "landscape": 5},
    "OWASP Top 10 for Agentic Applications": {"static": 3, "runtime": 6, "behavioral": 5, "landscape": 8},
    "Microsoft Agent Governance Toolkit": {"static": 4, "runtime": 7, "behavioral": 5, "landscape": 8},
    "MCP-38 — Comprehensive Threat Taxonomy for Model Context Protocol": {"static": 0, "runtime": 9, "behavioral": 1, "landscape": 4},
    "SkCC": {"static": 9, "runtime": 4, "behavioral": 1, "landscape": 2},
    "Trace-Based Assurance Framework": {"static": 8, "runtime": 6, "behavioral": 3, "landscape": 2},
    "SentinelAgent": {"static": 7, "runtime": 7, "behavioral": 1, "landscape": 2},
    "Evidence-Synthesis Framework": {"static": 6, "runtime": 4, "behavioral": 6, "landscape": 4},
    "LASM / Systematic Survey": {"static": 4, "runtime": 5, "behavioral": 4, "landscape": 9},
    "AIP / Agent Identity Protocol": {"static": 3, "runtime": 8, "behavioral": 1, "landscape": 2},
    "Auditable Agents": {"static": 5, "runtime": 7, "behavioral": 3, "landscape": 3},
    "GitHub Spec Kit / SDD (Specification-Driven Development)": {"static": 8, "runtime": 0, "behavioral": 0, "landscape": 4},
    "Web Skills Protocol (WSP)": {"static": 7, "runtime": 3, "behavioral": 0, "landscape": 3},
}


@dataclass
class Passage:
    field: str
    text: str


@dataclass
class PaperRecord:
    ordinal: int
    title: str
    url: Optional[str] = None
    pdf: Optional[str] = None
    paper_type: Optional[str] = None
    authors: Optional[str] = None
    date: Optional[str] = None
    layer: Optional[str] = None
    solution: Optional[str] = None
    focus_scores: Dict[str, int] = field(default_factory=dict)
    primary_focus: Optional[str] = None
    secondary_focuses: List[str] = field(default_factory=list)
    fields: Dict[str, str] = field(default_factory=dict)
    passages: List[Passage] = field(default_factory=list)

    def to_dict(self) -> dict:
        payload = asdict(self)
        payload["passages"] = [asdict(passage) for passage in self.passages]
        return payload


def _clean_text(text: str) -> str:
    lines = [line.strip() for line in text.strip().splitlines()]
    cleaned = []
    for line in lines:
        if line.startswith(">"):
            line = line[1:].strip()
        cleaned.append(line)
    return "\n".join(line for line in cleaned if line).strip()


def _parse_metadata_line(line: str, record: PaperRecord) -> None:
    metadata_match = re.match(r"- \*\*(.+?):\*\* (.+)", line)
    if not metadata_match:
        return
    key = metadata_match.group(1).strip()
    value = metadata_match.group(2).strip()
    mapping = {
        "URL": "url",
        "PDF": "pdf",
        "Type": "paper_type",
        "Authors": "authors",
        "Date": "date",
    }
    if key in mapping:
        setattr(record, mapping[key], value)


def _infer_focus_profile(record: PaperRecord) -> None:
    override = FOCUS_OVERRIDES.get(record.title)
    if override:
        record.focus_scores = dict(override)
    else:
        text = "\n".join(
            [
                record.title,
                record.layer or "",
                record.solution or "",
                record.fields.get("abstract", ""),
                record.fields.get("relevance", ""),
                record.fields.get("why_recommend", ""),
                record.fields.get("recommendation_reason", ""),
            ]
        ).lower()
        scores = {dimension: 0 for dimension in FOCUS_DIMENSIONS}
        for dimension, keywords in FOCUS_KEYWORDS.items():
            for keyword in keywords:
                if keyword in text:
                    scores[dimension] += 1
        record.focus_scores = scores

    ranked = sorted(record.focus_scores.items(), key=lambda item: (-item[1], item[0]))
    record.primary_focus = ranked[0][0] if ranked and ranked[0][1] > 0 else "landscape"
    record.secondary_focuses = [name for name, score in ranked[1:] if score > 0]


def parse_report(report_path: Path = DEFAULT_REPORT) -> List[PaperRecord]:
    content = report_path.read_text(encoding="utf-8")
    paper_section_match = re.search(
        r"## Papers & Products\n(.*?)(?=\n## The Three-Layer Stack in Detail)",
        content,
        re.DOTALL,
    )
    if not paper_section_match:
        return []
    section = paper_section_match.group(1).strip()

    entries = re.split(r"\n---\n+", section)
    records: List[PaperRecord] = []

    for entry in entries:
        entry = entry.strip()
        if not entry.startswith("### "):
            continue
        lines = entry.splitlines()
        header = lines[0]
        title_match = re.match(r"### (\d+)\. (.+)", header)
        if not title_match:
            continue

        record = PaperRecord(ordinal=int(title_match.group(1)), title=title_match.group(2).strip())
        current_field: Optional[str] = None
        field_buffer: List[str] = []

        def flush_field() -> None:
            nonlocal current_field, field_buffer
            if not current_field:
                return
            text = _clean_text("\n".join(field_buffer))
            if text:
                record.fields[current_field] = text
                record.passages.append(Passage(field=current_field, text=text))
            current_field = None
            field_buffer = []

        for raw_line in lines[1:]:
            line = raw_line.rstrip()
            if line.startswith("- **"):
                flush_field()
                _parse_metadata_line(line, record)
                continue

            inline_field = re.match(r"\*\*(.+?):\*\* (.+)", line)
            if inline_field:
                flush_field()
                label = inline_field.group(1).strip()
                value = inline_field.group(2).strip()
                if label == "Which layer":
                    record.layer = value
                elif label == "Is it a solution we're looking into?":
                    record.solution = value
                elif label in FIELD_HEADERS:
                    field_name = FIELD_HEADERS[label]
                    record.fields[field_name] = value
                    record.passages.append(Passage(field=field_name, text=value))
                continue

            block_field = re.match(r"\*\*(.+?):\*\*", line)
            if block_field:
                flush_field()
                label = block_field.group(1).strip()
                if label in FIELD_HEADERS:
                    current_field = FIELD_HEADERS[label]
                    field_buffer = []
                continue

            if current_field:
                field_buffer.append(line)

        flush_field()

        summary_bits = [record.title]
        for field_name in ("abstract", "relevance", "why_recommend", "recommendation_reason"):
            if record.fields.get(field_name):
                summary_bits.append(record.fields[field_name])
        if record.layer:
            summary_bits.append(record.layer)
        if record.solution:
            summary_bits.append(record.solution)
        record.passages.insert(0, Passage(field="paper_summary", text="\n".join(summary_bits)))
        _infer_focus_profile(record)
        records.append(record)

    return records


def _canonical_title(raw_title: str) -> str:
    title = raw_title.strip()
    title = re.sub(r"\s*\(arXiv:[^)]+\)", "", title).strip()
    return title


def parse_scout_log(log_path: Path = DEFAULT_SCOUT_LOG, starting_ordinal: int = 1000) -> List[PaperRecord]:
    if not log_path.exists():
        return []
    content = log_path.read_text(encoding="utf-8")
    records: List[PaperRecord] = []
    ordinal = starting_ordinal

    pattern = re.compile(
        r"^\d+\.\s+\*\*(?P<title>.+?)\*\*(?:\s+\(arXiv:(?P<arxiv>[0-9.]+)\))?\s+—\s+(?P<body>.+)$",
        re.MULTILINE,
    )

    for match in pattern.finditer(content):
        raw_title = match.group("title").strip()
        title = _canonical_title(raw_title)
        body = match.group("body").strip()
        arxiv_id = match.group("arxiv")

        url_match = re.search(r"URL:\s*(https?://\S+)", body)
        url = url_match.group(1).rstrip(" .") if url_match else (f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else None)

        layer_match = re.search(r"—\s+\*\*(Layer[^*]+)\*\*", body)
        layer = layer_match.group(1).strip() if layer_match else None

        abstract = body
        if "URL:" in abstract:
            abstract = abstract.split("URL:", 1)[0].strip()
        if layer_match:
            abstract = abstract[: layer_match.start()].strip()

        relevance = ""
        if layer_match:
            remainder = body[layer_match.end() :].strip(" —")
            relevance = remainder

        record = PaperRecord(
            ordinal=ordinal,
            title=title,
            url=url,
            authors=None,
            date=None,
            layer=layer,
            solution="Yes" if relevance else None,
        )
        if abstract:
            record.fields["abstract"] = abstract
            record.passages.append(Passage(field="abstract", text=_clean_text(abstract)))
        if relevance:
            record.fields["relevance"] = relevance
            record.passages.append(Passage(field="relevance", text=_clean_text(relevance)))

        summary_bits = [record.title]
        if abstract:
            summary_bits.append(_clean_text(abstract))
        if relevance:
            summary_bits.append(_clean_text(relevance))
        if record.layer:
            summary_bits.append(record.layer)
        record.passages.insert(0, Passage(field="paper_summary", text="\n".join(summary_bits)))
        _infer_focus_profile(record)
        records.append(record)
        ordinal += 1

    return records


def build_index(
    report_path: Path = DEFAULT_REPORT,
    output_path: Path = DEFAULT_INDEX,
    scout_log_path: Path = DEFAULT_SCOUT_LOG,
) -> List[PaperRecord]:
    primary_records = parse_report(report_path)
    existing_titles = {record.title for record in primary_records}
    scout_records = [
        record for record in parse_scout_log(scout_log_path, starting_ordinal=len(primary_records) + 100)
        if record.title not in existing_titles
    ]
    records = primary_records + scout_records
    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "report_path": str(report_path),
        "scout_log_path": str(scout_log_path),
        "paper_count": len(records),
        "papers": [record.to_dict() for record in records],
    }
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return records


def main() -> int:
    records = build_index()
    print(f"Indexed {len(records)} papers/products into {DEFAULT_INDEX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
