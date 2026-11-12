# here

**Source:** https://physionet.org/content/echonext

---

EchoNext: A Dataset for Detecting Echocardiogram-Confirmed Structural Heart Disease from ECGs

Elias, P., & Finer, J. (2026). EchoNext: A Dataset for Detecting Echocardiogram-Confirmed Structural Heart Disease from ECGs (version 1.1.1). PhysioNet . RRID:SCR_007345. https://doi.org/10.13026/7cfw-d091

Hughes, J. W., Jing, L., Finer, J., Hartzel, D., Kelsey, C., Long, A., Rocha, D., Ruhl, J., Poterucha, T., & Elias, P. (2026). EchoNext-mini: A dataset and baseline AI model for detecting structural heart disease from electrocardiograms. NEJM AI. https://doi.org/10.1056/aidbp2500516 https://ai.nejm.org/doi/full/10.1056/AIdbp2500516

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

This dataset contains a de-identified collection of 100,000 12-lead electrocardiograms (ECGs) with paired structural heart disease (SHD) labels derived from echocardiography, collected at Columbia University Irving Medical Center. Each ECG is provided with raw waveform data sampled at 250 Hz across all 12 leads, along with accompanying demographic and ECG-specific tabular metadata, including age, sex, heart rate, PR interval, QRS duration, and corrected QT interval. Each ECG is annotated with a binary label indicating the presence or absence of structural heart disease based on echocardiographic findings, including reduced left ventricular ejection fraction, increased ventricular wall thickness, significant valvular disease, right ventricular dysfunction, pulmonary hypertension, or pericardial effusion.

This dataset was developed as part of the creation of the Columbia Mini-Model , a lightweight deep learning model for SHD detection from ECGs. The dataset represents a simplified, focused subset of the larger EchoNext training population and was used to evaluate model performance in resource-constrained settings or smaller-scale deployment environments. It is being released to promote transparency and reproducibility, support further research in cardiovascular AI, and enable benchmarking of lightweight ECG-based screening models for structural heart disease.

Early detection of structural heart disease is critical to improving outcomes, but widespread screening remains limited by the cost and accessibility of imaging tools such as echocardiography [1,2] . Recent advances in machine learning applied to heart rhythm recordings have shown promise in identifying disease [3,4] , although previous work has been limited by development in narrow populations or targeting only select heart conditions [5] . We introduced a deep learning model, EchoNext, trained on more than 1 million heart rhythm and imaging records across a large and diverse health system to detect many forms of structural heart disease [6]. The model demonstrated high diagnostic accuracy in internal and external validation, outperforming cardiologists in a controlled evaluation and showing consistent performance across different care settings and racial and/or ethnic groups. The models were prospectively evaluated in a clinical trial of patients without previous cardiac imaging, successfully identifying previously undiagnosed heart disease. These findings support the potential of artificial intelligence to expand access to heart disease screening at scale. To enable further development and transparency, we have publicly released model weights from the Columbia Mini-Model and a large, annotated dataset linking heart rhythm data to imaging-based diagnoses.This resource includes the dataset, and the trained model weights and code are available at Github (Section 7) [7].

The dataset was derived from clinical care data at Columbia University Irving Medical Center, an academic tertiary care hospital. All data were retrospectively collected from adult patients (age ≥18 years) who underwent a digitally stored 12-lead electrocardiogram (ECG) and a transthoracic echocardiogram within a 1-year interval between 2008 and 2022. ECG waveform data were extracted from the GE MUSE ECG management system at a sampling frequency of 250 Hz across all 12 leads. Each ECG was paired with structured metadata including age, sex, heart rate, PR interval, QRS duration, QT interval, and corrected QT interval. All ECG features were extracted from XML files obtained from GE MUSE Nx 10.2.

