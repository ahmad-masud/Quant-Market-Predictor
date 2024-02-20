import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from scripts import plot_data

class test_plot_data(unittest.TestCase):
    def test_plot_data(self):
        self.assertTrue(plot_data('aapl', 10))
        self.assertTrue(plot_data('msft', 5))
        self.assertTrue(plot_data('amzn', 17))

if __name__ == '__main__':
    unittest.main()
