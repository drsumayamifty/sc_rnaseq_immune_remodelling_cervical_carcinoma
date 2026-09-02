# Data Availability

## Publicly Available Single-Cell RNA Sequencing Datasets

The single-cell transcriptomic data analyzed in this project were obtained from publicly available Gene Expression Omnibus (GEO) datasets.

The study integrates cervical tissue single-cell RNA sequencing datasets covering normal, precancerous, and cervical carcinoma states.

### Dataset Sources

| GEO Accession | Data Type | Description |
|---------------|-----------|-------------|
| **GSE197461** | scRNA-seq + TCR-seq | Single-cell transcriptome and T-cell receptor sequencing data used for immune profiling and characterization of T-cell states within the cervical tumor microenvironment. |
| **GSE208653** | scRNA-seq | Single-cell RNA sequencing dataset used for comprehensive characterization of cellular composition and transcriptional changes across cervical tissue conditions. |

## Data Processing

Due to the large size of raw sequencing matrices, original count matrices and sequencing files are not included in this repository.

The complete analysis workflow can be reproduced by downloading the original datasets from GEO and following the provided Scanpy-based pipeline.

Processed files generated during analysis, including:
- quality-controlled single-cell objects
- cell metadata
- cluster annotations
- marker gene tables
- pathway enrichment results
- visualization outputs

are provided within the repository structure.

## GEO Links

- GSE197461: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE197461  
- GSE208653: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE208653

## Reproducibility

The repository contains all scripts and notebooks required for:

- Quality control and filtering
- Normalization and highly variable gene selection
- PCA and dimensionality reduction
- Leiden clustering
- Cell-type annotation
- Tumor microenvironment characterization
- Immune checkpoint analysis
- Differential expression analysis
- Functional enrichment analysis

Researchers can reproduce the analysis by obtaining the raw datasets from GEO and executing the provided workflow.
