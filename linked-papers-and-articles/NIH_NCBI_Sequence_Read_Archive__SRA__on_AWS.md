# NIH NCBI Sequence Read Archive (SRA) on AWS

**Source:** https://registry.opendata.aws/ncbi-sra

---

NIH NCBI Sequence Read Archive (SRA) on AWS

bam cram fastq genetic genomic life sciences STRIDES transcriptomics whole exome sequencing whole genome sequencing

The Sequence Read Archive (SRA), produced by the National Center for Biotechnology Information (NCBI) at the National Library of Medicine (NLM) at the National Institutes of Health (NIH) , stores raw DNA sequencing data and alignment information from high-throughput sequencing platforms. The SRA provides open access to these biological sequence data to support the research community's efforts to enhance reproducibility and make new discoveries by comparing data sets. Buckets in this registry contain public SRA data in the original (user submitted) format from select high value and newly-released studies as well as all public-access SRA formatted ETL+BQS data. Also included is all SRA metadata that can be leveraged for attribute-based data discovery.

NCBI Policy and NIH Genomic Data Sharing Policy

https://www.ncbi.nlm.nih.gov/sra/docs/sra-cloud/

See all datasets managed by National Library of Medicine (NLM) .

NIH NCBI Sequence Read Archive (SRA) on AWS was accessed on DATE from https://registry.opendata.aws/ncbi-sra.

Access SRA data using Amazon Web Services (AWS) by NCBI SRA

Get started with the SRA and Amazon Athena by NCBI SRA

The Sequence Read Archive by Leinonen et al (2011)

Description .bam, .cram, and .fastq files in a public S3 bucket. This is the first of two S3 buckets for source submissions from sequencing methodologies such as PacBio, Oxford Nanopore Technologies, and 10X Genomics. Resource type S3 Bucket Amazon Resource Name (ARN) arn:aws:s3:::sra-pub-src-1 AWS Region us-east-1 AWS CLI Access (No AWS account required) aws s3 ls --no-sign-request s3://sra-pub-src-1/

Description .bam, .cram, and .fastq files in a public S3 bucket. This is the second of two S3 buckets for source submissions from sequencing methodologies such as PacBio, Oxford Nanopore Technologies, and 10X Genomics. Resource type S3 Bucket Amazon Resource Name (ARN) arn:aws:s3:::sra-pub-src-2 AWS Region us-east-1 AWS CLI Access (No AWS account required) aws s3 ls --no-sign-request s3://sra-pub-src-2/

Description .sra files in a public S3 bucket. This bucket contains all open access SRA submissions in the SRA Normalized format with full base quality scores. The SRA Toolkit will be required to convert these objects into FASTQ or SAM files. Note that this bucket is updated on a daily basis, however, there may be a one to two day lag between accessions being findable via the SRA Search and being accessible in this S3 bucket. Resource type S3 Bucket Amazon Resource Name (ARN) arn:aws:s3:::sra-pub-run-odp AWS Region us-east-1 AWS CLI Access (No AWS account required) aws s3 ls --no-sign-request s3://sra-pub-run-odp/

Description .sra files in a controlled-access S3 bucket. This bucket contains controlled-access dbGaP submissions in the SRA Normalized format with full base quality scores. The SRA Toolkit will be required to convert these objects into FASTQ or SAM files. Note that this bucket is updated on a daily basis, however, there may be a one to two day lag between accessions being findable via the SRA Search and being accessible in this S3 bucket. Resource type S3 Bucket Controlled Access Amazon Resource Name (ARN) arn:aws:s3:::sra-ca-run-odp AWS Region us-east-1

Description Metadata files for the Sequence Read Archive, ready to load into AWS Glue and query with Amazon Athena . Resource type S3 Bucket Amazon Resource Name (ARN) arn:aws:s3:::sra-pub-metadata-us-east-1/sra/metadata AWS Region us-east-1 AWS CLI Access (No AWS account required) aws s3 ls --no-sign-request s3://sra-pub-metadata-us-east-1/sra/metadata/

Description Update notifications for s3://sra-pub-run-odp. Users can subscribe to this SNS topic with AWS Lambda or AWS Simple Queue Service . Resource type SNS Topic Amazon Resource Name (ARN) arn:aws:sns:us-east-1:867126678632:sra-pub-run-odp-objects AWS Region us-east-1
