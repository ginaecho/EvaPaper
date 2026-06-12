import sys
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from governance_dashboard import (
    DashboardPaper,
    _paper_id,
    build_association_graph,
    build_dashboard_data,
    build_knowledge_wiki,
)


class DashboardDataTests(unittest.TestCase):
    def test_topic_ratios_sum_to_one(self):
        papers = [
            DashboardPaper("arxiv:a", "A", None, date(2026, 5, 30), "specification", (0,)),
            DashboardPaper("arxiv:b", "B", None, date(2026, 6, 1), "runtime", (1,)),
            DashboardPaper("arxiv:c", "C", None, date(2026, 6, 1), "runtime", (1, 2)),
        ]

        data = build_dashboard_data(papers)

        self.assertEqual(data["paper_count"], 3)
        self.assertAlmostEqual(sum(item["ratio"] for item in data["topic_mix"]), 1.0)
        self.assertEqual(data["runs"][-1]["cumulative"], 3)
        self.assertEqual(data["layer_mix"][1]["count"], 2)
        self.assertEqual(data["layer_mix"][2]["count"], 1)

    def test_paper_id_normalizes_arxiv_urls_and_labels(self):
        self.assertEqual(_paper_id("arXiv:2605.03159"), "arxiv:2605.03159")
        self.assertEqual(
            _paper_id("https://arxiv.org/abs/2605.03159"),
            "arxiv:2605.03159",
        )

    def test_association_graph_keeps_labeled_neighbors(self):
        papers = [
            DashboardPaper(
                "arxiv:a", "A", None, date(2026, 5, 30), "runtime", (1,), ("audit", "policy")
            ),
            DashboardPaper(
                "arxiv:b", "B", None, date(2026, 6, 1), "runtime", (1, 2), ("audit", "trace")
            ),
            DashboardPaper(
                "arxiv:c", "C", None, date(2026, 6, 1), "identity", (3,), ("provenance",)
            ),
        ]

        graph = build_association_graph(papers)

        self.assertEqual(graph["node_count"], 3)
        self.assertEqual(graph["edge_count"], 1)
        self.assertIn("same topic", graph["edges"][0]["reason"])
        self.assertIn("audit", graph["edges"][0]["shared_terms"])

    def test_wiki_has_overview_topic_layer_and_paper_pages(self):
        papers = [
            DashboardPaper(
                "arxiv:a", "A", None, date(2026, 5, 30), "runtime", (1,), ("audit",)
            ),
            DashboardPaper(
                "arxiv:b", "B", None, date(2026, 6, 1), "runtime", (1, 2), ("trace",)
            ),
        ]
        graph = build_association_graph(papers)

        wiki = build_knowledge_wiki(papers, graph)

        self.assertEqual(wiki["page_count"], 14)
        page_ids = {page["id"] for page in wiki["pages"]}
        self.assertIn("overview", page_ids)
        self.assertIn("topic:runtime", page_ids)
        self.assertIn("layer:1", page_ids)
        self.assertIn("arxiv:a", page_ids)


if __name__ == "__main__":
    unittest.main()
