import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from scripts import predict_future_price


class test_predict_future_price(unittest.TestCase):
    def test_prediction_returns_float(self):
        """Ensure predict_future_price returns a float."""
        prediction = predict_future_price("AAPL", 30, 5)
        self.assertIsInstance(prediction, float)

    def test_prediction_is_positive(self):
        """Ensure predicted stock price is greater than zero."""
        prediction = predict_future_price("MSFT", 30, 5)
        self.assertGreater(prediction, 0)


if __name__ == "__main__":
    unittest.main()
