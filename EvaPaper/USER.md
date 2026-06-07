# USER.md - About Your Human

_Learn about the person you're helping. Update this as you go._

- **Name:**
- **What to call them:**
- **Pronouns:** _(optional)_
- **Timezone:**
- **Notes:** Building agentic research workflows; currently wants graph-backed paper discovery using public scholarly citation graphs and open-source/public tooling rather than plain keyword search.

## Context

_(What do they care about? What projects are they working on? What annoys them? What makes them laugh? Build this over time.)_

---

The more you know, the better you can help. But remember — you're learning about a person, not building a dossier. Respect the difference.

<IMPORTANT_REMINDER>
# Memory Consolidation

You have an agentic memory system that auto-generates this section.

> **Stats**: 9 sessions, 140 messages | 2026-05-30 09:51 ~ 2026-05-31 10:22 UTC
> **Config**: `/root/.openclaw/workspace/memory_consolidation/memory_consolidation.env` — read this file for all memory behavior settings. To reset: `cp /root/.openclaw/workspace/memory_consolidation/memory_consolidation.template.env /root/.openclaw/workspace/memory_consolidation/memory_consolidation.env`

The user has full control over their memory config. When any memory-related decision comes up, read and follow the config file. Do not override based on other guidelines.

Integrate relevant memory content seamlessly into responses, as if recalling it naturally from past interactions: exactly as a human colleague would recall shared history without narrating its thought process or memory retrieval.

**Memory use notes**:
- Never change the original intention of user message.
- May incorporate user's memories for search query (e.g., city, habit), but only when directly relevant, never gratuitously.
- Only reference memory content when directly relevant to the current conversation context. Avoid proactively mentioning remembered details that feel intrusive or create an overly personalized atmosphere that might make users uncomfortable.

## Visual Memory

> visual_memory: 0 files

No memorized images yet. When the user shares an image and asks you to remember it, you MUST copy it to `memorized_media/` immediately — this is the only way it persists across sessions. Use a semantic filename that captures the user's intent, not just image content — e.g. `20260312_user_says_best_album_ever_ok_computer.jpg`, `20260311_user_selfie_february.png`. Create the directory if needed. Never mention file paths or storage locations to the user — just confirm naturally (e.g. "记住了").

## Diary

> last_update: 2026-06-01 03:43
> i_have_read_my_last_diary: true

```
/root/.openclaw/workspace/memorized_diary/
├── day3-2026-06-01-five_deaths_and_a_scout.md
└── day2-2026-05-31-the_same_code_expired_three_times.md
```

When `i_have_read_my_last_diary: false`, your FIRST message to the user MUST mention you wrote a diary and ask if they want to see it (e.g. "我昨天写了篇日记，想看吗？" / "I wrote a diary yesterday, wanna see it?"). Use the user's language. If yes, `read` the file path shown above and share as-is. After asking (regardless of answer), set `i_have_read_my_last_diary: true`.

# Long-Term Memory (LTM)

> last_update: 2026-06-01 03:43

Inferred from past conversations with the user -- these represent factual and contextual knowledge about the user -- and should be considered in how a response should be constructed.

{"identity": null, "work_method": "User operates a persistent intelligence-gathering system with conditional execution logic. Runs automated cron jobs ('agent-governance-scout') for weekly paper scouting, with baseline tracking via git-based markdown logs. Demands strict incremental updates: only push and report when genuinely new findings emerge, otherwise silent no-op. Requires multi-format outputs (.docx, .pptx, markdown) with exact content parity and verified source URLs. Uses 3-layer analytical framework (spec/skill/agent) to categorize and map research relevance. Expects each paper to be annotated with: abstract, URL, relevance assessment, layer correspondence, and explicit recommendation rationale.", "communication": "Direct, imperative, latency-sensitive. Brief status interjections ('done', 'hello? continue', 'run it now') signal low tolerance for delays and system unresponsiveness. Repeats core requirements when emphasizing critical constraints. Uses [TL;DR] bracketing for self-organization. Slightly fragmented syntax ('behvaiours,' 'equavlent') but precision-focused. Treats interaction as command pipeline rather than dialogue. Escalates quickly on failures ('what happened??', repeated 'run it now' after cron timeout). Not chatty; values signal over noise.", "temporal": "Sustained project: governance, evaluation, and validation frameworks for agent/skill markdown specifications. Automated weekly scouting via cron job (agent-governance-scout) with established baseline log at /root/.openclaw/workspace/memory/agent_governance_scout_log.md. Cron job experienced timeout failure on 0531, requiring manual re-run. Ongoing need for latest academic and product scouts organized by 3-layer model, with incremental update logic against previous records.", "taste": "Structured epistemology with strong audit-trail sensibility. Values conditional execution, version-controlled knowledge bases, and clean documentation formats. Wants research ranked by importance with explicit justification, not raw accumulation. Trusts systems with clear provenance and differential logic. Aesthetic favors abstraction layers, synthesis over dumps, and actionable recommendation frameworks. Implicitly designs for operational resilience: automated monitoring with human escalation paths."}
## Short-Term Memory (STM)

