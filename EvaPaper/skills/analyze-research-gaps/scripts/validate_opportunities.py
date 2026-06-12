#!/usr/bin/env python3
"""Validate the research-opportunity artifact consumed by the dashboard."""

from __future__ import annotations

import json
import sys
from pathlib import Path


GAP_TYPES = {"corpus_gap", "field_gap", "evidence_gap", "translation_gap"}
CONFIDENCE = {"low", "medium", "high"}
TOPICS = {
    "specification", "runtime", "evaluation", "supply_chain",
    "identity", "coordination", "policy",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate(payload: dict) -> None:
    require(isinstance(payload.get("generated_at"), str), "generated_at is required")
    require(isinstance(payload.get("analysis_model"), str), "analysis_model is required")
    require(isinstance(payload.get("summary"), str) and payload["summary"].strip(), "summary is required")
    snapshot = payload.get("corpus_snapshot")
    require(isinstance(snapshot, dict), "corpus_snapshot is required")
    for key in (
        "source_record_count", "academic_paper_count", "scope_note",
        "scout_run_count", "latest_scout", "graph_nodes", "graph_edges",
    ):
        require(key in snapshot, f"corpus_snapshot.{key} is required")

    opportunities = payload.get("opportunities")
    require(isinstance(opportunities, list), "opportunities must be a list")
    require(3 <= len(opportunities) <= 6, "opportunities must contain 3-6 entries")
    require(
        [item.get("rank") for item in opportunities] == list(range(1, len(opportunities) + 1)),
        "ranks must be consecutive and start at 1",
    )
    for item in opportunities:
        rank = item["rank"]
        require(item.get("gap_type") in GAP_TYPES, f"opportunity {rank}: invalid gap_type")
        require(
            isinstance(item.get("priority_score"), int) and 0 <= item["priority_score"] <= 100,
            f"opportunity {rank}: priority_score must be 0-100",
        )
        require(item.get("confidence") in CONFIDENCE, f"opportunity {rank}: invalid confidence")
        for key in ("title", "scope", "why_missing", "llm_reasoning", "uncertainty"):
            require(
                isinstance(item.get(key), str) and item[key].strip(),
                f"opportunity {rank}: {key} is required",
            )
        require(len(item.get("evidence", [])) >= 2, f"opportunity {rank}: at least two evidence items required")
        for evidence in item["evidence"]:
            require(evidence.get("observation") and evidence.get("source"), f"opportunity {rank}: invalid evidence")
        require(
            len(item.get("research_questions", [])) >= 2,
            f"opportunity {rank}: at least two research questions required",
        )
        require(
            len(item.get("scout_queries", [])) >= 2,
            f"opportunity {rank}: at least two scout queries required",
        )
        coverage = item.get("coverage_check")
        require(isinstance(coverage, dict), f"opportunity {rank}: coverage_check is required")
        require(
            coverage.get("query_terms") and coverage.get("matched_titles") is not None
            and coverage.get("interpretation"),
            f"opportunity {rank}: invalid coverage_check",
        )
        require(
            set(item.get("related_topics", [])).issubset(TOPICS),
            f"opportunity {rank}: invalid related topic",
        )
        require(
            all(isinstance(layer, int) and 0 <= layer <= 3 for layer in item.get("related_layers", [])),
            f"opportunity {rank}: invalid related layer",
        )


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_opportunities.py <research_opportunities.json>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        validate(payload)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    print(f"VALID: {len(payload['opportunities'])} ranked research opportunities")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
