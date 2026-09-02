"""
Cervical cancer scRNA-seq analysis
Generated from the original Scanpy notebook workflow.

This script corresponds to the notebook analysis step:
# Step 8.7: Differential Expression & Pathway Enrichment
"""

sc.tl.rank_genes_groups(
    adata,
    groupby="tissue_type",
    method="wilcoxon"
)

tumor_de_df = sc.get.rank_genes_groups_df(
    adata,
    group="Tumor"
)

tumor_de_df.head(15)

