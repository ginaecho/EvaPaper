# EvaPaper — Copilot Agent Instructions

## What This Repo Is

A living research archive on **AI Agent Governance**. The agent's job is to
scout for new papers, classify them, and integrate findings into curated
reports (markdown + HTML).

## Critical Rules (Learned the Hard Way — 2026-07-07)

### 1. EVERY paper entry MUST have a clickable URL

- arXiv: `[arXiv:NNNN.NNNNN](https://arxiv.org/abs/NNNN.NNNNN)`
- DOI: `[DOI](https://doi.org/10.xxxx/...)`
- **NEVER** extract arXiv IDs from DOI numbers. The regex `\d{4}\.\d{4,5}`
  matches DOI fragments like `1896.37365` (from `doi.org/10.1145/3711896.3736570`)
  which are NOT arXiv IDs. Only extract from `arxiv.org` URLs.

### 2. EVERY date section MUST be linked from a TOC

Each markdown report has a Table of Contents at the top. When adding a new
scout section:
- Add a TOC entry: `- [**July 8, 2026** — N papers: topic](#anchor-link)`
- The anchor must match the heading (lowercase, hyphens, no punctuation)
- TOC entries must be in **descending date order** (newest first)

### 3. Date sections must be in DESCENDING order

New scout addenda go at the TOP of the scout section list, not appended
at the bottom. Readers should see the latest findings first.

### 4. Relevance filter is MANDATORY

Never integrate irrelevant papers (medical imaging, bioinformatics,
chemistry, etc.) into curated reports. The filter requires ≥2 relevance
signals from: agent, llm, governance, benchmark, evaluation, safety,
security, trust, agentic, multi-agent, etc.

### 5. ALL deliverables must be updated together

When new papers are found, update ALL of these:
1. `EvaPaper/AI_Agent_Governance_Three_Layer_Stack_and_Papers.md`
2. `EvaPaper/Agent_Governance_Three_Questions_Synthesis.md`
3. `EvaPaper/ai-agent-governance-research.html`
4. `EvaPaper/governance-dashboard.html` (regenerated via script)

Do NOT stop after updating only one or two files.

### 6. Research HTML paper cards must be valid HTML

Format:
```html
<!-- Scout YYYY-MM-DD -->
<div class="paper-card layer2" data-year="2026" data-layer="layer2">
  <h3>Paper Title</h3>
  <div class="paper-meta">
    <span class="year">2026</span>
    <span class="layer-badge">Layer 2 (Behavioral-Level)</span>
    <span class="citations">23 citations</span>
  </div>
  <a href="https://doi.org/..." target="_blank" rel="noopener">DOI</a>
</div>
```

Never inject bare `<a>` tags without the full card structure.

### 7. Scout log format must use em-dash (—)

The dashboard parser (`paper_corpus.py`) expects:
```
N. **Title** (arXiv:ID) — body text. URL: https://... — **Layer X**
```
Using `-` instead of `—` will cause the parser to skip entries.

### 8. Scoring must favor recency

Papers from 2025-2026 should rank above highly-cited classics from 2001-2016.
The `compute_score` in `paper_graph.py` adds recency bonuses and penalizes
old highly-cited papers that aren't directly relevant.

## Key Scripts

| Script | Purpose |
|--------|---------|
| `scripts/daily_scout.py` | Daily paper scouting + integration |
| `scripts/paper_graph.py` | OpenAlex + Semantic Scholar discovery |
| `scripts/governance_dashboard.py` | Dashboard HTML regeneration |
| `scripts/paper_corpus.py` | Corpus index builder |
| `scripts/cleanup_reports.py` | Report reorganization + TOC generation |
| `scripts/deep_research_pass.py` | Multi-agent deep research |

## Make Targets

```bash
make daily-scout          # Standard daily scout
make daily-scout-deep     # With deep research pass
make scout QUERY="..."    # Single-topic scout
make dashboard            # Regenerate dashboard HTML
make index                # Rebuild corpus index
```

## Daily Schedule

- **Weekdays 9:00 AM**: Standard scout (OpenAlex + S2, filter, integrate, commit)
- **Weekends 9:00 AM**: Deep scout (standard + multi-agent research on top 20)
