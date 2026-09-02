"""
Cervical cancer scRNA-seq analysis
Generated from the original Scanpy notebook workflow.

This script corresponds to the notebook analysis step:
# Step 8.5: Tumor Microenvironment Cell Type Annotation
"""

lineage_dict = {
    "Epithelial_Tumor": ["EPCAM", "KRT5", "KRT14"],
    "T_cells": ["CD3D", "CD4", "CD8A"],
    "Tregs": ["FOXP3", "IL2RA", "CTLA4"],
    "NK": ["NKG7", "NCAM1"],
    "B_cells": ["MS4A1", "CD79A"],
    "Plasma": ["SDC1", "MZB1"],
    "Myeloid_TAM": ["CD14", "CD68", "CD163"],
    "Fibroblasts": ["COL1A1", "ACTA2"],
    "Endothelial": ["PECAM1", "VWF"]
}

sc.pl.dotplot(
    adata,
    var_names=lineage_dict,
    groupby="leiden_res_0.8"
)

sc.pl.umap(
    adata,
    color=["EPCAM", "CD3D", "CD68", "MS4A1", "COL1A1", "PECAM1"]
)

