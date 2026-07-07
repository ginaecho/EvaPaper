# EvaPaper Paper Scouting Integration

## Trigger
Run after paper scouting yields new relevant papers.

## Relevance Filter (CRITICAL)
Papers MUST pass a relevance gate before integration into curated reports.
Only papers related to **AI agent governance, evaluation, safety, security, or tool use** 
are integrated. Irrelevant domains (medical imaging, bioinformatics, chemistry, etc.) 
are kept in raw scout JSON but NEVER pushed to curated markdown or HTML deliverables.

**Minimum requirement:** At least 2 relevance signals from: agent, llm, language model, 
governance, benchmark, evaluation, safety, security, trust, sandbox, runtime, skill, 
tool use, multi-agent, autonomous, alignment, guardrail, agentic, etc.

## Mandatory Integration Targets
Newly discovered **relevant** papers must be added to **all four** deliverables:

1. **Markdown Synthesis**  
   `EvaPaper/AI_Agent_Governance_Three_Layer_Stack_and_Papers.md`  
   → Add papers to the appropriate governance layer(s) with citations and summaries.

2. **Three Questions Synthesis**  
   `EvaPaper/Agent_Governance_Three_Questions_Synthesis.md`  
   → Map new papers to the three governance questions framework.

3. **Research HTML Page**  
   `EvaPaper/ai-agent-governance-research.html`  
   → Update the interactive research page with new paper entries.

4. **Governance Dashboard**  
   `EvaPaper/governance-dashboard.html`  
   → Reflect new papers in the dashboard visualizations and data layers.

## Workflow
1. Finish paper scouting (source: arXiv, Google Scholar, Semantic Scholar, etc.).
2. For each new paper, extract: title, authors, year, venue, abstract, key contributions, and governance relevance.
3. Update **all four files above** — do not stop after updating only one or two.
4. Regenerate derived assets (`.docx`, `.pptx`) if they are tracked; otherwise update source Markdown/HTML only.
5. Commit with a clear message: `feat: integrate N new papers from scouting run YYYY-MM-DD`.

## Checklist
- [ ] `AI_Agent_Governance_Three_Layer_Stack_and_Papers.md` updated
- [ ] `Agent_Governance_Three_Questions_Synthesis.md` updated
- [ ] `ai-agent-governance-research.html` updated
- [ ] `governance-dashboard.html` updated
- [ ] (Optional) `.docx` / `.pptx` regenerated if needed
- [ ] Changes committed and pushed
