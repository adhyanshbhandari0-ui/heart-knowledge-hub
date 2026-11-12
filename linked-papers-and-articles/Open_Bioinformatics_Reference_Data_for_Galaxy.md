# Open Bioinformatics Reference Data for Galaxy

**Source:** https://registry.opendata.aws/open-bio-ref-data

---

Open Bioinformatics Reference Data for Galaxy

bioinformatics biology genetic genomic life sciences reference index

This dataset provides genomic reference data and software packages for use with Galaxy and Bioconductor applications. The reference data is available for hundreds of reference genomes and has been formatted for use with a variety of tools. The available configuration files make this data easily incorporable with a local Galaxy server without additional data preparation. Additionally, Bioconductor's AnnotationHub and ExperimentHub data are provided for use via R packages through which the data can be downloaded and installed into any R environment.

https://github.com/openbiorefdata/documentation/

See all datasets managed by Galaxy and Bioconductor Projects .

outreach@galaxyproject.org or https://support.bioconductor.org/

Open Bioinformatics Reference Data for Galaxy was accessed on DATE from https://registry.opendata.aws/open-bio-ref-data.

Using Open Bio Ref Data with Galaxy and Bioconductor by Enis Afgan, Alexandru Mahmoud, Nuwan Goonasekera

Accessible, curated metagenomic data through ExperimentHub by Edoardo Pasolli, Lucas Schiffer, Paolo Manghi, Audrey Renson, Valerie Obenchain, Duy Tin Truong, Francesco Beghini, Faizan Malik, Marcel Ramos, Jennifer B Dowd, Curtis Huttenhower, Martin Morgan, Nicola Segata, and Levi Waldron

TCGA Workflow: Analyze cancer genomics and epigenomics data using Bioconductor packages by Tiago C. Silva, Antonio Colaprico, Catharina Olsen, Fulvio D'Angelo, Gianluca Bontempi, Michele Ceccarelli, Houtan Noushmehr

Wrangling Galaxy's reference data by Daniel Blankenberg, James E. Johnson, The Galaxy Team, James Taylor, Anton Nekrutenko

Description The data is organized as versioned objects for reference data, and data packages for use with the R programming language. The reference data is primarily intended for use with the Galaxy application, and has been formatted for easy configuration. In the future, additional formats may be provided. The packages as well as the AnnotationHub and ExperimentHub data are intended for use with R / Bioconductor. Resource type S3 Bucket Amazon Resource Name (ARN) arn:aws:s3:::biorefdata AWS Region ap-southeast-2 AWS CLI Access (No AWS account required) aws s3 ls --no-sign-request s3://biorefdata/
