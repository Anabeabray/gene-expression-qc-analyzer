import unittest
import pandas as pd

from src.normalization import calculate_cpm, log2_transform


class TestNormalization(unittest.TestCase):

    def setUp(self):
        """
        Create a small gene expression matrix for testing.
        """

        self.counts = pd.DataFrame({
            "Sample1": [100, 200, 700],
            "Sample2": [200, 300, 500]
        }, index=["Gene1", "Gene2", "Gene3"])

    def test_calculate_cpm(self):
        """
        Test if CPM is calculated correctly.
        """

        cpm = calculate_cpm(self.counts)

        self.assertAlmostEqual(cpm["Sample1"].sum(), 1_000_000)
        self.assertAlmostEqual(cpm["Sample2"].sum(), 1_000_000)

        self.assertAlmostEqual(
            cpm.loc["Gene1", "Sample1"],
            100_000
        )

    def test_log2_transform(self):
        """
        Test if log2(CPM + 1) is applied correctly.
        """

        cpm = calculate_cpm(self.counts)
        result = log2_transform(cpm)

        self.assertAlmostEqual(
            result.loc["Gene1", "Sample1"],
            16.60965,
            places=4
        )

    def test_zero_values(self):
        """
        Test if zero values remain zero after log2 transformation.
        """

        cpm = pd.DataFrame({
            "Sample1": [0, 100]
        }, index=["Gene1", "Gene2"])

        result = log2_transform(cpm)

        self.assertEqual(result.loc["Gene1", "Sample1"], 0)

    def test_negative_counts(self):
        """
        Test if negative counts raise an error.
        """

        invalid_counts = pd.DataFrame({
            "Sample1": [100, -50]
        })

        with self.assertRaises(ValueError):
            calculate_cpm(invalid_counts)

    def test_zero_library_size(self):
        """
        Test if samples with zero total counts raise an error.
        """

        invalid_counts = pd.DataFrame({
            "Sample1": [0, 0],
            "Sample2": [100, 200]
        })

        with self.assertRaises(ValueError):
            calculate_cpm(invalid_counts)


if __name__ == "__main__":
    unittest.main()


