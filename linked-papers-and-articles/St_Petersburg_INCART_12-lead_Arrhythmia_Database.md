# St Petersburg INCART 12-lead Arrhythmia Database

**Source:** https://physionet.org/content/incartdb/1.0.0

---

St Petersburg INCART 12-lead Arrhythmia Database

St. Petersburg Institute of Cardiological Technics 12-lead Arrhythmia Database (May 1, 2008, midnight) The St. Petersburg Institute of Cardiological Technics 12-lead Arrhythmia Database has been contributed to PhysioNet by its creators. It consists of 75 half-hour recordings extracted from 32 Holter records from patients undergoing tests for coronary artery disease, with reference annotation files containing over 175,000 beat annotations in all.

The St. Petersburg Institute of Cardiological Technics 12-lead Arrhythmia Database has been contributed to PhysioNet by its creators. It consists of 75 half-hour recordings extracted from 32 Holter records from patients undergoing tests for coronary artery disease, with reference annotation files containing over 175,000 beat annotations in all.

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

This database consists of 75 annotated recordings extracted from 32 Holter records. Each record is 30 minutes long and contains 12 standard leads, each sampled at 257 Hz, with gains varying from 250 to 1100 analog-to-digital converter units per millivolt. Gains for each record are specified in its .hea file. The reference annotation files contain over 175,000 beat annotations in all.

The original records were collected from patients undergoing tests for coronary artery disease (17 men and 15 women, aged 18-80; mean age: 58). None of the patients had pacemakers; most had ventricular ectopic beats. In selecting records to be included in the database, preference was given to subjects with ECGs consistent with ischemia, coronary artery disease, conduction abnormalities, and arrhythmias; observations of those selected included:

These diagnoses were confirmed by enzyme assays, coronary angiography, electrophysiological study, and pressure monitoring where necessary. For each record, the .hea file includes the patient's age, sex, diagnoses, and a summary of features of the ECG. Each .hea file also includes a patient number (1–32) that identifies the source recording; all records with a given patient number were obtained from the same Holter recording. For convenience, this information is also collected in the files record-descriptions.txt and files-patients-diagnoses.txt .

The annotations were produced by an automatic algorithm and then corrected manually, following the standard PhysioBank beat annotation definitions . The algorithm generally places beat annotations in the middle of the QRS complex (as determined from all 12 leads); the locations have not been manually corrected, however, and there may be occasional misaligned annotations as a result.

This database was contributed by the St. Petersburg Institute of Cardiological Technics (Incart), St. Petersburg, Russia. The database was initially developed by Viktor Tihonenko ( vmt@incart.ru ) and Alexander Khaustov ( avk@incart.ru ). Additional verification was done by Sergey Ivanov and Alexei Rivin (Incart). Please refer questions and corrections to Evgeniy Yakushenko yes@incart.ru .

The header files have been updated to include the correct checksums and initial values for all signals. The signals and annotations have not been altered.

68 publications cite this project.
    The most recent are listed below.

Holtercare-Bench: A Multimodal Benchmark for Evaluating Long-Term Dynamic ECG Analysis Yihan Xie, Hanwen Cui, Runze Ye et al. ACM International Conference on Multimedia (ACM MM) ,
        2026.

A lightweight hybrid LSTM–GNN framework with context-aware risk calibration for physiological monitoring Mohamed Mostafa AbdulAli. Discover Artificial Intelligence ,
        2026.

Physiology-augmented deep representations improve cross-database electrocardiogram beat classification under unseen-domain shift Mujahid Shahid¹, Oliver Konyo. Research Square ,
        2026.

Transport What Shares the Conduction Pathway: Normal-Anchored SPD Geometric Transport for Source-Free Patient Adaptation of Holter and Patch ECG Jinkook Kim. arXiv (Cornell University) ,
        2026.

Patient and database shift in lightweight ECG arrhythmia classification: a controlled evaluation of noise, quantization, and embedded inference Hyun Mok Park, Woojin Cho, Seok-Oh Bang et al. Medical Engineering & Physics ,
        2026.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

Download
              the ZIP file (563.5 MB)

Download with the PhysioNet Python package : physionet download incartdb --version 1.0.0

Download the files using your terminal: wget -r -N -c -np https://physionet.org/files/incartdb/1.0.0/

Download the files using AWS command line tools: aws s3 sync --no-sign-request s3://physionet-open/incartdb/1.0.0/ DESTINATION
