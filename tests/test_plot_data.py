import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from modules import plot_data

class test_plot_data(unittest.TestCase):
    def test_plot_data(self):
        self.assertEqual(plot_data('aapl', 10), True)
        self.assertEqual(plot_data('msft', 5), True)
        self.assertEqual(plot_data('amzn', 17), True)

if __name__ == '__main__':
    unittest.main()
