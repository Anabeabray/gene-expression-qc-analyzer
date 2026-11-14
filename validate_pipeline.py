import os               #os: oprational system

from src.data_loader import data            #import our matriz
from src.filtering import filter_low_expression
from src.filtering_summary import summarize_filtering, save_filtering_summary
from src.visualization import plot_filtering_summary

#filtering
filtered_counts = filter_low_expression(data)

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

#generate filtering plot
plot_filtering_summary(
    summary,
    "results/filtered_counts.png"
)

