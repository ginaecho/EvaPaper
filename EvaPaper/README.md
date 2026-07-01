# EvaPaper

**AI Agent Governance Research Archive**

> "Even if the world forgets, I'll remember for you." — EvaPaper

---

## What This Is

A living research archive on **AI Agent Governance**, **Skill Markdown Validation**, and **Agent Behavior Evaluation**. Born from a single conversation and kept alive by a weekly scout.

## Three-Layer Governance Stack

The core framework distilled from 8+ research papers and industry implementations:

| Layer | Name | Focus |
|-------|------|-------|
| **Layer 0** | **Spec-Level Governance** | SKILL.md validation, schema soundness, contractual boundaries |
| **Layer 1** | **Runtime-Level Governance** | Execution sandboxing, intent verification, inter-agent authorization, audit logging |
| **Layer 2** | **Behavioral-Level Governance** | Safety benchmarks, task evaluation, reward hacking detection, enterprise trustworthiness |

## Contents

### 📄 Reports
- `AI_Agent_Governance_Three_Layer_Stack_and_Papers.docx` — Full report with all paper summaries
- `AI_Agent_Governance_Three_Layer_Stack_and_Papers.pptx` — 22-slide deck with dark navy theme
- `governance-dashboard.html` — Self-contained visual dashboard for topic ratios and scout trends
- `data/governance_dashboard.json` — Machine-readable dashboard metrics
- `data/research_opportunities.json` — Ranked LLM analysis of underexplored areas

### 📚 Papers Summarized
| Paper | arXiv | Focus |
|-------|-------|-------|
| **BeSafe-Bench** | 2603.25747 | Behavioral safety in real-world environments |
| **ST-WebAgentBench** | 2410.06703 | Safety + trustworthiness in enterprise web agents |
| **Layered Governance Architecture (LGA)** | 2603.07191 | Four-layer security framework |
| **Skilldex** | 2604.16911 | Skill package manager + registry |
| **GovernSpec / Contractual Skills** | 2605.22634 | Goal boundaries, permissions, evidence in skills |
| **OWASP Top 10 for Agentic Apps** | 2026 Edition | Risk taxonomy for autonomous agents |
| **Microsoft Agent Governance Toolkit** | 2025 | Enterprise governance framework |
| **Agent Evaluation Guide** | 2026 | Quality-focused evaluation frameworks |

### 🤖 Scout Log
- `logs/agent_governance_scout_log.md` — Weekly search tracking, new findings go here

## Weekly Scout

A cron job runs every **Sunday at 03:17 AM (Asia/Shanghai)** to search for new papers, products, and frameworks. Findings are committed to this repo.

## Scripts
- `generate_governance_docs.py` — DOCX/PPTX generation script
- `generate_beautiful_pptx.py` — PPTX design template
- `scripts/workspace_config.py` — repo-relative shared paths and workspace config
- `scripts/paper_graph.py` — graph-backed paper discovery using OpenAlex, arXiv fallback search, and optional Semantic Scholar enrichment
- `scripts/scout.py --discover "..."` — generic scout entrypoint with configurable paths
- `scripts/paper_corpus.py` — builds a structured local corpus index from the markdown report
- `scripts/governance_dashboard.py` — classifies papers and regenerates dashboard data/HTML
- `skills/analyze-research-gaps/SKILL.md` — sub-agent workflow for evidence-backed gap analysis
- `scripts/question_map.py` — maps a user question to the papers in the local corpus with supporting evidence snippets
- `scripts/agent_team.py` — generic multi-agent orchestration entrypoint for scouting, corpus maintenance, and synthesis

## Graph-Backed Discovery

The repo did not have a paper graph layer before. It now has a small discovery path built around public scholarly graphs and live scholarly feeds:

- `OpenAlex` as the default graph backend:
  - open data
  - works, references, citing works, and algorithmic related works
  - no SDK dependency required in this repo
- `arXiv` as the no-key live fallback:
  - used when OpenAlex search is degraded or unavailable
  - returns recent seed/candidate papers with abstracts, URLs, and subject categories
  - keeps scout runs useful instead of silently falling back to only the local corpus
- `Semantic Scholar` as an optional second signal:
  - search and recommendations API
  - enable by setting `SEMANTIC_SCHOLAR_API_KEY`
  - no-key access is rate-limited, so the scout reports provider degradation instead of blocking indefinitely

Example:

```bash
python3 scripts/scout.py --discover "agent governance skill markdown validation" --from-year 2024
```

Or directly:

```bash
python3 scripts/paper_graph.py "agent governance skill markdown validation" --from-year 2024
```

The scout is now repo-relative and not tied to OpenClaw/Kimi-specific paths. Optional writeback is explicit:

```bash
python3 scripts/scout.py --discover "agent governance skill markdown validation" --from-year 2024
python3 scripts/scout.py --commit
python3 scripts/scout.py --commit --push
```

## Question-to-Paper Mapping

The second half of the workflow is local cross-checking after collection:

```bash
python3 scripts/paper_corpus.py
python3 scripts/question_map.py "which papers propose runtime enforcement rather than only evaluation?"
python3 scripts/question_map.py "which papers are about static checking of agent interactions?" --mode static
python3 scripts/question_map.py --sota --mode static --top-k 10
python3 scripts/question_map.py --sota --mode all --top-k 10
```

