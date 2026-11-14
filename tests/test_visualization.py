
import unittest
import pandas as pd
import os

from src.visualization import plot_filtering_summary


class TestVisualization(unittest.TestCase):

    def test_plot_creation(self):

        summary = pd.DataFrame({
            "Metric": [
                "Genes retained",
                "Genes removed"
            ],
            "Value": [2, 2]
        })

        output_path = "results/test_plot.png"

        plot_filtering_summary(summary, output_path)

        self.assertTrue(os.path.exists(output_path))


if __name__ == "__main__":
    unittest.main()


