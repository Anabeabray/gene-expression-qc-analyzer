
import unittest
import pandas as pd

from src.filtering_summary import summarize_filtering


class TestFilteringSummary(unittest.TestCase):

    def test_summary(self):

        original = pd.DataFrame({
            "Sample1": [10, 0, 20, 0],
            "Sample2": [15, 0, 25, 0]
        })

        filtered = original.iloc[[0, 2]] #iloc selects rows by index, so we are keeping the first and the third row (index 0 and 2) and removing the second and fourth row (index 1 and 3)

        summary = summarize_filtering(original, filtered)

        self.assertEqual(                       #testing the results of the summarize_filtering function
            summary.loc[0, "Value"], 4
        )

        self.assertEqual(
            summary.loc[1, "Value"], 2
        )

        self.assertEqual(
            summary.loc[2, "Value"], 2
        )


if __name__ == "__main__":              #archive executable code to run the tests when the script is executed directly
    unittest.main()


