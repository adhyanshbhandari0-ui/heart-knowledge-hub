# MIT-BIH Atrial Fibrillation Database

**Source:** https://physionet.org/physiobank/database/afdb

---

MIT-BIH Atrial Fibrillation Database expanded (Nov. 4, 2000, midnight) Previously unreleased signal files for the MIT-BIH Atrial Fibrillation Database have been added to PhysioNet.

Previously unreleased signal files for the MIT-BIH Atrial Fibrillation Database have been added to PhysioNet.

Moody GB, Mark RG. A new method for detecting atrial fibrillation using R-R intervals. Computers in Cardiology. 10:227-230 (1983). http://ecg.mit.edu/george/publications/afib-cinc-1983.pdf

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

This database includes 25 long-term ECG recordings of human subjects with atrial fibrillation (mostly paroxysmal).

Of these, 23 records include the two ECG signals (in the .dat files); records 00735 and 03665 are represented only by the rhythm (.atr) and unaudited beat (.qrs annotation files.

The individual recordings are each 10 hours in duration, and contain two ECG signals each sampled at 250 samples per second with 12-bit resolution over a range of ±10 millivolts. The original analog recordings were made at Boston's Beth Israel Hospital (now the Beth Israel Deaconess Medical Center) using ambulatory ECG recorders with a typical recording bandwidth of approximately 0.1 Hz to 40 Hz. The rhythm annotation files (with the suffix .atr) were prepared manually; these contain rhythm annotations of types (AFIB (atrial fibrillation), (AFL (atrial flutter), (J (AV junctional rhythm), and (N (used to indicate all other rhythms). (The original rhythm annotation files, still available in the old directory, used AF, AFL, J, and N to mark these rhythms; the atr annotations in this directory have been revised for consistency with those used for the MIT-BIH Arrhythmia Database .) Beat annotation files (with the suffix .qrs) were prepared using an automated detector and have not been corrected manually. For some records, manually corrected beat annotation files (with the suffix .qrsc) are available. (The .qrs annotations may be useful for studies of methods for automated AF detection, where such methods must be robust with respect to typical QRS detection errors. The .qrsc annotations may be preferred for basic studies of AF itself, where QRS detection errors would be confounding.) Note that in both .qrs and .qrsc files, no distinction is made among beat types (all beats are labelled as if normal).

Until November 2000, only one of the signal files (for record 04936) was available. The original 9-track tapes from 1983 for these records have now been read to produce the other signal files in this directory. In a few cases (04043, 08405, and 08434) isolated data blocks from the original tapes were unreadable. In these cases, the missing data, corresponding to 10.24 seconds for each missing block, have been replaced with a flat segment of samples with amplitudes of zero. See notes.txt for details.

In March 2014, Henian Xia reported that the .qrs annotations were not aligned with the ECG waveforms in record 07859, and investigation showed that 2569 samples appeared to be missing from the beginning of the record. The original annotation file has been renamed 07859.qrs-, and a realigned version of it (without its initial 14 annotations) is available as 07859.qrs. A correctly aligned, manually reviewed annotation file was also produced at that time, and is now available here as 07859.qrsc.

18 publications cite this project.
    The most recent are listed below.

Recent advances in deep learning based arrhythmia classification using ECG and PPG signals: a systematic review Nitya N. Kulkarni, Nagaraja G. S., S. Nagaraja G. et al. Discover Computing ,
        2026.

Classification of intracardiac heart sounds for ventricular and atrial fibrillation based on feature fusion and voting ensemble learning Yiming Xin, Rongfeng Zhang, Yiheng Yang et al. Medical & Biological Engineering & Computing ,
        2026.

A computational decision framework based on wavelet-entropy feature modeling for nonlinear time-series analysis Shashi Kant Tiwari, Shweta Sinha, Karamjit Kaur et al. Engineering Research Express ,
        2026.

An Experimental Study of Atrial Fibrillation Detection Using Deep Neural Networks Under Noisy Conditions Dalia Vektarytė, Zigmantas Kęstutis Juškevičius, Jolita Bernatavičienė. Vilnius University Open Series ,
        2026.

Explainable electrocardiogram-based atrial fibrillation detection using deep learning Jyoti Maggu, Simranjit Kaur, Aabharan Gupta et al. The Computer Journal ,
        2026.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

Download
              the ZIP file (439.7 MB)

Download with the PhysioNet Python package : physionet download afdb --version 1.0.0

Download the files using your terminal: wget -r -N -c -np https://physionet.org/files/afdb/1.0.0/

Download the files using AWS command line tools: aws s3 sync --no-sign-request s3://physionet-open/afdb/1.0.0/ DESTINATION
