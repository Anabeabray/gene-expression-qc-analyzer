
import pandas as pd


def summarize_filtering(original, filtered):
    """
    Summarize the results of low-expression filtering
    """

    genes_before = original.shape[0]
    genes_after = filtered.shape[0]
    genes_removed = genes_before - genes_after

    summary = pd.DataFrame({
        "Metric": [
            "Genes before filtering",
            "Genes retained",
            "Genes removed",
            "Retention (%)",
            "Removal (%)"
        ],
        "Value": [
            genes_before,
            genes_after,
            genes_removed,
            round(genes_after / genes_before * 100, 2), #transform in percentage and round two decimal places
            round(genes_removed / genes_before * 100, 2) #transform in percentage and round two decimal places
        ]
    })

    return summary


def save_filtering_summary(summary, output_path):
    """
    Save filtering summary as CSV.
    """

    summary.to_csv(output_path, index=False) #index=False to avoid saving the index column in the CSV file


