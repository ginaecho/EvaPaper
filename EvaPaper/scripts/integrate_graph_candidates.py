#!/usr/bin/env python3
"""Promote live graph candidates from the latest team run into the scout log."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Sequence

from governance_dashboard import write_dashboard
from workspace_config import DEFAULT_WORKSPACE


STATIC_TERMS = {
    "certificate",
    "certificates",
    "cryptographic",
    "fingerprint",
    "identity",
    "registry",
    "skillbom",
    "validity",
    "validation",
}
RUNTIME_TERMS = {
    "constrain",
    "execution",
    "harness",
    "monitor",
    "orchestrate",
    "runtime",
}
BEHAVIORAL_TERMS = {
    "behavior",
    "benchmark",
    "evaluation",
    "feedback",
    "mining",
    "reinforcement",
}


def normalize_arxiv_id(paper_id: str) -> str | None:
    match = re.search(r"(\d{4}\.\d{4,5})(?:v\d+)?", paper_id)
    return match.group(1) if match else None


def existing_identifiers(*paths: Path) -> set[str]:
    identifiers: set[str] = set()
    for path in paths:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for arxiv_id in re.findall(r"(?:arxiv\.org/abs/|arXiv:)(\d{4}\.\d{4,5})", text, re.IGNORECASE):
            identifiers.add(f"arxiv:{arxiv_id}")
    return identifiers


def infer_layer(candidate: dict) -> str:
    text = " ".join(
        str(candidate.get(field) or "")
        for field in ("title", "abstract")
    ).lower()
    static_score = sum(term in text for term in STATIC_TERMS)
    runtime_score = sum(term in text for term in RUNTIME_TERMS)
    behavioral_score = sum(term in text for term in BEHAVIORAL_TERMS)
    if static_score >= max(runtime_score, behavioral_score):
        return "Layer 0/1"
    if runtime_score >= behavioral_score:
        return "Layer 1"
    return "Layer 2"


def relevance_sentence(candidate: dict, layer: str) -> str:
    title = str(candidate.get("title") or "")
    text = f"{title} {candidate.get('abstract') or ''}".lower()
    if "fingerprint" in text or "identity" in text or "skillbom" in text:
        return "Provides a structural identity signal for skill registries, useful for detecting tampered or reused skills before runtime trust decisions."
    if "cryptographic" in text or "certificate" in text:
        return "Turns policy satisfaction into independently checkable proof artifacts, directly relevant to enforceable agent-governance specifications."
    if "skillwiki" in text or "skill lifecycle" in text:
        return "Treats agent skills as governed knowledge assets with provenance, lifecycle management, and execution-driven evolution."
    if "harness" in text:
        return "Frames skills as governable runtime assets that must be registered, orchestrated, constrained, and monitored."
    if "behavior mining" in text:
        return "Makes agent behavior observable through process logs, supporting audit and policy-deviation detection."
    if "openclaw-style" in text or "workspace + skill" in text:
        return "Directly analyzes the OpenClaw-style workspace plus skill paradigm as a governed persistent-agent system."
    return f"Live graph candidate relevant to {layer} governance for agent skills, specifications, or behavior."


def format_entry(index: int, candidate: dict) -> str | None:
    arxiv_id = normalize_arxiv_id(str(candidate.get("paper_id") or candidate.get("url") or ""))
    if not arxiv_id:
        return None
    title = str(candidate.get("title") or "").strip()
    abstract = " ".join(str(candidate.get("abstract") or "").split())
    if not title or not abstract:
        return None
    layer = infer_layer(candidate)
    url = f"https://arxiv.org/abs/{arxiv_id}"
    relevance = relevance_sentence(candidate, layer)
    return (
        f"{index}. **{title}** (arXiv:{arxiv_id}) — "
        f"{candidate.get('year') or 'n.d.'}. {abstract} "
        f"URL: {url} — **{layer}** — {relevance}"
    )


def integrate_candidates(team_run: Path, scout_log: Path, report_md: Path, limit: int, date_token: str) -> list[str]:
    payload = json.loads(team_run.read_text(encoding="utf-8"))
    graph_artifact = Path(payload.get("graph", {}).get("artifact", ""))
    if graph_artifact.exists():
        graph_payload = json.loads(graph_artifact.read_text(encoding="utf-8"))
        candidates = graph_payload.get("candidates", [])[:limit]
    else:
        candidates = payload.get("graph", {}).get("top_candidates", [])[:limit]
    known = existing_identifiers(scout_log, report_md)
    entries: list[str] = []
    for candidate in candidates:
        arxiv_id = normalize_arxiv_id(str(candidate.get("paper_id") or candidate.get("url") or ""))
        if not arxiv_id or f"arxiv:{arxiv_id}" in known:
            continue
        entry = format_entry(len(entries) + 1, candidate)
        if entry:
            entries.append(entry)
            known.add(f"arxiv:{arxiv_id}")
    if not entries:
        return []

    today = datetime.now().strftime("%Y-%m-%d")
    section = [
        "",
        f"## {today} Scout Run — GRAPH CANDIDATES INTEGRATED",
        f"Search query: {payload.get('query', 'n/a')}",
        "Status: **NEW GRAPH FINDINGS FOUND**",
        "",
        f"### New Papers (Found: {date_token})",
        *entries,
        "",
        "### Notes",
        "- Integrated from `data/agent_team/last_team_run.json` so dashboard generation can see live graph candidates.",
        "- Provider degradation, if present, is recorded in the team-run JSON; arXiv live search supplied these candidates.",
        "",
    ]
    scout_log.write_text(scout_log.read_text(encoding="utf-8").rstrip() + "\n" + "\n".join(section), encoding="utf-8")
    return entries


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Integrate latest graph candidates into scout log and dashboard.")
    parser.add_argument("--team-run", type=Path, default=DEFAULT_WORKSPACE.team_dir / "last_team_run.json")
    parser.add_argument("--scout-log", type=Path, default=DEFAULT_WORKSPACE.scout_log)
    parser.add_argument("--report-md", type=Path, default=DEFAULT_WORKSPACE.report_md)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--date-token", default=datetime.now().strftime("%m%d"))
    parser.add_argument("--dashboard", action="store_true", help="Regenerate dashboard after integration.")
    return parser.parse_args(argv)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    entries = integrate_candidates(args.team_run, args.scout_log, args.report_md, args.limit, args.date_token)
    print(f"Integrated {len(entries)} new graph candidate(s).")
    if entries and args.dashboard:
        data = write_dashboard(args.report_md, args.scout_log)
        print(
            f"Dashboard updated: {data['association_graph']['node_count']} papers "
            f"across {data['scout_run_count']} scout runs -> {DEFAULT_WORKSPACE.dashboard_html}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(__import__("sys").argv[1:]))
