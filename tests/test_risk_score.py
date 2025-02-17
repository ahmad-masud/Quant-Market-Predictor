import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from scripts import risk_score

class TestRiskScore(unittest.TestCase):
    def test_risk_score_returns_float(self):
        """Ensure risk_score returns a float."""
        risk, level, color = risk_score("AAPL", 5)
        self.assertIsInstance(risk, float)

    def test_risk_score_is_within_range(self):
        """Ensure risk score is within reasonable bounds (0-2)."""
        risk, level, color = risk_score("AAPL", 5)
        self.assertGreaterEqual(risk, 0)
        self.assertLessEqual(risk, 2)

    def test_risk_score_returns_valid_level(self):
        """Ensure risk level is one of the expected categories."""
        risk, level, color = risk_score("AAPL", 5)
        expected_levels = [
            "Very Low Risk", "Low Risk", "Moderate Risk",
            "Moderately High Risk", "High Risk", "Very High Risk", "Extreme Risk"
        ]
        self.assertIn(level, expected_levels)

    def test_risk_score_returns_valid_color(self):
        """Ensure risk color is one of the expected colors."""
        risk, level, color = risk_score("AAPL", 5)
        expected_colors = ["green", "lightgreen", "yellow", "orange", "orangered", "red", "darkred"]
        self.assertIn(color, expected_colors)

if __name__ == "__main__":
    unittest.main()
