"""
Cervical cancer scRNA-seq analysis
Generated from the original Scanpy notebook workflow.

This script corresponds to the notebook analysis step:
# Step 8.6: Evaluating T-Cell Exhaustion & Immune Checkpoint Expression
"""

exhaustion_genes = [
    "PDCD1",
    "CTLA4",
    "HAVCR2",
    "LAG3",
    "TIGIT",
    "FOXP3"
]

available_exhaustion = [
    g for g in exhaustion_genes
    if g in adata.var_names
]

sc.pl.violin(
    adata,
    keys=available_exhaustion,
    groupby="group",
    rotation=45,
    multi_panel=True
)

