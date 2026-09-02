"""
Cervical cancer scRNA-seq analysis
Generated from the original Scanpy notebook workflow.

This script corresponds to the notebook analysis step:
# Step 8.2: Quality Control (QC) & Filtering
"""

adata.var["mt"] = adata.var_names.str.startswith("MT-")
adata.var["ribo"] = adata.var_names.str.startswith(("RPS", "RPL"))
adata.var["hb"] = adata.var_names.str.startswith(
    ("HBA", "HBB", "HBD", "HBE", "HBG", "HBM", "HBQ", "HBZ")
)

sc.pp.calculate_qc_metrics(
    adata,
    qc_vars=["mt", "ribo", "hb"],
    percent_top=None,
    log1p=False,
    inplace=True
)

sc.pl.violin(
    adata,
    ["n_genes_by_counts", "total_counts", "pct_counts_mt", "pct_counts_hb"],
    groupby="group",
    jitter=0.4,
    multi_panel=True
)

sc.pp.filter_cells(adata, min_genes=250)
sc.pp.filter_genes(adata, min_cells=5)

adata = adata[adata.obs["pct_counts_mt"] < 15, :].copy()
adata = adata[adata.obs["pct_counts_hb"] < 5, :].copy()

print(adata.n_obs)

