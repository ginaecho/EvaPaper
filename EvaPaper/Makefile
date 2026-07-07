PYTHON ?= python3
QUERY ?= agent governance skill markdown validation
QUESTION ?= which papers are about static checking of agent interactions?
MODE ?= static
TOP_K ?= 8
INPUT_TOKENS ?=
OUTPUT_TOKENS ?=
COST_USD ?=
COST_NOTE ?=

.PHONY: help index dashboard opportunities-check scout scout-json daily-scout integrate-graph sota sota-static sota-runtime sota-behavioral sota-all ask ask-static ask-runtime ask-behavioral team team-static team-runtime team-behavioral team-all workflow-static workflow-runtime workflow-behavioral workflow-all costs docs test

help:
	@printf "%s\n" \
	"Workflow targets:" \
	"  make index                                 Build/rebuild the local paper corpus" \
	"  make dashboard                             Refresh the visual research dashboard" \
	"  make opportunities-check                   Validate LLM research-gap analysis" \
	"  make scout QUERY='...'                     Run graph-backed discovery" \
	"  make integrate-graph                       Promote latest graph candidates into scout log + dashboard" \
	"  make sota MODE=static                      Show state of the art for a focus mode" \
	"  make ask MODE=static QUESTION='...'        Map a question to papers with evidence" \
	"  make team MODE=static QUERY='...'          Run the generic agent-team workflow" \
	"  make workflow-static                       Run index + static team + static question mapping" \
	"  make costs                                 Summarize daily workflow token/cost totals" \
	"  make docs                                  Regenerate DOCX/PPTX artifacts" \
	"" \
	"Shortcuts:" \
	"  make sota-static | sota-runtime | sota-behavioral | sota-all" \
	"  make ask-static | ask-runtime | ask-behavioral" \
	"  make team-static | team-runtime | team-behavioral | team-all" \
	"  make workflow-static | workflow-runtime | workflow-behavioral | workflow-all"

index:
	$(PYTHON) scripts/paper_corpus.py

dashboard:
	$(PYTHON) scripts/governance_dashboard.py

opportunities-check:
	$(PYTHON) skills/analyze-research-gaps/scripts/validate_opportunities.py data/research_opportunities.json

scout:
	$(PYTHON) scripts/scout.py --discover "$(QUERY)" --from-year 2024

scout-json:
	$(PYTHON) scripts/scout.py --discover "$(QUERY)" --from-year 2024 --json

daily-scout:
	$(PYTHON) scripts/daily_scout.py --from-year 2025

daily-scout-deep:
	$(PYTHON) scripts/daily_scout.py --from-year 2025 --deep

deep-research:
	$(PYTHON) scripts/deep_research_pass.py --topic "$(QUERY)"

integrate-graph:
	$(PYTHON) scripts/integrate_graph_candidates.py --dashboard

sota:
	$(PYTHON) scripts/question_map.py --sota --mode "$(MODE)" --top-k $(TOP_K)

sota-static:
	$(MAKE) sota MODE=static

sota-runtime:
	$(MAKE) sota MODE=runtime

sota-behavioral:
	$(MAKE) sota MODE=behavioral

sota-all:
	$(MAKE) sota MODE=all

ask:
	$(PYTHON) scripts/question_map.py "$(QUESTION)" --mode "$(MODE)" --top-k $(TOP_K)

ask-static:
	$(MAKE) ask MODE=static

ask-runtime:
	$(MAKE) ask MODE=runtime

ask-behavioral:
	$(MAKE) ask MODE=behavioral

team:
	$(PYTHON) scripts/agent_team.py --query "$(QUERY)" --question "$(QUESTION)" --mode "$(MODE)" --top-k $(TOP_K) --write-report $(if $(INPUT_TOKENS),--input-tokens $(INPUT_TOKENS),) $(if $(OUTPUT_TOKENS),--output-tokens $(OUTPUT_TOKENS),) $(if $(COST_USD),--cost-usd $(COST_USD),) $(if $(COST_NOTE),--cost-note "$(COST_NOTE)",)

team-static:
	$(MAKE) team MODE=static

team-runtime:
	$(MAKE) team MODE=runtime

team-behavioral:
	$(MAKE) team MODE=behavioral

team-all:
	$(MAKE) team MODE=all

workflow-static:
	$(MAKE) index
	$(MAKE) dashboard
	$(MAKE) team MODE=static

workflow-runtime:
	$(MAKE) index
	$(MAKE) dashboard
	$(MAKE) team MODE=runtime

workflow-behavioral:
	$(MAKE) index
	$(MAKE) dashboard
	$(MAKE) team MODE=behavioral

workflow-all:
	$(MAKE) index
	$(MAKE) dashboard
	$(MAKE) team MODE=all

costs:
	$(PYTHON) scripts/daily_cost_summary.py

docs:
	$(PYTHON) generate_governance_docs.py
	$(PYTHON) generate_beautiful_pptx.py

test:
	$(PYTHON) -m unittest discover -s tests
