import sys
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from governance_dashboard import DashboardPaper, _paper_id, build_dashboard_data


class DashboardDataTests(unittest.TestCase):
    def test_topic_ratios_sum_to_one(self):
        papers = [
            DashboardPaper("A", None, date(2026, 5, 30), "specification", (0,)),
            DashboardPaper("B", None, date(2026, 6, 1), "runtime", (1,)),
            DashboardPaper("C", None, date(2026, 6, 1), "runtime", (1, 2)),
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


if __name__ == "__main__":
    unittest.main()
