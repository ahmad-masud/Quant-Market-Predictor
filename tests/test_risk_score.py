import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from scripts import risk_score


class test_risk_score(unittest.TestCase):
    def test_risk_score_returns_float(self):
        """Ensure risk_score returns a float."""
        risk = risk_score("AAPL", 5)
        self.assertIsInstance(risk, float)

    def test_risk_score_is_within_range(self):
        """Ensure risk score is within reasonable bounds (0-2)."""
        risk = risk_score("MSFT", 5)
        self.assertGreaterEqual(risk, 0)
        self.assertLessEqual(risk, 2)


if __name__ == "__main__":
    unittest.main()
