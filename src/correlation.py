
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path            #python's native library


def calculate_sample_correlation(expression_data):
    """
    Calculate Pearson correlation between gene expression samples
    """

    correlation_matrix = expression_data.corr(method="pearson")

    return correlation_matrix


def plot_correlation_heatmap(correlation_matrix, output_path):
    """
    Generate and save a heatmap of sample correlations
    """

    plt.figure(figsize=(12, 10))

    sns.heatmap(
        correlation_matrix,
        annot=True,                 #show numeric values in the heatmap
        fmt=".2f",                  #format the numbers to 2 decimal places
        cmap="coolwarm",            #color map
        vmin=-1,                    #minimum value for the color scale
        vmax=1,                     #maximum value for the color scale
        center=0                    #center the color scale at 0
    )


    plt.title("Sample Correlation Heatmap")
    plt.xlabel("Samples")
    plt.ylabel("Samples")
    plt.tight_layout()      #adjusts the layout to avoid overlapping


    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()