Echocardiographic data were extracted from the Syngo Dynamics (Siemens) and Xcelera (Philips) systems. Five numerical values were extracted: left ventricular ejection fraction (LVEF), interventricular septum thickness, posterior wall thickness, pulmonary artery systolic pressure (PASP), and tricuspid regurgitation maximum velocity (TR Max Velocity). The maximum of the two wall thicknesses was considered the left ventricular wall thickness (LVWT). Additionally, six categorical diagnoses were extracted: aortic, mitral, tricuspid, and pulmonic regurgitation (AR, MR, TR, PR; given a value of none/trace, mild, moderate, or severe), RV systolic function (given a value of as normal, mildly reduced, moderately reduced, or severely reduced), pericardial effusion (given a value of none/trace, small, moderate, or large), and aortic stenosis (AS; given a value of none/trace, mild, moderate, or severe). Labels were then binarized to create labels for moderate or greater disease. Continuous labels were binarized to moderate disease at LVWT ≥ 13 mm, LVEF ≤ 45%, PASP ≥ 45 mmHg and TR Max Velocity ≥ 32 cm/s, and to severe disease at LVWT ≥ 16mm, LVEF ≤ 35%, PASP ≥ 60 mmHg and TR Max Velocity ≥ 36 cm/s. Echocardiograms with prosthetic valves, missing LVEF, or no wall thickness measurement were excluded from the dataset. The SHD label is defined as presence of one or more of these binarized labels.

For an ECG to be labeled as being "positive" for a disease, it must have been performed within 1 year prior to an echocardiogram with SHD. In patients without SHD (confirmed by at least one 'negative' echocardiogram), all ECGs prior to the most recent echo were labeled as negative and included in the study. More granular SHD labels are provided for ECGs taken within a year prior to an echocardiogram.

All data were de-identified prior to inclusion in this dataset. Patient identifiers were replaced with randomly generated surrogate keys. All direct identifiers, including names and full dates, were removed. Only the year of ECG acquisition was retained, and patient age was capped at 90 years. No date-shifting was performed.

This repository contains the dataset used to train the EchoNext Mini-Model , comprising a curated collection of 100,000 electrocardiograms (ECGs) sourced from Columbia and Allen hospitals.

The dataset is divided into training, validation, and test splits. Some ECGs are labeled as `no_split` and are not included in model training. The training set may include multiple ECGs per patient; validation and test sets include only the latest ECG per patient. Each ECG in the dataset is accompanied by tabular features, waveform data, and metadata including echocardiographic measurements and diagnostic labels.

