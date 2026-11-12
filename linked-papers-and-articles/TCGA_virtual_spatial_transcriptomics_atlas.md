# TCGA virtual spatial transcriptomics atlas

**Source:** https://huggingface.co/datasets/ratschlab/TCGA_virtual_spatial_transcriptomics_atlas

---

Eligibility declarations required to request access

This repository is publicly accessible, but you have to accept the conditions to access its files and content .

This dataset is released under CC-BY-NC-SA-4.0 strictly for non-commercial academic research. Commercial use is not permitted unless explicit written permission is granted by the authors. ELIGIBILITY. Access is granted only to individuals whose affiliations are exclusively academic or public non-profit research institutions. Anyone holding any concurrent commercial affiliation — employment, consulting, advisory roles, internships, or founding roles at a company or startup — is not eligible, regardless of intended use. SCOPE. Research performed at, for, funded by, or in collaboration with a commercial entity is commercial use and is prohibited. This includes corporate R&D, internal evaluation, benchmarking, and proof-of-concept work, even if exploratory and never productized. "Research" conducted in a commercial setting does not qualify as non-commercial academic research. REVIEW. All requests are reviewed manually against these criteria; please allow 3-5 business days. By submitting, you agree to share your contact information (email and username) with the repository authors. Vague, incomplete, or inaccurate submissions will be declined. False or incomplete declarations void any access granted and constitute a violation of the license terms. For commercial licensing, contact the maintainers.

Log in or Sign Up to review the conditions and access this dataset content.

TCGA virtual spatial transcriptomics atlas

This repository contains predicted spatial transcriptomics for TCGA H&E slides,
both fresh-frozen (FF) and formalin-fixed paraffin-embedded (FFPE), produced
with DeepSpot-M .

Authors : Kalin Nonchev, Sebastian Dawo, Karina Silina, Viktor Hendrik
Koelzer, and Gunnar Rätsch.

Model : ratschlab/DeepSpotM · Code : github.com/ratschlab/DeepSpotM · Paper : medRxiv 2026.06.19.26356060 .

[09.2026] Introducing Aurora - a no-code platform for virtual spatial transcriptomics from H&E images. Aurora makes virtual spatial transcriptomics accessible without requiring users to have their own GPUs, with a fully automated workflow designed to ensure that spatial transcriptomics predictions are performed correctly. Try the interactive Aurora demo .

One AnnData file ( .h5ad : HDF5 with internal gzip compression) per slide:

<TCGA_TYPE> is the TCGA project, e.g. TCGA_SKCM (codes below).

<FF|FFPE> follows the slide code in the TCGA barcode: TS , BS and MS (top, bottom and middle sections of a
frozen block) are FF, DX (diagnostic) slides are FFPE.

<slide_id> is the GDC slide file name without .svs , including its UUID; it is unique across the atlas.

metadata.csv has one row per file (columns below), for selecting slides before downloading.

Each spot is a square patch of 112 µm × 112 µm (224 × 224 px at 0.5 µm/px) on a non-overlapping lattice over
the tissue, and X holds the DeepSpot-M prediction of 19338 genes for each spot.

Contents (28,664 slides across 32 cancer types, 287,174,494 spots)

Model : the DeepSpot-M model finetuned on the matched spatial transcriptomics cohort (named in brackets) where one
exists, the base DeepSpot-M otherwise. Counts are computed from metadata.csv .

Folders use the TCGA study abbreviations below (full table: GDC code tables ).

A TCGA-SKCM slide: the H&E thumbnail (top-left) and DeepSpot-M predicted
expression for BRAF , CD37 and COL1A1 overlaid on the tissue. BRAF is a melanoma driver oncogene marking the tumour, CD37 is a
lymphocyte marker highlighting tumour-infiltrating immune cells, and COL1A1 is a collagen gene marking the stroma, so the three channels separate the
tumour, immune and stromal compartments.

This is a gated dataset, so log in first ( pip install huggingface_hub ):

Or select slides in metadata.csv first and download only those:

Each file is a standard spatial AnnData: the H&E overview is in uns['spatial'] and the spot centres are in obsm['spatial'] , so scanpy and squidpy plot it as it is:

X is stored as float16, the precision of the model output. Cast it to float32 before analysis: some scanpy
routines reject float16 (e.g. sc.tl.rank_genes_groups in scanpy 1.12), and in-place transforms such as sc.pp.scale would keep their result in float16.

The tissue QC is permissive (see Spots and QC ); a stricter filter can use the QC statistics stored per spot, e.g.
the rule applied to Visium spots:

Each file is data/<TCGA_TYPE>/<FF|FFPE>/<slide_id>.h5ad :

X : DeepSpot-M predicted expression of 19338 genes per spot, as log1p-normalised counts per
10,000 (log1p CP10k, log1p(counts / total counts × 10,000) , the scale DeepSpot-M is trained on); dense float16,
values >= 0.

