# MIMIC-III Waveform Database

**Source:** https://physionet.org/content/mimic3wdb/1.0

---

Benjamin Moody , George Moody , Mauricio Villarroel , Gari D. Clifford , Ikaro Silva

New Database Added: MIMIC-III Waveform Database (Aug. 9, 2017, midnight) The MIMIC-III Waveform Database has been released, containing our largest collection to date of physiologic signals collected by bedside patient monitors in adult and neonatal intensive care units. Over 44,000 recordings have been added to the existing MIMIC-II Waveform Database, for a total of over 67,000 recordings and over three million hours of waveform data. For about one third of the database (about 22,000 recordings from 10,000 patients), extensive clinical information is also available to qualified researchers via the MIMIC-III Clinical Database.

The MIMIC-III Waveform Database has been released, containing our largest collection to date of physiologic signals collected by bedside patient monitors in adult and neonatal intensive care units. Over 44,000 recordings have been added to the existing MIMIC-II Waveform Database, for a total of over 67,000 recordings and over three million hours of waveform data. For about one third of the database (about 22,000 recordings from 10,000 patients), extensive clinical information is also available to qualified researchers via the MIMIC-III Clinical Database.

Moody, B., Moody, G., Villarroel, M., Clifford, G. D., & Silva, I. (2020). MIMIC-III Waveform Database (version 1.0). PhysioNet . RRID:SCR_007345. https://doi.org/10.13026/c2607m

Johnson, A. E. W., Pollard, T. J., Shen, L., Lehman, L. H., Feng, M., Ghassemi, M., Moody, B., Szolovits, P., Celi, L. A., & Mark, R. G. (2016). MIMIC-III, a freely accessible critical care database. Scientific Data, 3, 160035. https://dx.doi.org/10.1038/sdata.2016.35

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

The MIMIC-III Waveform Database contains 67,830 record sets for approximately 30,000 ICU patients. Almost all record sets include a waveform record containing digitized signals (typically including ECG , ABP , respiration, and PPG , and frequently other signals) and a “numerics” record containing time series of periodic measurements, each presenting a quasi-continuous recording of vital signs of a single patient throughout an ICU stay (typically a few days, but many are several weeks in duration). A subset of this database contains waveform and numerics records that have been matched and time-aligned with MIMIC-III Clinical Database records.

The MIMIC-III Waveform Database contains thousands of recordings of multiple physiologic signals (“waveforms”) and time series of vital signs (“numerics”) collected from bedside patient monitors in adult and neonatal intensive care units ( ICUs ).

The MIMIC-III Waveform Database is a companion to the MIMIC-III Clinical Database , which contains detailed clinical information about most of the patients represented in the Waveform Database [1]. Since the contents of each database were collected independently, in partially deidentified form, matching the clinical data with the waveform data is a non-trivial task, and only a subset of Waveform Database records has been matched with Clinical Database records. See the MIMIC-III Waveform Database Matched Subset for more information.

Unlike the original MIMIC Database , waveforms were collected in a largely automated fashion, from all of the bedside monitors in certain adult and neonatal ICUs . Not all of the ICUs in the hospital were included, and the data archiving process did not run continuously, but while it was running, all waveforms from those ICUs were captured and archived. As a result, these records represent a random sample of patients in those specific ICUs .

Recorded waveforms and numerics vary depending on choices made by the ICU staff. Waveforms almost always include one or more ECG signals, and often include continuous arterial blood pressure ( ABP ) waveforms, fingertip photoplethysmogram ( PPG ) signals, and respiration, with additional waveforms (up to 8 simultaneously) as available. Numerics typically include heart and respiration rates, SpO 2 , and systolic, mean, and diastolic blood pressure, together with others as available. Recording lengths also vary; most are a few days in duration, but some are shorter and others are several weeks long.

The project was approved by the Institutional Review Boards of Beth Israel Deaconess Medical Center (Boston, MA) and the Massachusetts Institute of Technology (Cambridge, MA). Requirement for individual patient consent was waived because the project did not impact clinical care and all protected health information was deidentified.

Each recording comprises two records (a waveform record and a matching numerics record) in a single record directory (“folder”) with the name of the record. To reduce access time, the record directories have been distributed among ten intermediate-level directories (listed below). The names of these intermediate directories (30, 31, ..., 39) match the first two digits of the record directories they contain.

In almost all cases, the waveform records comprise multiple segments, each of which can be read as a separate record. Each segment contains an uninterrupted recording of a set of simultaneously observed signals, and the signal gains do not change at any time during the segment. Whenever the ICU staff changed the signals being monitored or adjusted the amplitude of a signal being monitored, this event was recorded in the raw data dump, and a new segment begins at that time.

Each composite waveform record includes a list of the segments that comprise it in its master header file . The list begins on the second line of the master header with a layout header file that specifies all of the signals that are observed in any segment belonging to the record. Each segment has its own header file and (except for the layout header) a matching (binary) signal (.dat) file . Occasionally, the monitor may be disconnected entirely for a short time; these intervals are recorded as gaps in the master header file, but there are no header or signal files corresponding to gaps.

The numerics records (designated by the letter n appended to the record name) are not divided into segments, since the storage savings that would be achieved by doing so would be relatively little.

Physiologic waveform records in this database contain up to eight simultaneously recorded signals digitized at 125 Hz with 8-, 10-, or (occasionally) 12-bit resolution. Numerics records typically contain 10 or more time series of vital signs sampled once per second or once per minute.

The following example illustrates the organization of the database:

Intermediate directory 31 contains all records with names that begin with 31 .

Record directory 3141595 is contained within intermediate directory 31.

