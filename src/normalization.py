import pandas as pd
import numpy as np


def calculate_cpm(counts):
    """
    Calculate Counts Per Million (CPM) for a gene expression matrix.

    Parameters
    ----------
    counts : pandas.DataFrame
        Raw gene count matrix, with genes as rows and samples as columns.

    Returns
    -------
    pandas.DataFrame
        CPM-normalized gene expression matrix.
    """

    #validating input
    if not isinstance(counts, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if counts.empty:
        raise ValueError("Input matrix is empty.")

    if counts.isna().any().any():
        raise ValueError("Input matrix contains missing values.")

    if not all(pd.api.types.is_numeric_dtype(dtype)
               for dtype in counts.dtypes):
        raise TypeError("All values must be numeric.")

    if not np.isfinite(counts.to_numpy()).all():
        raise ValueError("Input contains non-finite values.")

    if (counts < 0).any().any():
        raise ValueError("Counts cannot be negative.")



    #calculate total counts for each sample
    library_sizes = counts.sum(axis=0)              #library size for each sample (column)

    if (library_sizes == 0).any():
        raise ValueError("One or more samples have zero total counts.")

    #calculate CPM
    cpm = counts.div(library_sizes, axis=1) * 1_000_000

    return cpm



def log2_transform(cpm):
    """
    Apply log2(CPM + 1) transformation.

    Parameters
    ----------
    cpm : pandas.DataFrame
        CPM-normalized gene expression matrix.

    Returns
    -------
    pandas.DataFrame
        Log2-transformed expression matrix.
    """

    #validating input
    if not isinstance(cpm, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if cpm.empty:
        raise ValueError("Input matrix is empty.")

    if cpm.isna().any().any():
        raise ValueError("Input matrix contains missing values.")

    if not all(pd.api.types.is_numeric_dtype(dtype)
               for dtype in cpm.dtypes):
        raise TypeError("All values must be numeric.")

    if not np.isfinite(cpm.to_numpy()).all():
        raise ValueError("Input contains non-finite values.")

    if (cpm < 0).any().any():
        raise ValueError("CPM values cannot be negative.")

    #apply log2(CPM + 1)
    log2_cpm = np.log2(cpm + 1)

    return log2_cpm


