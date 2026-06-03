# MEMORY.md

## Workflow Agreements

### Agent-Governance-Scout Run Protocol
When the user asks me to "run" the agent-governance-scout (or "update findings"):
1. Execute the search queries and identify new papers/products/frameworks
2. Compare against the baseline in `memory/agent_governance_scout_log.md`
3. If new findings exist:
   - Update `memory/agent_governance_scout_log.md` with the new findings (append by date)
   - Update `AI_Agent_Governance_Three_Layer_Stack_and_Papers.docx` with the new findings and updated summary
   - Update `AI_Agent_Governance_Three_Layer_Stack_and_Papers.pptx` with the new findings and updated summary
   - Git commit the changes
   - Tell the user how to push to GitHub (since the workspace lacks auth credentials)
4. If no new findings exist: do NOT update the files, do NOT report, finish silently

### Git Push Instructions (for this workspace)
The workspace uses HTTPS with no stored credentials. The user must push from their terminal using one of these methods:
- **SSH (recommended):** `git remote set-url origin git@github.com:ginaecho/EvaPaper.git` then `git push`
- **Token via HTTPS:** `git push https://<token>@github.com/ginaecho/EvaPaper.git` (or set `GIT_ASKPASS` / `gh` CLI)

I will include this in every scout report so the user can copy-paste.

## Scout Findings History
- 2026-05-30: Initial baseline established
- 2026-05-31: 7 new papers + 4 new products discovered
- 2026-06-01: 11 new papers + 7 new products discovered (commit 5e9c44b, not pushed)
