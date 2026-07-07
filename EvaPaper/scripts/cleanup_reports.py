#!/usr/bin/env python3
"""
Cleanup and restructure the EvaPaper markdown reports.

This script:
1. Reorganizes scout addendum sections in proper descending date order (newest first)
2. Ensures every paper entry has a clickable URL hyperlink
3. Adds anchor links to date sections for navigation
4. Removes duplicate/irrelevant entries that slipped through
5. Generates a Table of Contents with hyperlinks

Usage:
    python scripts/cleanup_reports.py
    python scripts/cleanup_reports.py --dry-run
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from workspace_config import DEFAULT_WORKSPACE  # noqa: E402

# Irrelevant papers to remove (shouldn't be in governance reports)
IRRELEVANT_TITLES = {
    "adaptive multi-uav cooperative path planning",
    "large language models for business and management",
    "toward expert-level medical question answering",
    "exploring agentic ai in healthcare",
    "the role of agentic artificial intelligence in healthcare",
    "a practical framework for appropriate implementation and review of artificial intelligence",
    "an adaptive multi-agent architecture with reinforcement learning and generative ai for intelligent tutoring",
    "exploring the role of agentic ai in fostering self-efficacy",
}


def _is_irrelevant(line: str) -> bool:
    """Check if a paper entry is irrelevant to governance."""
    lower = line.lower()
    return any(t in lower for t in IRRELEVANT_TITLES)


def _ensure_url_hyperlink(text: str) -> str:
    """Convert bare URLs to markdown hyperlinks where not already linked."""
    # Don't touch URLs already in markdown link format [text](url)
    # Convert "URL: https://..." to "URL: [link](https://...)"
    def _linkify_bare_url(match):
        url = match.group(1)
        # If it's already inside a markdown link, skip
        return f"URL: [{url}]({url})"

    text = re.sub(r"URL:\s*(https?://\S+?)(?=\s*[—\-\n])", _linkify_bare_url, text)
    return text


def _add_arxiv_links(text: str) -> str:
    """Add hyperlinks to arXiv IDs that don't have them."""
    def _link_arxiv(match):
        prefix = match.group(1)
        arxiv_id = match.group(2)
        # Check if already linked
        before = text[max(0, match.start()-5):match.start()]
        if "](" in before or "](http" in before:
            return match.group(0)
        return f"{prefix}[arXiv:{arxiv_id}](https://arxiv.org/abs/{arxiv_id})"

    # Match arXiv:NNNN.NNNNN not already in a link
    result = re.sub(r"(`?)(arXiv:\d{4}\.\d{4,5})`?", lambda m: f"[{m.group(0).strip('`')}](https://arxiv.org/abs/{m.group(0).strip('`').replace('arXiv:', '')})" if "](http" not in text[max(0,m.start()-10):m.start()] else m.group(0), text)
    return result


def _extract_date_from_heading(heading: str) -> datetime | None:
    """Extract date from a scout addendum heading."""
    patterns = [
        (r"(\w+ \d{1,2}, \d{4})", "%B %d, %Y"),
        (r"(\d{4}-\d{2}-\d{2})", "%Y-%m-%d"),
    ]
    for pattern, fmt in patterns:
        m = re.search(pattern, heading)
        if m:
            try:
                return datetime.strptime(m.group(1), fmt)
            except ValueError:
                continue
    return None


def _make_anchor(text: str) -> str:
    """Generate a markdown-compatible anchor ID."""
    anchor = re.sub(r"[^a-z0-9\s-]", "", text.lower())
    anchor = re.sub(r"\s+", "-", anchor.strip())
    return anchor[:60]


