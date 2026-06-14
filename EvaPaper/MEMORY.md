# MEMORY.md

## Workflow Agreements

### Research Dashboard
The user wants a visual dashboard updated after every scout run that produces new findings. It must summarize primary paper-topic ratios, governance-layer coverage, topic growth over scout discovery dates, an Obsidian-style graph, a Karpathy-style in-HTML wiki, and ranked underexplored areas with explicit LLM reasoning. The Claw sub-agent must use `skills/analyze-research-gaps/SKILL.md` to write `data/research_opportunities.json` before dashboard regeneration. No-new-finding scout runs must not rewrite these artifacts.

### Agent-Governance-Scout Run Protocol
When the user asks me to "run" the agent-governance-scout (or "update findings"):
1. Execute the search queries and identify new papers/products/frameworks
2. Compare against the baseline in `memory/agent_governance_scout_log.md`
3. If new findings exist:
   - Update `memory/agent_governance_scout_log.md` with the new findings (append by date)
   - **Format requirement:** Every paper and product entry must include `Found: YYMMDD` (e.g., `Found: 0606` or `Found: 0606-evening` for multiple runs per day)
   - **MANDATORY:** Integrate new findings into `ai-agent-governance-research.html` (add paper cards, update layer pills, update paper counts)
   - **MANDATORY:** Integrate new findings into `Agent_Governance_Three_Questions_Synthesis.md` (add numbered entries, update comparison tables)
   - **MANDATORY:** Regenerate DOCX and PPTX via `make docs`
   - **MANDATORY:** Refresh dashboard via `make dashboard`
   - Git commit and push all changes
   - Tell the user the commit hash and push status
4. If no new findings exist: do NOT update the files, do NOT report, finish silently

### Git Push Instructions (for this workspace)
- The workspace has git credentials configured and can push directly via `git push`
- Fallback methods if needed:
  - **SSH:** `git remote set-url origin git@github.com:ginaecho/EvaPaper.git` then `git push`
  - **Token via HTTPS:** `git push https://<token>@github.com/ginaecho/EvaPaper.git`

## Scout Findings History
- 2026-05-30: Initial baseline established
- 2026-05-31: 7 new papers + 4 new products discovered
- 2026-06-01: 11 new papers + 7 new products discovered (commit 5e9c44b, not pushed)
- 2026-06-04: 10 new papers + 5 new products discovered (commit 7e0e687)
  - Key: Formal methods momentum accelerating — ABC (Design-by-Contract for agents), AgentVerify (LTL model checking), SkillFortify (formal skill supply chain verification), AgentAssay (regression testing), ACP (temporal admission control, 1.7M req/s). Benchmark consistency analysis reveals zero concordance (Kendall's W=0.10) across safety benchmarks. Agent Governance Series (6 papers) by Marcelo Fernandez is the most concentrated formal governance research program currently active.
  - Critical insight: "benchmark choice can yield contradictory safety conclusions" — current safety rankings are mostly noise.
- 2026-06-06: 5 new papers + 3 new products discovered (commit 52af337)
  - Key: SkillGuard introduces permission-based skill governance (SELinux for skills). From Craft to Kernel proposes governance-first execution architecture. TAIP provides continuous assurance. AgentWarden uses RL for adaptive capability boundaries. Cisco (DefenseClaw) and NVIDIA (NemoClaw) enter agent security market. Format updated to include discovery dates (Found: YYMMDD).
