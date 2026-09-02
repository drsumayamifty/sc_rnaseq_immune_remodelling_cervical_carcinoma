# Single-Cell Transcriptomic Analysis of Immune Remodeling Across the Cervical Cancer Progression Continuum

## Overview

This repository contains a complete single-cell RNA sequencing (scRNA-seq) analysis workflow investigating immune and epithelial remodeling during cervical cancer progression.

The study reconstructs the transcriptional landscape across the normal cervix–high-grade squamous intraepithelial lesion (HSIL)–cervical carcinoma continuum using publicly available 10x Genomics datasets. The primary objective was to characterize changes in cellular composition, tumor microenvironment remodeling, immune checkpoint activation, T-cell exhaustion-associated signatures, and stage-specific biological pathways.

The analysis was performed using a reproducible Python-based Scanpy workflow with downstream differential expression and pathway enrichment analysis.

---

# Research Questions

This project addresses the following biological questions:

1. How does the cellular landscape change from normal cervix to precancerous HSIL and invasive cervical carcinoma?

2. Can major epithelial, immune, stromal, and endothelial cell populations be identified from public cervical cancer scRNA-seq datasets?

3. Does cervical cancer progression associate with increased immune checkpoint and T-cell exhaustion signatures?

4. Which biological pathways characterize normal cervix, HSIL, squamous cell carcinoma (SCC), and adenocarcinoma (ADC) states?

---

# Dataset Information

## Data Accession

Raw single-cell RNA sequencing data were obtained from:

- **GSE197461**
  - scRNA-seq + TCR-seq cervical cancer dataset

- **GSE208653**
  - scRNA-seq cervical tissue dataset

The analysis included nine 10x Genomics samples representing five histological groups:

| Group | Samples |
|---|---|
| HPV-negative normal cervix | N_HPV_NEG_1, N_HPV_NEG_2 |
| HPV-positive normal cervix | N_1, N_2 |
| Precancerous HSIL | HSIL_1, HSIL_2 |
| Squamous cell carcinoma (SCC) | SCC_4, SCC_5 |
| Adenocarcinoma (ADC) | ADC_6 |

After quality filtering, the final dataset contained:

- **74,722 cells**
- **18,361 genes**
- **27 transcriptional clusters**

---

# Analysis Workflow

## Step 1: Data Loading and Preparation

Raw 10x Genomics count matrices were imported using Scanpy and merged into a unified AnnData object.

Performed:

- 10x matrix loading
- Sample integration
- Gene filtering
- Metadata preparation

---

## Step 2: Quality Control and Filtering

Quality metrics were calculated for each cell.

Filtering criteria:

- Minimum detected genes per cell: 250
- Genes detected in fewer than 5 cells removed
- Mitochondrial reads >15% removed
- Hemoglobin contamination >5% removed

QC metrics evaluated:

- Number of detected genes
- Total UMI counts
- Mitochondrial percentage
- Hemoglobin percentage

---

## Step 3: Normalization and Feature Selection

Processing steps:

- Library-size normalization
- Log1p transformation
- Selection of highly variable genes

Parameters:

- 2,500 highly variable genes selected
- PCA performed using 50 components

---

## Step 4: Dimensional Reduction and Clustering

A graph-based clustering workflow was applied:

- PCA
- k-nearest neighbor graph construction
- UMAP visualization
- Leiden clustering

Parameters:

- 30 principal components
- n_neighbors = 20
- Leiden resolution = 0.8

The analysis identified 27 transcriptionally distinct clusters.

---

## Step 5: Cell Type Annotation

Clusters were annotated using canonical marker genes.

Identified cell populations:

| Cell Type | Marker Genes |
|-|-|
| Epithelial/Tumor cells | EPCAM, KRT5, KRT14 |
| T cells | CD3D, CD4, CD8A |
| Regulatory T cells | FOXP3, IL2RA, CTLA4 |
| NK cells | NKG7, NCAM1 |
| B cells | MS4A1, CD79A |
| Plasma cells | SDC1, MZB1 |
| Myeloid/TAM | CD14, CD68, CD163 |
| Fibroblasts | COL1A1, ACTA2 |
| Endothelial cells | PECAM1, VWF |

---

## Step 6: Immune Checkpoint and T-cell Exhaustion Analysis

Immune regulatory genes were evaluated across disease stages.

Genes analyzed:

- PDCD1
- CTLA4
- HAVCR2
- LAG3
- TIGIT
- FOXP3

The SCC group showed increased expression of multiple exhaustion-associated genes, suggesting progressive immune suppression during malignant transformation.

---

## Step 7: Differential Expression Analysis

