import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from modules import predict_future_price

class test_predict_future_price(unittest.TestCase):
    def test_predict_future_price(self):
        self.assertIsNotNone(predict_future_price('aapl', 50, 10))
        self.assertIsNotNone(predict_future_price('msft', 75, 5))
        self.assertIsNotNone(predict_future_price('amzn', 300, 17))

if __name__ == '__main__':
    unittest.main()