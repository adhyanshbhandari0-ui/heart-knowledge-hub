# Abdominal and Direct Fetal ECG Database

**Source:** https://physionet.org/content/adfecgdb

---

Abdominal and Direct Fetal ECG Database (Aug. 9, 2012, 6:30 p.m.) PhysioBank has received a contribution of five-minute multichannel fetal ECG recordings, with cardiologist-verified annotations of all fetal heart beats, from five women in labor, from the Medical University of Silesia, Poland. Each record includes four signals from the maternal abdomen and a simultaneously recorded reference direct fetal ECG from the fetal scalp; all signals are sampled at 1 KHz with 16-bit resolution.

PhysioBank has received a contribution of five-minute multichannel fetal ECG recordings, with cardiologist-verified annotations of all fetal heart beats, from five women in labor, from the Medical University of Silesia, Poland. Each record includes four signals from the maternal abdomen and a simultaneously recorded reference direct fetal ECG from the fetal scalp; all signals are sampled at 1 KHz with 16-bit resolution.

Jezewski J, Matonia A, Kupka T, Roj D, Czabanski R. >Determination of the fetal heart rate from abdominal signals: evaluation of beat-to-beat accuracy in relation to the direct fetal electrocardiogram. Biomedical Engineering/Biomedizinische Technik 2012 Jul;57(5):383-394. doi:10.1515/bmt-2011-0130. http://www.degruyter.com/view/j/bmte.ahead-of-print/bmt-2011-0130/bmt-2011-0130.xml

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

The research material included in the Abdominal and Direct Fetal Electrocardiogram Database contains multichannel fetal electrocardiogram (FECG) recordings obtained from 5 different women in labor, between 38 and 41 weeks of gestation. The recordings were acquired in the Department of Obstetrics at the Medical University of Silesia, by means of the KOMPOREL system for acquisition and analysis of fetal electrocardiogram (ITAM Institute, Zabrze, Poland). Each recording comprises four differential signals acquired from maternal abdomen and the reference direct fetal electrocardiogram registered from the fetal head.

The configuration of the abdominal electrodes comprised four electrodes placed around the navel, a reference electrode placed above the pubic symphysis and a common mode reference electrode (with active-ground signal) placed on the left leg. To reduce the skin impedance, the areas under the Ag-AgCl electrodes were abraded. In all cases, the scalp electrode was placed for a clinical indication and all women consented to participate in this study.

The acquisition of direct fetal electrocardiogram was carried out with a typical spiral electrode, commonly used in a direct FECG channel of popular fetal monitors. The R-wave locations were automatically determined in the direct FECG signal by means of on-line analysis applied in the KOMPOREL system. These locations were then verified (off-line) by a group of cardiologists, resulting in a set of reference markers precisely indicating the R-wave locations. The markers have been stored together with the direct and indirect FECG signals in EDF/EDF+ format.

The provided recordings constitute an excellent material for testing and evaluation of efficacy of new FECG processing techniques, e.g. algorithms for suppression of maternal electrocardiogram in abdominal signals or for detection of fetal QRS complexes. In the authors' studies (1-4 above), these recordings were used to evaluate the accuracy of fetal heart rate measurement and to estimate its influence on the quantification of the beat-to-beat fetal heart rate (FHR) variability.

Signals recorded in labor, between 38 and 41 weeks of gestation

Four signals acquired from maternal abdomen

Direct electrocardiogram recorded simultaneously from fetal head

Positioning of electrodes was constant during all recordings

Ag-AgCl electrodes (3M Red Dot 2271) and abrasive material to improve skin conductance (3M Red Dot Trace Prep 2236)

Bandwidth: 1Hz - 150Hz (synchronous sampling of all signals)

Additional digital filtering for removal of power-line interference (50Hz) and baseline drift

Input ranges are included in the records in EDF format

Jezewski J, Matonia A, Kupka T, Roj D, Czabanski R. >Determination of the fetal heart rate from abdominal signals: evaluation of beat-to-beat accuracy in relation to the direct fetal electrocardiogram . Biomedical Engineering/Biomedizinische Technik 2012 Jul;57(5):383-394. doi:10.1515/bmt-2011-0130.

Matonia A, Jezewski J, Kupka T, Horoba K, Wrobel J, Gacek A. The influence of coincidence of fetal and maternal QRS complexes on fetal heart rate reliability . Medical & Biological Engineering & Computing 2006;44(5):393-403.

Kotas M, Jezewski J, Horoba L, Matonia A. Application of spatio-temporal filtering to fetal electrocardiogram enhancement . Computer Methods and Programs in Biomedicine . 2011 Oct;104(1):1-9.

Kotas M, Jezewski J, Matonia A, Kupka T. Towards noise immune detection of fetal QRS complexes . Computer Methods and Programs in Biomedicine . 2010 Mar;97(3):241-256.

6 publications cite this project.
    The most recent are listed below.

Untitled Microsystems Electronics and Acoustics ,
        2026.

A Complex Method for Non-invasive Fetal Electrocardiogram Signal Extraction and Cardiac Arrhythmia Classification Dmytro A. Shevchuk, Н. Г. Иванушкина. Microsystems Electronics and Acoustics ,
        2026.

PCA-Based Preprocessing for Clustering-Based Fetal Heart Rate Extraction in Non-Invasive Fetal Electrocardiograms Luis Oyarzún, Encarnación Castillo, Luis Parrilla et al. Electronics ,
        2024.

Improved multivariate multiscale sample entropy and its application in multi-channel data Weijia Li, Xiaohong Shen, Yaan Li et al. Chaos An Interdisciplinary Journal of Nonlinear Science ,
        2023.

Window Polarization in PCA-based Analysis of Non-Invasive Fetal ECG recordings Luis Oyarzún, Encarnación Castillo, Luis Parrilla et al. Conference on Design of Circuits and Integrated Systems ,
        2021.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

Download
              the ZIP file (14.6 MB)

Download with the PhysioNet Python package : physionet download adfecgdb --version 1.0.0

Download the files using your terminal: wget -r -N -c -np https://physionet.org/files/adfecgdb/1.0.0/

Download the files using AWS command line tools: aws s3 sync --no-sign-request s3://physionet-open/adfecgdb/1.0.0/ DESTINATION
