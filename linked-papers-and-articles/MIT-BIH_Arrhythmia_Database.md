# MIT-BIH Arrhythmia Database

**Source:** https://www.physionet.org/content/mitdb/1.0.0

---

MIT-BIH Arrhythmia Database expanded (Feb. 24, 2005, midnight) The entire MIT-BIH Arrhythmia Database is now freely available on PhysioNet. Somewhat more than half of the database has been available here since PhysioNet's inception; the remainder has now been posted.

The entire MIT-BIH Arrhythmia Database is now freely available on PhysioNet. Somewhat more than half of the database has been available here since PhysioNet's inception; the remainder has now been posted.

Moody, G., & Mark, R. (2005). MIT-BIH Arrhythmia Database (version 1.0.0). PhysioNet . RRID:SCR_007345. https://doi.org/10.13026/C2F305

Moody GB, Mark RG. The impact of the MIT-BIH Arrhythmia Database. IEEE Eng in Med and Biol 20(3):45-50 (May-June 2001). (PMID: 11446209) http://ecg.mit.edu/george/publications/mitdb-embs-2001.pdf

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

The MIT-BIH Arrhythmia Database contains 48 approximately half-hour, two-channel ambulatory electrocardiogram (ECG) recordings from 47 subjects. The recordings were collected at Boston's Beth Israel Hospital between 1975 and 1979 and include both randomly selected excerpts and recordings selected to represent less common, clinically significant arrhythmias. Signals were digitized at 360 samples per second per channel with 11-bit resolution over a 10 mV range. Each recording includes expert-reviewed reference annotations, comprising approximately 110,000 beat annotations across the database. First distributed in 1980, the database provides a shared resource for developing and evaluating arrhythmia detection algorithms and investigating cardiac dynamics.

Research groups at the Massachusetts Institute of Technology (MIT) and Boston's Beth Israel Hospital, now Beth Israel Deaconess Medical Center, began collaborating on arrhythmia analysis in 1975. This work led to the MIT-BIH Arrhythmia Database, which was completed and first distributed in 1980 [1].

The database was the first generally available collection of standard test recordings for evaluating arrhythmia detectors. By providing shared ECG recordings and reference annotations, it enabled reproducible comparisons of algorithm performance and supported research into cardiac dynamics [1].

The database was initially distributed on digital and analog tape, followed by a CD-ROM edition in August 1989. Twenty-five complete recordings and reference annotations for all 48 records became freely available through PhysioNet in September 1999. The remaining 23 waveform recordings were added in February 2005, making the entire database freely accessible.

Recordings were drawn from approximately 4,000 24-hour ambulatory ECG recordings collected by the Beth Israel Hospital Arrhythmia Laboratory between 1975 and 1979. Approximately 60% of the source recordings were from inpatients and 40% from outpatients. Twenty-three excerpts were selected randomly; another 25 were chosen to include uncommon but clinically important arrhythmias [1, 2].

The original two-channel analog recordings were digitized at 360 samples per second per channel with 11-bit resolution over a 10 mV range [1, 2].

Initial beat labels were generated automatically. Two cardiologists independently reviewed each recording, correcting beat detections and classifications and adding rhythm labels, signal-quality annotations, and comments. Disagreements were reviewed and resolved by consensus to produce the reference annotations [2].

The database contains 48 approximately half-hour recordings from 47 subjects. Each record includes two ECG signals and accompanying reference annotations. Across the database, there are approximately 110,000 beat annotations [1].

The subjects comprise 25 men aged 32–89 years and 22 women aged 23–89 years. Records 201 and 202 originate from the same subject [2].

For each record, the principal files are:

Signal file (.dat): The digitized two-channel ECG recording.

Header file (.hea): Metadata describing the recording and signals.

Annotation file (.atr): Reference annotations for beats, rhythms, signal quality, and comments.

Detailed record descriptions, ECG plots, annotation definitions, and available subject information are provided in the MIT-BIH Arrhythmia Database Directory [2].

The database supports the development and evaluation of ECG analysis algorithms, including beat detection, beat classification, and arrhythmia detection [1]. Users should report the records included in their analysis, any exclusions, and the annotation classes and evaluation procedures used.

