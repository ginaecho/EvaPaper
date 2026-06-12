# Research Opportunity Schema

Write valid JSON with this shape:

```json
{
  "generated_at": "YYYY-MM-DD",
  "analysis_model": "model or agent name",
  "corpus_snapshot": {
    "source_record_count": 70,
    "academic_paper_count": 52,
    "scope_note": "The source index mixes papers/products; the dashboard uses deduplicated scholarly IDs.",
    "scout_run_count": 8,
    "latest_scout": "YYYY-MM-DD",
    "graph_nodes": 52,
    "graph_edges": 97
  },
  "summary": "Two or three sentences describing the overall missing-area pattern.",
  "opportunities": [
    {
      "rank": 1,
      "title": "Specific missing research area",
      "gap_type": "field_gap",
      "priority_score": 92,
      "confidence": "high",
      "scope": "What is missing.",
      "why_missing": "Evidence-backed explanation.",
      "evidence": [
        {
          "observation": "Corpus fact with a number, named paper, or graph pattern.",
          "source": "data/governance_dashboard.json"
        }
      ],
      "llm_reasoning": "Explicit inference connecting evidence to the opportunity.",
      "uncertainty": "What could make this conclusion wrong or incomplete.",
      "coverage_check": {
        "query_terms": ["terms used to inspect the local corpus"],
        "matched_titles": ["Relevant titles found"],
        "interpretation": "What the result does and does not establish."
      },
      "research_questions": [
        "A falsifiable research question?"
      ],
      "scout_queries": [
        "A targeted future search query"
      ],
      "related_topics": ["coordination"],
      "related_layers": [1, 2]
    }
  ]
}
```

Constraints:

- `opportunities`: 3-6 entries.
- `rank`: consecutive integers starting at 1.
- `gap_type`: one of `corpus_gap`, `field_gap`, `evidence_gap`, `translation_gap`.
- `priority_score`: integer 0-100.
- `confidence`: `low`, `medium`, or `high`.
- `evidence`: at least two entries.
- `coverage_check`: required; include query terms, matched titles, and a bounded interpretation.
- `research_questions`: at least two entries.
- `scout_queries`: at least two entries.
- `related_topics`: values from:
  - `specification`
  - `runtime`
  - `evaluation`
  - `supply_chain`
  - `identity`
  - `coordination`
  - `policy`
- `related_layers`: integers 0-3.

The HTML renders this file verbatim as attributed LLM analysis. Keep prose concise.
