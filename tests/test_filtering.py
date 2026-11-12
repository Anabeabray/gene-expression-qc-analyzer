import unittest 
import pandas as pd 
from src.filtering import filter_low_expression

class TestFiltering(unittest.TestCase):

    def test_filter_low_expression(self):

        test_data = pd.DataFrame(
            {
                "Sample_1": [20, 0, 5, 0],
                "Sample_2": [15, 0, 8, 0],
                "Sample_3": [30, 0, 12, 0],
                "Sample_4": [25, 0, 0, 0],
            },
            index=["Gene_A", "Gene_B", "Gene_C", "Gene_D"]
        )

        filtered_data = filter_low_expression(
            test_data,
            min_count=10,
            min_fraction=0.5
        )

        self.assertEqual(
            list(filtered_data.index),
            ["Gene_A"]
        )


if __name__ == "__main__":
    unittest.main()
