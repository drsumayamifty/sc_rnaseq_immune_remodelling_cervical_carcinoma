"""
Cervical cancer scRNA-seq analysis
Generated from the original Scanpy notebook workflow.

This script corresponds to the notebook analysis step:
# Step 8.3: Normalization & Feature Selection
"""

adata.layers["counts"] = adata.X.copy()

sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

adata.raw = adata

sc.pp.highly_variable_genes(
    adata,
    n_top_genes=2500,
    batch_key="sample"
)

sc.pl.highly_variable_genes(adata)

sc.pp.regress_out(
    adata,
    ["total_counts", "pct_counts_mt"]
)

sc.pp.scale(adata, max_value=10)

