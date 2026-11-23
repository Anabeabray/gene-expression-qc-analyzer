
from src.data_loader import data
from src.filtering import filter_low_expression
from src.normalization import calculate_cpm, log2_transform
from src.correlation import (
    calculate_sample_correlation,
    plot_correlation_heatmap
)

#filter low-expression genes
filtered_counts = filter_low_expression(data)

#calculate CPM
normalized_cpm = calculate_cpm(filtered_counts)

#apply log2(CPM + 1)
normalized_log2_cpm = log2_transform(normalized_cpm)

#calculate sample correlation
correlation_matrix = calculate_sample_correlation(
    normalized_log2_cpm
)

#check correlation matrix
print("Correlation matrix:")
print(correlation_matrix)

print("\nCorrelation matrix dimensions:")
print(correlation_matrix.shape)

print("\nMissing correlation values:")
print(correlation_matrix.isna().sum().sum())

#generate heatmap
plot_correlation_heatmap(
    correlation_matrix,
    "results/correlation_heatmap.png"
)

print("\nCorrelation heatmap generated successfully!")

