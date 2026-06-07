PYTHON ?= python3
QUERY ?= agent governance skill markdown validation
QUESTION ?= which papers are about static checking of agent interactions?
MODE ?= static
TOP_K ?= 8

.PHONY: help index scout scout-json sota sota-static sota-runtime sota-behavioral sota-all ask ask-static ask-runtime ask-behavioral team team-static team-runtime team-behavioral team-all docs

help:
	@printf "%s\n" \
	"Workflow targets:" \
	"  make index                                 Build/rebuild the local paper corpus" \
	"  make scout QUERY='...'                     Run graph-backed discovery" \
	"  make sota MODE=static                      Show state of the art for a focus mode" \
	"  make ask MODE=static QUESTION='...'        Map a question to papers with evidence" \
	"  make team MODE=static QUERY='...'          Run the generic agent-team workflow" \
	"  make docs                                  Regenerate DOCX/PPTX artifacts" \
	"" \
	"Shortcuts:" \
	"  make sota-static | sota-runtime | sota-behavioral | sota-all" \
	"  make ask-static | ask-runtime | ask-behavioral" \
	"  make team-static | team-runtime | team-behavioral | team-all"

index:
	$(PYTHON) scripts/paper_corpus.py

scout:
	$(PYTHON) scripts/scout.py --discover "$(QUERY)" --from-year 2024

scout-json:
	$(PYTHON) scripts/scout.py --discover "$(QUERY)" --from-year 2024 --json

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
	$(PYTHON) scripts/agent_team.py --query "$(QUERY)" --question "$(QUESTION)" --mode "$(MODE)" --top-k $(TOP_K)

team-static:
	$(MAKE) team MODE=static

team-runtime:
	$(MAKE) team MODE=runtime

team-behavioral:
	$(MAKE) team MODE=behavioral

team-all:
	$(MAKE) team MODE=all

docs:
	$(PYTHON) generate_governance_docs.py
	$(PYTHON) generate_beautiful_pptx.py