Stage-specific differential expression was performed using:

- Wilcoxon rank-sum test
- One-versus-rest comparison

Groups analyzed:

- Normal
- HSIL
- SCC
- ADC

Output:

- Differential expression tables
- Ranked marker genes
- Stage-specific signatures

---

## Step 8: Pathway Enrichment Analysis

Significantly upregulated genes were analyzed using:

- KEGG
- Gene Ontology Biological Process
- Reactome

Tools:

- GSEApy
- Enrichr

Major biological signatures:

### Normal Cervix

Enriched pathways:

- Extracellular matrix organization
- Focal adhesion
- Tissue homeostasis

### HSIL

Enriched pathways:

- Cilium organization
- DNA repair
- Homologous recombination

### SCC

Enriched pathways:

- Immune system activation
- Cytokine signaling
- Inflammatory response
- Negative regulation of T-cell proliferation

### ADC

Enriched pathways:

- Neutrophil migration
- Granulocyte chemotaxis

---

# Software and Reproducibility

The workflow was developed using:

- Python 3.11
- Scanpy
- AnnData
- NumPy
- Pandas
- SciPy
- Matplotlib
- Seaborn
- GSEApy

Environment management:

- uv package manager
- requirements.txt
- uv.lock

The separated scripts reproduce each major analysis stage from data loading to pathway enrichment.

---

# Main Outputs

The repository contains:

## Figures

- Quality control plots
- UMAP clustering visualization
- Cell-type annotation plots
- Marker gene dot plots
- Immune checkpoint expression plots
- Pathway enrichment visualization

## Tables

- Differential expression results
- Stage-specific marker genes
- Enrichment analysis results

---

# Biological Summary

This analysis demonstrates progressive immune remodeling during cervical carcinogenesis.

The normal cervix showed epithelial and extracellular matrix-associated programs, whereas SCC demonstrated increased immune activation, inflammatory signaling, and immune checkpoint-associated transcriptional states.

The results support a transition toward an immune-suppressive tumor microenvironment during malignant progression.

---

# Limitations

- ADC analysis was based on a single patient sample.
- Batch correction methods were not applied.
- T-cell and myeloid populations were not deeply sub-clustered.
- Ligand-receptor communication analysis was not performed.

Future extensions may include:

- T-cell receptor clonotype analysis
- inferCNV-based malignant cell identification
- CellPhoneDB ligand-receptor analysis
- Dedicated immune compartment sub-clustering

---

# References

1. Guo C et al. Spatiotemporally deciphering the mysterious mechanism of persistent HPV-induced malignant transition and immune remodelling from HPV-infected normal cervix, precancer to cervical cancer. Clinical and Translational Medicine. 2023.

2. Qu X et al. Interactions of IDO1+ LAMP3+ dendritic cells with regulatory T cells and exhausted T cells in cervical cancer. Cancer Communications. 2023.

3. Wolf FA et al. SCANPY: large-scale single-cell gene expression data analysis. Genome Biology. 2018.

4. Becht E et al. Dimensionality reduction for visualizing single-cell data using UMAP. Nature Biotechnology. 2019.

---

# Single-Cell Transcriptomic Analysis of Immune Remodeling Across the Cervical Cancer Progression Continuum

## Authors and Affiliations

**Dr. Sumaya Khan Mifty**  
Dhaka Medical College and Hospital, Dhaka, Bangladesh  

**Jerin Shubah Lamia**  
Doctor of Veterinary Medicine (DVM)  
Sylhet Agricultural University, Sylhet-3100, Bangladesh  

**Sayma Anjum Sujana**  
Department of Biochemistry & Biotechnology  
Independent University, Bangladesh  

---

## AI Usage Disclosure

Generative artificial intelligence (AI) tools were used as a supporting tool during the development of this project.

AI assistance was used for:

- Improving scientific writing structure and clarity.
- Organizing the repository documentation and README formatting.
- Assisting with interpretation of computational outputs generated from the author's own analysis pipeline.
- Supporting code organization and documentation.

All computational analyses, including data preprocessing, quality control, normalization, dimensionality reduction, clustering, cell-type annotation, differential expression analysis, immune checkpoint analysis, and pathway enrichment analysis were performed using the authors' own workflow.

All reported numerical results, including:

- cell numbers,
- gene counts,
- differential expression statistics,
- adjusted P-values,
- pathway enrichment results,
- and generated figures,

were derived from the original Scanpy/GSEApy analysis outputs and were manually reviewed by the authors.

AI tools were not used to generate biological results, fabricate experimental findings, or replace scientific interpretation. The authors take full responsibility for the accuracy, integrity, and interpretation of the presented analysis.
