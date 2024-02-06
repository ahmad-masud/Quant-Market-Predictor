import unittest
from ..modules import risk_score

class test_risk_score(unittest.TestCase):
    def test_risk_score(self):
        self.assertEqual(risk_score('aapl', 10), 0.2829)
        self.assertEqual(risk_score('msft', 5), 0.3029)
        self.assertEqual(risk_score('amzn', 17), 0.3845)

if __name__ == '__main__':
    unittest.main()