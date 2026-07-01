import unittest
from unittest.mock import patch

from paper_graph import ArxivClient, discover_from_query


class PaperGraphTests(unittest.TestCase):
    def test_arxiv_query_syntax_keeps_phrase_and_bigrams(self):
        query = ArxivClient._query_syntax("agent governance skill markdown validation")

        self.assertIn('all:"agent governance skill markdown validation"', query)
        self.assertIn('all:"agent governance"', query)
        self.assertIn("all:agent AND all:governance AND all:skill", query)

    def test_discovery_uses_arxiv_when_openalex_is_unavailable(self):
        arxiv_paper = {
            "paperId": "arXiv:2606.31272v1",
            "title": "The Decomposition Is the Fingerprint: Per-Component Identity for Agent Skills",
            "year": 2026,
            "abstract": "Skill identity paper.",
            "citationCount": 0,
            "url": "http://arxiv.org/abs/2606.31272v1",
            "topics": ["cs.CR"],
        }

        with patch("paper_graph.OpenAlexClient.search_works", side_effect=RuntimeError("openalex down")):
            with patch("paper_graph.ArxivClient.search_papers", return_value=[arxiv_paper]):
                with patch("paper_graph.SemanticScholarClient.search_papers", side_effect=RuntimeError("s2 limited")):
                    result = discover_from_query("agent governance skill markdown validation", seed_limit=5)

        self.assertEqual(len(result["seeds"]), 1)
        self.assertEqual(len(result["candidates"]), 1)
        self.assertEqual(result["candidates"][0]["source"], "arxiv")
        self.assertIn("arxiv_live_search", result["candidates"][0]["matched_edges"])
        self.assertTrue(any("openalex search failed" in error for error in result["provider_errors"]))
        self.assertTrue(any("semantic scholar search failed" in error for error in result["provider_errors"]))


if __name__ == "__main__":
    unittest.main()