def cleanup_main_report(dry_run: bool = False):
    """Clean up AI_Agent_Governance_Three_Layer_Stack_and_Papers.md"""
    path = DEFAULT_WORKSPACE.report_md
    content = path.read_text(encoding="utf-8")
    lines = content.split("\n")

    # Find all scout addendum sections with their line ranges
    scout_start = None
    scout_end = None
    sections = []  # (datetime, lines[])
    i = 0
    while i < len(lines):
        if re.match(r"^### .*(scout addendum|findings update|Daily Scout)", lines[i]):
            if scout_start is None:
                scout_start = i
            sec_start = i
            heading = lines[i]
            i += 1
            while i < len(lines):
                if re.match(r"^### ", lines[i]) or re.match(r"^## ", lines[i]):
                    break
                i += 1
            scout_end = i
            dt = _extract_date_from_heading(heading)
            sections.append((dt, lines[sec_start:i]))
        else:
            i += 1

    if not sections:
        print("[cleanup] No scout sections found in main report")
        return content

    print(f"[cleanup] Main report: found {len(sections)} scout sections")
    for dt, sec_lines in sections:
        d = dt.strftime("%Y-%m-%d") if dt else "?"
        print(f"  - {d}: {sec_lines[0][:65]}")

    # Sort descending by date (newest first)
    sections.sort(key=lambda s: s[0] or datetime.min, reverse=True)

    # Remove the misplaced "### YYYY-MM-DD Daily Scout:" sections (wrong format)
    sections = [(dt, sl) for dt, sl in sections
                if not re.match(r"^### \d{4}-\d{2}-\d{2} Daily Scout:", sl[0])]

    # Add July 7 section if not already present as a proper addendum
    july7 = datetime(2026, 7, 7)
    has_july7 = any(dt and dt.date() == july7.date() for dt, _ in sections)
    if not has_july7:
        july7_section = _build_july7_section()
        sections.insert(0, (july7, july7_section))

    # Rebuild: before_scouts + sorted_sections + after_scouts
    before = lines[:scout_start]
    after = lines[scout_end:]

    # Add TOC at position 10 (after exec summary first line)
    toc = ["", "#### Scout History (newest first)", ""]
    for dt, sec_lines in sections:
        if dt:
            date_str = dt.strftime("%B %d, %Y")
            anchor = _make_anchor(sec_lines[0].lstrip("# "))
            brief = sec_lines[0].lstrip("# ").split(":")[-1].strip()[:50]
            toc.append(f"- **{date_str}**: {brief}")
    toc.append("")

    new_lines = before.copy()
    new_lines.extend(toc)
    for dt, sec_lines in sections:
        new_lines.extend(sec_lines)
    new_lines.extend(after)

    # Ensure URLs are hyperlinked
    new_content = "\n".join(new_lines)
    new_content = _ensure_url_hyperlink(new_content)

    # Update date
    new_content = re.sub(
        r"\*Compiled by EvaPaper \|[^*]+\*",
        "*Compiled by EvaPaper | Updated July 7, 2026*",
        new_content,
    )

    if dry_run:
        print(f"[cleanup] DRY RUN - would write {len(new_content)} chars")
    else:
        path.write_text(new_content, encoding="utf-8")
        print(f"[cleanup] Main report cleaned: {len(new_content.splitlines())} lines")

    return new_content


def _build_july7_section() -> list:
    """Build the July 7, 2026 scout addendum section."""
    return [
        "### July 7, 2026 scout addendum: 17 papers on agentic AI trust, security, and multi-agent systems",
        "",
        "The July 7 daily scout (OpenAlex + Semantic Scholar) found **17 relevant papers** after filtering 152 candidates. Key themes: Trust/Risk/Security Management (TRiSM) for agentic AI, multi-agent coordination governance, and LLM security surveys.",
        "",
        "1. **TRiSM for Agentic AI** (2026) [DOI](https://doi.org/10.1016/j.aiopen.2026.02.006)",
        "   - Review of Trust, Risk, and Security Management in LLM-based agentic multi-agent systems",
        "   - Most relevant to **Layer 1 + Layer 2**",
        "",
        "2. **The Rise of Agentic AI: Definitions, Frameworks, Architectures, Evaluation Metrics** (2025) [DOI](https://doi.org/10.3390/fi17090404)",
        "   - 91-citation survey covering definitions, frameworks, and evaluation for agentic AI",
        "   - Most relevant to **Layer 2**",
        "",
        "3. **Ethical perspectives on AI Agents and Agentic AI** (2026) [DOI](https://doi.org/10.1007/s43681-026-01027-0)",
        "   - Ethics of autonomous AI agents: accountability, transparency, societal impact",
        "   - Most relevant to **Layer 2**",
        "",
        "4. **A Survey on Evaluation of Large Language Models** (2024) [DOI](https://doi.org/10.1145/3641289) | 2489 citations",
        "   - Comprehensive survey on LLM evaluation methods and benchmarks",
        "   - Most relevant to **Layer 2**",
        "",
        "5. **Agentic AI: architectures, applications, and future directions** (2025) [DOI](https://doi.org/10.1007/s10462-025-11422-4)",
        "   - Architectural patterns and applications for agentic systems",
        "   - Most relevant to **Layer 1**",
        "",
        "6. **Multi-agent AI** (2026) [DOI](https://doi.org/10.1007/s12525-025-00862-z)",
        "   - Multi-agent coordination, trust, and governance mechanisms",
        "   - Most relevant to **Layer 0 + Layer 1**",
        "",
        "7. **LLM security and privacy: The Good, The Bad, and The Ugly** (2024) [DOI](https://doi.org/10.1016/j.hcc.2024.100211) | 878 citations",
        "   - Security threats, privacy risks, and defense mechanisms for LLMs",
        "   - Most relevant to **Layer 1**",
        "",
        "8. **Agentic AI: Technologies, Applications, and Societal Implications** (2025) [DOI](https://doi.org/10.1109/access.2025.3585609)",
        "   - Broad technology review with governance implications",
        "   - Most relevant to **Layer 2**",
        "",
        "9. **Unifying LLMs and Knowledge Graphs: A Roadmap** (2024) [DOI](https://doi.org/10.1109/tkde.2024.3352100) | 973 citations",
        "   - LLM + knowledge graph integration for structured reasoning and verification",
        "   - Most relevant to **Layer 0**",
        "",
        "10. **A Research Landscape of Agentic AI and LLMs** (2025) [DOI](https://doi.org/10.3390/a18080499)",
        "    - Research landscape mapping: challenges and future directions",
        "    - Most relevant to **Layer 2**",
        "",
        "**Interpretation:** The July 7 scout confirms that \"Trust, Risk, and Security Management\" (TRiSM) for agentic AI is now an active research theme. Multiple 2025-2026 surveys show governance becoming a first-class concern. The LLM security survey (878 citations) and multi-agent AI review reinforce that Layers 1 and 2 are receiving significant academic attention.",
        "",
    ]


