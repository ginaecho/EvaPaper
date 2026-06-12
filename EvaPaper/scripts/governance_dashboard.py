#!/usr/bin/env python3
"""Generate the EvaPaper research dashboard from the report and scout log."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Iterable

from paper_corpus import PaperRecord, parse_report, parse_scout_log
from workspace_config import DEFAULT_WORKSPACE


TOPICS = {
    "specification": {
        "label": "Specification & validation",
        "color": "#e4572e",
        "keywords": (
            "skill.md", "specification", "schema", "contract", "pseudocode",
            "static analysis", "representation", "compiler", "well-defined",
        ),
    },
    "runtime": {
        "label": "Runtime enforcement",
        "color": "#1d6f75",
        "keywords": (
            "runtime", "sandbox", "admission control", "policy enforcement",
            "monitoring", "audit", "intervention", "capability", "authorization",
        ),
    },
    "evaluation": {
        "label": "Evaluation & benchmarks",
        "color": "#f3a712",
        "keywords": (
            "benchmark", "evaluation", "red team", "testing", "assay",
            "behavioral safety", "trustworthiness", "regression",
        ),
    },
    "supply_chain": {
        "label": "Skill & tool security",
        "color": "#963484",
        "keywords": (
            "skill supply chain", "third-party", "tool poisoning", "mcp",
            "marketplace", "skillattack", "skillguard", "dependency",
        ),
    },
    "identity": {
        "label": "Identity & provenance",
        "color": "#4267ac",
        "keywords": (
            "identity", "provenance", "delegation", "attribution", "attestation",
            "accountability", "machine identity",
        ),
    },
    "coordination": {
        "label": "Coordination & composition",
        "color": "#5b8e3e",
        "keywords": (
            "multi-agent", "coordination", "composition", "compositional",
            "message sequence", "orchestration", "agent economy",
        ),
    },
    "policy": {
        "label": "Policy & governance landscape",
        "color": "#636363",
        "keywords": (
            "governance", "taxonomy", "survey", "framework", "constitutional",
            "alignment", "owasp", "nist", "continuous assurance",
        ),
    },
}

TOPIC_PRECEDENCE = (
    "specification",
    "supply_chain",
    "identity",
    "coordination",
    "evaluation",
    "runtime",
    "policy",
)

TOPIC_OVERRIDES = {
    "BeSafe-Bench (BSB)": "evaluation",
    "ST-WebAgentBench": "evaluation",
    "Skilldex": "specification",
    "GovernSpec / Contractual Skills": "specification",
    "Layered Governance Architecture (LGA)": "runtime",
    "TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling": "runtime",
}

TERM_STOPWORDS = {
    "about", "across", "agent", "agents", "based", "behavior", "behavioral",
    "framework", "governance", "large", "layer", "model", "models", "paper",
    "proposes", "research", "safety", "system", "systems", "through", "using",
    "with", "this", "that", "from", "into", "their", "which", "while",
    "skill", "skills", "runtime", "validation", "verification", "evaluation",
}


@dataclass(frozen=True)
class DashboardPaper:
    paper_id: str
    title: str
    url: str | None
    discovered: date
    topic: str
    layers: tuple[int, ...]
    terms: tuple[str, ...] = ()
    summary: str = ""
    relevance: str = ""
    recommendation: str = ""


def _normalize_title(title: str) -> str:
    title = re.sub(r"\s*\(arXiv:[^)]+\)", "", title)
    title = re.sub(r"\s+", " ", title)
    return title.strip()


def _parse_found_date(token: str, year: int = 2026) -> date:
    match = re.match(r"(?P<month>\d{2})(?P<day>\d{2})", token)
    if not match:
        raise ValueError(f"Unsupported discovery date: {token}")
    return date(year, int(match.group("month")), int(match.group("day")))


def _paper_id(text: str) -> str | None:
    arxiv = re.search(r"(?:arxiv\.org/(?:abs|pdf)/|arXiv:|arXiv ID:\s*)(\d{4}\.\d{4,5})", text, re.IGNORECASE)
    if arxiv:
        return f"arxiv:{arxiv.group(1)}"
    preprint = re.search(r"(10\.20944/preprints\d{6}\.\d+\.v\d+)", text, re.IGNORECASE)
    if preprint:
        return f"doi:{preprint.group(1).lower()}"
    return None


def _extract_discovery_dates(log_path: Path, report_path: Path) -> tuple[dict[str, date], dict[str, date]]:
    title_dates: dict[str, date] = {}
    id_dates: dict[str, date] = {}
    log = log_path.read_text(encoding="utf-8")

    current_found: date | None = None
    for line in log.splitlines():
        heading = re.match(r"### New Papers \(Found: ([^)]+)\)", line)
        if heading:
            current_found = _parse_found_date(heading.group(1))
            continue
        baseline = re.match(r"- (?:\*\*)?(.+?)(?:\*\*)?.*Found:\s*(\d{4})", line)
        if baseline:
            discovered = _parse_found_date(baseline.group(2))
            title_dates[_normalize_title(baseline.group(1))] = discovered
            identifier = _paper_id(line)
            if identifier:
                id_dates[identifier] = discovered
            continue
        numbered = re.match(r"\d+\.\s+\*\*(.+?)\*\*", line)
        if numbered and current_found:
            title_dates[_normalize_title(numbered.group(1))] = current_found
            identifier = _paper_id(line)
            if identifier:
                id_dates[identifier] = current_found

    report = report_path.read_text(encoding="utf-8")
    addendum_pattern = re.compile(
        r"### ([A-Z][a-z]+ \d{1,2}, 2026) scout addendum.*?"
        r"(?=\n### [A-Z][a-z]+ \d{1,2}, 2026 scout addendum|\n\*\*The Three-Layer Stack|\n## Papers & Products)",
        re.DOTALL,
    )
    for section in addendum_pattern.finditer(report):
        discovered = datetime.strptime(section.group(1), "%B %d, %Y").date()
        for title in re.findall(r"^\d+\.\s+\*\*(.+?)\*\*", section.group(0), re.MULTILINE):
            title_dates.setdefault(_normalize_title(title), discovered)
        for identifier_text in re.findall(r"(?:arXiv:?\s*`?|\()(\d{4}\.\d{4,5})", section.group(0), re.IGNORECASE):
            id_dates.setdefault(f"arxiv:{identifier_text}", discovered)
    return title_dates, id_dates


def _record_text(record: PaperRecord) -> str:
    fields = " ".join(record.fields.values())
    return f"{record.title} {record.layer or ''} {fields}".lower()


def classify_topic(record: PaperRecord) -> str:
    if record.title in TOPIC_OVERRIDES:
        return TOPIC_OVERRIDES[record.title]
    text = _record_text(record)
    scores = {
        topic: sum(text.count(keyword) for keyword in config["keywords"])
        for topic, config in TOPICS.items()
    }
    return max(TOPIC_PRECEDENCE, key=lambda topic: (scores[topic], -TOPIC_PRECEDENCE.index(topic)))


def parse_layers(record: PaperRecord) -> tuple[int, ...]:
    text = f"{record.layer or ''} {_record_text(record)}"
    layers = sorted({int(value) for value in re.findall(r"\bLayer\s*([0-3])\b", text, re.IGNORECASE)})
    return tuple(layers)


def extract_terms(record: PaperRecord, limit: int = 24) -> tuple[str, ...]:
    text = _record_text(record)
    tokens = re.findall(r"[a-z][a-z0-9-]{3,}", text)
    counts = Counter(token for token in tokens if token not in TERM_STOPWORDS)
    title_tokens = {
        token for token in re.findall(r"[a-z][a-z0-9-]{3,}", record.title.lower())
        if token not in TERM_STOPWORDS
    }
    ranked = sorted(
        counts,
        key=lambda token: (token not in title_tokens, -counts[token], token),
    )
    return tuple(ranked[:limit])


def collect_papers(report_path: Path, log_path: Path) -> list[DashboardPaper]:
    title_dates, id_dates = _extract_discovery_dates(log_path, report_path)
    report_records = parse_report(report_path)
    log_records = parse_scout_log(log_path, starting_ordinal=len(report_records) + 100)
    records: dict[str, PaperRecord] = {}
    for record in [*log_records, *report_records]:
        searchable = " ".join(
            [record.title, record.url or "", *record.fields.values()]
        )
        identifier = _paper_id(searchable)
        if identifier:
            records[identifier] = record

    fallback = min([*title_dates.values(), *id_dates.values()], default=date(2026, 5, 30))
    papers = []
    for identifier, record in records.items():
        normalized_title = _normalize_title(record.title)
        papers.append(
            DashboardPaper(
                paper_id=identifier,
                title=record.title,
                url=record.url,
                discovered=id_dates.get(identifier, title_dates.get(normalized_title, fallback)),
                topic=classify_topic(record),
                layers=parse_layers(record),
                terms=extract_terms(record),
                summary=record.fields.get("abstract", ""),
                relevance=record.fields.get("relevance", ""),
                recommendation=(
                    record.fields.get("why_recommend")
                    or record.fields.get("recommendation_reason")
                    or ""
                ),
            )
        )
    return sorted(papers, key=lambda paper: (paper.discovered, paper.title.lower()))


def _topic_payload(counter: Counter[str], total: int) -> list[dict]:
    return [
        {
            "id": topic,
            "label": TOPICS[topic]["label"],
            "color": TOPICS[topic]["color"],
            "count": counter[topic],
            "ratio": counter[topic] / total if total else 0,
        }
        for topic in TOPIC_PRECEDENCE
    ]


def build_association_graph(papers: Iterable[DashboardPaper], neighbors: int = 3) -> dict:
    papers = list(papers)
    candidates: dict[str, list[tuple[float, DashboardPaper, list[str], list[str]]]] = defaultdict(list)

    for index, left in enumerate(papers):
        left_terms = set(left.terms)
        left_layers = set(left.layers)
        for right in papers[index + 1 :]:
            right_terms = set(right.terms)
            right_layers = set(right.layers)
            shared_terms = sorted(left_terms & right_terms)
            shared_layers = sorted(left_layers & right_layers)
            layer_union = left_layers | right_layers
            layer_score = len(shared_layers) / len(layer_union) if layer_union else 0
            term_base = min(len(left_terms), len(right_terms)) or 1
            term_score = len(shared_terms) / term_base
            same_topic = left.topic == right.topic
            score = (1.7 if same_topic else 0) + (1.4 * layer_score) + (4.5 * term_score)

            if score < 1.75:
                continue
            reasons = []
            if same_topic:
                reasons.append("same topic")
            if shared_layers:
                reasons.append("shared " + "/".join(f"L{layer}" for layer in shared_layers))
            if shared_terms:
                reasons.append("terms: " + ", ".join(shared_terms[:3]))
            candidates[left.paper_id].append((score, right, reasons, shared_terms))
            candidates[right.paper_id].append((score, left, reasons, shared_terms))

    selected: dict[tuple[str, str], dict] = {}
    for paper in papers:
        ranked = sorted(
            candidates[paper.paper_id],
            key=lambda item: (-item[0], item[1].title.lower()),
        )[:neighbors]
        for score, other, reasons, shared_terms in ranked:
            source, target = sorted((paper.paper_id, other.paper_id))
            key = (source, target)
            edge = {
                "source": source,
                "target": target,
                "kind": "conceptual",
                "weight": round(score, 3),
                "reason": "; ".join(reasons),
                "shared_terms": shared_terms[:5],
            }
            if key not in selected or edge["weight"] > selected[key]["weight"]:
                selected[key] = edge

    edges = sorted(selected.values(), key=lambda edge: (edge["source"], edge["target"]))
    degree = Counter()
    for edge in edges:
        degree[edge["source"]] += 1
        degree[edge["target"]] += 1

    nodes = [
        {
            "id": paper.paper_id,
            "title": paper.title,
            "url": paper.url,
            "topic": paper.topic,
            "topic_label": TOPICS[paper.topic]["label"],
            "color": TOPICS[paper.topic]["color"],
            "layers": list(paper.layers),
            "discovered": paper.discovered.isoformat(),
            "degree": degree[paper.paper_id],
        }
        for paper in papers
    ]
    hubs = sorted(nodes, key=lambda node: (-node["degree"], node["title"].lower()))[:5]
    return {
        "nodes": nodes,
        "edges": edges,
        "node_count": len(nodes),
        "edge_count": len(edges),
        "hubs": [
            {"id": node["id"], "title": node["title"], "degree": node["degree"]}
            for node in hubs
        ],
        "method": (
            "Each paper keeps its three strongest corpus neighbors. Association "
            "strength combines primary topic, shared governance layers, and shared "
            "technical terms. These are conceptual associations, not claimed citations."
        ),
    }


def build_knowledge_wiki(papers: Iterable[DashboardPaper], graph: dict) -> dict:
    papers = list(papers)
    edges_by_id: dict[str, list[dict]] = defaultdict(list)
    node_by_id = {node["id"]: node for node in graph["nodes"]}
    for edge in graph["edges"]:
        edges_by_id[edge["source"]].append(edge)
        edges_by_id[edge["target"]].append(edge)

    pages = [
        {
            "id": "overview",
            "type": "overview",
            "title": "Agent Governance Research Overview",
            "subtitle": f"{len(papers)} papers compiled into a living research wiki",
            "body": (
                "EvaPaper compiles specification, runtime, behavioral, ecosystem, "
                "security, identity, and coordination research into maintained pages. "
                "Use topic and layer pages to browse the corpus, then follow explicit "
                "related-paper links to inspect local research trails."
            ),
            "links": [f"topic:{topic}" for topic in TOPIC_PRECEDENCE]
            + [f"layer:{layer}" for layer in range(4)],
            "provenance": "Generated from the report, scout log, and dashboard taxonomy.",
        }
    ]

    for topic in TOPIC_PRECEDENCE:
        members = [paper for paper in papers if paper.topic == topic]
        pages.append(
            {
                "id": f"topic:{topic}",
                "type": "topic",
                "title": TOPICS[topic]["label"],
                "subtitle": f"{len(members)} papers in this primary topic",
                "body": (
                    "This page groups papers by their primary dashboard classification. "
                    "Papers may also connect to other topics through layers and conceptual associations."
                ),
                "links": [paper.paper_id for paper in members],
                "provenance": "Primary-topic classification generated from corpus text and curated overrides.",
            }
        )

    layer_names = {0: "Specification", 1: "Runtime", 2: "Behavioral", 3: "Ecosystem"}
    for layer in range(4):
        members = [paper for paper in papers if layer in paper.layers]
        pages.append(
            {
                "id": f"layer:{layer}",
                "type": "layer",
                "title": f"Layer {layer}: {layer_names[layer]}",
                "subtitle": f"{len(members)} papers mapped to this governance layer",
                "body": (
                    "Layer membership is multi-label. A paper appears here when its "
                    "methods or evaluation claims materially address this layer."
                ),
                "links": [paper.paper_id for paper in members],
                "provenance": "Layer mapping compiled from report and scout annotations.",
            }
        )

    for paper in papers:
        related = []
        for edge in sorted(edges_by_id[paper.paper_id], key=lambda item: -item["weight"]):
            other_id = edge["target"] if edge["source"] == paper.paper_id else edge["source"]
            related.append(
                {
                    "id": other_id,
                    "title": node_by_id[other_id]["title"],
                    "reason": edge["reason"],
                }
            )
        pages.append(
            {
                "id": paper.paper_id,
                "type": "paper",
                "title": paper.title,
                "subtitle": (
                    f"{TOPICS[paper.topic]['label']} · "
                    + (" / ".join(f"Layer {layer}" for layer in paper.layers) or "Layer unassigned")
                ),
                "body": paper.summary or "Summary pending corpus enrichment.",
                "relevance": paper.relevance or "Relevance is represented by topic, layer, and association metadata.",
                "recommendation": paper.recommendation or "Recommendation rationale pending corpus enrichment.",
                "source_url": paper.url,
                "discovered": paper.discovered.isoformat(),
                "links": [f"topic:{paper.topic}"]
                + [f"layer:{layer}" for layer in paper.layers]
                + [item["id"] for item in related],
                "related": related,
                "provenance": (
                    "Generated from AI_Agent_Governance_Three_Layer_Stack_and_Papers.md "
                    "and memory/agent_governance_scout_log.md."
                ),
            }
        )

    return {
        "page_count": len(pages),
        "pages": pages,
        "method": (
            "Karpathy-style compiled wiki: source records remain authoritative; "
            "generated pages maintain summaries, indexes, provenance, and cross-references."
        ),
    }


def build_dashboard_data(papers: Iterable[DashboardPaper], research_opportunities: dict | None = None) -> dict:
    papers = list(papers)
    topic_counts = Counter(paper.topic for paper in papers)
    layer_counts = Counter(layer for paper in papers for layer in paper.layers)
    by_run: dict[date, list[DashboardPaper]] = defaultdict(list)
    for paper in papers:
        by_run[paper.discovered].append(paper)

    cumulative = 0
    runs = []
    previous_counts: Counter[str] = Counter()
    for run_date in sorted(by_run):
        run_papers = by_run[run_date]
        run_counts = Counter(paper.topic for paper in run_papers)
        cumulative += len(run_papers)
        current_counts = previous_counts + run_counts
        leader = max(TOPIC_PRECEDENCE, key=lambda topic: (run_counts[topic], -TOPIC_PRECEDENCE.index(topic)))
        runs.append(
            {
                "date": run_date.isoformat(),
                "new_papers": len(run_papers),
                "cumulative": cumulative,
                "leading_topic": TOPICS[leader]["label"],
                "topics": {topic: run_counts[topic] for topic in TOPIC_PRECEDENCE},
                "cumulative_topics": {topic: current_counts[topic] for topic in TOPIC_PRECEDENCE},
            }
        )
        previous_counts = current_counts

    latest_date = max((paper.discovered for paper in papers), default=date.today())
    recent_cutoff = runs[-3]["date"] if len(runs) >= 3 else (runs[0]["date"] if runs else latest_date.isoformat())
    recent_counts = Counter(
        paper.topic for paper in papers if paper.discovered.isoformat() >= recent_cutoff
    )
    trending = sorted(
        TOPIC_PRECEDENCE,
        key=lambda topic: (recent_counts[topic], topic_counts[topic]),
        reverse=True,
    )[:3]

    association_graph = build_association_graph(papers)
    return {
        "generated_from_latest_scout": latest_date.isoformat(),
        "paper_count": len(papers),
        "scout_run_count": len(runs),
        "topic_mix": _topic_payload(topic_counts, len(papers)),
        "layer_mix": [
            {
                "layer": layer,
                "label": {
                    0: "Spec",
                    1: "Runtime",
                    2: "Behavior",
                    3: "Ecosystem",
                }[layer],
                "count": layer_counts[layer],
            }
            for layer in range(4)
        ],
        "runs": runs,
        "trending_topics": [
            {
                "id": topic,
                "label": TOPICS[topic]["label"],
                "recent_count": recent_counts[topic],
                "total_count": topic_counts[topic],
                "color": TOPICS[topic]["color"],
            }
            for topic in trending
        ],
        "association_graph": association_graph,
        "knowledge_wiki": build_knowledge_wiki(papers, association_graph),
        "research_opportunities": research_opportunities or {
            "generated_at": None,
            "analysis_model": None,
            "summary": "Opportunity analysis has not been generated yet.",
            "opportunities": [],
        },
        "papers": [
            {
                "id": paper.paper_id,
                "title": paper.title,
                "url": paper.url,
                "discovered": paper.discovered.isoformat(),
                "topic": paper.topic,
                "topic_label": TOPICS[paper.topic]["label"],
                "layers": list(paper.layers),
            }
            for paper in papers
        ],
        "methodology": {
            "ratio": "Each paper receives one primary topic so topic ratios sum to 100%.",
            "layers": "Layer counts are multi-label and may exceed the total paper count.",
            "trend": "Trend lines use discovery dates from scout runs, not publication dates.",
            "graph": (
                "Graph edges are labeled corpus associations derived from shared topics, "
                "layers, and technical terms; they do not imply direct citation."
            ),
        },
    }


HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>EvaPaper Research Signal</title>
  <style>
    :root { --ink:#17201f; --paper:#f3efe4; --panel:#fffdf6; --line:#c9c1b1; --muted:#706c63; --accent:#e4572e; }
    * { box-sizing:border-box; }
    body { margin:0; color:var(--ink); background:var(--paper); font-family:"Avenir Next","Gill Sans",sans-serif; }
    body::before { content:""; position:fixed; inset:0; pointer-events:none; opacity:.28; background-image:radial-gradient(#817b70 0.55px,transparent 0.55px); background-size:7px 7px; }
    main { position:relative; width:min(1480px,calc(100% - 32px)); margin:0 auto; padding:36px 0 64px; }
    header { display:grid; grid-template-columns:1.5fr .7fr; gap:24px; align-items:end; border-top:8px solid var(--ink); padding-top:20px; }
    .kicker,.eyebrow { text-transform:uppercase; letter-spacing:.15em; font-size:11px; font-weight:800; }
    h1 { margin:7px 0 4px; max-width:900px; font-family:Georgia,serif; font-size:clamp(42px,7vw,94px); line-height:.88; letter-spacing:-.055em; }
    .subtitle { max-width:720px; color:var(--muted); font-size:16px; }
    .stamp { justify-self:end; border:1px solid var(--ink); padding:14px 18px; min-width:220px; background:var(--panel); }
    .stamp strong { display:block; font:700 27px Georgia,serif; margin-top:5px; }
    .metrics { display:grid; grid-template-columns:repeat(4,1fr); gap:1px; margin:28px 0; background:var(--line); border:1px solid var(--line); }
    .metric { background:var(--panel); padding:18px; min-height:118px; }
    .metric b { display:block; margin-top:18px; font:700 38px Georgia,serif; }
    .grid { display:grid; grid-template-columns:1fr 1.45fr; gap:18px; }
    .panel { background:rgba(255,253,246,.92); border:1px solid var(--line); padding:20px; min-width:0; }
    .panel h2 { margin:4px 0 18px; font:700 25px Georgia,serif; }
    .wide { grid-column:1/-1; }
    .topic-row { display:grid; grid-template-columns:minmax(150px,1fr) 2.2fr 54px; gap:10px; align-items:center; margin:13px 0; }
    .bar { height:13px; background:#ded8ca; overflow:hidden; }
    .bar i { display:block; height:100%; width:var(--w); background:var(--c); }
    .ratio { text-align:right; font-variant-numeric:tabular-nums; font-weight:800; }
    .legend { display:flex; flex-wrap:wrap; gap:8px 16px; margin:4px 0 14px; font-size:12px; }
    .legend span::before { content:""; display:inline-block; width:9px; height:9px; margin-right:6px; background:var(--c); }
    svg { width:100%; height:auto; overflow:visible; }
    .axis { stroke:#bcb4a4; stroke-width:1; }
    .chart-label { fill:#706c63; font-size:11px; }
    .trend-line { fill:none; stroke-width:3; vector-effect:non-scaling-stroke; }
    .run-dot { stroke:var(--panel); stroke-width:2; }
    .layers { display:grid; grid-template-columns:repeat(4,1fr); gap:8px; align-items:end; min-height:250px; }
    .layer { display:flex; flex-direction:column; justify-content:flex-end; min-width:0; }
    .layer-bar { height:var(--h); min-height:8px; background:var(--ink); position:relative; }
    .layer-bar b { position:absolute; top:-28px; font:700 20px Georgia,serif; }
    .layer small { margin-top:8px; color:var(--muted); }
    .signals { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }
    .signal { border-top:5px solid var(--c); padding:12px 0; }
    .signal b { display:block; font:700 21px Georgia,serif; }
    .signal strong { font-size:34px; }
    .graph-panel { padding:0; overflow:hidden; background:#17201f; color:#f3efe4; }
    .graph-head { display:flex; justify-content:space-between; gap:20px; align-items:end; padding:20px; border-bottom:1px solid #44504e; }
    .graph-head h2 { margin-bottom:0; }
    .graph-controls { display:flex; flex-wrap:wrap; gap:8px; }
    .graph-controls input,.graph-controls select,.graph-controls button { border:1px solid #66716e; background:#202b29; color:#f3efe4; padding:9px 11px; font:inherit; }
    .graph-controls input { width:min(280px,44vw); }
    .graph-controls button { cursor:pointer; font-weight:800; }
    .graph-layout { display:grid; grid-template-columns:minmax(0,1fr) 280px; min-height:650px; }
    .graph-stage { position:relative; min-width:0; overflow:hidden; background:radial-gradient(circle at 50% 45%,#263330 0,#17201f 62%,#111817 100%); }
    #paper-graph { display:block; width:100%; height:650px; cursor:grab; touch-action:none; }
    #paper-graph.dragging { cursor:grabbing; }
    .graph-hint { position:absolute; left:14px; bottom:12px; color:#9da8a5; font-size:11px; pointer-events:none; }
    .graph-detail { padding:20px; border-left:1px solid #44504e; background:#1c2725; }
    .graph-detail h3 { margin:8px 0 12px; font:700 24px/1.08 Georgia,serif; }
    .graph-detail p { color:#b9c1be; font-size:13px; line-height:1.5; }
    .graph-detail a { color:#f3efe4; font-weight:800; text-underline-offset:4px; }
    .graph-stat { display:grid; grid-template-columns:1fr 1fr; gap:1px; background:#44504e; margin:18px 0; }
    .graph-stat div { background:#202b29; padding:11px; }
    .graph-stat b { display:block; font:700 24px Georgia,serif; }
    .graph-key { display:flex; flex-wrap:wrap; gap:8px 12px; margin-top:14px; }
    .graph-key span { font-size:10px; color:#bdc6c3; }
    .graph-key i { display:inline-block; width:8px; height:8px; margin-right:5px; background:var(--c); border-radius:50%; }
    .opportunity-intro { display:grid; grid-template-columns:1fr auto; gap:20px; align-items:end; border-bottom:1px solid var(--line); padding-bottom:16px; margin-bottom:16px; }
    .opportunity-intro p { max-width:900px; margin:8px 0 0; color:var(--muted); line-height:1.5; }
    .opportunity-meta { text-align:right; color:var(--muted); font-size:11px; }
    .opportunity-list { display:grid; gap:10px; }
    .opportunity { display:grid; grid-template-columns:72px minmax(0,1fr) 260px; gap:18px; padding:18px 0; border-bottom:1px solid #d9d2c4; }
    .opportunity:last-child { border-bottom:0; }
    .opportunity-rank { font:700 42px Georgia,serif; color:var(--accent); }
    .opportunity h3 { margin:0 0 7px; font:700 22px Georgia,serif; }
    .opportunity p { margin:7px 0; line-height:1.45; }
    .opportunity-reason { color:var(--muted); }
    .opportunity-side { border-left:1px solid var(--line); padding-left:16px; }
    .opportunity-score { font:700 34px Georgia,serif; }
    .opportunity ul { padding-left:18px; margin:8px 0; }
    .opportunity li { margin:5px 0; }
    .gap-tag { display:inline-block; border:1px solid var(--ink); padding:3px 7px; margin-right:6px; text-transform:uppercase; letter-spacing:.06em; font-size:9px; font-weight:800; }
    .wiki-panel { padding:0; overflow:hidden; }
    .wiki-head { display:flex; justify-content:space-between; align-items:end; gap:20px; padding:20px; border-bottom:1px solid var(--line); }
    .wiki-head h2 { margin-bottom:0; }
    .wiki-head input { width:min(340px,48vw); border:1px solid var(--ink); background:transparent; padding:10px 12px; font:inherit; }
    .wiki-layout { display:grid; grid-template-columns:270px minmax(0,1fr); min-height:650px; }
    .wiki-nav { border-right:1px solid var(--line); padding:12px; max-height:720px; overflow:auto; background:#eee8dc; }
    .wiki-nav button { display:block; width:100%; border:0; border-bottom:1px solid #d2cabb; background:transparent; padding:10px 8px; text-align:left; color:var(--ink); cursor:pointer; }
    .wiki-nav button:hover,.wiki-nav button.active { background:var(--panel); }
    .wiki-nav small { display:block; margin-top:3px; color:var(--muted); text-transform:uppercase; letter-spacing:.07em; }
    .wiki-page { padding:clamp(22px,4vw,54px); max-height:720px; overflow:auto; }
    .wiki-page h3 { max-width:900px; margin:8px 0 12px; font:700 clamp(30px,5vw,58px)/.98 Georgia,serif; letter-spacing:-.035em; }
    .wiki-page .lede { max-width:850px; font:italic 19px/1.45 Georgia,serif; color:var(--muted); }
    .wiki-page h4 { margin:28px 0 8px; font:700 18px Georgia,serif; }
    .wiki-page p { max-width:900px; line-height:1.65; }
    .wiki-links { display:flex; flex-wrap:wrap; gap:7px; margin-top:12px; }
    .wiki-link { border:1px solid var(--line); background:transparent; color:var(--ink); padding:7px 9px; cursor:pointer; text-align:left; }
    .wiki-link:hover { border-color:var(--ink); background:#eee8dc; }
    .wiki-related { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:8px; }
    .wiki-related button { border:1px solid var(--line); background:#f7f3e9; padding:12px; text-align:left; color:var(--ink); cursor:pointer; }
    .wiki-related small { display:block; margin-top:5px; color:var(--muted); }
    .wiki-source { display:inline-block; margin-top:12px; color:var(--ink); font-weight:800; text-underline-offset:4px; }
    .wiki-provenance { margin-top:34px; border-top:1px solid var(--line); padding-top:12px; color:var(--muted); font-size:11px; }
    table { width:100%; border-collapse:collapse; font-size:13px; }
    th,td { padding:10px 8px; text-align:left; border-bottom:1px solid #d9d2c4; }
    th { position:sticky; top:0; background:var(--panel); text-transform:uppercase; letter-spacing:.08em; font-size:10px; }
    td a { color:var(--ink); font-weight:700; text-decoration-thickness:1px; text-underline-offset:3px; }
    .pill { display:inline-block; padding:3px 7px; border:1px solid currentColor; font-size:10px; font-weight:800; text-transform:uppercase; }
    .method { color:var(--muted); font-size:12px; margin-top:18px; }
    @media(max-width:850px) {
      header,.grid { grid-template-columns:1fr; }
      .stamp { justify-self:start; }
      .metrics { grid-template-columns:1fr 1fr; }
      .wide { grid-column:auto; }
      .signals { grid-template-columns:1fr; }
      .topic-row { grid-template-columns:1fr 1.4fr 45px; font-size:12px; }
      .graph-head { align-items:start; flex-direction:column; }
      .graph-layout { grid-template-columns:1fr; }
      .graph-detail { border-left:0; border-top:1px solid #44504e; }
      #paper-graph { height:520px; }
      .opportunity-intro,.opportunity { grid-template-columns:1fr; }
      .opportunity-meta { text-align:left; }
      .opportunity-side { border-left:0; border-top:1px solid var(--line); padding:12px 0 0; }
      .wiki-head { align-items:start; flex-direction:column; }
      .wiki-layout { grid-template-columns:1fr; }
      .wiki-nav { border-right:0; border-bottom:1px solid var(--line); max-height:220px; }
      .wiki-page { max-height:none; }
      .wiki-related { grid-template-columns:1fr; }
      .table-wrap { overflow-x:auto; }
    }
  </style>
</head>
<body>
<main>
  <header>
    <div><div class="kicker">EvaPaper / Research intelligence</div><h1>Agent governance signal.</h1><p class="subtitle">Topic concentration, layer coverage, and the direction of research discovered across scout runs.</p></div>
    <div class="stamp"><span class="eyebrow">Latest evidence</span><strong id="latest-date"></strong><span id="latest-note"></span></div>
  </header>
  <section class="metrics" id="metrics"></section>
  <section class="grid">
    <article class="panel"><div class="eyebrow">Distribution</div><h2>What the corpus studies</h2><div id="topic-mix"></div></article>
    <article class="panel"><div class="eyebrow">Momentum</div><h2>Cumulative topic growth</h2><div class="legend" id="legend"></div><svg id="trend" viewBox="0 0 820 330" role="img" aria-label="Cumulative paper topics over scout runs"></svg></article>
    <article class="panel"><div class="eyebrow">Coverage</div><h2>Governance layers</h2><div class="layers" id="layers"></div><p class="method">Multi-layer papers count in every applicable layer.</p></article>
    <article class="panel"><div class="eyebrow">Last three scout windows</div><h2>Topics gaining attention</h2><div class="signals" id="signals"></div><p class="method">Momentum is based on discovery dates, not publication dates.</p></article>
    <article class="panel wide wiki-panel" id="wiki">
      <div class="wiki-head"><div><div class="eyebrow">Living knowledge base</div><h2>EvaPaper Wiki</h2></div><input id="wiki-search" type="search" placeholder="Search wiki pages"></div>
      <div class="wiki-layout"><nav class="wiki-nav" id="wiki-nav"></nav><article class="wiki-page" id="wiki-page"></article></div>
    </article>
    <article class="panel wide graph-panel">
      <div class="graph-head">
        <div><div class="eyebrow">Knowledge graph</div><h2>Paper associations</h2></div>
        <div class="graph-controls"><input id="graph-search" type="search" placeholder="Find a paper"><select id="graph-topic"><option value="all">All topics</option></select><button id="graph-reset" type="button">Reset view</button></div>
      </div>
      <div class="graph-layout">
        <div class="graph-stage"><canvas id="paper-graph" aria-label="Interactive graph of paper associations"></canvas><div class="graph-hint">Drag nodes · drag background to pan · scroll to zoom · click for evidence</div></div>
        <aside class="graph-detail" id="graph-detail"></aside>
      </div>
    </article>
    <article class="panel wide">
      <div class="opportunity-intro">
        <div><div class="eyebrow">LLM gap analysis</div><h2>Underexplored areas & research opportunities</h2><p id="opportunity-summary"></p></div>
        <div class="opportunity-meta" id="opportunity-meta"></div>
      </div>
      <div class="opportunity-list" id="opportunities"></div>
      <p class="method">These rankings are reasoned hypotheses over the collected corpus, not proof that no outside literature exists. Each scout update must reassess them using the workspace skill.</p>
    </article>
    <article class="panel wide"><div class="eyebrow">Evidence ledger</div><h2>Paper inventory</h2><div class="table-wrap"><table><thead><tr><th>Found</th><th>Paper</th><th>Primary topic</th><th>Layers</th></tr></thead><tbody id="papers"></tbody></table></div><p class="method" id="method"></p></article>
  </section>
</main>
<script id="dashboard-data" type="application/json">__DATA__</script>
<script>
const data=JSON.parse(document.getElementById("dashboard-data").textContent);
const pct=n=>`${Math.round(n*100)}%`;
const topicById=Object.fromEntries(data.topic_mix.map(x=>[x.id,x]));
document.getElementById("latest-date").textContent=new Date(`${data.generated_from_latest_scout}T12:00:00`).toLocaleDateString("en",{month:"short",day:"numeric",year:"numeric"});
document.getElementById("latest-note").textContent=`${data.runs.at(-1)?.new_papers||0} papers in latest run`;
const leaders=[...data.topic_mix].sort((a,b)=>b.count-a.count);
document.getElementById("metrics").innerHTML=[
  ["Indexed papers",data.paper_count],
  ["Associations",data.association_graph.edge_count],
  ["Scout runs",data.scout_run_count],
  ["Largest topic",leaders[0]?.label||"—"]
].map(([label,value])=>`<div class="metric"><span class="eyebrow">${label}</span><b>${value}</b></div>`).join("");
document.getElementById("topic-mix").innerHTML=data.topic_mix.map(t=>`<div class="topic-row"><span>${t.label}</span><span class="bar"><i style="--w:${pct(t.ratio)};--c:${t.color}"></i></span><span class="ratio">${pct(t.ratio)}</span></div>`).join("");
document.getElementById("legend").innerHTML=data.topic_mix.map(t=>`<span style="--c:${t.color}">${t.label}</span>`).join("");
const svg=document.getElementById("trend"), W=820,H=330,pad={l:42,r:16,t:12,b:40}, runs=data.runs, max=Math.max(1,...runs.flatMap(r=>Object.values(r.cumulative_topics)));
const x=i=>pad.l+(runs.length===1?0:i*(W-pad.l-pad.r)/(runs.length-1)), y=v=>H-pad.b-v*(H-pad.t-pad.b)/max;
let chart=`<line class="axis" x1="${pad.l}" y1="${H-pad.b}" x2="${W-pad.r}" y2="${H-pad.b}"/>`;
for(let i=0;i<=4;i++){const v=Math.round(max*i/4);chart+=`<line class="axis" opacity=".35" x1="${pad.l}" y1="${y(v)}" x2="${W-pad.r}" y2="${y(v)}"/><text class="chart-label" x="4" y="${y(v)+4}">${v}</text>`;}
runs.forEach((r,i)=>{if(i===0||i===runs.length-1||i%2===0)chart+=`<text class="chart-label" text-anchor="middle" x="${x(i)}" y="${H-12}">${r.date.slice(5)}</text>`;});
data.topic_mix.forEach(t=>{const pts=runs.map((r,i)=>`${x(i)},${y(r.cumulative_topics[t.id])}`).join(" ");chart+=`<polyline class="trend-line" stroke="${t.color}" points="${pts}"/>`;});
svg.innerHTML=chart;
const layerMax=Math.max(1,...data.layer_mix.map(x=>x.count));
document.getElementById("layers").innerHTML=data.layer_mix.map(x=>`<div class="layer"><div class="layer-bar" style="--h:${Math.max(8,x.count/layerMax*190)}px"><b>${x.count}</b></div><small>Layer ${x.layer}<br><strong>${x.label}</strong></small></div>`).join("");
document.getElementById("signals").innerHTML=data.trending_topics.map(t=>`<div class="signal" style="--c:${t.color}"><strong>${t.recent_count}</strong><b>${t.label}</b><span>${t.total_count} total</span></div>`).join("");
const opportunityData=data.research_opportunities;
document.getElementById("opportunity-summary").textContent=opportunityData.summary;
document.getElementById("opportunity-meta").innerHTML=opportunityData.generated_at?`Analyzed ${opportunityData.generated_at}<br>${opportunityData.analysis_model||"LLM sub-agent"}`:"Awaiting analysis";
document.getElementById("opportunities").innerHTML=opportunityData.opportunities.length?opportunityData.opportunities.map(item=>`<section class="opportunity"><div class="opportunity-rank">0${item.rank}</div><div><span class="gap-tag">${item.gap_type.replace("_"," ")}</span><span class="gap-tag">${item.confidence} confidence</span><h3>${item.title}</h3><p>${item.scope}</p><p class="opportunity-reason"><strong>Why this is missing:</strong> ${item.why_missing}</p><p><strong>LLM reasoning:</strong> ${item.llm_reasoning}</p><h4>Evidence used</h4><ul>${item.evidence.map(evidence=>`<li>${evidence.observation} <small>(${evidence.source})</small></li>`).join("")}</ul><p class="opportunity-reason"><strong>Coverage check:</strong> ${item.coverage_check?.interpretation||"Not recorded."}</p><p class="opportunity-reason"><strong>Uncertainty:</strong> ${item.uncertainty}</p></div><aside class="opportunity-side"><div class="eyebrow">Priority</div><div class="opportunity-score">${item.priority_score}/100</div><div class="eyebrow">Research questions</div><ul>${item.research_questions.slice(0,3).map(question=>`<li>${question}</li>`).join("")}</ul></aside></section>`).join(""):`<p>No opportunity analysis is available.</p>`;
document.getElementById("papers").innerHTML=[...data.papers].reverse().map(p=>`<tr><td>${p.discovered.slice(5)}</td><td>${p.url?`<a href="${p.url}">${p.title}</a>`:p.title}</td><td><span class="pill" style="color:${topicById[p.topic].color}">${p.topic_label}</span></td><td>${p.layers.length?p.layers.map(x=>`L${x}`).join(" · "):"—"}</td></tr>`).join("");
document.getElementById("method").textContent=`${data.methodology.ratio} ${data.methodology.layers} ${data.methodology.trend} ${data.methodology.graph}`;

const wiki=data.knowledge_wiki,wikiNav=document.getElementById("wiki-nav"),wikiPage=document.getElementById("wiki-page"),wikiSearch=document.getElementById("wiki-search");
const wikiById=Object.fromEntries(wiki.pages.map(page=>[page.id,page]));
let currentWikiPage="overview",wikiQuery="";
const wikiTypeOrder={overview:0,topic:1,layer:2,paper:3};
function wikiButton(page,compact=false){
  return `<button type="button" class="${page.id===currentWikiPage?"active":""}" data-wiki="${page.id}">${page.title}${compact?"":`<small>${page.type}</small>`}</button>`;
}
function renderWikiNav(){
  const pages=[...wiki.pages].filter(page=>!wikiQuery||`${page.title} ${page.subtitle} ${page.body}`.toLowerCase().includes(wikiQuery)).sort((a,b)=>(wikiTypeOrder[a.type]-wikiTypeOrder[b.type])||a.title.localeCompare(b.title));
  wikiNav.innerHTML=pages.map(page=>wikiButton(page)).join("");
}
function openWikiPage(id,scroll=true){
  const page=wikiById[id];if(!page)return;currentWikiPage=id;renderWikiNav();
  const linkPages=(page.links||[]).map(link=>wikiById[link]).filter(Boolean);
  const related=page.related||[];
  wikiPage.innerHTML=`<div class="eyebrow">${page.type} page</div><h3>${page.title}</h3><p class="lede">${page.subtitle||""}</p><p>${page.body||""}</p>${page.source_url?`<a class="wiki-source" href="${page.source_url}">Open original source ↗</a>`:""}${page.relevance?`<h4>Relevance</h4><p>${page.relevance}</p>`:""}${page.recommendation?`<h4>Why it matters</h4><p>${page.recommendation}</p>`:""}${related.length?`<h4>Related papers</h4><div class="wiki-related">${related.slice(0,8).map(item=>`<button type="button" data-wiki="${item.id}"><strong>${item.title}</strong><small>${item.reason}</small></button>`).join("")}</div>`:""}${linkPages.length&&!related.length?`<h4>Linked pages</h4><div class="wiki-links">${linkPages.map(link=>`<button type="button" class="wiki-link" data-wiki="${link.id}">${link.title}</button>`).join("")}</div>`:""}<div class="wiki-provenance"><strong>Provenance:</strong> ${page.provenance}<br>${wiki.method}</div>`;
  if(scroll)wikiPage.scrollTop=0;
}
document.getElementById("wiki").addEventListener("click",event=>{const target=event.target.closest("[data-wiki]");if(target)openWikiPage(target.dataset.wiki);});
wikiSearch.addEventListener("input",event=>{wikiQuery=event.target.value.trim().toLowerCase();renderWikiNav();});
renderWikiNav();openWikiPage("overview",false);

const graph=data.association_graph, canvas=document.getElementById("paper-graph"), ctx=canvas.getContext("2d");
const graphTopic=document.getElementById("graph-topic"), graphSearch=document.getElementById("graph-search"), graphDetail=document.getElementById("graph-detail");
graphTopic.innerHTML+=data.topic_mix.map(t=>`<option value="${t.id}">${t.label}</option>`).join("");
const clusterIndex=Object.fromEntries(data.topic_mix.map((t,i)=>[t.id,i]));
const nodes=graph.nodes.map((node,i)=>{
  const angle=(clusterIndex[node.topic]/data.topic_mix.length)*Math.PI*2;
  const ring=76+(i%7)*9;
  return {...node,x:Math.cos(angle)*ring+(i%3)*7,y:Math.sin(angle)*ring+(i%5)*6,vx:0,vy:0};
});
const nodeById=Object.fromEntries(nodes.map((node,i)=>[node.id,{node,index:i}]));
const edges=graph.edges.map(edge=>({...edge,a:nodeById[edge.source].node,b:nodeById[edge.target].node}));
const initialGraphScale=.62;
let view={x:0,y:0,scale:initialGraphScale}, selected=null, hovered=null, drag=null, frame=0, query="", topic="all";
const visible=node=>topic==="all"||node.topic===topic;
function resizeGraph(){
  const rect=canvas.getBoundingClientRect(), ratio=Math.min(window.devicePixelRatio||1,2);
  canvas.width=Math.round(rect.width*ratio);canvas.height=Math.round(rect.height*ratio);
  ctx.setTransform(ratio,0,0,ratio,0,0);drawGraph();
}
function screen(node){
  const rect=canvas.getBoundingClientRect();
  return {x:rect.width/2+view.x+node.x*view.scale,y:rect.height/2+view.y+node.y*view.scale};
}
function world(clientX,clientY){
  const rect=canvas.getBoundingClientRect();
  return {x:(clientX-rect.left-rect.width/2-view.x)/view.scale,y:(clientY-rect.top-rect.height/2-view.y)/view.scale};
}
function hitNode(clientX,clientY){
  const point=world(clientX,clientY);
  let best=null,bestDistance=Infinity;
  for(const node of nodes){if(!visible(node))continue;const d=Math.hypot(node.x-point.x,node.y-point.y);const radius=(5+Math.sqrt(node.degree+1)*2)/view.scale;if(d<radius&&d<bestDistance){best=node;bestDistance=d;}}
  return best;
}
function simulate(){
  if(frame++<420){
    for(let i=0;i<nodes.length;i++)for(let j=i+1;j<nodes.length;j++){
      const a=nodes[i],b=nodes[j],dx=b.x-a.x,dy=b.y-a.y,d2=Math.max(dx*dx+dy*dy,70),force=66/d2;
      a.vx-=dx*force;a.vy-=dy*force;b.vx+=dx*force;b.vy+=dy*force;
    }
    for(const edge of edges){
      const dx=edge.b.x-edge.a.x,dy=edge.b.y-edge.a.y,d=Math.max(Math.hypot(dx,dy),1),target=44+(3.4-edge.weight)*10,force=(d-target)*.003;
      edge.a.vx+=dx/d*force;edge.a.vy+=dy/d*force;edge.b.vx-=dx/d*force;edge.b.vy-=dy/d*force;
    }
    for(const node of nodes){
      const angle=(clusterIndex[node.topic]/data.topic_mix.length)*Math.PI*2,targetX=Math.cos(angle)*92,targetY=Math.sin(angle)*92;
      node.vx+=(targetX-node.x)*.0011-node.x*.00075;node.vy+=(targetY-node.y)*.0011-node.y*.00075;
      node.vx*=.88;node.vy*=.88;if(drag?.node!==node){node.x+=node.vx;node.y+=node.vy;}
    }
  }
  drawGraph();requestAnimationFrame(simulate);
}
function drawGraph(){
  const rect=canvas.getBoundingClientRect();
  ctx.clearRect(0,0,rect.width,rect.height);
  for(const edge of edges){
    if(!visible(edge.a)||!visible(edge.b))continue;
    const a=screen(edge.a),b=screen(edge.b),active=selected&&(edge.a===selected||edge.b===selected);
    ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.strokeStyle=active?"rgba(243,239,228,.62)":"rgba(180,194,190,.13)";ctx.lineWidth=active?1.7:.7;ctx.stroke();
  }
  for(const node of nodes){
    if(!visible(node))continue;
    const p=screen(node),active=node===selected||node===hovered,radius=(5+Math.sqrt(node.degree+1)*1.8)*(active?1.35:1);
    ctx.beginPath();ctx.arc(p.x,p.y,radius,0,Math.PI*2);ctx.fillStyle=node.color;ctx.fill();
    if(active){ctx.strokeStyle="#fffdf6";ctx.lineWidth=2;ctx.stroke();}
    if(active||node.degree>=6&&view.scale>1.15){
      ctx.font=active?"700 12px Avenir Next":"11px Avenir Next";ctx.fillStyle="#f3efe4";ctx.textAlign="left";
      const label=node.title.length>44?node.title.slice(0,41)+"...":node.title;ctx.fillText(label,p.x+radius+6,p.y+4);
    }
  }
}
function showDetail(node){
  if(!node){
    graphDetail.innerHTML=`<div class="eyebrow">Graph guide</div><h3>${graph.node_count} papers, ${graph.edge_count} associations</h3><p>Select a node to inspect its strongest conceptual neighbors. Node size reflects degree; color reflects the primary topic.</p><div class="graph-stat"><div><b>${graph.node_count}</b><span>nodes</span></div><div><b>${graph.edge_count}</b><span>edges</span></div></div><p>${graph.method}</p><div class="graph-key">${data.topic_mix.map(t=>`<span><i style="--c:${t.color}"></i>${t.label}</span>`).join("")}</div>`;
    return;
  }
  const links=edges.filter(edge=>edge.a===node||edge.b===node).sort((a,b)=>b.weight-a.weight);
  graphDetail.innerHTML=`<div class="eyebrow">${node.topic_label}</div><h3>${node.title}</h3><p>Found ${node.discovered} · ${node.layers.length?node.layers.map(x=>`Layer ${x}`).join(", "):"Layer not assigned"}</p><p><button type="button" class="wiki-link" id="open-node-wiki">Open wiki page</button></p>${node.url?`<p><a href="${node.url}">Open paper ↗</a></p>`:""}<div class="graph-stat"><div><b>${node.degree}</b><span>associations</span></div><div><b>${links[0]?.weight.toFixed(1)||"0"}</b><span>top strength</span></div></div><div class="eyebrow">Strongest neighbors</div>${links.slice(0,5).map(edge=>{const other=edge.a===node?edge.b:edge.a;return `<p><strong>${other.title}</strong><br><small>${edge.reason}</small></p>`}).join("")}`;
  document.getElementById("open-node-wiki").addEventListener("click",()=>{openWikiPage(node.id);document.getElementById("wiki").scrollIntoView({behavior:"smooth"});});
}
canvas.addEventListener("pointerdown",event=>{canvas.setPointerCapture(event.pointerId);const node=hitNode(event.clientX,event.clientY);drag=node?{node}:{pan:true,startX:event.clientX,startY:event.clientY,viewX:view.x,viewY:view.y};canvas.classList.add("dragging");});
canvas.addEventListener("pointermove",event=>{if(drag?.node){const p=world(event.clientX,event.clientY);drag.node.x=p.x;drag.node.y=p.y;drag.node.vx=drag.node.vy=0;frame=Math.min(frame,360);}else if(drag?.pan){view.x=drag.viewX+event.clientX-drag.startX;view.y=drag.viewY+event.clientY-drag.startY;}else{hovered=hitNode(event.clientX,event.clientY);canvas.style.cursor=hovered?"pointer":"grab";}});
canvas.addEventListener("pointerup",event=>{const node=drag?.node;drag=null;canvas.classList.remove("dragging");if(node){selected=node;showDetail(node);}});
canvas.addEventListener("wheel",event=>{event.preventDefault();const before=world(event.clientX,event.clientY),factor=event.deltaY<0?1.12:.89;view.scale=Math.max(.45,Math.min(3.5,view.scale*factor));const after=world(event.clientX,event.clientY);view.x+=(after.x-before.x)*view.scale;view.y+=(after.y-before.y)*view.scale;},{passive:false});
graphSearch.addEventListener("input",event=>{query=event.target.value.trim().toLowerCase();const match=nodes.find(node=>query&&node.title.toLowerCase().includes(query));if(match){selected=match;showDetail(match);view.x=-match.x*view.scale;view.y=-match.y*view.scale;}});
graphTopic.addEventListener("change",event=>{topic=event.target.value;selected=null;showDetail(null);});
document.getElementById("graph-reset").addEventListener("click",()=>{view={x:0,y:0,scale:initialGraphScale};selected=null;query="";topic="all";graphSearch.value="";graphTopic.value="all";showDetail(null);});
window.addEventListener("resize",resizeGraph);showDetail(null);resizeGraph();simulate();
</script>
</body>
</html>
"""


