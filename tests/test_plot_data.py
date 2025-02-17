import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from scripts import plot_data


class TestPlotData(unittest.TestCase):
    def test_plot_data_runs(self):
        """Ensure plot_data runs without errors."""
        try:
            plot_data("AAPL", 10)
            plot_data("MSFT", 5)
            plot_data("AMZN", 17)
        except Exception as e:
            self.fail(f"plot_data raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