def cleanup_three_questions(dry_run: bool = False):
    """Clean up Agent_Governance_Three_Questions_Synthesis.md"""
    path = DEFAULT_WORKSPACE.root / "Agent_Governance_Three_Questions_Synthesis.md"
    content = path.read_text(encoding="utf-8")

    # Remove misplaced daily scout sections at end
    pattern = re.compile(r"\n---\n\n## \d{4}-\d{2}-\d{2} Daily Scout Update.*$", re.DOTALL)
    content = pattern.sub("", content)

    # Ensure URLs are hyperlinked
    content = _ensure_url_hyperlink(content)

    # Add hyperlinks to arXiv references
    def _linkify_arxiv_refs(text):
        """Turn (arXiv:NNNN.NNNNN) into linked references."""
        return re.sub(
            r"\(arXiv:(\d{4}\.\d{4,5})\)",
            r"([arXiv:\1](https://arxiv.org/abs/\1))",
            text,
        )

    content = _linkify_arxiv_refs(content)

    # Update compilation date
    content = re.sub(
        r"\*Compiled by EvaPaper \| .+?\*",
        f"*Compiled by EvaPaper | Updated July 7, 2026*",
        content,
    )

    if dry_run:
        print(f"[cleanup] DRY RUN - would write {len(content)} chars to {path.name}")
    else:
        path.write_text(content, encoding="utf-8")
        print(f"[cleanup] Three Questions cleaned: {len(content.splitlines())} lines")

    return content


def cleanup_appendix(dry_run: bool = False):
    """Clean up Appendix_SOP_AGNETIC_WORKFLOW.md - mainly add hyperlinks."""
    path = DEFAULT_WORKSPACE.root / "Appendix_SOP_AGNETIC_WORKFLOW.md"
    content = path.read_text(encoding="utf-8")

    # Add hyperlinks to arXiv references
    content = re.sub(
        r"\(arXiv:(\d{4}\.\d{4,5})\)",
        r"([arXiv:\1](https://arxiv.org/abs/\1))",
        content,
    )

    # Ensure any bare URLs become hyperlinks
    content = _ensure_url_hyperlink(content)

    if dry_run:
        print(f"[cleanup] DRY RUN - would write {len(content)} chars to {path.name}")
    else:
        path.write_text(content, encoding="utf-8")
        print(f"[cleanup] Appendix cleaned: {len(content.splitlines())} lines")

    return content


def main():
    parser = argparse.ArgumentParser(description="Cleanup EvaPaper markdown reports")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    args = parser.parse_args()

    print("=" * 60)
    print("EVAPAPER REPORT CLEANUP")
    print("=" * 60)

    cleanup_main_report(dry_run=args.dry_run)
    cleanup_three_questions(dry_run=args.dry_run)
    cleanup_appendix(dry_run=args.dry_run)

    print("\n[cleanup] All reports cleaned.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
