---
name: analyze-research-gaps
description: Analyze the EvaPaper agent-governance corpus after a scout update and produce ranked, evidence-backed missing areas and research opportunities for the HTML dashboard. Use when a scout finds new papers, when the dashboard opportunity analysis is stale, or when asked what the corpus has not explored enough and what should be researched next.
---

# Analyze Research Gaps

Produce LLM reasoning as structured data. Do not hard-code conclusions in the dashboard.

## Workflow

1. Read:
   - `data/governance_dashboard.json`
   - `data/paper_corpus.json`
   - `memory/agent_governance_scout_log.md`
   - `AI_Agent_Governance_Three_Layer_Stack_and_Papers.md`
2. Read [references/opportunity-schema.md](references/opportunity-schema.md).
3. Assess gaps using all five signals:
   - **Coverage scarcity:** low topic/layer counts or missing intersections.
   - **Graph structure:** weakly connected clusters, orphan concerns, or missing bridges.
   - **Evidence maturity:** conceptual proposals without benchmarks, replications, deployments, or longitudinal studies.
   - **Contradictions:** papers or benchmarks that disagree without resolution.
   - **Decision importance:** gaps that block trustworthy specification, deployment, evaluation, or governance.
4. Distinguish:
   - `corpus_gap`: relevant work may exist but EvaPaper has not captured it.
   - `field_gap`: the reviewed literature itself lacks convincing solutions.
   - `evidence_gap`: proposals exist but validation is weak.
   - `translation_gap`: research exists but operational tooling or standards are missing.
5. Rank 3-6 opportunities. A small category alone is not enough.
6. For every opportunity:
   - cite at least two corpus facts;
   - explain the inference from those facts;
   - state uncertainty and plausible counterevidence;
   - propose falsifiable research questions;
   - provide future scout search queries.
   - include a reproducible `coverage_check` with corpus query terms and matched titles.
7. Reconcile scope explicitly:
   - `data/paper_corpus.json` may include papers, products, standards, and duplicate title variants.
   - `data/governance_dashboard.json` is the deduplicated scholarly-ID paper subset.
   - Record both totals and state which one supports each claim.
8. Write `data/research_opportunities.json`.
9. Run:

```bash
python3 skills/analyze-research-gaps/scripts/validate_opportunities.py data/research_opportunities.json
python3 scripts/governance_dashboard.py
```

## Reasoning Rules

- Never claim exhaustive field coverage from this corpus.
- Phrase absence as "the current corpus does not contain" unless external search establishes a field-wide absence.
- Never treat discovery count as publication count.
- Never describe conceptual association edges as citations.
- Prefer specific missing intersections over vague topics.
- Separate observed evidence from LLM inference.
- Lower confidence when source summaries are thin or classifications are ambiguous.
- Update the artifact only after a scout run with accepted new findings, unless explicitly asked for a manual reassessment.
- If no ranking changes materially, refresh the snapshot date and explain why priorities stayed stable.

## Output Quality

Good:

- "Layer 3 has five papers, but the stronger signal is that none provides longitudinal post-deployment incident data; this is an evidence gap."

Bad:

- "Layer 3 is small, so more research is needed."
