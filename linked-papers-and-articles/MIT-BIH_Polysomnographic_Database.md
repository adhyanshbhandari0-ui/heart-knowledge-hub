# MIT-BIH Polysomnographic Database

**Source:** https://physionet.org/content/slpdb/1.0.0

---

Moody, G. (1999). MIT-BIH Polysomnographic Database (version 1.0.0). PhysioNet . RRID:SCR_007345. https://doi.org/10.13026/C23K5S

Ichimaru Y, Moody GB. Development of the polysomnographic database on CD-ROM. Psychiatry and Clinical Neurosciences 53:175-177 (April 1999). http://ecg.mit.edu/george/publications/slpdb-pcn-1999.pdf

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

The MIT-BIH Polysomnographic Database is a collection of recordings of multiple physiologic signals during sleep. Subjects were monitored in Boston's Beth Israel Hospital Sleep Laboratory for evaluation of chronic obstructive sleep apnea syndrome, and to test the effects of constant positive airway pressure (CPAP), a standard therapeutic intervention that usually prevents or substantially reduces airway obstruction in these subjects.

Polysomnography provides simultaneous measurements of sleep and cardiorespiratory physiology, supporting investigation of sleep-related events such as apnea, arrhythmias, hemodynamic changes, and myocardial ischemia. Historically, polysomnographic recordings were stored on paper or microfilm, making them difficult to reanalyze and share between research centers.

This database was developed to make polysomnographic recordings available in a digital format for research and education. Following the example of the MIT-BIH Arrhythmia Database [1], it was originally distributed on CD-ROM to facilitate access to physiological waveforms and accompanying annotations [2]. The recordings support studies of sleep apnea physiology and non-linear physiological dynamics, development and evaluation of automated signal-analysis methods, and teaching of sleep physiology and sleep staging.

Sixteen polysomnographic recordings were selected from a cohort of 60 male subjects with or without sleep apnea syndrome. The selected subjects had a mean age of 40 years (range: 32–56 years). Recording durations ranged from 2 to 7 hours.

Physiological measurements included electrocardiography (ECG), electroencephalography (EEG), electrooculography (EOG), chin electromyography (EMG), invasive blood pressure, oxygen saturation, nasal and chest respiration, and cardiac volume measured using the VEST system (Capintec). Signals were digitized at 250 Hz with a resolution of 12 bits per sample.

Recordings were reviewed and edited using WAVE (Waveform Analyzer, Viewer, and Editor), developed at the Massachusetts Institute of Technology. QRS complexes were detected automatically, and the resulting annotations were reviewed and corrected using WAVE. Sleep stages were assigned according to the criteria of Rechtschaffen and Kales.

The database contains physiological waveform recordings and accompanying metadata and annotations for 16 subjects. Each recording is associated with the following files:

Waveform files: Digitized physiological signals from polysomnographic monitoring.

Header files: Recording metadata, including duration, signal gains and offsets, data structure, and the date and start time of monitoring.

QRS annotation files: Reviewed annotations identifying QRS complexes in the ECG.

Sleep-stage files: Sleep-stage classifications assigned using the Rechtschaffen and Kales criteria.

Additional event information described in the original distribution includes the timing of sleep apnea episodes and periods of continuous positive airway pressure (CPAP).

The original CD-ROM distribution also included software written in C and Bourne shell for waveform visualization and physiological signal analysis. These tools supported beat-by-beat analysis of heart rate, blood pressure, and ventricular volume; frequency-domain analysis using discrete Fourier transforms and maximum entropy methods; and estimation of periodic components using least-squares cosine spectrum analysis.

These data have been used in several studies: (i) Rigney investigated the non-linear dynamics of respiration, heart rate, and blood pressure during sleep apnea; [3] (ii) Garpestad examined cardiovascular dynamics at the termination of obstructive apnea using the VEST method, which requires a specialized device to monitor cardiac volume; [4] and (iii) we investigated how sleep stage affects cardiorespiratory events during the night, [5] including counts of K-complexes and sleep spindles during sleep apnea, the frequency of apnea episodes, and automated sleep-stage classification.

This dataset may be useful for: (i) mathematicians investigating non-linear dynamics in physiological data; (ii) engineers developing software to analyze sleep-related data; (iii) clinicians studying the physiology of sleep apnea; and (iv) students learning about sleep physiology, including sleep staging through visual inspection of physiological recordings.

Moody GB, Mark RG. The impact of the MIT-BIH Arrhythmia Database. IEEE Eng in Med and Biol 20(3):45-50 (May-June 2001). (PMID: 11446209). https://doi.org/10.1109/51.932724

Ichimaru Y, Moody GB. Development of the polysomnographic database on CD-ROM. Psychiatry and Clinical Neurosciences 53:175-177 (April 1999).

Rigney DR, Goldberger AL, Ocasio WC et al. Multichannel physiological data description and analysis. In: Weigend AS, Gerschenfeld NA (eds), Time Series Prediction. Addison-Wesley 1994; 105–129.

Garpestad E & Katayama H et al. Stroke volume and cardiac output decrease at termination of obstructive apneas. J. Appl. Physiol. 1992; 73(5): 1743–1748.

Ichimaru Y, Clark K, Weiss WJ et al. Effect of sleep on the relationship between respiration and heart rate variability. IEEE Comp. Soc. Computers in Cardiology 1990; 657–660.

7 publications cite this project.
    The most recent are listed below.

Synthetic data generation methods for longitudinal and time series health data: a systematic review Marko Miletic, Murat Sariyar. BMC Medical Informatics and Decision Making ,
        2025.

Robust performances of a nocturnal long-term ECG algorithm for the evaluation of sleep apnea syndrome: A pilot study Pauline Guyot, Morgane Eveilleau, Thierry Bastogne et al. PLoS ONE ,
        2025.

Deep learning framework for automatic detection and classification of sleep apnea severity from polysomnography signals A. Raja Brundha, A. Lakshmi Sangeetha, A. Balajiganesh. Neural Computing and Applications ,
        2024.

Hidden Hazards Beneath Cross-Validation Methods in Machine Learning-Based Sleep Apnea Detection Daniele Padovano, Arturo Martínez‐Rodrigo, Jose Manuel Pastor et al. Computing in cardiology ,
        2022.

A novel solution of deep learning for sleep apnea detection: enhancement of SC and elimination of GVICS Narayan Limbu, Abeer Alsadoon, P. W. C. Prasad et al. Multimedia Tools and Applications ,
        2022.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

Download
              the ZIP file (632.4 MB)

Download with the PhysioNet Python package : physionet download slpdb --version 1.0.0

Download the files using your terminal: wget -r -N -c -np https://physionet.org/files/slpdb/1.0.0/

Download the files using AWS command line tools: aws s3 sync --no-sign-request s3://physionet-open/slpdb/1.0.0/ DESTINATION
