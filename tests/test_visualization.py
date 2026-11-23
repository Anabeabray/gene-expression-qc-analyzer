
import unittest
import pandas as pd
import numpy as np
import os

from src.visualization import (
    plot_filtering_summary,
    plot_normalization_boxplots
)


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

        os.makedirs("results", exist_ok=True)

        plot_filtering_summary(summary, output_path)

        self.assertTrue(os.path.exists(output_path))

    def test_normalization_boxplot_creation(self):

        counts = pd.DataFrame({
    "Sample_1": [10, 20, 30, 40, 50],
    "Sample_2": [15, 25, 35, 45, 55]
    })
        cpm = counts.div(counts.sum(axis=0), axis=1) * 1_000_000

        log2_cpm = np.log2(cpm + 1)

        output_path = "results/test_boxplot.png"

        plot_normalization_boxplots(
            counts, 
            cpm, 
            log2_cpm,
            output_path
        )

        self.assertTrue(os.path.exists(output_path))

if __name__ == "__main__":
    unittest.main()


