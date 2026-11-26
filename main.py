print("Gene Expression QC Analyzer")

import os

from src.data_loader import data
from src.filtering import filter_low_expression
from src.normalization import calculate_cpm, log2_transform


def main():

    # Create results directory if it does not exist
    os.makedirs("results", exist_ok=True)

    # 1. Load and validate raw count data
    print("Raw data loaded successfully.")
    print("Original matrix shape:", data.shape)

    # 2. Filter low-expression genes
    filtered_data = filter_low_expression(data)
    print("Filtering completed.")
    print("Filtered matrix shape:", filtered_data.shape)

    # 3. Calculate CPM
    cpm_data = calculate_cpm(filtered_data)
    print("CPM normalization completed.")

    # 4. Apply log2 transformation
    log2_cpm_data = log2_transform(cpm_data)
    print("Log2 transformation completed.")

    # 5. Save processed matrices
    filtered_data.to_csv("results/filtered_counts.csv")
    cpm_data.to_csv("results/cpm_counts.csv")
    log2_cpm_data.to_csv("results/normalized_expression.csv")

    print("All processing steps completed successfully.")


if __name__ == "__main__":
    main()