This works over the collected markdown corpus and returns:

- ranked papers
- whether the match is `direct`, `partial`, or `background`
- supporting snippets from the exact fields that matched

Focus modes:

- `--mode static`:
  spec validation, contractual skills, static interaction checking, pre-execution governance
- `--mode runtime`:
  runtime enforcement, sandboxing, protocol/tool execution controls
- `--mode behavioral`:
  benchmarks, trustworthiness, post-build evaluation
- `--mode all`:
  whole governance state of the art

## Agent Team Mode

The workflow can now run as a generic agent team rather than a single platform-specific agent shell:

```bash
python3 scripts/agent_team.py --query "agent governance skill markdown validation" --mode static
python3 scripts/agent_team.py --query "agent governance skill markdown validation" --question "which papers are about static checking of agent interactions?" --mode static
```

Built-in team roles:

- `scout`
- `librarian`
- `static_analyst`
- `runtime_analyst`
- `behavioral_analyst`
- `synthesizer`

Latest orchestration output:

- `data/agent_team/last_team_run.json`

## Easiest Workflow

The easiest way to run this repo now is through the root `Makefile`.

Common commands:

```bash
make help
make index
make dashboard
make opportunities-check
make sota-static
make sota-all
make ask-static QUESTION="which papers are about static checking of agent interactions?"
make team-static QUERY="agent governance skill markdown validation"
make workflow-static QUERY="agent governance skill markdown validation" QUESTION="which papers are about static checking of agent interactions?"
```

## Research Dashboard

Refresh the dashboard after editing the report or scout log:

```bash
make dashboard
```

The dashboard shows:

- the percentage of papers in each primary research topic
- cumulative topic growth across scout discovery dates
- multi-label coverage of governance Layers 0-3
- topics gaining the most attention in the latest three scout windows
- an interactive Obsidian-style association graph with search, filtering, pan, zoom, and paper details
- a Karpathy-style in-HTML wiki with overview, topic, layer, and paper pages
- ranked underexplored areas and research opportunities with explicit LLM reasoning
- a linked evidence ledger for every indexed paper

Each paper receives one primary topic so the topic ratio sums to 100%. Layer
coverage remains multi-label. The scout workflow regenerates the dashboard only
when new findings are written, preserving the existing no-change/no-update rule.

The association graph uses arXiv/DOI identifiers as stable node IDs. Each paper
keeps its strongest corpus neighbors based on shared primary topic, governance
layers, and technical terms. Every edge exposes its reason in the paper detail
panel. These conceptual links complement the OpenAlex citation graph used during
discovery; they are not presented as direct citation claims.

The wiki is compiled into the HTML from the authoritative report and scout log.
It contains a searchable index, one page per paper, topic and governance layer,
provenance, and cross-references. The graph links directly into those wiki pages.

Research opportunities are not produced by fixed counting rules. After a scout
finds accepted papers, a Claw sub-agent follows
`skills/analyze-research-gaps/SKILL.md`, writes
`data/research_opportunities.json`, validates it, and then regenerates the
dashboard. The HTML labels these conclusions as LLM reasoning over the current
corpus rather than proof that outside literature does not exist.

Useful variables:

- `QUERY`
- `QUESTION`
- `MODE`
- `TOP_K`
- `INPUT_TOKENS`
- `OUTPUT_TOKENS`
- `COST_USD`
- `COST_NOTE`

Examples:

```bash
make scout QUERY="agent governance skill markdown validation"
make ask MODE=runtime QUESTION="which papers propose runtime enforcement?"
make team MODE=all QUERY="agent governance skill markdown validation" QUESTION="which papers are about static checking of agent interactions?"
make workflow-all QUERY="agent governance skill markdown validation" QUESTION="which papers are about static checking of agent interactions?"
make workflow-static QUERY="agent governance skill markdown validation" QUESTION="which papers are about static checking of agent interactions?" INPUT_TOKENS=12000 OUTPUT_TOKENS=2300 COST_USD=0.184
```

Automatic cost source:

- `data/run_costs.json`

Default format:

```json
{
  "input_tokens": 0,
  "output_tokens": 0,
  "cost_usd": 0.0,
  "cost_note": "Default local workflow accounting. Update this file or pass CLI overrides when you have real API/model usage numbers."
}
```

Every `make team...` and `make workflow...` run now appends a run entry to:

- `AI_Agent_Governance_Three_Layer_Stack_and_Papers.md`

The entry includes:

- mode
- query
- question
- graph coverage
- input tokens
- output tokens
- total tokens
- estimated USD cost
- cost note

Default behavior:

- if `data/run_costs.json` exists, values are read from it automatically
- CLI values override the file if both are provided
- if neither is provided:
  - tokens = `0`
  - cost = `0`
  - note says the run used default local accounting

Daily summary:

```bash
make costs
python3 scripts/daily_cost_summary.py --date 2026-06-07
```

This reads the `## Workflow Run Log` section in `AI_Agent_Governance_Three_Layer_Stack_and_Papers.md` and totals:

- runs
- input tokens
- output tokens
- total tokens
- total recorded USD cost

---

*Last updated: 2026-05-31*  
*Maintained by: EvaPaper (OpenClaw agent)*
