import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from toolkit import inquiry_prompt, operations_prompt, analyze_metrics


class TestToolkit(unittest.TestCase):
    def test_inquiry_uses_approved_facts_and_review(self):
        result = inquiry_prompt("Are you open Saturday?", "Open Mon-Fri")
        self.assertIn("Open Mon-Fri", result)
        self.assertIn("review and approve", result)

    def test_inquiry_rejects_blank(self):
        with self.assertRaises(ValueError):
            inquiry_prompt("  ", "known facts")

    def test_operations_does_not_claim_completion(self):
        self.assertIn("Do not invent", operations_prompt("Event next week"))

    def test_metrics(self):
        r = analyze_metrics([{"before_minutes": "20", "after_minutes": "5"},
                             {"before_minutes": "10", "after_minutes": "10"}])
        self.assertEqual(r["saved_minutes"], 15)
        self.assertEqual(r["change_percent"], 50)

    def test_invalid_metrics(self):
        with self.assertRaises(ValueError):
            analyze_metrics([{"before_minutes": "-2", "after_minutes": "1"}])

    def test_overflow(self):
        with self.assertRaises(ValueError):
            analyze_metrics([{"before_minutes": "1e308", "after_minutes": "0"}] * 2)
        with self.assertRaises(ValueError):
            analyze_metrics([{"before_minutes": "5e-324", "after_minutes": "100"}])

    def test_zero_baseline(self):
        self.assertIsNone(analyze_metrics([{"before_minutes": "0", "after_minutes": "0"}])["change_percent"])


if __name__ == "__main__":
    unittest.main()
