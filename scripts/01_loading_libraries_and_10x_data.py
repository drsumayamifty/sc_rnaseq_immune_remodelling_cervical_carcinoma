"""
Cervical cancer scRNA-seq analysis
Generated from the original Scanpy notebook workflow.

This script corresponds to the notebook analysis step:
# Step 8.1: Loading Libraries & 10x Data into Scanpy
"""

import scanpy as sc
import anndata as ad
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

sc.settings.verbosity = 3
sc.settings.set_figure_params(dpi=120, facecolor="white", frameon=False)

data_dir = Path("data")

selected_samples = ["N_HPV_NEG_1", "N_HPV_NEG_2", "SCC_4", "SCC_5",
                    "HSIL_1", "HSIL_2", "N_1", "N_2", "ADC_6"]

sample_dirs = [data_dir / s for s in selected_samples if (data_dir / s).exists()]

adatas = {}

for sample_path in sample_dirs:
    sample_id = sample_path.name

    adata_sample = sc.read_10x_mtx(
        path=sample_path,
        var_names="gene_symbols",
        cache=False
    )

    adata_sample.obs["sample"] = sample_id

    if "HPV_NEG" in sample_id:
        adata_sample.obs["group"] = "Normal_HPV_Neg"
        adata_sample.obs["tissue_type"] = "Normal"
    elif sample_id.startswith("SCC"):
        adata_sample.obs["group"] = "Cervical_SCC"
        adata_sample.obs["tissue_type"] = "Tumor"
    elif sample_id.startswith("HSIL"):
        adata_sample.obs["group"] = "Precancerous_HSIL"
        adata_sample.obs["tissue_type"] = "Precancer"
    elif sample_id.startswith("ADC"):
        adata_sample.obs["group"] = "Cervical_ADC"
        adata_sample.obs["tissue_type"] = "Tumor"
    else:
        adata_sample.obs["group"] = "Normal_HPV_Pos"
        adata_sample.obs["tissue_type"] = "Normal"

    adatas[sample_id] = adata_sample

adata = ad.concat(adatas, label="sample_batch", index_unique="-", join="outer")
adata.var_names_make_unique()

print(adata)