Because 25 recordings were deliberately selected to include uncommon arrhythmias [2], pooled results should not be interpreted as estimates of arrhythmia prevalence in a general clinical population. For subject-independent evaluation, records 201 and 202 should be assigned to the same partition because they originate from the same subject [2].

Lead configurations vary between records. Analog tape artifacts may affect heart-rate variability analysis, and interchannel timing skew may affect analyses that combine both signals. Users should consult the database directory for recording-specific details [2].

the MIT-BIH Noise Stress Test Database, which comprises ECG recordings generated by adding calibrated noise to recordings from the MIT-BIH Arrhythmia Database [3]

the MIT-BIH P-wave Annotations [4], which provides reference P-wave annotations for twelve recordings from this database.

Annotation correction: In the 2018 update to 102.atr , annotation 1991 (zero-based indexing) was moved from sample 590296 to sample 590262. The previous file is retained as 102-0.atr .

The database was developed through contributions from cardiologists, Holter technicians, laboratory assistants, and engineers at MIT and Beth Israel Hospital. Particular contributions were made by Paul Schluter to the original database design and implementation; Scott Peterson to data selection, digitization, annotation, editing, and software development; George Moody to database formatting and documentation; Larry Siegal to waveform editing tools; Cheryl Jackson to annotation transcription and quality control; and Diane Perry to recording selection and annotation [2].

The physicians who contributed to beat-by-beat annotation were Esmerey Acarturk, John Aumiller, Sidney Blake, Alvin Blaustein, Chester Conrad, Gary Heller, Michael Malagold, Roger Mark, and Candice Miklozek. Colleagues at Washington University in St. Louis, particularly Russell Hermes, helped establish a compatible data format. Joe Mietus and Ted Baker contributed to subsequent analysis, distribution, and software portability [2].

Moody GB, Mark RG. The impact of the MIT-BIH Arrhythmia Database. IEEE Engineering in Medicine and Biology Magazine. 2001;20(3):45–50. https://doi.org/10.1109/51.932724

Moody GB, Mark RG. MIT-BIH Arrhythmia Database Directory. PhysioNet. Available from: https://archive.physionet.org/physiobank/database/html/mitdbdir/mitdbdir.htm

Moody GB, Muldrow WE, Mark RG. A noise stress test for arrhythmia detectors. Computers in Cardiology 1984; 11:381-384.

Maršánová L, Němcová A, Smíšek R, Goldmann T, Vítek M, Smital L. Automatic Detection of P Wave in ECG During Ventricular Extrasystoles.. World Congress on Medical Physics and Biomedical Engineering 2018: Springer, Singapore; 2018. p. 381-5. DOI: 10.1007/978-981-10-9038-7_72.

122 publications cite this project.
    The most recent are listed below.

BLiSS: A Beat-Local, Signal-Quality-Informed Kalman Smoother for ECG Denoising under Non-Stationary Muscle Artifact, with Ectopic-Beat Reconstruction Assessment Khanh Duy Tran. Research Square ,
        2026.

A lightweight hybrid LSTM–GNN framework with context-aware risk calibration for physiological monitoring Mohamed Mostafa AbdulAli. Discover Artificial Intelligence ,
        2026.

Physiology-augmented deep representations improve cross-database electrocardiogram beat classification under unseen-domain shift Mujahid Shahid¹, Oliver Konyo. Research Square ,
        2026.

Deep Learning-driven ECG Signal Interpretation for Predictive Cardiac Health Monitoring in Personalized Medical Care Systems Mahmood Hameed Majeed, Mohammed H. Dosh, Safa L. Kailan et al. International journal of intelligent engineering and systems ,
        2026.

Federated learning with adaptive reliability aware aggregation for privacy preserving healthcare IoT systems Vishal Barot, Jashvant Dave, Manoj R. et al. Scientific Reports ,
        2026.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

Download
              the ZIP file (73.5 MB)

Download with the PhysioNet Python package : physionet download mitdb --version 1.0.0

Download the files using your terminal: wget -r -N -c -np https://physionet.org/files/mitdb/1.0.0/

Download the files using AWS command line tools: aws s3 sync --no-sign-request s3://physionet-open/mitdb/1.0.0/ DESTINATION
