#!/usr/bin/env python3
"""
Deep Research Pass using Microsoft Scout-inspired multi-agent pattern.

This script implements the Research Briefing squad pattern from Microsoft Scout:
  Researcher -> Analyst -> Fact Checker -> Synthesizer

It takes high-signal papers from the daily scout and does a deeper investigation:
- Fetches full arXiv abstracts and metadata
- Cross-references with Semantic Scholar for citation context
- Classifies papers into governance layers with detailed justification
- Produces a synthesized briefing for the human

Usage:
    python scripts/deep_research_pass.py
    python scripts/deep_research_pass.py --input data/daily_scouts/scout_2026-07-07.json
    python scripts/deep_research_pass.py --topic "agent governance runtime enforcement"
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))

from workspace_config import DEFAULT_WORKSPACE  # noqa: E402

ARXIV_API = "https://export.arxiv.org/api/query"
S2_API = "https://api.semanticscholar.org/graph/v1"
OPENALEX_API = "https://api.openalex.org"

DEEP_RESEARCH_DIR = DEFAULT_WORKSPACE.root / "data" / "deep_research"


def _fetch_url(url: str, timeout: int = 20) -> str:
    """Fetch URL content as text."""
    req = urllib.request.Request(url, headers={"User-Agent": "EvaPaper/1.0 (research-pass)"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8")
    except Exception:
        return ""


def _fetch_json(url: str, timeout: int = 20) -> dict:
    """Fetch URL content as JSON."""
    text = _fetch_url(url, timeout)
    if text:
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass
    return {}


# ---------------------------------------------------------------------------
# Agent 1: Researcher — fetches detailed metadata from arXiv + Semantic Scholar
# ---------------------------------------------------------------------------

def researcher_fetch_details(papers: list[dict]) -> list[dict]:
    """Fetch full details for candidate papers (arXiv abstract, S2 context)."""
    enriched = []
    for paper in papers:
        title = paper.get("title", "")
        url = paper.get("url", "")
        arxiv_id = _extract_arxiv_id(url) or _extract_arxiv_id(paper.get("openalex_id", ""))

        enriched_paper = {**paper, "arxiv_abstract": None, "s2_tldr": None, "s2_fields": []}

        # Try arXiv API for full abstract
        if arxiv_id:
            arxiv_url = f"{ARXIV_API}?id_list={arxiv_id}"
            xml_text = _fetch_url(arxiv_url)
            if xml_text:
                try:
                    root = ET.fromstring(xml_text)
                    ns = {"atom": "http://www.w3.org/2005/Atom"}
                    entry = root.find("atom:entry", ns)
                    if entry is not None:
                        abstract_el = entry.find("atom:summary", ns)
                        if abstract_el is not None and abstract_el.text:
                            enriched_paper["arxiv_abstract"] = abstract_el.text.strip()
                except ET.ParseError:
                    pass
            time.sleep(0.5)  # Rate limit

        # Try Semantic Scholar for TLDR and fields
        if title:
            s2_search = f"{S2_API}/paper/search?query={urllib.parse.quote(title[:100])}&limit=1&fields=tldr,fieldsOfStudy,citationCount,year"
            s2_data = _fetch_json(s2_search)
            if s2_data.get("data"):
                s2_paper = s2_data["data"][0]
                tldr = s2_paper.get("tldr")
                if tldr and isinstance(tldr, dict):
                    enriched_paper["s2_tldr"] = tldr.get("text")
                enriched_paper["s2_fields"] = s2_paper.get("fieldsOfStudy") or []
                # Update citation count if S2 has a higher number
                s2_cites = s2_paper.get("citationCount", 0)
                if s2_cites > paper.get("citation_count", 0):
                    enriched_paper["citation_count"] = s2_cites
            time.sleep(0.3)

        enriched.append(enriched_paper)

    return enriched


# ---------------------------------------------------------------------------
# Agent 2: Analyst — classifies and interprets papers
# ---------------------------------------------------------------------------

GOVERNANCE_SIGNALS = {
    "Layer 0 (Spec-Level)": [
        "specification", "schema", "validation", "contract", "manifest",
        "skill definition", "metadata", "well-formed", "lint", "compile",
        "pre-execution", "permission", "boundary", "static analysis",
    ],
    "Layer 1 (Runtime-Level)": [
        "runtime", "sandbox", "execution", "monitor", "orchestrat",
        "policy enforcement", "authorization", "audit", "admission control",
        "intervention", "containment", "guardrail",
    ],
    "Layer 2 (Behavioral-Level)": [
        "benchmark", "evaluation", "safety", "trustworth", "red team",
        "task completion", "behavioral", "alignment", "reward hack",
        "agent behavior", "regression", "reliability",
    ],
}


def analyst_classify(papers: list[dict]) -> list[dict]:
    """Classify papers with detailed governance layer analysis."""
    for paper in papers:
        text = f"{paper.get('title', '')} {paper.get('arxiv_abstract', '') or paper.get('abstract', '')}".lower()

        scores = {}
        matched_signals = {}
        for layer, signals in GOVERNANCE_SIGNALS.items():
            layer_matches = [s for s in signals if s in text]
            scores[layer] = len(layer_matches)
            matched_signals[layer] = layer_matches

        # Primary and secondary layers
        sorted_layers = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        paper["primary_layer"] = sorted_layers[0][0] if sorted_layers[0][1] > 0 else "Uncategorized"
        paper["secondary_layer"] = sorted_layers[1][0] if len(sorted_layers) > 1 and sorted_layers[1][1] > 0 else None
        paper["governance_signals"] = matched_signals
        paper["governance_relevance"] = "high" if sorted_layers[0][1] >= 3 else ("medium" if sorted_layers[0][1] >= 1 else "low")

    return papers


# ---------------------------------------------------------------------------
# Agent 3: Fact Checker — verifies claims and confidence
# ---------------------------------------------------------------------------

def fact_checker_verify(papers: list[dict]) -> list[dict]:
    """Grade confidence and flag issues."""
    for paper in papers:
        confidence_issues = []

        # Check if we have a real abstract
        has_abstract = bool(paper.get("arxiv_abstract") or paper.get("abstract"))
        if not has_abstract:
            confidence_issues.append("No abstract available - classification based on title only")

        # Check citation count credibility
        cites = paper.get("citation_count", 0)
        year = paper.get("year")
        if year and year >= 2026 and cites > 100:
            confidence_issues.append(f"Unusually high citations ({cites}) for {year} paper - verify")

        # Check if arXiv ID is valid
        arxiv_id = _extract_arxiv_id(paper.get("url", ""))
        if arxiv_id and not paper.get("arxiv_abstract"):
            confidence_issues.append("arXiv ID found but abstract fetch failed")

        # Governance relevance confidence
        if paper.get("governance_relevance") == "low":
            confidence_issues.append("Low governance relevance - may not belong in the collection")

        paper["confidence_issues"] = confidence_issues
        paper["confidence_grade"] = (
            "A" if not confidence_issues else
            "B" if len(confidence_issues) == 1 else
            "C"
        )

    return papers


# ---------------------------------------------------------------------------
# Agent 4: Synthesizer — produces the final briefing
# ---------------------------------------------------------------------------

def synthesizer_brief(papers: list[dict], topic: str) -> dict:
    """Produce an executive-ready research briefing."""
    # Group by layer
    by_layer = {}
    for paper in papers:
        layer = paper.get("primary_layer", "Uncategorized")
        by_layer.setdefault(layer, []).append(paper)

    # High-confidence picks
    high_conf = [p for p in papers if p.get("confidence_grade") == "A" and p.get("governance_relevance") in ("high", "medium")]
    high_conf.sort(key=lambda x: x.get("score", 0), reverse=True)

    briefing = {
        "date": datetime.now().isoformat(),
        "topic": topic,
        "total_papers_analyzed": len(papers),
        "layer_distribution": {k: len(v) for k, v in by_layer.items()},
        "high_confidence_picks": [
            {
                "title": p.get("title"),
                "year": p.get("year"),
                "layer": p.get("primary_layer"),
                "relevance": p.get("governance_relevance"),
                "url": p.get("url"),
                "tldr": p.get("s2_tldr") or (p.get("arxiv_abstract", "") or "")[:200],
                "signals": p.get("governance_signals", {}),
            }
            for p in high_conf[:10]
        ],
        "key_takeaways": _generate_takeaways(papers, by_layer),
        "gaps_identified": _identify_gaps(by_layer),
        "papers_by_layer": {
            layer: [
                {"title": p["title"], "year": p.get("year"), "confidence": p.get("confidence_grade"), "url": p.get("url")}
                for p in layer_papers[:10]
            ]
            for layer, layer_papers in by_layer.items()
        },
    }

    return briefing


def _generate_takeaways(papers: list[dict], by_layer: dict) -> list[str]:
    """Generate key takeaways from the research."""
    takeaways = []
    total = len(papers)
    high_rel = sum(1 for p in papers if p.get("governance_relevance") == "high")

    takeaways.append(f"{high_rel}/{total} papers have high governance relevance")

    for layer, layer_papers in sorted(by_layer.items()):
        if layer_papers:
            takeaways.append(f"{layer}: {len(layer_papers)} papers")

    recent = [p for p in papers if p.get("year") and p.get("year") >= 2026]
    if recent:
        takeaways.append(f"{len(recent)} papers from 2026 (cutting edge)")

    return takeaways


def _identify_gaps(by_layer: dict) -> list[str]:
    """Identify research gaps."""
    gaps = []
    if not by_layer.get("Layer 0 (Spec-Level)"):
        gaps.append("No spec-level papers found - consider adding skill validation search terms")
    if not by_layer.get("Layer 1 (Runtime-Level)"):
        gaps.append("No runtime-level papers found - consider adding sandboxing/enforcement terms")
    if not by_layer.get("Layer 2 (Behavioral-Level)"):
        gaps.append("No behavioral-level papers found - consider adding benchmark/evaluation terms")
    return gaps


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def _extract_arxiv_id(text: str) -> Optional[str]:
    if not text:
        return None
    m = re.search(r"(\d{4}\.\d{4,5})", text)
    return m.group(1) if m else None


def save_briefing(briefing: dict, topic: str):
    """Save the research briefing."""
    DEEP_RESEARCH_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = re.sub(r"[^a-z0-9]+", "-", topic.lower())[:40]

    # JSON
    json_path = DEEP_RESEARCH_DIR / f"briefing_{date_str}_{slug}.json"
    json_path.write_text(json.dumps(briefing, indent=2, ensure_ascii=False), encoding="utf-8")

    # Markdown
    md_path = DEEP_RESEARCH_DIR / f"briefing_{date_str}_{slug}.md"
    lines = [
        f"# Deep Research Briefing: {topic}",
        f"",
        f"**Date:** {date_str}",
        f"**Papers analyzed:** {briefing['total_papers_analyzed']}",
        "",
        "## Key Takeaways",
        "",
    ]
    for t in briefing.get("key_takeaways", []):
        lines.append(f"- {t}")

    lines.extend(["", "## Layer Distribution", ""])
    for layer, count in briefing.get("layer_distribution", {}).items():
        lines.append(f"- **{layer}**: {count} papers")

    lines.extend(["", "## High-Confidence Picks", ""])
    for i, pick in enumerate(briefing.get("high_confidence_picks", []), 1):
        lines.append(f"### {i}. {pick['title']} ({pick['year']})")
        lines.append(f"- Layer: {pick['layer']}")
        lines.append(f"- Relevance: {pick['relevance']}")
        if pick.get("url"):
            lines.append(f"- URL: {pick['url']}")
        if pick.get("tldr"):
            lines.append(f"- Summary: {pick['tldr']}")
        lines.append("")

    if briefing.get("gaps_identified"):
        lines.extend(["## Research Gaps", ""])
        for g in briefing["gaps_identified"]:
            lines.append(f"- {g}")
        lines.append("")

    lines.append("---")
    lines.append("*Generated by EvaPaper Deep Research Pass (Microsoft Scout-inspired multi-agent pattern)*")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[deep-research] Briefing saved: {md_path.relative_to(DEFAULT_WORKSPACE.root)}")
    return md_path


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run_deep_research(papers: list[dict], topic: str = "daily scout deep dive") -> dict:
    """Run the full Scout-inspired research pipeline."""
    print(f"\n[deep-research] Starting multi-agent research pass")
    print(f"[deep-research] Topic: {topic}")
    print(f"[deep-research] Input papers: {len(papers)}")
    print("-" * 60)

    # Stage 1: Researcher
    print("[1/4] Researcher: Fetching detailed metadata...")
    enriched = researcher_fetch_details(papers)
    abstracts_found = sum(1 for p in enriched if p.get("arxiv_abstract"))
    tldrs_found = sum(1 for p in enriched if p.get("s2_tldr"))
    print(f"       Abstracts fetched: {abstracts_found} | TLDRs found: {tldrs_found}")

    # Stage 2: Analyst
    print("[2/4] Analyst: Classifying governance layers...")
    classified = analyst_classify(enriched)
    high_rel = sum(1 for p in classified if p.get("governance_relevance") == "high")
    print(f"       High relevance: {high_rel} | Medium: {sum(1 for p in classified if p.get('governance_relevance') == 'medium')}")

    # Stage 3: Fact Checker
    print("[3/4] Fact Checker: Verifying confidence...")
    verified = fact_checker_verify(classified)
    grade_a = sum(1 for p in verified if p.get("confidence_grade") == "A")
    print(f"       Grade A: {grade_a} | Grade B: {sum(1 for p in verified if p.get('confidence_grade') == 'B')}")

    # Stage 4: Synthesizer
    print("[4/4] Synthesizer: Producing briefing...")
    briefing = synthesizer_brief(verified, topic)

    save_briefing(briefing, topic)

    print(f"\n[deep-research] COMPLETE")
    print(f"  High-confidence governance picks: {len(briefing['high_confidence_picks'])}")
    for i, pick in enumerate(briefing["high_confidence_picks"][:5], 1):
        print(f"  {i}. {pick['title']} ({pick['year']}) [{pick['layer']}]")

    return briefing


def main():
    parser = argparse.ArgumentParser(description="Deep Research Pass (Scout-inspired)")
    parser.add_argument("--input", type=Path, help="Path to daily scout JSON report")
    parser.add_argument("--topic", default="agent governance and evaluation", help="Research topic label")
    parser.add_argument("--top-k", type=int, default=15, help="Number of top papers to deep-research")
    args = parser.parse_args()

    # Load papers from latest scout or specified input
    if args.input and args.input.exists():
        data = json.loads(args.input.read_text(encoding="utf-8"))
        papers = data.get("top_papers", [])[:args.top_k]
    else:
        # Find latest scout report
        scout_dir = DEFAULT_WORKSPACE.root / "data" / "daily_scouts"
        if scout_dir.exists():
            reports = sorted(scout_dir.glob("scout_*.json"), reverse=True)
            if reports:
                data = json.loads(reports[0].read_text(encoding="utf-8"))
                papers = data.get("top_papers", [])[:args.top_k]
                print(f"[deep-research] Using latest scout: {reports[0].name}")
            else:
                print("[deep-research] No scout reports found. Run daily_scout.py first.")
                return 1
        else:
            print("[deep-research] No scout data directory. Run daily_scout.py first.")
            return 1

    if not papers:
        print("[deep-research] No papers to research.")
        return 0

    run_deep_research(papers, args.topic)
    return 0


if __name__ == "__main__":
    sys.exit(main())