def render_dashboard(data: dict) -> str:
    payload = json.dumps(data, separators=(",", ":"), ensure_ascii=True).replace("</", "<\\/")
    return HTML_TEMPLATE.replace("__DATA__", payload)


def write_dashboard(
    report_path: Path = DEFAULT_WORKSPACE.report_md,
    log_path: Path = DEFAULT_WORKSPACE.scout_log,
    data_path: Path = DEFAULT_WORKSPACE.dashboard_data,
    html_path: Path = DEFAULT_WORKSPACE.dashboard_html,
    opportunities_path: Path = DEFAULT_WORKSPACE.research_opportunities,
) -> dict:
    opportunities = None
    if opportunities_path.exists():
        opportunities = json.loads(opportunities_path.read_text(encoding="utf-8"))
    data = build_dashboard_data(collect_papers(report_path, log_path), opportunities)
    data_path.parent.mkdir(parents=True, exist_ok=True)
    data_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    html_path.write_text(render_dashboard(data), encoding="utf-8")
    return data


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, default=DEFAULT_WORKSPACE.report_md)
    parser.add_argument("--scout-log", type=Path, default=DEFAULT_WORKSPACE.scout_log)
    parser.add_argument("--data", type=Path, default=DEFAULT_WORKSPACE.dashboard_data)
    parser.add_argument("--html", type=Path, default=DEFAULT_WORKSPACE.dashboard_html)
    parser.add_argument("--opportunities", type=Path, default=DEFAULT_WORKSPACE.research_opportunities)
    args = parser.parse_args()
    data = write_dashboard(args.report, args.scout_log, args.data, args.html, args.opportunities)
    print(
        f"Dashboard updated: {data['paper_count']} papers across "
        f"{data['scout_run_count']} scout runs -> {args.html}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