ECG Metadata ( EchoNext_metadata_100k.csv ). A CSV file containing 100,000 rows of metadata and labels for each ECG record: Note: The order of ECGs in the metadata file matches the row order in the corresponding NumPy array files. This alignment is essential for correct data usage. The following columns are provided in the metadata file: ECG Demographic Data patient_key : De-identified patient identifier. acquisition_year : Year the ECG was acquired. location_setting : Clinical context of ECG acquisition. Values include 'inpatient' , 'emergency' , 'outpatient' , and 'procedural' . race_ethnicity : Combined race and ethnicity classification. Values include 'hispanic' , 'white' , 'black' , 'asian' , 'other' , and 'unknown' . most_recent_ecg : Binary flag indicating whether the ECG is the most recent for the patient ( 1 for most recent, 0 otherwise`). Raw ECG-Derived Tabular Features sex: Patient sex (male or female) ventricular_rate : The rate of ventricular contractions (beats per minute), as measured from the ECG. atrial_rate : The rate of atrial contractions (beats per minute), as measured from the ECG. pr_interval : The time interval (in milliseconds) from the onset of the P wave to the start of the QRS complex, reflecting atrioventricular conduction. qrs_duration : The duration (in milliseconds) of the QRS complex, representing the time for ventricular depolarization. qt_corrected : The corrected QT interval (in milliseconds), adjusted for heart rate, representing the total time for ventricular depolarization and repolarization. age_at_ecg : Patient age (in years) at the time of ECG acquisition. Note: Age values are capped at 90 years for de-identification purposes. Echo-Derived Features aortic_stenosis_value : Aortic stenosis severity, graded none/trace, mild, moderate, or severe aortic_regurgitation_value : Aortic regurgitation severity, graded from none to severe. mitral_regurgitation_value : Mitral regurgitation severity, graded from none to severe. tricuspid_regurgitation_value : Tricuspid regurgitation severity, graded from none to severe. pulmonary_regurgitation_value : Pulmonary regurgitation, graded from none to severe. rv_systolic_function_value : Qualitative assessment of right ventricular systolic function, categorized as normal, mildly reduced, moderately reduced, or severely reduced. pericardial_effusion_value : Presence and size of fluid accumulation in the pericardial space, categorized as none, small, moderate, or large. ivs_measurement : Thickness (in centimeters) of the interventricular septum, measured during diastole. lvpw_measurement : Thickness (in centimeters) of the left ventricular posterior wall, measured during diastole. pasp_value : Estimated pulmonary artery systolic pressure (in mmHg), derived from Doppler measurements. tr_max_velocity_value : Maximum velocity (in m/s) of tricuspid regurgitation jet, used to estimate pulmonary pressures. lvef_value : Left ventricular ejection fraction (in %), representing the percentage of blood ejected from the left ventricle during systole. Echo-Derived Binary Labels These binary labels were derived from structured echocardiogram report fields and binarized using clinically relevant thresholds to indicate moderate or greater disease severity lvef_lte_45_flag : Indicates whether the left ventricular ejection fraction (LVEF) is less than or equal to 45%, suggesting moderately reduced systolic function. lvwt_gte_13_flag : Indicates whether the maximum of the interventricular septum (IVS) or posterior wall (LVPW) thickness is greater than or equal to 1.3 cm, suggesting moderate left ventricular hypertrophy. aortic_stenosis_moderate_or_greater_flag : Indicates moderate or severe aortic stenosis, based on categorical grading in the echocardiogram report. aortic_regurgitation_moderate_or_greater_flag : Indicates moderate or severe aortic regurgitation. mitral_regurgitation_moderate_or_greater_flag : Indicates moderate or severe mitral regurgitation. tricuspid_regurgitation_moderate_or_greater_flag : Indicates moderate or severe tricuspid regurgitation. pulmonary_regurgitation_moderate_or_greater_flag : Indicates moderate or severe pulmonary regurgitation. rv_systolic_dysfunction_moderate_or_greater_flag : Indicates moderate or severe right ventricular systolic dysfunction. pericardial_effusion_moderate_large_flag : Indicates presence of a moderate or large pericardial effusion. pasp_gte_45_flag : Indicates whether pulmonary artery systolic pressure (PASP) is greater than or equal to 45 mmHg, suggesting pulmonary hypertension. tr_max_gte_32_flag : Indicates whether tricuspid regurgitation maximum velocity is greater than or equal to 3.2 m/s (32 cm/s), a surrogate for elevated pulmonary pressures. shd_moderate_or_greater_flag: Composite binary label indicating the presence of moderate or greater structural heart disease, defined as meeting the threshold for one or more of the above conditions. Split Information split: Indicates the data partition — one of train, val, test, or no_split.

ECG Demographic Data patient_key : De-identified patient identifier. acquisition_year : Year the ECG was acquired. location_setting : Clinical context of ECG acquisition. Values include 'inpatient' , 'emergency' , 'outpatient' , and 'procedural' . race_ethnicity : Combined race and ethnicity classification. Values include 'hispanic' , 'white' , 'black' , 'asian' , 'other' , and 'unknown' . most_recent_ecg : Binary flag indicating whether the ECG is the most recent for the patient ( 1 for most recent, 0 otherwise`).

patient_key : De-identified patient identifier.

acquisition_year : Year the ECG was acquired.

location_setting : Clinical context of ECG acquisition. Values include 'inpatient' , 'emergency' , 'outpatient' , and 'procedural' .

race_ethnicity : Combined race and ethnicity classification. Values include 'hispanic' , 'white' , 'black' , 'asian' , 'other' , and 'unknown' .

