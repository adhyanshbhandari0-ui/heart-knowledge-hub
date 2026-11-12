# MIMIC-IV-ECHO

**Source:** https://physionet.org/content/mimic-iv-echo/0.1

---

MIMIC-IV-ECHO: Echocardiogram Matched Subset

Brian Gow , Tom Pollard , Nathaniel Greenbaum , Benjamin Moody , Alistair Johnson , Elizabeth Herbst , Jonathan W Waks , Parastou Eslami , Ashish Chaudhari , Tanner Carbonati , Seth Berkowitz , Roger Mark , Steven Horng

Gow, B., Pollard, T., Greenbaum, N., Moody, B., Johnson, A., Herbst, E., Waks, J. W., Eslami, P., Chaudhari, A., Carbonati, T., Berkowitz, S., Mark, R., & Horng, S. (2023). MIMIC-IV-ECHO: Echocardiogram Matched Subset (version 0.1). PhysioNet . RRID:SCR_007345. https://doi.org/10.13026/ef48-v217

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

The MIMIC-IV-ECHO module contains more than 500,000 echocardiograms across 7,243 studies from 4,579 distinct patients. A given study consists of numerous sequences of images, with each sequence representing a particular view of the patient's heart. This subset contains echocardiograms for patients who appear in the MIMIC-IV Clinical Database and were admitted between 2017 and 2019. We have provided information for linking a given echocardiogram to the cardiologist's report where available. Records in MIMIC-IV-ECHO are matched to the MIMIC-IV Clinical Database, making it possible to link to information across the MIMIC-IV modules..

An echocardiogram uses high frequency sound waves (ultrasound) to take pictures of the heart [1], revealing information about the heart's structure and how it is functioning. Echocardiography is used to diagnose, monitor, and assess treatment results in patients who have or are suspected to have heart problems.

An echocardiogram study typically contains multiple views and sometimes uses multiple ultrasound techniques. A change in the position and angle of the ultrasound probe relative to the heart produces a different view [2]. Different views reveal information about different areas in the heart. All views provided here are taken with the probe at the patient's chest (i.e. TTE or Transthoracic Echocardiography). Common types of echocardiography include 2-D, Doppler, and 3-D [2]. In a 2-D echocardiogram, real-time cross-sectional images of the heart are produced. Doppler echocardiography is an extension of 2-D with information on blood flow velocities and directions. 3-D echocardiography produces three dimensional images of the heart.

While echocardiograms are an extremely valuable tool for the management of heart problems, they typically only comprise a small part of understanding the overall condition of a patient at the hospital. Echocardiograms are most informative when combined with a broader set of data such as: patient demographics, diagnoses, medications, laboratory tests, and electrocardiograms. This broader set of information is shared as part of the MIMIC-IV Database [3].

Echocardiograms are collected across Beth Israel Deaconess Medical Center (BIDMC). Each electrocardiogram consists of a sequence of images for a particular view of the heart along with metadata. Algorithms in the electrocardiogram machine analyze the images and produce a report of measurements (ex: left ventricle ejection fraction, mitral valve E/A ratio, etc). We refer to these as machine measurements.

We provide unique identifiers, such as subject_id , that allow studies to be connected to other information in the MIMIC-IV Database. All of the information is de-identified to satisfy the US Health Insurance Portability and Accountability Act of 1996 (HIPAA) Safe Harbor requirements.

The dataset contains a subset of the available echocardiograms recorded between 2017 - 2019 from patients in the MIMIC-IV Clinical Database. Echocardiograms were collected on General Electric Vivid E90, Vivid E95, and Vivid S7 machines.

When the echocardiograms are recorded, the machine is populated with the patient's demographic details and their medical record number (MRN). The MRN was used to match records to the corresponding patient in the MIMIC-IV Clinical Database. Dates were shifted to obscure the actual date, but relative date shifts are retained for a given patient. A unique study_id was generated for each record.

Text embedded in the images was identified by using Optical Character Recognition. When images were found to contain PHI, the entire study was omitted from the dataset. This occurred in a very small number of studies.

We also scrubbed all of the PHI from the electrocardiogram metadata:

IDs: Source identifiers used by the hospital were shifted to a random value. In particular, mrn was translated to subject_id , consistent with MIMIC-IV. A unique study_id was also generated.

UIDs: Unique identifiers (UIDs) provide the capability to identify a wide variety of items, typically providing a guarantee of uniqueness across countries, sites, vendors, equipment, and formats. Some UIDs, such as the Study Instance UID, contain sensitive information. In such cases, we deterministically shifted the UID by using a UID root assigned to our laboratory ( 1.2.840.113554.6.1. ) followed by a three digit value specific to the variable and a randomized value.

