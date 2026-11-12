import math
import pandas as pd 

def filter_low_expression(
    data,
    min_count=10,
    min_fraction=0.1
):
    """
    Remove genes with low expression across samples.

    A gene is retained if it has at least min_count
    counts in at least min_fraction of the samples.
    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if data.empty:
        raise ValueError("The expression matrix is empty.")

    if data.isnull().values.any():
        raise ValueError("The matrix contains missing values.")

    if (data < 0).values.any():
        raise ValueError("The matrix contains negative values.")

    required_samples = math.ceil(
        min_fraction * data.shape[1]
    )

    expressed_genes = (data >= min_count).sum(axis=1)

    filtered_data = data.loc[
        expressed_genes >= required_samples
    ]

    return filtered_data
