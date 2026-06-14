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

### 4. Dashboard (`governance-dashboard.html`)
The dashboard is a self-contained HTML file with embedded JSON data. It has two parallel representations:
1. **JSON data** (`data/governance-dashboard.json`) — the source of truth
2. **Embedded JSON** in the HTML `<script id="dashboard-data">` tag — what the browser reads

**Integration Steps:**
1. **Check if items are already in the dashboard** — the June 12 run may have already added some arXiv papers. Run:
   ```bash
   python3 -c "import json; d=json.loads(open('data/governance_dashboard.json').read()); print([n['id'] for n in d['association_graph']['nodes']])"
   ```
   If an arXiv ID is already in the nodes list, skip it (don't double-count).

2. **Add new nodes** to the JSON's `association_graph.nodes` list. Each node needs:
   ```json
   {
     "id": "arxiv:XXXX.XXXXX" or "vendor:product-name",
     "title": "Paper Title",
     "url": "https://arxiv.org/abs/XXXX.XXXXX" or null,
     "topic": "specification|supply_chain|identity|coordination|evaluation|runtime|policy",
     "topic_label": "Human-readable topic label",
     "color": "#hexcolor",
     "layers": [0, 1, 2, 3],
     "discovered": "2026-06-14",
     "degree": 1
   }
   ```
   Use existing topic colors from the JSON. For non-arXiv items (OWASP, MITRE, NIST, GitHub tools), use a vendor-scoped ID like `owasp:mcp-guide`, `mitre:atlas-agentic`, `nist:ir-8596`.

3. **Add edges** for new nodes. Connect each new node to at least one existing node with the same topic. Edge structure:
   ```json
   {
     "source": "new-node-id",
     "target": "existing-node-id",
     "kind": "conceptual",
     "weight": 2.5,
     "reason": "same topic; shared L1",
     "shared_terms": []
   }
   ```

4. **Update topic mix** — recalculate `count` and `ratio` for all 7 topics based on the full node list.

5. **Update layer mix** — recalculate counts for layers 0–3.

6. **Add a new scout run** to the `runs` array:
   ```json
   {
     "date": "2026-06-14",
     "new_papers": 8,
     "cumulative": 59,
     "leading_topic": "Policy & governance landscape",
     "topics": {"specification": 1, "supply_chain": 1, ...},
     "cumulative_topics": {"specification": 8, "supply_chain": 9, ...}
   }
   ```

7. **Recalculate trending topics** from the last 2 runs.

8. **Update wiki pages** in `knowledge_wiki.pages`:
   - Add a `paper` page for each new node
   - Update `topic:*` and `layer:*` pages with new counts and links
   - Update the `overview` page subtitle with the new total count

9. **Sync to HTML** — replace the `<script id="dashboard-data">` block with the updated JSON, and update the `stat-value` divs for paper count and run count.

10. **Verification** — open the HTML (or grep) to confirm the new data is present:
    ```bash
    grep -c "59 papers\|8 runs\|2026-06-14" governance-dashboard.html
    ```

**Shortcut:** Use `scripts/patch_dashboard_june14.py` as a template. It performs steps 1–9 automatically. For future runs, copy and modify it with the new item list.

### 5. Regenerate Artifacts
- [ ] Run `make docs` — regenerates DOCX and PPTX from updated MD files
- [ ] Run `make dashboard` — refreshes `governance-dashboard.html` (only if the JSON was already updated manually; otherwise the script will miss new addendum items)
- [ ] Verify no import errors (python-docx, python-pptx must be installed)

### 6. Git Commit & Push
- [ ] `cd /root/.openclaw/workspace/EvaPaper`
- [ ] Stage only EvaPaper files (do NOT stage parent workspace files like AGENTS.md, SOUL.md, etc.)
- [ ] Commit with descriptive message: "[Date] integration: N new governance papers into HTML, Synthesis MD, DOCX, PPTX, and dashboard"
- [ ] Push to origin/master

### 7. Documentation
- [ ] Update `memory/agent_governance_scout_log.md` with integration status
- [ ] Create or update task file in `skills/analyze-research-gaps/tasks/`
- [ ] Note any pending follow-up tasks

## Quick Reference: Paper Count History
- Baseline (Jun 7): ~24 papers
- Jun 12 additions: +4 (EmbodiedGovBench, Agent Skills for LLMs, Learning Correct Behavior, Owner-Harm)
- Jun 14 additions: +8 total (2 already in dashboard from Jun 12, 6 new: OWASP MCP, MITRE ATLAS, NIST IR 8596, reprobe-audit, Agent Security Harness, WSP)
- Dashboard total: 59 papers (53 + 6 new)
- HTML total: 40 papers (32 + 8 new)

## Automation Wishlist
- [x] Script to auto-patch dashboard JSON and HTML (`scripts/patch_dashboard_june14.py` — template for future runs)
- [ ] Script to auto-generate paper cards from structured data
- [ ] Script to auto-update paper counts across all files
- [ ] Script to auto-sync layer pills between HTML and MD
- [ ] Consider: make the HTML source data-driven (JSON → HTML templating) instead of hand-editing HTML
