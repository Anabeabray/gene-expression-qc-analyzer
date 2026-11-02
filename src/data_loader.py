import pandas as pd 

# Load gene expression matrix (Carrega a matriz de expressão gênica)
data = pd.read_csv(
    "data/GSE175759_raw_counts_GRCh38.p13_NCBI.tsv.gz",
    sep = "\t",
    index_col = 0,
    compression= "gzip"
)

# Initial data exploration (Exploração inicial dos dados)
print("First 5 rows of the gene expression matrix:")
print(data.head())

print("\nMatrix dimensions:")
print(data.shape)

print("\nSample identifiers:")
print(data.columns)

print("\nGene identifiers:")
print(data.index)   

print("\nDescriptive statistics of the gene expression values:")
print(data.describe())  