Dates: Raw dates were either shifted (consistent with all date shifts in MIMIC-IV for a given subject) or removed (in the case of Patient Birth Date).

Names: Person names were either deterministically replaced with a randomized string or removed (in the case of Referring Physician Name).

Private tags: Information recorded in private tags was removed.

Timestamps for events in the MIMIC-IV Clinical Database, such as drug administration, are aligned with the timestamps in MIMIC-IV-ECHO. However, some of the echocardiograms provided here were collected outside of Emergency Department (ED) or Intensive Care Unit (ICU) visits at the hospital. Since the MIMIC-IV Clinical Database is composed solely of ED and ICU data, the echocardiogram timestamp can occur before or after a visit in the clinical database.

The machine measurements will be released in an upcoming version of this project.

Cardiologist interpretations of the echocardiograms will be made available at a later date in the MIMIC-IV Note module [4]. These reports were de-identified using a hybrid rule-based and machine learning approach [5-8], similar to that used for other MIMIC reports. Each instance of PHI was replaced by three underscores.

Approximately 525,000 echocardiograms across 7,243 studies from 4,579 distinct patients are provided in the MIMIC-IV-ECHO module. Around 5% of the available echocardiograms were withheld for later use as a hidden test set. Patients in this module are linked to the MIMIC-IV Clinical Database on subject_id . Many but not all of the echocardiograms overlap with a hospital or emergency department stay.

The electrocardiograms are stored as DICOM (.dcm) files. DICOM or Digital Imaging and Communications in Medicine defines standards for the storage of medical images and related information [9]. Each DICOM file contains a sequence of images for a particular view of the heart.

Echocardiograms are grouped into subdirectories based on subject_id . Each DICOM record path follows the pattern files/pNN/pXXXXXXXX/sZZZZZZZZ/ZZZZZZZZ_VVVV , where:

NN is the first two characters of the subject_id ,

An example of the file structure is as follows:

Here we show a subject under the p10 directory and another under the p19 directory. Subject p10690270 has two studies. The first study, s95240362 , has 90 DICOM files with view numbers between 4 and 93. The second study, s90045402 , has 83 DICOM files with view numbers between 1 and 88. The subject under the p19 directory, p19425623 , has only one study s90267113 . We find 83 DICOM files under this study with view numbers between 1 and 88.

A number of open-source programs are available for viewing DICOMs such as Miele-LXIV(Mac), MicroDicom(Windows), and ImageMagick(Linux, Mac, Windows). We also provide example code for loading DICOMs into Python in the Usage Notes section below.

Our source data does not include an identifier that directly links a cardiologist report to a given study. To help address this issue, we have provided a derived table (detailed below) that indicates which reports occur within two days of a given study. Approximately 12% of the electrocardiograms are linked to a cardiologist report in the derived table. An update of this note data is in the works which will increase the percentage of linked notes. The cardiologist reports will be released under the MIMIC-IV Note module at a later date.

The echo-record-list.csv provides the path to each DICOM file ( dicom_filepath ) along with the acquisition_datetime of the DICOM (date and time that the acquisition started for a given view), the associated study_id and the subject's MIMIC-IV subject_id .

The echo-study-list.csv provides a link between the study_id and the associated cardiologist report, where available. When a cardiologist report / note is available within two days of the study, the note_id , note_seq , and note_charttime are provided. This information can be used to link to the note text in the MIMIC-IV Note module. The patient's subject_id and the date and time for the study ( study_datetime ) are also provided.

These summary tables are also provided on BigQuery [10].

The MIMIC-IV-ECHO module augments existing information in MIMIC-IV, providing an important new resource - particularly for cardiac-related research.

The code snippet below shows how to use the pydicom library to load a DICOM into python, read its metadata and plot an image.

In the example below, we show how a patient in MIMIC-IV-ECHO with subject_id = p10690270 can be linked to admission information in the MIMIC-IV Clinical Database. Running the following SQL command in Google BigQuery gives us the dates of available echocardiograms for the patient:

Executing the following queries gives us the admission and discharge times for the patient in the MIMIC-IV Clinical Database:

The results show two hospital admissions and one emergency department stay for the patient. Our echocardiogram with study_id = 95240362 , is associated with the admission in the (deidentified) year of 2179. In 2176 the patient was seen in the emergency department and admitted to the hospital. This visit does not have an associated echocardiogram and likely occurred prior to the date range for inclusion in MIMIC-IV-ECHO.

Our echocardiogram with study_id = 90045402 does not appear to be associated with a clinical database visit. Some of the echocardiograms in this dataset were collected outside of ED or ICU visits. Since the MIMIC-IV Clinical Database is currently composed solely of ED and ICU data, the echocardiograms timestamp may occur before or after a visit recorded in the clinical database.

