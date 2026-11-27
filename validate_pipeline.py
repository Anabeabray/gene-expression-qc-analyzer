import os               #os: oprational system

from src.data_loader import data            #import our matriz
from src.filtering import filter_low_expression
from src.filtering_summary import summarize_filtering, save_filtering_summary
from src.visualization import plot_filtering_summary
from src.normalization import calculate_cpm, log2_transform
from src.correlation import calculate_sample_correlation, plot_correlation_heatmap

#filtering
filtered_counts = filter_low_expression(data)

# normalization
normalized_cpm = calculate_cpm(filtered_counts)
normalized_log2_cpm = log2_transform(normalized_cpm)

#sample correlation
correlation_matrix = calculate_sample_correlation(normalized_log2_cpm)

#generating correlation heatmap
plot_correlation_heatmap(
    correlation_matrix,
    "results/correlation_heatmap.png"
)


#filtering summary
summary = summarize_filtering(data, filtered_counts)

#display results
print("\nFiltering summary:")
print(summary)

print("\nOriginal matrix dimensions:")
print(data.shape)

print("\nFiltered matrix dimensions:")
print(filtered_counts.shape)        #.shape: returns a tuple representing the dimensionality of the DataFrame (number of rows, number of columns)

#create results directory
os.makedirs("results", exist_ok=True)

#save filtering summary
save_filtering_summary(
    summary,
    "results/filtered_counts.csv"
)

#save normalized matrices
normalized_cpm.to_csv("results/normalized_cpm.csv")
normalized_log2_cpm.to_csv("results/normalized_log2_cpm.csv")

#generate filtering plot
plot_filtering_summary(
    summary,
    "results/filtered_counts.png"
)



#normalization summary
print("\nNormalized CPM matrix dimensions:")
print(normalized_cpm.shape)

print("\nLog2(CPM + 1) matrix dimensions:")
print(normalized_log2_cpm.shape)
