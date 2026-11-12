# Lobachevsky University Electrocardiography Database (LUDB)

**Source:** https://physionet.org/content/ludb/1.0.1

---

Lobachevsky University Electrocardiography Database

Alena Kalyakulina , Igor Yusipov , Viktor Moskalenko , Alexander Nikolskiy , Konstantin Kosonogov , Nikolai Zolotykh , Mikhail Ivanchenko

Kalyakulina, A., Yusipov, I., Moskalenko, V., Nikolskiy, A., Kosonogov, K., Zolotykh, N., & Ivanchenko, M. (2021). Lobachevsky University Electrocardiography Database (version 1.0.1). PhysioNet . RRID:SCR_007345. https://doi.org/10.13026/eegm-h675

Kalyakulina,  A.I.,  Yusipov,  I.I.,  Moskalenko,  V.A.,  Nikolskiy,  A.V.,  Kosonogov,  K.A.,  Osipov, G.V.,  Zolotykh,  N.Yu.,  Ivanchenko,  M.V.:  LUDB: A New Open-Access Validation Tool for Electrocardiogram Delineation Algorithms, IEEE Access, vol. 8, pp. 186181-186190, 2020, doi: 10.1109/ACCESS.2020.3029211

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

Lobachevsky University Electrocardiography Database (LUDB) is an ECG signal database with marked boundaries and peaks of P, T waves and QRS complexes. The database consists of 200 10-second 12-lead ECG signal records representing different morphologies of the ECG signal. The ECGs were collected from healthy volunteers and patients of the Nizhny Novgorod City Hospital No 5 in 2017–2018. The patients had various cardiovascular diseases while some of them had pacemakers. The boundaries of P, T waves and QRS complexes were manually annotated by cardiologists for all 200 records. Also, each record is annotated with the corresponding diagnosis. The database can be used for educational purposes as well as for training and testing algorithms for ECG delineation, i.e. for automatic detection of boundaries and peaks of P, T waves and QRS complexes.

Validating ECG delineation algorithms requires standardized databases with complexes and waves, manually annotated by specialists. Several collections are currently available: MIT-BIH Arrhythmia Database [1], European ST-T Database [2], and QT Database [3], however their annotation is not exhaustive. For example, MIT-BIH Arrhythmia Database and European ST-T Database has a markup only for QRS complexes. The QT Database contains annotations for P, QRS and T waves, but several complexes are unmarked. By assembling a new ECG database at Lobachevsky University (LUDB), we sought to eliminate these shortcomings.

