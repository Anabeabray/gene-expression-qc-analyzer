
import matplotlib.pyplot as plt


def plot_filtering_summary(summary, output_path):
    """
    Plot the number of retained and removed genes
    """

    retained = summary.loc[
        summary["Metric"] == "Genes retained", "Value"
    ].iloc[0]           #extract the value of the "Genes retained" metric from the summary DataFrame

    removed = summary.loc[
        summary["Metric"] == "Genes removed", "Value"
    ].iloc[0]

    labels = ["Retained", "Removed"]        #define the bar plot's x-axis labels
    values = [retained, removed]            #define the bar plot's y-axis values

    plt.figure(figsize=(7, 5))              #define the figure size for the bar plot

    bars = plt.bar(labels, values)          #create the bar plot

    #add title and axis labels
    plt.title("Low-Expression Filtering Results")
    plt.ylabel("Number of Genes")
    plt.xlabel("Filtering Status")

    plt.bar_label(bars, fmt="%.0f")         #add the value labels on top of the bars

    plt.tight_layout()                      #adjust the layout to prevent overlapping elements
    plt.savefig(output_path, dpi=300)       #save the plot with specifc resolution (dpi=300)
    plt.close()                             #close the plot to free up memory and avoid displaying it in interactive environments

def plot_normalization_boxplots(counts, cpm, log2_cpm, output_path):
    """
    Compare gene expression distributions before and after normalization.
    """

    fig, axes = plt.subplots(1, 3, figsize=(20, 6))

    matrices = [
        (counts, "Filtered counts"),
        (cpm, "CPM"),
        (log2_cpm, "log2(CPM + 1)")
    ]

    for ax, (matrix, title) in zip(axes, matrices):
        ax.boxplot(matrix.values, showfliers=False)
        ax.set_title(title)
        ax.set_xlabel("Samples")
        ax.set_ylabel("Expression values")
        ax.tick_params(axis="x", labelbottom=False)

    fig.suptitle(
        "Gene Expression Distributions Before and After Normalization"
    )

    plt.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)



