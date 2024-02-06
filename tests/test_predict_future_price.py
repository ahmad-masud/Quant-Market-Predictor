import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from modules import predict_future_price

class test_predict_future_price(unittest.TestCase):
    def test_predict_future_price(self):
        self.assertEqual(predict_future_price('aapl', 50, 10), 196.34)
        self.assertEqual(predict_future_price('msft', 75, 5), 341.89)
        self.assertEqual(predict_future_price('amzn', 300, 17), 97.09)

if __name__ == '__main__':
    unittest.main()