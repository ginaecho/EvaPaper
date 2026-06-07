#!/usr/bin/env python3
"""
Generic multi-agent orchestration for governance-paper scouting and synthesis.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from typing import List, Sequence
from urllib.error import URLError

from paper_corpus import build_index
from paper_graph import discover_from_query
from question_map import normalize_mode, retrieve, summarize_state_of_art
from workspace_config import DEFAULT_WORKSPACE


ROLE_DESCRIPTIONS = {
    "scout": "Expands seed queries through public paper graphs and proposes candidate papers.",
    "librarian": "Maintains the normalized corpus, deduplicates records, and rebuilds evidence indexes.",
    "static_analyst": "Focuses on pre-execution governance: specs, skills, contracts, and delegation chains.",
    "runtime_analyst": "Tracks runtime controls such as sandboxing, intent verification, auditability, and protocol security.",
    "behavioral_analyst": "Tracks benchmarks, trustworthiness evaluation, and post-build governance measurements.",
    "synthesizer": "Combines role outputs into state-of-the-art summaries and evidence-backed answers.",
}


@dataclass
class TeamTask:
    role: str
    objective: str
    artifact: str


def build_team_plan(query: str, question: str | None, mode: str) -> List[TeamTask]:
    normalized_mode = normalize_mode(mode)
    tasks = [
        TeamTask("scout", f"Expand the paper graph for query: {query}", "graph_candidates.json"),
        TeamTask("librarian", "Rebuild the local governance corpus and deduplicate records.", "paper_corpus.json"),
    ]
    if normalized_mode in ("static", "all"):
        tasks.append(TeamTask("static_analyst", "Rank static-time governance papers and standards.", "static_sota.json"))
    if normalized_mode in ("runtime", "all"):
        tasks.append(TeamTask("runtime_analyst", "Rank runtime governance papers and standards.", "runtime_sota.json"))
    if normalized_mode in ("behavioral", "all"):
        tasks.append(TeamTask("behavioral_analyst", "Rank behavioral governance papers and benchmarks.", "behavioral_sota.json"))
    if normalized_mode == "landscape":
        tasks.append(TeamTask("synthesizer", "Summarize the full governance landscape.", "landscape_sota.json"))
    if question:
        tasks.append(TeamTask("synthesizer", f"Answer the question with paper evidence: {question}", "question_answer.json"))
    return tasks


def run_team(query: str, question: str | None, mode: str, top_k: int) -> dict:
    workspace = DEFAULT_WORKSPACE
    workspace.team_dir.mkdir(parents=True, exist_ok=True)
    normalized_mode = normalize_mode(mode)

    graph_error = None
    try:
        graph = discover_from_query(query=query, from_year=2024)
    except URLError as exc:
        graph = {"query": query, "seeds": [], "candidates": []}
        graph_error = str(exc)
    build_index(workspace.report_md, workspace.corpus_index, workspace.scout_log)

    result = {
        "query": query,
        "question": question,
        "mode": normalized_mode,
        "tasks": [asdict(task) for task in build_team_plan(query, question, mode)],
        "roles": ROLE_DESCRIPTIONS,
        "graph": {
            "seed_count": len(graph["seeds"]),
            "candidate_count": len(graph["candidates"]),
            "top_candidates": graph["candidates"][:top_k],
        },
        "all_sota": summarize_state_of_art(mode="all", top_k=top_k),
    }
    if graph_error:
        result["graph_warning"] = f"Discovery graph unavailable; fell back to local corpus only: {graph_error}"

    if normalized_mode in ("static", "all"):
        result["static_sota"] = summarize_state_of_art(mode="static", top_k=top_k)
    if normalized_mode in ("runtime", "all"):
        result["runtime_sota"] = summarize_state_of_art(mode="runtime", top_k=top_k)
    if normalized_mode in ("behavioral", "all"):
        result["behavioral_sota"] = summarize_state_of_art(mode="behavioral", top_k=top_k)
    if normalized_mode == "landscape":
        result["landscape_sota"] = summarize_state_of_art(mode="landscape", top_k=top_k)
    if question:
        result["answer"] = retrieve(question=question, top_k=top_k, mode=normalized_mode)

    output_path = workspace.team_dir / "last_team_run.json"
    output_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    result["output_path"] = str(output_path)
    return result


def format_report(result: dict) -> str:
    lines = [f"Query: {result['query']}", f"Mode: {result['mode']}", "", "Team plan:"]
    for task in result["tasks"]:
        lines.append(f"- {task['role']}: {task['objective']} -> {task['artifact']}")
    lines.append("")
    lines.append(
        f"Discovery graph: {result['graph']['seed_count']} seed papers, {result['graph']['candidate_count']} candidates"
    )
    if result.get("graph_warning"):
        lines.append(result["graph_warning"])
    if "answer" in result:
        lines.append("")
        lines.append(f"Question: {result['answer']['question']}")
        for idx, item in enumerate(result["answer"]["results"][:5], start=1):
            lines.append(f"{idx}. {item['title']} | focus={item.get('primary_focus')} | score={item['score']}")
    return "\n".join(lines)


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the governance-paper workflow as a generic agent team.")
    parser.add_argument("--query", required=True)
    parser.add_argument("--question")
    parser.add_argument("--mode", default="all", choices=["all", "sota", "static", "static-first", "spec", "runtime", "behavioral", "landscape"])
    parser.add_argument("--top-k", type=int, default=8)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    result = run_team(query=args.query, question=args.question, mode=args.mode, top_k=args.top_k)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(format_report(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(__import__("sys").argv[1:]))
