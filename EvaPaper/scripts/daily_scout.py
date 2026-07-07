#!/usr/bin/env python3
"""
Daily Paper Scout for EvaPaper.

Runs multiple research queries against OpenAlex (and optionally Semantic Scholar)
to discover new papers relevant to our research areas. Deduplicates against
previously seen papers, logs new findings, and optionally commits results.

Usage:
    python scripts/daily_scout.py
    python scripts/daily_scout.py --commit
    python scripts/daily_scout.py --commit --push
    python scripts/daily_scout.py --topics "custom topic 1" "custom topic 2"
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

# Ensure scripts/ is on the path for sibling imports
sys.path.insert(0, str(Path(__file__).resolve().parent))

from paper_graph import discover_from_query  # noqa: E402  (supports include_semantic_scholar=True)
from workspace_config import DEFAULT_WORKSPACE  # noqa: E402

# Default research topics to scout daily
DEFAULT_TOPICS = [
    "LLM agent evaluation benchmark 2025 2026",
    "AI agent safety benchmark behavioral",
    "agent governance skill validation framework",
    "multi-agent evaluation reliability",
    "LLM agent tool use evaluation",
    "deep research agent benchmark",
    "agent-as-a-judge evaluation",
    "LLM coding agent benchmark SWE",
    "agentic AI security vulnerability assessment",
]

SCOUT_REPORT_DIR = DEFAULT_WORKSPACE.root / "data" / "daily_scouts"
SEEN_PAPERS_FILE = DEFAULT_WORKSPACE.root / "data" / "seen_papers.json"


def load_seen_papers() -> set:
    """Load previously seen paper IDs."""
    if SEEN_PAPERS_FILE.exists():
        data = json.loads(SEEN_PAPERS_FILE.read_text(encoding="utf-8"))
        return set(data.get("seen_ids", []))
    return set()


def save_seen_papers(seen: set):
    """Save seen paper IDs."""
    SEEN_PAPERS_FILE.parent.mkdir(parents=True, exist_ok=True)
    SEEN_PAPERS_FILE.write_text(
        json.dumps({"seen_ids": sorted(seen), "last_updated": datetime.now().isoformat()}, indent=2),
        encoding="utf-8",
    )


def run_daily_scout(
    topics: list[str] | None = None,
    from_year: int = 2025,
    seed_limit: int = 5,
    neighbors_per_seed: int = 10,
    include_semantic_scholar: bool = True,
) -> dict:
    """Run discovery across all topics and return deduplicated new findings."""
    topics = topics or DEFAULT_TOPICS
    seen = load_seen_papers()
    all_candidates = []
    all_seeds = []
    errors = []

    print(f"[scout] Daily Scout - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"[scout] Scouting {len(topics)} topics (from_year={from_year}, semantic_scholar={include_semantic_scholar})")
    print("-" * 60)

    for i, topic in enumerate(topics, 1):
        print(f"\n[{i}/{len(topics)}] >> {topic}")
        try:
            result = discover_from_query(
                query=topic,
                seed_limit=seed_limit,
                neighbors_per_seed=neighbors_per_seed,
                from_year=from_year,
                include_semantic_scholar=include_semantic_scholar,
            )
            seeds = result.get("seeds", [])
            candidates = result.get("candidates", [])
            all_seeds.extend(seeds)

            # Filter to new papers only
            new_for_topic = []
            for c in candidates:
                paper_id = c.get("openalex_id") or c.get("url") or c.get("title", "")
                if paper_id not in seen:
                    new_for_topic.append(c)
                    seen.add(paper_id)

            all_candidates.extend(new_for_topic)
            print(f"   Seeds: {len(seeds)} | Candidates: {len(candidates)} | New: {len(new_for_topic)}")

            for pe in result.get("provider_errors", []):
                errors.append(f"{topic}: {pe}")

        except Exception as e:
            err_msg = f"{topic}: {type(e).__name__}: {e}"
            errors.append(err_msg)
            print(f"   WARNING: {e}")

    # Deduplicate across topics by title similarity
    unique_candidates = _deduplicate_by_title(all_candidates)

    # Sort by score descending
    unique_candidates.sort(key=lambda x: x.get("score", 0), reverse=True)

    # Save seen papers
    save_seen_papers(seen)

    report = {
        "date": datetime.now().isoformat(),
        "topics_searched": len(topics),
        "total_seeds": len(all_seeds),
        "total_candidates_raw": len(all_candidates),
        "total_candidates_unique": len(unique_candidates),
        "errors": errors,
        "top_papers": unique_candidates[:30],  # Keep top 30
    }

    return report


def _deduplicate_by_title(candidates: list[dict]) -> list[dict]:
    """Remove duplicates by normalized title."""
    seen_titles = set()
    unique = []
    for c in candidates:
        title_norm = c.get("title", "").lower().strip()
        if title_norm and title_norm not in seen_titles:
            seen_titles.add(title_norm)
            unique.append(c)
    return unique


def save_report(report: dict):
    """Save daily scout report to data/daily_scouts/."""
    SCOUT_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    report_file = SCOUT_REPORT_DIR / f"scout_{date_str}.json"
    report_file.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n[save] Report saved: {report_file.relative_to(DEFAULT_WORKSPACE.root)}")

    # Also write a human-readable markdown summary
    md_file = SCOUT_REPORT_DIR / f"scout_{date_str}.md"
    lines = [
        f"# Daily Scout Report - {date_str}",
        "",
        f"- **Topics searched:** {report['topics_searched']}",
        f"- **Seeds found:** {report['total_seeds']}",
        f"- **New unique papers:** {report['total_candidates_unique']}",
        "",
    ]

    if report["errors"]:
        lines.append("## Errors")
        for err in report["errors"]:
            lines.append(f"- {err}")
        lines.append("")

    lines.append("## Top New Papers")
    lines.append("")
    lines.append("| # | Title | Year | Score | Citations | Source |")
    lines.append("|---|-------|------|-------|-----------|--------|")

    for i, paper in enumerate(report["top_papers"][:30], 1):
        title = paper.get("title", "Unknown")[:80]
        year = paper.get("year", "?")
        score = f"{paper.get('score', 0):.2f}"
        cites = paper.get("citation_count", 0)
        url = paper.get("url", "")
        via = paper.get("via", "")
        lines.append(f"| {i} | [{title}]({url}) | {year} | {score} | {cites} | {via} |")

    lines.append("")
    lines.append("---")
    lines.append(f"*Generated by EvaPaper Daily Scout at {datetime.now().strftime('%H:%M')}*")

    md_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"[save] Markdown summary: {md_file.relative_to(DEFAULT_WORKSPACE.root)}")


# ---------------------------------------------------------------------------
# INTEGRATION: Update all deliverables when new papers are found
# ---------------------------------------------------------------------------

# Relevance filter: only papers matching these terms get integrated into reports
_RELEVANCE_TERMS = {
    "agent", "llm", "language model", "governance", "benchmark", "evaluation",
    "safety", "security", "trust", "sandbox", "runtime", "skill", "tool use",
    "multi-agent", "autonomous", "alignment", "guardrail", "prompt injection",
    "specification", "validation", "policy", "authorization", "audit",
    "adversarial", "red team", "vulnerability", "attack", "defense",
    "coding agent", "web agent", "embodied agent", "robot",
    "mcp", "protocol", "framework", "orchestrat", "agentic",
}

# Irrelevant domains to reject
_IRRELEVANT_TERMS = {
    "biobank", "cancer imaging", "radiomics", "biopython", "bioinformatics",
    "clinical trial", "drug discovery", "peptide", "genomic", "molecular biology",
    "medical imaging", "radiology", "oncology", "pathology", "surgical",
    "ecology", "agriculture", "astronomy", "geology", "chemistry",
    "materials science", "quantum computing", "condensed matter",
    "laundry", "cooking", "weather forecast",
}


def _is_relevant_paper(paper: dict) -> bool:
    """Filter out papers not relevant to AI agent governance/evaluation."""
    text = f"{paper.get('title', '')} {paper.get('abstract', '')}".lower()
    topics = " ".join(paper.get("topics", [])).lower()
    full_text = f"{text} {topics}"

    # Reject if clearly irrelevant domain
    if any(t in full_text for t in _IRRELEVANT_TERMS):
        return False

    # Accept if matches relevance terms
    relevance_hits = sum(1 for t in _RELEVANCE_TERMS if t in full_text)
    return relevance_hits >= 2  # Need at least 2 relevance signals


# Layer inference terms (same as integrate_graph_candidates.py)
_STATIC_TERMS = {"certificate", "certificates", "cryptographic", "fingerprint", "identity",
                 "registry", "skillbom", "validity", "validation", "specification", "schema",
                 "contract", "lint", "static", "skill.md", "manifest"}
_RUNTIME_TERMS = {"constrain", "execution", "harness", "monitor", "orchestrate", "runtime",
                  "sandbox", "policy enforcement", "authorization", "audit"}
_BEHAVIORAL_TERMS = {"behavior", "benchmark", "evaluation", "feedback", "mining",
                     "reinforcement", "trustworthiness", "red team", "safety"}


def _infer_layer(paper: dict) -> str:
    """Classify a paper into governance layer 0/1/2."""
    text = f"{paper.get('title', '')} {paper.get('abstract', '')}".lower()
    s = sum(t in text for t in _STATIC_TERMS)
    r = sum(t in text for t in _RUNTIME_TERMS)
    b = sum(t in text for t in _BEHAVIORAL_TERMS)
    if s >= max(r, b):
        return "Layer 0 (Spec-Level)"
    if r >= b:
        return "Layer 1 (Runtime-Level)"
    return "Layer 2 (Behavioral-Level)"


def _extract_arxiv_id(paper: dict) -> str:
    """Try to extract arXiv ID from paper data."""
    import re
    for field in ("url", "openalex_id", "paper_id"):
        val = str(paper.get(field, ""))
        m = re.search(r"(\d{4}\.\d{4,5})", val)
        if m:
            return m.group(1)
    return ""


def integrate_into_scout_log(papers: list[dict]):
    """Append new papers to the scout log markdown."""
    scout_log = DEFAULT_WORKSPACE.scout_log
    if not scout_log.exists():
        scout_log.parent.mkdir(parents=True, exist_ok=True)
        scout_log.write_text("# Agent Governance Scout Log\n\n", encoding="utf-8")

    date_str = datetime.now().strftime("%Y-%m-%d")
    date_token = datetime.now().strftime("%m%d")

    section_lines = [
        "",
        f"## {date_str} Daily Scout Run",
        f"Status: **NEW FINDINGS FOUND** ({len(papers)} papers)",
        "",
        f"### New Papers (Found: {date_token})",
    ]

    for i, paper in enumerate(papers, 1):
        title = paper.get("title", "Unknown")
        arxiv_id = _extract_arxiv_id(paper)
        year = paper.get("year", "n.d.")
        layer = _infer_layer(paper)
        url = paper.get("url", "")
        score = paper.get("score", 0)
        cites = paper.get("citation_count", 0)

        if arxiv_id:
            section_lines.append(
                f"{i}. **{title}** (arXiv:{arxiv_id}) - {year}. "
                f"Score={score:.2f}, Citations={cites}. "
                f"URL: {url} - **{layer}**"
            )
        else:
            section_lines.append(
                f"{i}. **{title}** - {year}. "
                f"Score={score:.2f}, Citations={cites}. "
                f"URL: {url} - **{layer}**"
            )

    section_lines.append("")

    content = scout_log.read_text(encoding="utf-8")
    content = content.rstrip() + "\n" + "\n".join(section_lines) + "\n"
    scout_log.write_text(content, encoding="utf-8")
    print(f"[integrate] Scout log updated with {len(papers)} papers")


def integrate_into_main_report(papers: list[dict]):
    """Append new papers to AI_Agent_Governance_Three_Layer_Stack_and_Papers.md."""
    report_md = DEFAULT_WORKSPACE.report_md
    if not report_md.exists():
        print("[integrate] WARNING: Main report not found, skipping")
        return

    date_str = datetime.now().strftime("%Y-%m-%d")
    content = report_md.read_text(encoding="utf-8")

    section_lines = [
        "",
        f"### {date_str} Daily Scout: {len(papers)} newly surfaced papers",
        "",
    ]

    for i, paper in enumerate(papers, 1):
        title = paper.get("title", "Unknown")
        arxiv_id = _extract_arxiv_id(paper)
        year = paper.get("year", "n.d.")
        layer = _infer_layer(paper)
        url = paper.get("url", "")
        cites = paper.get("citation_count", 0)
        topics = ", ".join(paper.get("topics", [])[:3]) if paper.get("topics") else ""

        lines = [f"{i}. **{title}**"]
        if arxiv_id:
            lines[0] += f" (`arXiv:{arxiv_id}`)"
        lines.append(f"   - Year: {year} | Citations: {cites} | {layer}")
        if url:
            lines.append(f"   - URL: {url}")
        if topics:
            lines.append(f"   - Topics: {topics}")
        lines.append(f"   - Why relevant: Discovered via daily scout graph expansion; classified as {layer}")
        lines.append("")
        section_lines.extend(lines)

    # Insert after the executive summary section (before first ## that isn't exec summary)
    # Find a good insertion point - append before the last line
    content = content.rstrip() + "\n" + "\n".join(section_lines) + "\n"
    report_md.write_text(content, encoding="utf-8")
    print(f"[integrate] Main report MD updated")


def integrate_into_three_questions(papers: list[dict]):
    """Append new papers to Agent_Governance_Three_Questions_Synthesis.md."""
    three_q = DEFAULT_WORKSPACE.root / "Agent_Governance_Three_Questions_Synthesis.md"
    if not three_q.exists():
        print("[integrate] WARNING: Three Questions Synthesis not found, skipping")
        return

    date_str = datetime.now().strftime("%Y-%m-%d")
    content = three_q.read_text(encoding="utf-8")

    # Group papers by layer
    by_layer = {"Layer 0 (Spec-Level)": [], "Layer 1 (Runtime-Level)": [], "Layer 2 (Behavioral-Level)": []}
    for paper in papers:
        layer = _infer_layer(paper)
        by_layer[layer].append(paper)

    section_lines = [
        "",
        "---",
        "",
        f"## {date_str} Daily Scout Update",
        "",
        f"New papers discovered: **{len(papers)}** across governance layers.",
        "",
    ]

    for layer, layer_papers in by_layer.items():
        if not layer_papers:
            continue
        section_lines.append(f"### {layer} ({len(layer_papers)} papers)")
        section_lines.append("")
        for p in layer_papers[:10]:  # Cap per layer
            title = p.get("title", "Unknown")
            arxiv_id = _extract_arxiv_id(p)
            year = p.get("year", "n.d.")
            ref = f" (arXiv:{arxiv_id})" if arxiv_id else ""
            section_lines.append(f"- **{title}**{ref} - {year}")
        section_lines.append("")

    section_lines.append(
        "*These papers were auto-discovered by the daily scout and classified by keyword-based layer inference. "
        "Manual review recommended for governance question mapping.*"
    )
    section_lines.append("")

    content = content.rstrip() + "\n" + "\n".join(section_lines) + "\n"
    three_q.write_text(content, encoding="utf-8")
    print(f"[integrate] Three Questions Synthesis MD updated")


def integrate_into_research_html(papers: list[dict]):
    """Add new paper entries to ai-agent-governance-research.html."""
    import re
    html_path = DEFAULT_WORKSPACE.root / "ai-agent-governance-research.html"
    if not html_path.exists():
        print("[integrate] WARNING: Research HTML not found, skipping")
        return

    content = html_path.read_text(encoding="utf-8")

    # Build paper card entries to inject into the HTML
    date_str = datetime.now().strftime("%Y-%m-%d")
    new_entries = []
    for paper in papers[:20]:  # Top 20 into HTML
        title = paper.get("title", "Unknown").replace('"', '&quot;').replace('<', '&lt;')
        arxiv_id = _extract_arxiv_id(paper)
        year = paper.get("year", "n.d.")
        layer = _infer_layer(paper)
        url = paper.get("url", "")
        cites = paper.get("citation_count", 0)
        layer_class = "layer0" if "0" in layer else ("layer1" if "1" in layer else "layer2")

        entry = (
            f'        <!-- Daily Scout {date_str} -->\n'
            f'        <div class="paper-card {layer_class}" data-year="{year}" data-layer="{layer_class}">\n'
            f'          <h3>{title}</h3>\n'
            f'          <div class="paper-meta">\n'
            f'            <span class="year">{year}</span>\n'
            f'            <span class="layer-badge">{layer}</span>\n'
            f'            <span class="citations">{cites} citations</span>\n'
            f'          </div>\n'
        )
        if arxiv_id:
            entry += f'          <a href="https://arxiv.org/abs/{arxiv_id}" target="_blank">arXiv:{arxiv_id}</a>\n'
        elif url:
            entry += f'          <a href="{url}" target="_blank">Link</a>\n'
        entry += '        </div>\n'
        new_entries.append(entry)

    if not new_entries:
        return

    # Find insertion point - look for the papers container or a comment marker
    insertion_block = "\n".join(new_entries)

    # Try to find a papers section/container to insert into
    # Look for </section> or a marker we can append before
    marker_patterns = [
        r'(<!-- END PAPERS -->)',
        r'(</section>\s*<!-- papers -->)',
        r'(<section[^>]*id="papers"[^>]*>)',
    ]

    inserted = False
    for pattern in marker_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            pos = match.start()
            content = content[:pos] + insertion_block + "\n" + content[pos:]
            inserted = True
            break

    if not inserted:
        # Fallback: insert before closing </main> or </body>
        for tag in ("</main>", "</body>"):
            pos = content.rfind(tag)
            if pos > 0:
                content = content[:pos] + f'\n    <!-- Daily Scout {date_str}: {len(new_entries)} new papers -->\n' + insertion_block + "\n" + content[pos:]
                inserted = True
                break

    if inserted:
        html_path.write_text(content, encoding="utf-8")
        print(f"[integrate] Research HTML updated with {len(new_entries)} paper cards")
    else:
        print("[integrate] WARNING: Could not find insertion point in research HTML")


def regenerate_dashboard():
    """Regenerate governance-dashboard.html from the updated report and scout log."""
    try:
        from governance_dashboard import write_dashboard
        data = write_dashboard(DEFAULT_WORKSPACE.report_md, DEFAULT_WORKSPACE.scout_log)
        print(
            f"[integrate] Dashboard regenerated: {data['paper_count']} papers, "
            f"{data['scout_run_count']} scout runs"
        )
    except Exception as e:
        print(f"[integrate] WARNING: Dashboard regeneration failed: {e}")


def rebuild_corpus_index():
    """Rebuild the paper corpus index so question_map picks up new papers."""
    try:
        from paper_corpus import build_index
        records = build_index()
        print(f"[integrate] Corpus index rebuilt: {len(records)} papers indexed")
    except Exception as e:
        print(f"[integrate] WARNING: Corpus rebuild failed: {e}")


def integrate_all(papers: list[dict]):
    """
    Full integration pipeline: update ALL deliverables when new papers are found.

    Filters papers for relevance first — only AI agent governance/evaluation
    papers get integrated into reports. Irrelevant papers (medical, biology, etc.)
    are kept in the daily scout JSON but NOT pushed to curated deliverables.

    Updates:
      1. Scout log (memory/agent_governance_scout_log.md)
      2. Main report (AI_Agent_Governance_Three_Layer_Stack_and_Papers.md)
      3. Three Questions Synthesis (Agent_Governance_Three_Questions_Synthesis.md)
      4. Research HTML (ai-agent-governance-research.html)
      5. Governance Dashboard HTML (governance-dashboard.html) - regenerated
      6. Paper corpus index (data/paper_corpus.json) - rebuilt
    """
    if not papers:
        print("[integrate] No new papers to integrate.")
        return

    # FILTER: Only integrate relevant papers into curated reports
    relevant = [p for p in papers if _is_relevant_paper(p)]
    rejected = len(papers) - len(relevant)

    print(f"\n{'='*60}")
    print(f"INTEGRATING PAPERS INTO ALL DELIVERABLES")
    print(f"{'='*60}")
    print(f"  Total candidates: {len(papers)}")
    print(f"  Relevant (passing filter): {len(relevant)}")
    print(f"  Rejected (irrelevant domain): {rejected}")

    if not relevant:
        print("[integrate] No relevant papers passed the filter. Skipping integration.")
        return

    integrate_into_scout_log(relevant)
    integrate_into_main_report(relevant)
    integrate_into_three_questions(relevant)
    integrate_into_research_html(relevant)
    regenerate_dashboard()
    rebuild_corpus_index()

    print(f"\n[integrate] All deliverables updated with {len(relevant)} relevant papers.")


def main():
    parser = argparse.ArgumentParser(description="EvaPaper Daily Paper Scout")
    parser.add_argument("--topics", nargs="+", help="Override default topics")
    parser.add_argument("--from-year", type=int, default=2025, help="Minimum publication year")
    parser.add_argument("--seed-limit", type=int, default=5, help="Seeds per topic")
    parser.add_argument("--neighbors-per-seed", type=int, default=10, help="Neighbors per seed")
    parser.add_argument("--no-s2", action="store_true", help="Disable Semantic Scholar (enabled by default)")
    parser.add_argument("--deep", action="store_true", help="Run deep research pass on top papers (Scout-inspired)")
    parser.add_argument("--deep-top-k", type=int, default=15, help="How many papers to deep-research")
    parser.add_argument("--commit", action="store_true", help="Git commit results")
    parser.add_argument("--push", action="store_true", help="Git push after commit")
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    args = parser.parse_args()

    report = run_daily_scout(
        topics=args.topics,
        from_year=args.from_year,
        seed_limit=args.seed_limit,
        neighbors_per_seed=args.neighbors_per_seed,
        include_semantic_scholar=not args.no_s2,
    )

    save_report(report)

    # If new papers found, integrate into ALL deliverables (MDs + HTMLs + dashboard)
    if report["top_papers"]:
        integrate_all(report["top_papers"])

    # Optional: Deep research pass (Scout-inspired multi-agent pattern)
    if args.deep and report["top_papers"]:
        try:
            from deep_research_pass import run_deep_research
            top_papers = report["top_papers"][:args.deep_top_k]
            run_deep_research(top_papers, topic="daily scout deep dive")
        except Exception as e:
            print(f"[deep-research] WARNING: Deep research pass failed: {e}")

    # Print summary
    print("\n" + "=" * 60)
    print("DAILY SCOUT SUMMARY")
    print("=" * 60)
    print(f"Topics: {report['topics_searched']}")
    print(f"Seeds: {report['total_seeds']}")
    print(f"New unique papers: {report['total_candidates_unique']}")

    if report["top_papers"]:
        print(f"\nTop 5 new papers:")
        for i, paper in enumerate(report["top_papers"][:5], 1):
            title = paper.get("title", "Unknown")
            year = paper.get("year", "?")
            score = paper.get("score", 0)
            print(f"   {i}. {title} ({year}) [score={score:.2f}]")
            if paper.get("url"):
                print(f"      {paper['url']}")

    if report["errors"]:
        print(f"\nWARNING: {len(report['errors'])} error(s) during scouting")

    if args.json:
        print("\n" + json.dumps(report, indent=2))

    if args.commit:
        import subprocess, os
        os.chdir(DEFAULT_WORKSPACE.root)
        # Stage ALL deliverables that may have been updated
        files_to_add = [
            "data/daily_scouts/",
            "data/seen_papers.json",
            "data/paper_corpus.json",
            "data/governance_dashboard.json",
            "memory/agent_governance_scout_log.md",
            "AI_Agent_Governance_Three_Layer_Stack_and_Papers.md",
            "Agent_Governance_Three_Questions_Synthesis.md",
            "ai-agent-governance-research.html",
            "governance-dashboard.html",
        ]
        for f in files_to_add:
            p = DEFAULT_WORKSPACE.root / f
            if p.exists() or p.is_dir():
                subprocess.run(["git", "add", f], capture_output=True, cwd=str(DEFAULT_WORKSPACE.root))

        date_str = datetime.now().strftime("%Y-%m-%d")
        n_papers = report['total_candidates_unique']
        result = subprocess.run(
            ["git", "commit", "-m",
             f"feat: daily scout {date_str} - {n_papers} new papers integrated\n\n"
             f"Updated: scout log, main report MD, three questions MD,\n"
             f"research HTML, governance dashboard HTML, corpus index."],
            capture_output=True, text=True, cwd=str(DEFAULT_WORKSPACE.root),
        )
        if "nothing to commit" not in (result.stdout + result.stderr):
            print("Committed all updated deliverables")
            if args.push:
                subprocess.run(["git", "push"], capture_output=True, cwd=str(DEFAULT_WORKSPACE.root))
                print("Pushed to remote")
        else:
            print("Nothing new to commit")

    return 0


if __name__ == "__main__":
    sys.exit(main())
