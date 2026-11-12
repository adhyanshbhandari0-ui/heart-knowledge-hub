# Cell Painting Gallery

**Source:** https://registry.opendata.aws/cellpainting-gallery

---

bioinformatics biology cancer cell biology cell imaging cell painting chemical biology computer vision csv deep learning fluorescence imaging genetic high-throughput imaging image processing image-based profiling imaging life sciences machine learning medicine microscopy organelle

The Cell Painting Gallery is a collection of image datasets created using the Cell Painting assay. 
The images of cells are captured by microscopy imaging, and reveal the response of various labeled cell components to whatever treatments are tested, which can include genetic perturbations, chemicals or drugs, or different cell types. 
The datasets can be used for diverse applications in basic biology and pharmaceutical research, such as identifying disease-associated phenotypes, understanding disease mechanisms, and predicting a drugâs activity, toxicity, or mechanism of action ( Chandrasekaran et al 2020 ). 
This collection is maintained by the CarpenterâSingh lab and the Cimini lab at the Broad Institute .
A human-friendly listing of datasets, instructions for accessing them, and other documentation is at the corresponding GitHub page about the Gallery.

Typically when an associated publication is posted on biorxiv

CC0 1.0 Universal (CC0 1.0) Public Domain Dedication, but please do cite the corresponding publication for each dataset, as listed here .

https://github.com/broadinstitute/cellpainting-gallery

Carpenter-Singh and Cimini Labs at the Broad Institute

See all datasets managed by Carpenter-Singh and Cimini Labs at the Broad Institute .

Cell Painting Gallery was accessed on DATE from https://registry.opendata.aws/cellpainting-gallery.

Center for Open Bioimage Analysis (COBA) YouTube Channel - video tutorials of CellProfiler and other softwares by Multiple Authors

Image-based Profiling Handbook - for processing image-based profiling datasets using CellProfiler and pycytominer by Multiple Authors

Image-based profiling introductory exercise - data and an exercise on exploring image-based profiles, including understanding the various data levels by Beth Cimini

Scientific Community Image Forum - for software-oriented aspects of scientific imaging including analysis, processing, and acquisition by Multiple Authors

Accelerating Drug Discovery with high-throughput Cell Painting on AWS by Chris Kaspar

Deep Profiler - Morphological profiling using deep learning by Multiple Authors

Distributed CellProfiler - Run encapsulated docker containers with CellProfiler in the Amazon Web Services infrastructure by Multiple Authors

Image-based Profiling Recipe by Multiple Authors

Pycytominer - Data processing functions for profiling perturbations by Multiple Authors

A dataset of images and morphological profiles of 30 000 small-molecule treatments using the Cell Painting assay by Bray M-A, Gustafsdottir SM, Rohban MH, Singh S, Ljosa V, Sokolnicki KL, Bittker JA, Bodycombe NE, Dancik V, Hasaka TP, Hon CS, Kemp MM, Li K, Walpita D, Wawer MJ, Golub TR, Schreiber SL, Clemons PA, Shamji AF, & Carpenter AE

Cell Painting predicts impact of lung cancer variants by Caicedo JC, Arevalo J, Piccioni F, Bray MA, Hartland CL, Wu X, Brooks AN, Berger AH, Boehm JS, Carpenter AE, & Singh S

Cell Painting, a high-content image-based assay for morphological profiling using multiplexed fluorescent dyes by Bray M-A, Singh S, Han H, Davis CT, Borgeson B, Hartland C, Kost-Alimova M, Gustafsdottir SM, Gibson CC, & Carpenter AE

Morphological Profiles of RNAi-Induced Gene Knockdown Are Highly Reproducible but Dominated by Seed Effects by Singh S, Wu X, Ljosa V, Bray M-A, Piccioni F, Root DE, Doench JG, Boehm JS, & Carpenter AE

Multiplex Cytological Profiling Assay to Measure Diverse Cellular States by Gustafsdottir SM, Ljosa V, Sokolnicki KL, Wilson JA, Walpita D, Kemp MM, Seiler KP, Carrel HA, Golub TR, Schreiber SL, Clemons PA, Carpenter AE, and Shamji AF

Systematic morphological profiling of human gene and allele function via Cell Painting by Rohban MH, Singh S, Wu X, Berthet JB, Bray M-A, Shrestha Y, Varelas X, Boehm JS, & Carpenter AE

Toward performance-diverse small-molecule libraries for cell-based phenotypic screening using multiplexed high-dimensional profiling by Wawer MJ, Li K, Gustafsdottir SM, Ljosa V, BodycombeNE, Marton MA, Sokolnicki KL, Bray M-A, Kemp MM, Winchester E, Taylor B, Grant GB, Hon CSK, Duvall JR, Wilson JA, Bittker JA, Dancik V, Narayan R, Subramanian A, Winckler W, Golub TR, Carpenter AE, Shamji AF, Schreiber SL, & Clemons PA

Description Cell Painting data, comprising fluorescence microscopy cell images (TIFF), extracted features (CSV), and associated metadata (CSV and TXT). Resource type S3 Bucket Amazon Resource Name (ARN) arn:aws:s3:::cellpainting-gallery AWS Region us-east-1 AWS CLI Access (No AWS account required) aws s3 ls --no-sign-request s3://cellpainting-gallery/ Explore Documentation Browse Bucket

Description Notifications for new Cell Painting Gallery data Resource type SNS Topic Amazon Resource Name (ARN) arn:aws:sns:us-east-1:309624411020:cellpainting-repository-object_created AWS Region us-east-1
