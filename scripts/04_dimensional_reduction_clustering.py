"""
Cervical cancer scRNA-seq analysis
Generated from the original Scanpy notebook workflow.

This script corresponds to the notebook analysis step:
# Step 8.4: Dimensional Reduction & Graph-Based Clustering
"""

sc.tl.pca(
    adata,
    svd_solver="arpack",
    use_highly_variable=True
)

sc.pl.pca_variance_ratio(
    adata,
    log=True,
    n_pcs=50
)

sc.pp.neighbors(
    adata,
    n_neighbors=20,
    n_pcs=30
)

sc.tl.umap(adata)

sc.tl.leiden(
    adata,
    resolution=0.8,
    key_added="leiden_res_0.8"
)

sc.pl.umap(
    adata,
    color=["leiden_res_0.8", "group", "tissue_type", "sample"]
)

