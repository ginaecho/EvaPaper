# Scout Integration Skill — Auto-Integrate New Governance Findings
## Created: 2026-06-14
## Trigger: When new agent governance findings arrive (scout, research, or manual discovery)

## Standing Rule
> **When the Agent Governance Scout reports new findings, I MUST automatically integrate them into ALL deliverables — not just acknowledge them.**

## Integration Checklist (Run in Order)

### 1. HTML Page (`ai-agent-governance-research.html`)
- [ ] Add new paper cards to the `papers-scroll` gallery section
- [ ] Follow existing card structure: `paper-arxiv` → `paper-title` → `paper-layer` → `paper-finding` → optional `paper-opensource`
- [ ] Use `&mdash;` for em-dashes, `&amp;` for ampersands, `&ndash;` for en-dashes
- [ ] Stagger reveal delays: `reveal-delay-1` through `reveal-delay-5`, then loop
- [ ] Update layer pills in each `layer-card` to include new items
- [ ] Update paper count in the gallery header (e.g. "32 papers" → "40 papers")
- [ ] Update paper count in footer meta

### 2. Synthesis Markdown (`Agent_Governance_Three_Questions_Synthesis.md`)
- [ ] Add numbered entries under the relevant Question section (typically Question 3 for enforcement mechanisms)
- [ ] Include: deterministic status, coverage, mechanism, results, gap analysis
- [ ] Update comparison tables (Deterministic vs LLM-as-Judge, Missing Capabilities)
- [ ] Update Overall Assessment table if the finding changes any verdicts

### 3. Three-Layer Stack Markdown (`AI_Agent_Governance_Three_Layer_Stack_and_Papers.md`)
- [ ] Add findings to the Executive Summary addendum section
- [ ] Add full paper entries to the papers catalog section if this is the primary report

### 4. Regenerate Artifacts
- [ ] Run `make docs` — regenerates DOCX and PPTX from updated MD files
- [ ] Run `make dashboard` — refreshes `governance-dashboard.html`
- [ ] Verify no import errors (python-docx, python-pptx must be installed)

### 5. Git Commit & Push
- [ ] `cd /root/.openclaw/workspace/EvaPaper`
- [ ] Stage only EvaPaper files (do NOT stage parent workspace files like AGENTS.md, SOUL.md, etc.)
- [ ] Commit with descriptive message: "[Date] integration: N new governance papers into HTML, Synthesis MD, DOCX, PPTX, and dashboard"
- [ ] Push to origin/master

### 6. Documentation
- [ ] Update `memory/agent_governance_scout_log.md` with integration status
- [ ] Create or update task file in `skills/analyze-research-gaps/tasks/`
- [ ] Note any pending follow-up tasks

## Quick Reference: Paper Count History
- Baseline (Jun 7): ~24 papers
- Jun 12 additions: +2 (Learning Correct Behavior, Owner-Harm)
- Jun 14 additions: +8 (EmbodiedGovBench, Skill Trust Framework, OWASP MCP, MITRE ATLAS, NIST IR 8596, reprobe-audit, Agent Security Harness, WSP)
- Current total: 40 papers

## Automation Wishlist
- [ ] Script to auto-generate paper cards from structured data
- [ ] Script to auto-update paper counts across all files
- [ ] Script to auto-sync layer pills between HTML and MD
- [ ] Consider: make the HTML source data-driven (JSON → HTML templating) instead of hand-editing HTML
