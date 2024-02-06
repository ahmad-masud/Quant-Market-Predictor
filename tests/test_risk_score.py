import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from modules import risk_score

class test_risk_score(unittest.TestCase):
    def test_risk_score(self):
        self.assertIsNotNone(risk_score('aapl', 10))
        self.assertIsNotNone(risk_score('msft', 5))
        self.assertIsNotNone(risk_score('amzn', 17))

if __name__ == '__main__':
    unittest.main()