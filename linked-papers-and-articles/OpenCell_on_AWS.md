# OpenCell on AWS

**Source:** https://registry.opendata.aws/czb-opencell

---

Biohub biology cell biology cell imaging computer vision fluorescence imaging imaging life sciences machine learning microscopy

The OpenCell project is a proteome-scale effort to measure the localization and interactions of human proteins using high-throughput genome engineering to endogenously tag thousands of proteins in the human proteome. This dataset consists of the raw confocal fluorescence microscopy images for all tagged cell lines in the OpenCell library.These images can be interpreted both individually, to determine the localization of particular proteins of interest,  and in aggregate, by training machine learning models to classify or quantify subcellular localization patterns.

This is the final version of the dataset.

OpenCell on AWS was accessed on DATE from https://registry.opendata.aws/czb-opencell.

cytoself (an unsupervised ML model to quantify localization patterns) by Hirofumi Kobayashi, Keith C. Cheveralls, Manuel D. Leonetti, Loic A. Royer

OpenCell: proteome-scale endogenous tagging enables the cartography of human cellular organization by Nathan H. Cho, Keith C. Cheveralls, Andreas-David Brunner, Kibeom Kim, AndrÃ© C. Michaelis, Preethi Raghavan, et al.

Self-Supervised Deep-Learning Encodes High-Resolution Features of Protein Subcellular Localization by Hirofumi Kobayashi, Keith C. Cheveralls, Manuel D. Leonetti, Loic A. Royer

Description Live-cell confocal fluorescence microscopy images of the OpenCell library of fluorescently tagged cell lines Resource type S3 Bucket Amazon Resource Name (ARN) arn:aws:s3:::czb-opencell AWS Region us-west-2 AWS CLI Access (No AWS account required) aws s3 ls --no-sign-request s3://czb-opencell/