ECG 10 seconds records were obtained by the Schiller Cardiovit AT-101 cardiograph, with conventional 12 leads (i, ii, iii, avr, avl, avf, v1, v2, v3, v4, v5, v6). Signals are digitized at 500 samples per second. The boundaries and peaks of P, T waves and QRS complexes were determined by certified cardiologists by an eye inspection of each ECG signal and independently for each of 12 leads. The records were made by specialized medical staff (functional diagnostics nurses). All volunteers provided informed written consent before collecting the data. The research was approved by Lobachevsky University IRB (#23; 19 October 2017) .

The database consists of 200 10-second 12-lead ECG signal records collected from 2017 to 2018: in total, 16797 P waves, 21966 QRS complexes, 19666 T waves (in total, 58429 annotated waves). The age of all volunteers ranged from a minimum of 11 years old to a maximum of >89 years old with an average 52 years old while the distribution by gender was 85 women and 115 men.

The number of records with specified heart rate types in the dataset:

The number of records with specified types of the position of the electrical axis of the heart:

The number of records with specified types of conduction abnormalities:

The numbers of records with specified types of extrasystolies:

The number of records with specified types of hypertrophies:

The number of records with cardiac pacing:

The number of records with non-specific repolarization abnormalities:

The data is stored in wfdb-compatible format, which is supported by WFDB Python Toolbox or WFDB Software Package . The database was successfully used in testing and training algorithms for ECG delineation [4-10]. One of the most accurate ECG delineation algorithms [7] uses LUDB as the training set while the algorithm is based on a deep learning approach. F1-measures for detecting the beginnings and the ends of P and T waves and for QRS-complexes are at least 97.8%, 99.5%, and 99.9%, respectively.

1.0.1 Corrected information about scaling of the waveforms. Added information about rhythms to header files. Added ludb.csv file with aggregated information about the patients (gender, age, rhythm type, direction of the electrical axis of the heart, the presence of a cardiac pacemaker, etc.).

The study was supported by the Ministry of Education of the Russian Federation (contract No. 02.G25.31.0157 of 01.12.2015).

The authors declare that there are no known conflicts of interest.

Kalyakulina, A. I., Yusipov, I. I., Moskalenko, V. A., Nikolskiy, A. V., Kozlov, A. A., Zolotykh, N. Y., & Ivanchenko, M. V. (2019). Finding morphology points of electrocardiographic-signal waves using wavelet analysis. Radiophysics and Quantum Electronics, 61(8-9), 689-703.

Moody, G. B., & Mark, R. G. (2001). The impact of the MIT-BIH arrhythmia database. IEEE Engineering in Medicine and Biology Magazine, 20(3), 45-50.

Taddei, A., Distante, G., Emdin, M., Pisani, P., Moody, G. B., Zeelenberg, C., & Marchesi, C. (1992). The European ST-T database: standard for evaluating systems for the analysis of ST-T changes in ambulatory electrocardiography. European heart journal, 13(9), 1164-1172.

Laguna, P., Mark, R. G., Goldberg, A., & Moody, G. B. (1997, September). A database for evaluation of algorithms for measurement of QT and other waveform intervals in the ECG. In Computers in cardiology 1997 (pp. 673-676). IEEE.

Sereda, I., Alekseev, S., Koneva, A., Kataev, R., & Osipov, G. (2019, July). ECG segmentation by neural networks: errors and correction. In 2019 International Joint Conference on Neural Networks (IJCNN) (pp. 1-7). IEEE.

Bogdanov, M., Baigildin, S., Fabarisova, A., Ushenin, K., & Solovyova, O. (2019). Effects of lead position, cardiac rhythm variation and drug-induced QT prolongation on performance of machine learning methods for ECG processing. arXiv preprint arXiv:1912.04672.

Moskalenko, V., Zolotykh, N., & Osipov, G. (2019, October). Deep Learning for ECG Segmentation. In International Conference on Neuroinformatics (pp. 246-254). Springer, Cham.

Kuznetsov, V. V., Moskalenko, V. A., & Zolotykh, N. Y. (2020). Electrocardiogram Generation and Feature Extraction Using a Variational Autoencoder. arXiv preprint arXiv:2002.00254.

Ruiz, A., Arias, M. A., Pachón, M. I., Langley, P., Rieta, J. J., & Alcaraz, R. (2019, November). Thorough Assessment of a P-wave Delineation Algorithm Through the Use of Diverse Electrocardiographic Databases. In 2019 E-Health and Bioengineering Conference (EHB) (pp. 1-4). IEEE.

Chen, G., Chen, M., Zhang, J., Zhang, L., & Pang, C. (2020). A Crucial Wave Detection and Delineation Method for Twelve-Lead ECG Signals. IEEE Access, 8, 10707-10717.

34 publications cite this project.
    The most recent are listed below.

Holtercare-Bench: A Multimodal Benchmark for Evaluating Long-Term Dynamic ECG Analysis Yihan Xie, Hanwen Cui, Runze Ye et al. ACM International Conference on Multimedia (ACM MM) ,
        2026.

Does QRS-T loop coupling add to the QRS-T angle? Frechet distance and reduced ejection fraction in hospital ECGs, with named measurement-error scenarios Leo Probst. Research Square ,
        2026.

Repeat variation and definition dependence of ECG/VCG markers: an exploratory audit of one implementation (LoopLens 10.1) Leo Probst. Research Square ,
        2026.

Physiology-augmented deep representations improve cross-database electrocardiogram beat classification under unseen-domain shift Mujahid Shahid¹, Oliver Konyo. Research Square ,
        2026.

Inherently Interpretable Machine Learning Models for Time-Series: A Systematic Literature Review Ruqayyah Nabage, Zahra Asghari Varzaneh, Reza Malekian et al. Research Square ,
        2026.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

Download
              the ZIP file (13.8 MB)

Download with the PhysioNet Python package : physionet download ludb --version 1.0.1

Download the files using your terminal: wget -r -N -c -np https://physionet.org/files/ludb/1.0.1/

Download the files using AWS command line tools: aws s3 sync --no-sign-request s3://physionet-open/ludb/1.0.1/ DESTINATION