This release contains echocardiogram DICOM files for subjects in MIMIC-IV.

The project was approved by the Institutional Review Boards of Beth Israel Deaconess Medical Center (Boston, MA) and the Massachusetts Institute of Technology (Cambridge, MA). Requirement for individual patient consent was waived because the project did not impact clinical care and all protected health information was deidentified.

SH, RM, BG, and TP are funded by the Massachusetts Life Sciences Center, Nov. 30, 2020. NG is supported by National Institutes of Health National Library of Medicine Biomedical Informatics and Data Science Research Training Program under grant number T15LM007092-30. BG, TP, AJ, BM, CF, DM, and RM are supported by the National Institute of Biomedical Imaging and Bioengineering (NIBIB) under NIH grant number R01EB030362.

The author(s) have no conflicts of interest to declare.

Ashley EA, Niebauer J. Cardiology Explained. London: Remedica; 2004. Chapter 4, Understanding the echocardiogram. Available from: https://www.ncbi.nlm.nih.gov/books/NBK2215/

Lang RM, Badano LP, Mor-Avi V, Afilalo J, Armstrong A, Ernande L, Flachskampf FA, Foster E, Goldstein SA, Kuznetsova T, Lancellotti P. Recommendations for cardiac chamber quantification by echocardiography in adults: an update from the American Society of Echocardiography and the European Association of Cardiovascular Imaging. European Heart Journal-Cardiovascular Imaging. 2015 Mar 1;16(3):233-71.

Johnson, A., Bulgarelli, L., Pollard, T., Horng, S., Celi, L. A., & Mark, R. (2021). MIMIC-IV (version 1.0). PhysioNet. https://doi.org/10.13026/s6n6-xd98.

Johnson, A., Pollard, T., Horng, S., Celi, L. A., & Mark, R. (2023). MIMIC-IV-Note: Deidentified free-text clinical notes (version 2.2). PhysioNet. https://doi.org/10.13026/1n74-ne17.

Margaret Douglass, Computer-assisted de-identification of free-text nursing notes. Master's Thesis, 2005. MIT.

Neamatullah, I., Douglass, M.M., Lehman, L.H., Reisner, A., Villarroel, M., Long, W.J., Szolovits, P., Moody, G.B., Mark, R.G., Clifford, G.D. (2007). De-Identification Software Package (version 1.1). PhysioNet. doi:10.13026/C20M3F

Neamatullah I, Douglass MM, Lehman LH, Reisner A, Villarroel M, Long WJ, Szolovits P, Moody GB, Mark RG, Clifford GD. Automated de-identification of free-text medical records. BMC medical informatics and decision making. 2008 Dec;8(1):1-7. doi:10.1186/1472-6947-8-32

Johnson AEW, Bulgarelli L, Pollard TJ. Deidentification of free-text medical records using pre-trained bidirectional transformers. Proc ACM Conf Health Inference Learn (2020). 2020 Apr;2020:214-221. doi: 10.1145/3368555.3384455. Epub 2020 Apr 2. PMID: 34350426; PMCID: PMC8330601.

Digital Imaging and Communications in Medicine About Page. https://www.dicomstandard.org/about/ [Accessed 18 July 2023]

Documentation about using the Medical Information Mart for Intensive Care (MIMIC) Database with Google BigQuery. https://mimic.mit.edu/docs/gettingstarted/cloud/ [Accessed 21 June 2022]

50 publications cite this project.
    The most recent are listed below.

Development and internal evaluation of a model combining ECG waveforms with machine reports to identify recorded right ventricular systolic dysfunction in adults Junze Li¹, Yongfeng Shao. Research Square ,
        2026.

Body‐Size Indexation of Left Atrial Volume in Heart Failure with Preserved Ejection Fraction: Retrospective Reclassification and E/e′ Concordance Xiaolin Wu, Heqiang Zhang. Echocardiography ,
        2026.

Physiology-informed deep learning for early identification of sepsis-induced cardiomyopathy from echocardiographic cine loops: a multicenter development and external validation study Yuhan Zhao, Qinxue Wang, Jiawei Wang et al. Research Square ,
        2026.

Blood pressure history improves near-term hypotension prediction and reassessment prioritisation in sepsis Luomeng Wang, Jiajun Zhu, Rongyang Zhou et al. medRxiv ,
        2026.

Incremental value of resting electrocardiography and echocardiography for coronary artery disease: a retrospective cross-dataset evaluation Tao Guo, Huan Wang, Qingqing Niu et al. Research Square ,
        2026.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.