All files associated with physiologic waveform record 3141595 and its companion numerics record 3141595n are contained within record directory 31/3141595 . The first line of the master header file for waveform record 314595 ( 31/3141595/3141595.hea ) indicates that the record is 242353557 sample intervals (about 22 days at 125 samples per second) in duration, and that it contains 427 segments and gaps. (See header(5) in the WFDB Applications Guide for details on the format of this text file.) The first segment is named 3141595_0001, and it is 2888500 sample intervals (6 hours, 15 minutes, and 8 seconds, at 125 samples per second) in duration. At the end of the master header file, a comment ( # Location: nicu ) specifies the ICU in which the recording was made (the neonatal ICU , in this case). The layout header file for this record ( 31/3141595/3141595_layout.hea ) indicates that five ECG signals (I, II, III, AVR, and “V”), a respiration signal, and a PPG signal are available during portions of the record. (The five ECG signals are not all available simultaneously.) The header file for the first segment of this record ( 31/3141595/3141595_0001.hea ) shows that a PPG signal (“PLETH”), a respiration signal, and ECG leads II and AVR are available throughout this initial segment.

The first line of the master header file for waveform record 314595 ( 31/3141595/3141595.hea ) indicates that the record is 242353557 sample intervals (about 22 days at 125 samples per second) in duration, and that it contains 427 segments and gaps. (See header(5) in the WFDB Applications Guide for details on the format of this text file.) The first segment is named 3141595_0001, and it is 2888500 sample intervals (6 hours, 15 minutes, and 8 seconds, at 125 samples per second) in duration. At the end of the master header file, a comment ( # Location: nicu ) specifies the ICU in which the recording was made (the neonatal ICU , in this case).

The layout header file for this record ( 31/3141595/3141595_layout.hea ) indicates that five ECG signals (I, II, III, AVR, and “V”), a respiration signal, and a PPG signal are available during portions of the record. (The five ECG signals are not all available simultaneously.)

The header file for the first segment of this record ( 31/3141595/3141595_0001.hea ) shows that a PPG signal (“PLETH”), a respiration signal, and ECG leads II and AVR are available throughout this initial segment.

The matching numerics record is named 3141595n, and its header file ( 31/3141595/3141595n.hea ) shows that it is 1938730 sample intervals (about 22 days at 1 sample per second) in duration, and that it contains heart rate (“HR”, which is measured from the ECG , as well as “PULSE”, measured from one or more pulsatile signals), noninvasive blood pressure (raw as well as systolic, diastolic, and mean), respiration rate, and SpO 2 .

Any WFDB application can read any waveform record from this database directly from the PhysioNet web server (i.e., without downloading the record first) using a record name of the form mimic3wdb/3 x /3 xyyyyy / . Numerics records can be read using the longer form mimic3wdb/3 x /3 xyyyyy /3 xyyyyy n (note that the final 3 xyyyyy must be repeated and followed by n to specify the numerics record).

For example, if you have installed the WFDB Software Package , you can read the first 10 seconds of waveform record 3141595 using this rdsamp command:

To read the first 10 seconds of the matching numerics record 3141595n, use this command instead:

Notice that the first command produces 1250 samples of each waveform (125 samples per second, for 10 seconds), but the second command produces only 10 samples of each vital sign (1 sample per second, for 10 seconds).

Version 1.0 of the MIMIC-III Waveform Database supersedes previously-released versions of the MIMIC-II Waveform Database. The numbered records (3000003 to 3999988) are identical to those in version 3.2 of the MIMIC-II Waveform Database. The Matched Subset , however, uses different subject IDs and surrogate dates, corresponding to version 1.4 of the MIMIC-III Clinical Database .

We wish to thank Philips Healthcare, as well as the Beth Israel Deaconess Medical Center, for their invaluable support in making this project possible.

Many people have contributed to this project over the past 18 years, and it would be impossible to list them all. In particular, we would like to acknowledge Michael Craig, Tin Kyaw, and Mohammed Saeed, for their efforts in collecting and organizing the original MIMIC-II Waveform Database, upon which this database is based.

The authors have no conflicts of interests to declare.

Johnson, A. E. W., Pollard, T. J., Shen, L., Lehman, L. H., Feng, M., Ghassemi, M., Moody, B., Szolovits, P., Celi, L. A., & Mark, R. G. (2016). MIMIC-III, a freely accessible critical care database. Scientific Data, 3, 160035. https://dx.doi.org/10.1038/sdata.2016.35

8381 publications cite this project.
    The most recent are listed below.

Lightweight Calibration-Based Blood Pressure Tracking from Photoplethysmography Features for Smart Devices: Accuracy, Model Size and Recalibration Interval Soojeong Lee, Mugahed A. Al–antari, Gangseong Lee. Diagnostics ,
        2026.

Transformer architectures scaling laws and in context learning in foundation models Mebrahatom Yihdego Mekonen, Abrham Mamu Abebe, Gebrekiros Gebreyesus Gebremariam et al. Discover Artificial Intelligence ,
        2026.

Acute kidney injury and in-hospital mortality in critically ill patients with gynecologic malignancies: a retrospective cohort study across three intensive care databases wenjing liu, Teng Liu, Caihong Lv. Research Square ,
        2026.

Explainable time-series machine learning for early sepsis prediction and risk stratification: a multi-dataset computational study Agostino Aiezzo, Martina Falasca, Silvia Spoto et al. Research Square ,
        2026.

MedDP : A Graph‐Based Large Language Disease Prediction Model Ran Wang, Guilin Qi. Expert Systems ,
        2026.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

Download with the PhysioNet Python package : physionet download mimic3wdb --version 1.0

Download the files using your terminal: wget -r -N -c -np https://physionet.org/files/mimic3wdb/1.0/

To download the files using AWS command line tools, first configure your AWS credentials .
