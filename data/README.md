# Dataset Documentation

## 1. Dataset Information

| Attribute | Description |
| :--------  | :---------- |
| Dataset ID | GSE175759 |
| Status | Public on May 02, 2022 |
| Contributor(s) | Park S, Lee H, Yang S, Kim D, Lee S, Lee J, Choi M |
| Title | RNA-seq profiling of tubulointerstitial tissue reveals a potential therapeutic role of dual anti-phosphatase 1 in kidney diseases |
| Repository | NCBI Gene Expression Omnibus (GEO) |
| Organism | *Homo sapiens* |
| Tissue | Kidney (renal tubulointerstitial tissue) |
| Data type | RNA-seq |
| Reference genome | GRCh37.p13 |
| Data format | .tsv (tab-separated values) |
| Data representation | Raw gene expression counts |

## 2. Data Source

The dataset was obtained from the **NCBI Gene Expression Omnibus (GEO)**.

- **GEO accession:** GSE175759
- **Dataset page:** [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE175759](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE175759)
- **Associated article:** [RNA-seq profiling of tubulointerstitial tissue reveals a potential therapeutic role of dual anti-phosphatase 1 in glomerulonephritis](https://pubmed.ncbi.nlm.nih.gov/35488446/)
- **File:** `GSE175759_raw_counts_GRCh38.p13_NCBI.tsv.gz`

## 3. Experimental Design
The study investigates gene expression in renal tubulointerstitial tissue.

The study comprises 87 samples:

| Group | Number of samples |
| :------ | ----------------: |
| IgA nephropathy | 43 |
| *Diabetes mellitus* nephropathy | 3 |
| Focal segmental glomerulosclerosis | 3 |
| Lupus nephritis | 3 |
| Membranous nephropathy | 4 |
| Minimal change disease | 9 |
| Control | 22 |
| Total   | 87 |

- The 3 outliers which were not included in the main analysis were also uploaded in the database.

## 4. File Description

The file `GSE175759_raw_counts_GRCh38.p13_NCBI.tsv.gz` contains a gene expression count matrix.

CHECK IF THE INFOS BELOW ARE CORRECT

- Rows represent genes.
- Columns represent biological samples.
- Gene identifiers are provided in the first column.
- Expression values represent raw read counts.
- The file is compressed using gzip.

The matrix is suitable for exploratory gene expression analysis and quality control workflows.

## 5. Data Processing in Gene Expression QC Analyzer

The dataset is used to evaluate the functionality of the **Gene Expression QC Analyzer**.

The planned processing steps include:

CHECK IF THIS IS THE WORKFLOW WE WILL FOLLOW:

1. Importing the raw count matrix.
2. Checking matrix dimensions and data integrity.
3. Filtering genes with low expression.
4. Calculating Counts Per Million (CPM).
5. Applying log2(CPM + 1) transformation.
6. Performing basic quality control.
7. Generating visualizations for exploratory analysis.

## 6. Data Availability

The dataset is publicly available through the **NCBI GEO** repository.

The original compressed file is not included in this repository. Users should download it directly from GEO.

## 7. Reference

NCBI Gene Expression Omnibus (GEO).

GSE175759: RNA-seq profiling of tubulointerstitial tissue reveals a potential therapeutic role of dual anti-phosphatase 1 in kidney diseases.