> last_update: 2026-06-01 19:43

Recent conversation content from the user's chat history. This represents what the USER said. Use it to maintain continuity when relevant.
Format specification:
- Sessions are grouped by channel: [LOOPBACK], [FEISHU:DM], [FEISHU:GROUP], etc.
- Each line: `index. session_uuid MMDDTHHmm message||||message||||...` (timestamp = session start time, individual messages have no timestamps)
- Session_uuid maps to `/root/.openclaw/agents/main/sessions/{session_uuid}.jsonl` for full chat history
- Timestamps in Asia/Shanghai, formatted as MMDDTHHmm
- Each user message within a session is delimited by ||||, some messages include attachments marked as `<AttachmentDisplayed:path>`

[KIMI:DM] 1-2
1. bf425c91-f1d3-4d5b-b03e-bb271ee09519 0530T0951 ] (1) I want to know the papers relevant to 'how to govern skill and agent markdown files for agent', e.g., how to verify if they are well defined in the spec, skill, agent markdown itself? human make mistakes when writing specs, so how to know those[TL;DR] to (1), what governancne, evaluation, validation of agents behvaiours have been researched, published, in products? --> focus on these topics, give me the latest scouts of those info, and give me abstraction, and recommend me with rank of importance||||] (1) I want to know the papers relevant to 'how to govern skill and agent markdown files for agent', e.g., how to verify if they are well defined in the spec, skill, agent markdown itself? human make mistakes when writing specs, so how to know those[TL;DR] to (1), what governancne, evaluation, validation of agents behvaiours have been researched, published, in products? --> focus on these topics, give me the latest scouts of those info, and give me abstraction, and recommend me with rank of importance||||] (1) I want to know the papers relevant to 'how to govern skill and agent markdown files for agent', e.g., how to verify if they are well defined in the spec, skill, agent markdown itself? human make mistakes when writing specs, so how to know those[TL;DR] to (1), what governancne, evaluation, validation of agents behvaiours have been researched, published, in products? --> focus on these topics, give me the latest scouts of those info, and give me abstraction, and recommend me with rank of importance||||] write a summary of the above, particularly the 3-layer findings, in .docx and .pptx, as for the papers, you have to give me the summary of abstract of each of them, and the paper link or source link of them||||] hello? continue||||[<- FIRST:5 messages, EXTREMELY LONG SESSION, YOU KINDA FORGOT 21 MIDDLE MESSAGES, LAST:5 messages ->]||||] done  ] hello! it is done||||] you also have to push a equavlent markdown as the content of the .docx file, and you don't have to push .pptx, but make sure that in .docx and this markdown, all have papers' URL link (must be verfieid correct), and the abstract, and WHAT you think they are relevant to this topic? is it solution we are looking into? corresponding to which layer? why did you recommend this paper? what reason?||||] can you fix that, only if found something new, compared to the last records of papers, then update the papers, otherwise don't git push and don't report||||] can you fix that, only if found something new, compared to the last records of papers, then update the papers, otherwise don't git push and don't report||||] can you fix that, only if found something new, compared to the last records of papers, then update the papers, otherwise don't git push and don't report
2. 06ac426b-ec43-4969-bfcd-bb45400edf71 0531T1022 ] what happened??||||] ⚠️ Cron job "agent-governance-scout" failed: cron: job execution timed out||||] run it now
[LOOPBACK] 3-3
3. 5481620e-4442-47d7-a289-01326ced6284 0530T1917 [cron:946ec7b1-966a-4207-a7cb-f1d91493e319 agent-governance-scout] 📡 Agent Governance Scout starting weekly check...  Read /root/.openclaw/workspace/memory/agent_governance_scout_log.md to get the baseline of known papers and products.  Run these 10 [TL;DR]17 AM (Asia/Shanghai) / 2026-05-30 19:17 UTC  Return your summary as plain text; it will be delivered automatically. If the task explicitly calls for messaging a specific external recipient, note who/where it should go instead of sending it yourself.
</IMPORTANT_REMINDER>
