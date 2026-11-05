import pandas as pd 

# Load gene expression matrix (Carrega a matriz de expressão gênica)
data = pd.read_csv(
    "data/GSE175759_raw_counts_GRCh38.p13_NCBI.tsv.gz",
    sep = "\t",
    index_col = 0,
    compression= "gzip"
)



#data validation
def validate_counts(data):

    #missing values
    if data.isna().any().any():
        print("Warning: Missing values detected.")

    #duplicated genes
    if data.index.duplicated().any():
        print("Warning: Duplicated genes detected.")

    #duplicated samples
    if data.columns.duplicated().any():
        print("Warning: Duplicated samples detected.")

    #invalid gene identifiers
    if data.index.isna().any():
        print("Warning: Missing gene identifiers.")

    if (data.index.astype(str).str.strip() == "").any():
        print("Warning: Empty gene identifiers.")

    #negative values
    if (data < 0).any().any():
        print("Warning: Negative values detected.")

    #non numeric columns
    if not all(data.dtypes.apply(pd.api.types.is_numeric_dtype)):
        print("Warning: Non-numeric columns detected.")

    print("Data validation completed.")

    return data

#execute data validation
data = validate_counts(data)



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