.obs (one row per spot) index <array_row>x<array_col>_<slide_id> (e.g. 12x40_TCGA-… ), unique across the atlas; barcode is <array_row>x<array_col> , as <barcode>_<sample> in Visium data; sample_id (the slide id), dataset , slide_type . array_row , array_col : the patch's row and column on the lattice. Patch (r, c) covers level-0 rows [r·s, (r+1)·s) and columns [c·s, (c+1)·s) , with s = uns['he2st']['level0_patch_px'] (112 µm / mpp). x_pixel , y_pixel : the patch centre in level-0 (full-resolution) pixels, named as in Visium data: x_pixel is the row (vertical), y_pixel the column (horizontal). qc_* , per patch: qc_tissue_frac (fraction inside the tissue mask), qc_stained_pct (% of pixels with HSV
saturation > 15 and value < 240), qc_blur_var (variance of the Laplacian at 1 µm/px), qc_ink_frac (fraction
of pen ink), qc_sat_mean , qc_val_mean , qc_hue (mean HSV saturation, value and hue), qc_he_frac (fraction of the patch's 4 µm/px pixels with H&E colour: pink, purple or red hue and saturation >= 20).

index <array_row>x<array_col>_<slide_id> (e.g. 12x40_TCGA-… ), unique across the atlas; barcode is <array_row>x<array_col> , as <barcode>_<sample> in Visium data; sample_id (the slide id), dataset , slide_type .

array_row , array_col : the patch's row and column on the lattice. Patch (r, c) covers level-0 rows [r·s, (r+1)·s) and columns [c·s, (c+1)·s) , with s = uns['he2st']['level0_patch_px'] (112 µm / mpp).

x_pixel , y_pixel : the patch centre in level-0 (full-resolution) pixels, named as in Visium data: x_pixel is the row (vertical), y_pixel the column (horizontal).

qc_* , per patch: qc_tissue_frac (fraction inside the tissue mask), qc_stained_pct (% of pixels with HSV
saturation > 15 and value < 240), qc_blur_var (variance of the Laplacian at 1 µm/px), qc_ink_frac (fraction
of pen ink), qc_sat_mean , qc_val_mean , qc_hue (mean HSV saturation, value and hue), qc_he_frac (fraction of the patch's 4 µm/px pixels with H&E colour: pink, purple or red hue and saturation >= 20).

.var : index HGNC gene symbol; ensembl_ids , hgnc_id .

.obsm['spatial'] : the patch centres as (x, y) = (column, row) level-0 pixels (float64), as scanpy and
squidpy expect; equal to obs[['y_pixel', 'x_pixel']] .

.uns['spatial'][<slide_id>] : images['hires'] , an RGB overview of the slide (uint8, longest side at most
2,000 px); scalefactors['tissue_hires_scalef'] (level-0 pixels to hires pixels) and scalefactors['spot_diameter_fullres'] (the patch side in level-0 pixels); metadata['source_image'] (the slide
file name). The whole-slide image itself is not included.

.uns['he2st'] : provenance. Geometry: mpp (µm per level-0 pixel) and mpp_source , appmag , um_per_px (0.5), patch_px (224), patch_um (112), level0_patch_px , level0_width , level0_height , lattice . QC: qc (thresholds), patches (lattice cells kept and removed, per reason), subsample ( n_qc_pass , n_selected , cap , seed , method ). model : name, head, checkpoint sha256, gene-embedding source ( scgpt ), precision, resize. genes (gene table and its sha256); patch_step and hf_build (versions of the processing scripts).

Geometry: mpp (µm per level-0 pixel) and mpp_source , appmag , um_per_px (0.5), patch_px (224), patch_um (112), level0_patch_px , level0_width , level0_height , lattice .

QC: qc (thresholds), patches (lattice cells kept and removed, per reason), subsample ( n_qc_pass , n_selected , cap , seed , method ).

model : name, head, checkpoint sha256, gene-embedding source ( scgpt ), precision, resize.

genes (gene table and its sha256); patch_step and hf_build (versions of the processing scripts).

Patches. Each slide is tiled from its origin into non-overlapping squares of 112 µm, i.e. 112 µm / mpp
level-0 pixels, using the slide's own resolution ( openslide.mpp-x , else aperio.MPP , else the scanner
magnification; recorded in uns['he2st']['mpp_source'] ). Each patch is resampled to 224 × 224 px (0.5 µm/px)
for the model.

Tissue QC (permissive). A patch is kept when at least 10% of it lies inside the slide's tissue mask (stained or
tissue-coloured pixels, with enclosed holes such as fat and lumina filled). Removed are background and glass,
blank patches, uniform non-H&E blocks (marker, labels, slide edges, shadows), gray or black shadows without H&E
colour that are darker than the slide's glass (scan-edge bands, coverslip and bubble rims, the rims of marker
signs) and patches with at least 25% pen ink. The QC statistics are kept in obs for stricter filtering.

At most 50,000 spots per slide. On slides with more patches that pass QC, 50,000 are drawn at random with a
per-slide seed (the first 8 bytes of sha256(slide_id), numpy default_rng ); the spots stay in raster order. uns['he2st']['subsample'] has the counts, and metadata.csv marks these slides ( subsampled ).

Model. DeepSpot-M with scGPT gene embeddings: the finetuned model of the matched cohort for the cancer types
listed with one under Contents , the base model otherwise. Negative outputs are clipped to 0.

Computational data analysis was performed at Leonhard Med , the secure trusted research environment at ETH Zurich. Our pipeline aligns with the specific cluster requirements and resources.

Models trained or fine-tuned on ratschlab/TCGA_virtual_spatial_transcriptomics_atlas