most_recent_ecg : Binary flag indicating whether the ECG is the most recent for the patient ( 1 for most recent, 0 otherwise`).

Raw ECG-Derived Tabular Features sex: Patient sex (male or female) ventricular_rate : The rate of ventricular contractions (beats per minute), as measured from the ECG. atrial_rate : The rate of atrial contractions (beats per minute), as measured from the ECG. pr_interval : The time interval (in milliseconds) from the onset of the P wave to the start of the QRS complex, reflecting atrioventricular conduction. qrs_duration : The duration (in milliseconds) of the QRS complex, representing the time for ventricular depolarization. qt_corrected : The corrected QT interval (in milliseconds), adjusted for heart rate, representing the total time for ventricular depolarization and repolarization. age_at_ecg : Patient age (in years) at the time of ECG acquisition. Note: Age values are capped at 90 years for de-identification purposes.

ventricular_rate : The rate of ventricular contractions (beats per minute), as measured from the ECG.

atrial_rate : The rate of atrial contractions (beats per minute), as measured from the ECG.

pr_interval : The time interval (in milliseconds) from the onset of the P wave to the start of the QRS complex, reflecting atrioventricular conduction.

qrs_duration : The duration (in milliseconds) of the QRS complex, representing the time for ventricular depolarization.

qt_corrected : The corrected QT interval (in milliseconds), adjusted for heart rate, representing the total time for ventricular depolarization and repolarization.

age_at_ecg : Patient age (in years) at the time of ECG acquisition. Note: Age values are capped at 90 years for de-identification purposes.

Echo-Derived Features aortic_stenosis_value : Aortic stenosis severity, graded none/trace, mild, moderate, or severe aortic_regurgitation_value : Aortic regurgitation severity, graded from none to severe. mitral_regurgitation_value : Mitral regurgitation severity, graded from none to severe. tricuspid_regurgitation_value : Tricuspid regurgitation severity, graded from none to severe. pulmonary_regurgitation_value : Pulmonary regurgitation, graded from none to severe. rv_systolic_function_value : Qualitative assessment of right ventricular systolic function, categorized as normal, mildly reduced, moderately reduced, or severely reduced. pericardial_effusion_value : Presence and size of fluid accumulation in the pericardial space, categorized as none, small, moderate, or large. ivs_measurement : Thickness (in centimeters) of the interventricular septum, measured during diastole. lvpw_measurement : Thickness (in centimeters) of the left ventricular posterior wall, measured during diastole. pasp_value : Estimated pulmonary artery systolic pressure (in mmHg), derived from Doppler measurements. tr_max_velocity_value : Maximum velocity (in m/s) of tricuspid regurgitation jet, used to estimate pulmonary pressures. lvef_value : Left ventricular ejection fraction (in %), representing the percentage of blood ejected from the left ventricle during systole.

aortic_stenosis_value : Aortic stenosis severity, graded none/trace, mild, moderate, or severe

aortic_regurgitation_value : Aortic regurgitation severity, graded from none to severe.

mitral_regurgitation_value : Mitral regurgitation severity, graded from none to severe.

tricuspid_regurgitation_value : Tricuspid regurgitation severity, graded from none to severe.

pulmonary_regurgitation_value : Pulmonary regurgitation, graded from none to severe.

rv_systolic_function_value : Qualitative assessment of right ventricular systolic function, categorized as normal, mildly reduced, moderately reduced, or severely reduced.

pericardial_effusion_value : Presence and size of fluid accumulation in the pericardial space, categorized as none, small, moderate, or large.

ivs_measurement : Thickness (in centimeters) of the interventricular septum, measured during diastole.

lvpw_measurement : Thickness (in centimeters) of the left ventricular posterior wall, measured during diastole.

pasp_value : Estimated pulmonary artery systolic pressure (in mmHg), derived from Doppler measurements.

tr_max_velocity_value : Maximum velocity (in m/s) of tricuspid regurgitation jet, used to estimate pulmonary pressures.

lvef_value : Left ventricular ejection fraction (in %), representing the percentage of blood ejected from the left ventricle during systole.

Echo-Derived Binary Labels These binary labels were derived from structured echocardiogram report fields and binarized using clinically relevant thresholds to indicate moderate or greater disease severity lvef_lte_45_flag : Indicates whether the left ventricular ejection fraction (LVEF) is less than or equal to 45%, suggesting moderately reduced systolic function. lvwt_gte_13_flag : Indicates whether the maximum of the interventricular septum (IVS) or posterior wall (LVPW) thickness is greater than or equal to 1.3 cm, suggesting moderate left ventricular hypertrophy. aortic_stenosis_moderate_or_greater_flag : Indicates moderate or severe aortic stenosis, based on categorical grading in the echocardiogram report. aortic_regurgitation_moderate_or_greater_flag : Indicates moderate or severe aortic regurgitation. mitral_regurgitation_moderate_or_greater_flag : Indicates moderate or severe mitral regurgitation. tricuspid_regurgitation_moderate_or_greater_flag : Indicates moderate or severe tricuspid regurgitation. pulmonary_regurgitation_moderate_or_greater_flag : Indicates moderate or severe pulmonary regurgitation. rv_systolic_dysfunction_moderate_or_greater_flag : Indicates moderate or severe right ventricular systolic dysfunction. pericardial_effusion_moderate_large_flag : Indicates presence of a moderate or large pericardial effusion. pasp_gte_45_flag : Indicates whether pulmonary artery systolic pressure (PASP) is greater than or equal to 45 mmHg, suggesting pulmonary hypertension. tr_max_gte_32_flag : Indicates whether tricuspid regurgitation maximum velocity is greater than or equal to 3.2 m/s (32 cm/s), a surrogate for elevated pulmonary pressures. shd_moderate_or_greater_flag: Composite binary label indicating the presence of moderate or greater structural heart disease, defined as meeting the threshold for one or more of the above conditions.

lvef_lte_45_flag : Indicates whether the left ventricular ejection fraction (LVEF) is less than or equal to 45%, suggesting moderately reduced systolic function.

lvwt_gte_13_flag : Indicates whether the maximum of the interventricular septum (IVS) or posterior wall (LVPW) thickness is greater than or equal to 1.3 cm, suggesting moderate left ventricular hypertrophy.

aortic_stenosis_moderate_or_greater_flag : Indicates moderate or severe aortic stenosis, based on categorical grading in the echocardiogram report.

aortic_regurgitation_moderate_or_greater_flag : Indicates moderate or severe aortic regurgitation.

mitral_regurgitation_moderate_or_greater_flag : Indicates moderate or severe mitral regurgitation.

tricuspid_regurgitation_moderate_or_greater_flag : Indicates moderate or severe tricuspid regurgitation.

pulmonary_regurgitation_moderate_or_greater_flag : Indicates moderate or severe pulmonary regurgitation.

rv_systolic_dysfunction_moderate_or_greater_flag : Indicates moderate or severe right ventricular systolic dysfunction.

pericardial_effusion_moderate_large_flag : Indicates presence of a moderate or large pericardial effusion.

pasp_gte_45_flag : Indicates whether pulmonary artery systolic pressure (PASP) is greater than or equal to 45 mmHg, suggesting pulmonary hypertension.

tr_max_gte_32_flag : Indicates whether tricuspid regurgitation maximum velocity is greater than or equal to 3.2 m/s (32 cm/s), a surrogate for elevated pulmonary pressures.

shd_moderate_or_greater_flag: Composite binary label indicating the presence of moderate or greater structural heart disease, defined as meeting the threshold for one or more of the above conditions.

Split Information split: Indicates the data partition — one of train, val, test, or no_split.

split: Indicates the data partition — one of train, val, test, or no_split.

Tabular Features Filenames follow the convention EchoNext_<SPLIT>_tabular_features.npy where split is one of: train, val, test, or no_split. Each file is a NumPy array of shape N x 7 . The order of ECGs in the NumPy array files matches the row order in the corresponding metadata file. Preprocessed tabular features for each ECG, separated by split: sex: Binary indicator of patient sex. Encoded as 0 for female and 1 for male. ventricular_rate : Preprocessed ventricular rate. atrial_rate : Preprocessed atrial rate. pr_interval : Preprocessed PR interval. qrs_duration : Preprocessed QRS duration. qt_corrected : Preprocessed QT interval. age_at_ecg : Preprocessed patient age at time of ECG. Preprocessing Notes: Continuous features were standardized. Missing values were imputed using the median, except for atrial_rate and pr_interval , which were set to 0. sex was binarized.

Filenames follow the convention EchoNext_<SPLIT>_tabular_features.npy where split is one of: train, val, test, or no_split.

Each file is a NumPy array of shape N x 7 .

The order of ECGs in the NumPy array files matches the row order in the corresponding metadata file.

Preprocessed tabular features for each ECG, separated by split: sex: Binary indicator of patient sex. Encoded as 0 for female and 1 for male. ventricular_rate : Preprocessed ventricular rate. atrial_rate : Preprocessed atrial rate. pr_interval : Preprocessed PR interval. qrs_duration : Preprocessed QRS duration. qt_corrected : Preprocessed QT interval. age_at_ecg : Preprocessed patient age at time of ECG. Preprocessing Notes: Continuous features were standardized. Missing values were imputed using the median, except for atrial_rate and pr_interval , which were set to 0. sex was binarized.

sex: Binary indicator of patient sex. Encoded as 0 for female and 1 for male.

ventricular_rate : Preprocessed ventricular rate.

qrs_duration : Preprocessed QRS duration.

age_at_ecg : Preprocessed patient age at time of ECG.

Preprocessing Notes: Continuous features were standardized. Missing values were imputed using the median, except for atrial_rate and pr_interval , which were set to 0. sex was binarized.

Missing values were imputed using the median, except for atrial_rate and pr_interval , which were set to 0.

Waveform Features Filenames follow the convention EchoNext_<SPLIT>_waveforms.npy . Each file contains preprocessed waveform data for ECGs in the corresponding split. The ECGs are stored as a NumPy array with shape N × 1 × 2500 × 12 , representing a 10-second, 12-lead ECG segment sampled at 250 Hz, and N is the size of the split. The order of ECGs in the NumPy array files matches the row order in the corresponding metadata file. Waveform Preprocessing Median-filtered per lead. Clipped at the 0.1st and 99.9th percentiles. Normalized using dataset-wide mean and standard deviation.

Filenames follow the convention EchoNext_<SPLIT>_waveforms.npy . Each file contains preprocessed waveform data for ECGs in the corresponding split. The ECGs are stored as a NumPy array with shape N × 1 × 2500 × 12 , representing a 10-second, 12-lead ECG segment sampled at 250 Hz, and N is the size of the split.

The order of ECGs in the NumPy array files matches the row order in the corresponding metadata file.

Waveform Preprocessing Median-filtered per lead. Clipped at the 0.1st and 99.9th percentiles. Normalized using dataset-wide mean and standard deviation.

Clipped at the 0.1st and 99.9th percentiles.

Normalized using dataset-wide mean and standard deviation.

More details on running inference available at Github [7] (Section 7).

This dataset was developed as part of the EchoNext study, Detecting Structural Heart Disease from Electrocardiograms Using AI [6]. It enables reproducible research and scalable AI-driven screening for structural heart disease (SHD). The dataset can serve as a benchmark for evaluating existing ECG-based models or as a resource for training new deep learning models for SHD detection.

The EchoNext Mini-Model and dataset offer several opportunities for reuse. Researchers can use the dataset to train or fine-tune models for SHD classification, explore model interpretability in ECG-based diagnostics, or incorporate SHD risk scores as features in downstream clinical prediction tasks. The dataset is also well-suited for benchmarking lightweight models in resource-constrained settings. Instructions for running inference using the EchoNext Mini-Model are available in the public GitHub repository (Section 7) [7].

Several limitations should be noted. The dataset uses fixed binary thresholds to define SHD labels (e.g., LVEF ≤ 45%), which may not align with all clinical guidelines. Some echocardiographic measurements are subject to interobserver variability, introducing potential label noise. Certain conditions, such as pulmonary regurgitation, are underrepresented. The dataset includes only patients who had both an ECG and an echocardiogram within a one-year window, which may introduce selection bias. Additionally, disease labels were derived from structured report fields and may not fully capture the nuance of clinical interpretation.

Other limitations include potential inaccuracies in automatically extracted ECG features, particularly the corrected QT interval (QTc), which is known to be error-prone [8]. While the dataset includes a high proportion of Hispanic and Black patients, it contains only 3.4% Asian patients and is limited to a single institution, which may affect generalizability across populations and ECG acquisition systems.

Version 1.1.1 was released on April 20, 2026. Updated the citation. Version 1.1.0 was released on September 15, 2025. It added 3 new informational fields to the patient ECG metadata file.

location_setting Clinical context of ECG acquisition

race_ethnicity Combined race and ethnicity classification

Combined race and ethnicity classification

most_recent_ecg Indicating whether the ECG is the most recent for the patient

Indicating whether the ECG is the most recent for the patient

The DISCOVERY trial and associated analyses were approved by the Institutional Review Board at NewYork-Presbyterian Hospital/Columbia University Irving Medical Center. Written informed consent was obtained from all participants in the prospective study. Retrospective data used to train and evaluate the EchoNext model were analyzed under IRB-approved protocols. These protocols include provisions allowing the sharing of de-identified data for research purposes. The authors declare no additional ethics concerns.

Columbia University has submitted a patent application (#63/555,968) on the EchoNext ECG algorithm on which TJP, LJ, CMH, and PE are inventors.

Otto CM, Nishimura RA, Bonow RO, Carabello BA, Erwin JP 3rd, Gentile F, et al. 2020 ACC/AHA guideline for the management of patients with valvular heart disease: a report of the American College of Cardiology/American Heart Association Joint Committee on Clinical Practice Guidelines. J Am Coll Cardiol. 2021 Feb 2;77(4):e25–197.

Heidenreich PA, Bozkurt B, Aguilar D, Allen LA, Byun JJ, Colvin MM, et al. 2022 AHA/ACC/HFSA guideline for the management of heart failure: executive summary: a report of the American College of Cardiology/American Heart Association Joint Committee on Clinical Practice Guidelines. J Am Coll Cardiol. 2022 May 3;79(17):1757–80.

Elias P, Poterucha TJ, Rajaram V, Moller LM, Rodriguez V, Bhave S, et al. Deep learning electrocardiographic analysis for detection of left-sided valvular heart disease. J Am Coll Cardiol. 2022 Aug 9;80(6):613–26.

Ulloa-Cerna AE, Jing L, Pfeifer JM, Raghunath S, Ruhl JA, Rocha DB, et al. rECHOmmend: an ECG-based machine learning approach for identifying patients at increased risk of undiagnosed structural heart disease detectable by echocardiography. Circulation. 2022 Jul 5;146(1):36–47.

Siontis KC, Noseworthy PA, Attia ZI, Friedman PA. Artificial intelligence-enhanced electrocardiography in cardiovascular disease management. Nat Rev Cardiol. 2021 Jul;18(7):465–78.

Poterucha TJ, Jing L, Ricart RP, Adjei-Mosi M, Finer J, Hartzel D, et al. Detecting structural heart disease from electrocardiograms using AI. Nature. 2025 Jul 16.

IntroECG: A full-process library for deep learning on 12-lead electrocardiograms. Available from: https://github.com/PierreElias/IntroECG [Accessed July 29, 2025]

Neumann B, Vink AS, Hermans BJM, et al. Manual vs. automatic assessment of the QT-interval and corrected QT. Europace [Internet] 2023;25(9). Available from: http://dx.doi.org/10.1093/europace/euad213

24 publications cite this project.
    The most recent are listed below.

CardioJEPA: A Framework for Holistic Cardiac Representations Through Predictive Multimodal Alignment with ECG-Preservation Daniel Uyterlinde, Laura Alvarez-Florez, Samuel Ruipérez-Campillo et al. Research Square ,
        2026.

EchoGraph-FusionNet: Adaptive Disease-Graph and Mixture-of-Experts Learning for Predicting Echocardiographic Abnormalities from ECGs Çetin Mirzaoğlu, Tolga Çakmak, Melike Demir et al. Life ,
        2026.

Privacy-Budget Allocation for Heterogeneous Query Batches: Calibration and Execution Boundaries Yudong Zheng, Jinan Shen. Zenodo (CERN European Organization for Nuclear Research) ,
        2026.

MS-ECG-FM: Towards a More Universal Electrocardiogram Foundation Model for Health Monitoring using Multi-source Contrastive Learning Robert A. Lewis, I-Min Chiu, Kyle Verrier et al. arXiv (Cornell University) ,
        2026.

Cross-Modal Contrastive Learning of ECG and Angiography Representations for Severe Stenosis Classification Nikola Cenikj, Özgün Turgut, Alexander Müller et al. Lecture notes in computer science ,
        2026.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

EchoNext: A Dataset for Detecting Echocardiogram-Confirmed Structural Heart Disease from ECGs v1.0.0

sign the data use agreement for the project
