---
authors: Dr. Sumaya Khan Mifty; Jerin Shubah Lamia; Sayma Anjum Sujana
title: Single-Cell Transcriptomic Dissection of Immune and Epithelial
  Remodeling Across the Normal Cervix--HSIL--Carcinoma Continuum
---

# Abstract

This report describes a single-cell RNA sequencing analysis of cervical
carcinogenesis using publicly available 10x Genomics datasets. The study
reconstructs immune and epithelial remodeling across HPV-negative normal
cervix, HPV-positive normal cervix, HSIL, squamous cell carcinoma (SCC),
and adenocarcinoma (ADC).

Raw count matrices were obtained from GEO datasets GSE197461
(scRNA-seq + TCR-seq) and GSE208653 (scRNA-seq). Nine samples were
processed using Scanpy with quality control, normalization, highly
variable gene selection, PCA, UMAP, Leiden clustering, cell-type
annotation, immune checkpoint analysis, differential expression, and
pathway enrichment.

After quality control, 74,722 cells and 18,361 genes were retained.
Twenty-seven transcriptional clusters were identified. SCC showed
increased immune checkpoint and T-cell exhaustion-associated transcripts
including HAVCR2, TIGIT, LAG3, CTLA4, and FOXP3. Pathway analysis
identified extracellular matrix organization in normal tissue, DNA
repair programs in HSIL, immune and cytokine signaling in SCC, and
neutrophil-related pathways in ADC.

# Data Availability

Datasets: - GSE197461 (scRNA-seq + TCR-seq) - GSE208653 (scRNA-seq)

Raw data format: - barcodes.tsv.gz - features.tsv.gz - matrix.mtx.gz

# Computational Workflow

## Quality Control

Filtering criteria:

  Metric                   Threshold
  ------------------------ -----------
  Minimum genes per cell   ≥250
  Minimum cells per gene   ≥5
  Mitochondrial reads      \<15%
  Hemoglobin reads         \<5%

## Normalization and Clustering

The workflow included: - Library size normalization - Log
transformation - Highly variable gene selection - PCA - k-nearest
neighbor graph construction - UMAP visualization - Leiden clustering

## Cell Type Annotation

Canonical markers were used to identify: - Epithelial/tumor cells - T
cells - Regulatory T cells - NK cells - B cells - Plasma cells -
Myeloid/TAM cells - Fibroblasts - Endothelial cells

# Results Summary

## Immune Remodeling

Immune checkpoint and exhaustion markers increased toward carcinoma,
especially SCC. The observed pattern supports progressive immune
suppression during cervical cancer progression.

## Pathway Enrichment

Normal: - Extracellular matrix organization - Tissue homeostasis

HSIL: - DNA repair - Ciliary organization

SCC: - Immune system activation - Cytokine signaling - Negative
regulation of T-cell proliferation

ADC: - Neutrophil migration - Granulocyte chemotaxis

# Limitations

-   ADC analysis was based on a single patient.
-   Batch correction methods were not applied.
-   T-cell and myeloid sub-clustering were not performed.
-   Ligand-receptor analysis was not included.

# Conclusion

This Scanpy-based single-cell RNA-seq workflow reconstructs the cervical
cancer progression continuum and identifies progressive immune
checkpoint enrichment and tumor microenvironment remodeling from normal
tissue to carcinoma.

# AI Usage Disclosure

AI tools were used for literature comprehension, scientific writing
refinement, code explanation, debugging assistance, and figure
interpretation support.

All final analysis decisions, interpretations, and conclusions were
reviewed by the authors.

# Authors

## Dr. Sumaya Khan Mifty

Dhaka Medical College and Hospital

## Jerin Shubah Lamia

Doctor of Veterinary Medicine, Sylhet Agricultural University

## Sayma Anjum Sujana

Biochemistry & Biotechnology, Independent University, Bangladesh
