# HEST Xenium virtual spatial transcriptomics

**Source:** https://huggingface.co/datasets/ratschlab/HEST_Xenium_virtual_spatial_transcriptomics

---

Eligibility declarations required to request access

This repository is publicly accessible, but you have to accept the conditions to access its files and content .

This dataset is released under CC-BY-NC-SA-4.0 strictly for non-commercial academic research. Commercial use is not permitted unless explicit written permission is granted by the authors. ELIGIBILITY. Access is granted only to individuals whose affiliations are exclusively academic or public non-profit research institutions. Anyone holding any concurrent commercial affiliation — employment, consulting, advisory roles, internships, or founding roles at a company or startup — is not eligible, regardless of intended use. SCOPE. Research performed at, for, funded by, or in collaboration with a commercial entity is commercial use and is prohibited. This includes corporate R&D, internal evaluation, benchmarking, and proof-of-concept work, even if exploratory and never productized. "Research" conducted in a commercial setting does not qualify as non-commercial academic research. REVIEW. All requests are reviewed manually against these criteria; please allow 3-5 business days. By submitting, you agree to share your contact information (email and username) with the repository authors. Vague, incomplete, or inaccurate submissions will be declined. False or incomplete declarations void any access granted and constitute a violation of the license terms. For commercial licensing, contact the maintainers.

Log in or Sign Up to review the conditions and access this dataset content.

HEST Xenium virtual spatial transcriptomics

Virtual spatial transcriptomics for 59 H&E sections of the 10x Xenium samples in HEST-1k (14 OncoTree codes): 19,338 genes in each of 13,328,590 cells , predicted with DeepSpot-M . Each file also holds the measured Xenium panel of the sample.

Model : DeepSpot-M ( ratschlab/DeepSpotM ) · Code : github.com/ratschlab/DeepSpotM · Paper : medRxiv 2026.06.19.26356060 .

[11.2026] Files re-encoded as float16 with identical values and renamed from data/<id>.h5ad.gz to data/<id>.h5ad .

[09.2026] Introducing Aurora - a no-code platform for virtual spatial transcriptomics from H&E images. Try the interactive Aurora demo .

Lung section NCBI866 : H&E and virtual FOXJ1 (ciliated epithelium), PTPRC (immune cells) and LUM (stroma).

This is a gated dataset: log in first ( pip install huggingface_hub ).

X : virtual expression of 19,338 genes per cell, log1p-CPM, stored as float16 (cast to float32 before
analysis).

layers['ground_truth'] : measured Xenium expression (log1p counts per 10,000 over the panel genes), sparse,
zero outside the panel genes.

obs : one row per cell: cell_id , barcode , n_counts , n_genes , grid position ( x_array , y_array ) and
centre in pixels ( x_pixel , y_pixel ).

var : gene_symbol , is_panel (measured on the sample's panel), is_seed / is_holdout (panel genes used /
withheld in fine-tuning), per-gene Pearson correlation with the measurement ( pearson_raw , pearson_knn5 ).

obsm['spatial'] and uns['spatial'] : cell centres and an H&E overview image, as scanpy and squidpy
expect; uns also holds per-sample accuracy ( pearson_* ) and provenance.

metadata.csv : one row per sample (key id ): the HEST metadata (organ, disease state, OncoTree code, panel
size, study link, ...), n_spots and file_path .

CC BY-NC-SA 4.0 , non-commercial academic research only. The
H&E images and measured Xenium data come from HEST-1k and remain
subject to its terms.

Computational data analysis was performed at Leonhard Med , the secure trusted research environment at ETH Zurich. Our pipeline aligns with the specific cluster requirements and resources.

Models trained or fine-tuned on ratschlab/HEST_Xenium_virtual_spatial_transcriptomics
