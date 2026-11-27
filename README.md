# Gene Expression QC Analyzer
A Python tool for gene expression data preprocessing and quality control

## About the Project

**Gene Expression QC Analyzer** is a bioinformatics project developed to explore and implement basic preprocessing and quality control (QC) procedures for gene expression data, with a focus on RNA sequencing (RNA-seq) count matrices.

## Objectives
The project aims to provide a simple and reproducible workflow for checking data quality, filtering lowly expressed genes, normalizing counts using *Counts Per Million (CPM)*, and visualizing gene expression distributions.

## Features
1. Validate RNA-seq count matrices;
2. Identify potential data inconsistencies;
3. Filter genes with low expression;
4. Normalize counts using CPM;
5. Apply log2(CPM + 1) transformation;
6. Generate a filtering summary;
7. Visualize filtering results;
8. Export processed data and figures.

## Technologies
- Python
- pandas
- NumPy
- Matplotlib
- Seaborn
- Git and GitHub

## Setup
Clone the repository:

```bash
git clone https://github.com/Anabeabray/gene-expression-qc-analyzer.git
```

Navigate to the project directory:
```bash
cd gene-expression-qc-analyzer
```

Install the dependecies using the *requirements.txt* file, once available:
```bash
pip install -r requirements.txt
```
Make sure the input count matrix is available in the data/ directory before running the pipeline.

## Usage
### 1. Prepare your input data
Place your gene expression count matrix in the data/ directory.

The input matrix should contain:
- Genes as rows.
- Samples as columns.
- Raw gene expression counts as values.
- Gene identifiers as row identifiers.

*Supported input formats: CSV and TSV.*

### 2. Run the pipeline
Execute the main script, providing the path to your input matrix:
```bash
python main.py data/my_gene_counts.csv
```
### 3. Output files
Processed matrices, filtering summaries, and visualizations are automatically saved in the results/ directory.

## Autores
- Ana Beatriz Brayner 
- Mari Anne Merlotto

## License
To be determined 
