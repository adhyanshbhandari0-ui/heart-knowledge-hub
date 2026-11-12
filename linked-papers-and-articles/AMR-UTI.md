# AMR-UTI

**Source:** https://physionet.org/content/antimicrobial-resistance-uti/1.0.0

---

AMR-UTI: Antimicrobial Resistance in Urinary Tract Infections

Michael Oberst , Soorajnath Boominathan , Helen Zhou , Sanjat Kanjilal , David Sontag

Oberst, M., Boominathan, S., Zhou, H., Kanjilal, S., & Sontag, D. (2020). AMR-UTI: Antimicrobial Resistance in Urinary Tract Infections (version 1.0.0). PhysioNet . RRID:SCR_007345. https://doi.org/10.13026/se6w-f455

Kanjilal S., Oberst M., Boominathan S., Zhou H., Hooper D.C., Sontag D. (2020). A decision algorithm to promote outpatient antimicrobial stewardship for uncomplicated urinary tract infection. Science Translational Medicine, Volume 12, Issue 568. http://doi.org/10.1126/scitranslmed.aay5067

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

AMR-UTI is a freely accessible dataset, derived from electronic health record (EHR) information on over 80,000 patients with urinary tract infections (UTI) treated at Massachusetts General Hospital and Brigham & Women's Hospital in Boston, MA, USA between 2007 and 2016.

Each observation in the dataset corresponds to a urine specimen sent to the clinical microbiology laboratory to assess for antimicrobial resistance (AMR).  Each observation includes (1) the antimicrobial susceptibility profile, (2) the empiric antibiotic treatment decision, which is made without knowledge of the susceptibility testing results, and (3) patient and specimen features useful for prediction of AMR.

Urinary tract infections (UTIs) represent one of the most common complaints faced by healthcare providers in inpatient and outpatient settings. It is a common indication for antibiotic treatment, but overuse of broad spectrum therapies has selected for antimicrobial resistant pathogens. With this in mind, clinicians send urine specimens to the microbiology laboratory to conduct antibiotic susceptibility testing.

The receipt of definitive data from the microbiology laboratory, however, can take as long as 72 hours to return, and an antibiotic must be chosen in the meantime. This situation is referred to as empiric antibiotic treatment. When selecting an antibiotic therapy, providers must balance between the goal of using narrow spectrum antibiotics, while avoiding inappropriate antibiotic therapy (the selection of an antibiotic to which the patient is resistant).

This dataset is designed to support the development of algorithms to guide empiric treatment decisions in the context of uncomplicated UTIs, helping providers to choose effective antibiotics while avoiding the overuse of broad spectrum therapies.

Because antibiotic susceptibility testing provides a proxy for counterfactual outcomes under different treatments, this dataset supports the development and validation of causal inference and policy learning methods more broadly. To support the study of transfer learning, we also include a broader cohort of more complicated UTIs.

The primary focus of this dataset is the study of uncomplicated UTIs, and the prescription of commonly used antibiotics in this context: Nitrofurantoin (NIT), trimethoprim-sulfamethoxazole (SXT), ciprofloxacin (CIP), and levofloxacin (LVX).

Uncomplicated UTIs are defined as specimens where the infection site was specified to be urinary, and the following criteria are met:

No diagnosis indicating pregnancy in past 90 days.

No indication of pyelonephritis, based on string matching of "pyelo" to diagnosis names.

Exactly one antibiotic in (NIT, SXT, LVX, CIP) prescribed.

All AMR test results for NIT, SXT, LVX, CIP are available.

* Selected procedures used to exclude specimens are as follows: (i) placement of a central venous catheter (CVC), (ii) mechanical ventilation, (iii) parenteral nutrition, (iv) hemodialysis, and (v) any surgical procedure.

The entire dataset additionally includes a broader set of urine specimens that do not satisfy the above conditions. This broader cohort includes many patients who have complex infections that might be treated with a range of antibiotics. The specimens that meet our definition of an “uncomplicated UTI” are marked with the binary indicator "uncomplicated" in the relevant CSV files .

Multiple microbiology specimens can be taken from a single suspected site of infection. To mimic the empiric treatment setting, we restrict to the first specimen from an infection and exclude any specimens taken within a 14 day period from the same body site as duplicates. Specimens taken on the same day are merged or kept separate, depending on whether they come from the same or different body sites (respectively).

Note that while we will commonly refer to "specimens" in the remainder of the documentation, this should be taken to include both single specimens, as well as multiple specimens that have been merged (as described above) into a single observation.

We define the empiric antibiotic prescription as any antibiotic medication prescribed two days before, to one day after, the specimen was collected. As noted above, the uncomplicated UTI cohort contains specimens for which exactly one antibiotic in (NIT, SXT, LVX, CIP) was prescribed in this window. For uncomplicated UTIs, the vast majority of these prescriptions are observed on the same day as the specimen (91.1%) or the day after (8.0%), with a small fraction occurring on the day before (0.8%) or two days before (0.1%).

The medical record contains microbiological testing results for all specimens sent to the labs at Massachusetts General Hospital (MGH) and Brigham & Women's Hospital (BWH). This raw data includes the identity of the infecting pathogen and susceptibility testing to various antibiotics. The data contains the metric used for each test (minimum inhibitory concentration (MIC) vs. disk diameter (DD)) and the numeric value of the corresponding test result, as well as the date and location of specimen collection.

For this dataset release, we have transformed these numeric results into categorical phenotypes by applying the published 2017 CLSI clinical breakpoints [CSLI, 2017], which convert the raw semi-quantitative and quantitative results into one of three phenotypes: susceptible (S), intermediate (I), and resistant (R). We treat both intermediate and resistant phenotypes as resistant, which is generally how they are treated in clinical practice.

A unique example_id is assigned to each specimen, and was generated randomly. This is used to link between the various CSV files.

No dates or times are included in this dataset, and age is censored so that any individual with an age >89 is recorded as having an age of 90.

Any binary feature with all positive examples coming from fewer than 20 unique patients is dropped. All colonization pressure features (see "Data Description") are rounded to the nearest 0.01.

This dataset was divided into a training and a test set, based on years. All entries marked with is_train are in the training set, and others are in the test set. These were constructed such that:

All training specimens are in the years 2007-2013.

All test specimens are in the years 2014-2016.

There are no patients from the uncomplicated UTI cohort who have specimens in both train/test.

In the uncomplicated UTI cohort, there are 3629 unique patients in the test set, and 10053 unique patients in the training set. In total, the specimens in the test dataset are derived from 26807 patients, and in the training set from 55078 patients.

This study was approved by the Institutional Review Board (IRB) of Massachusetts General Hospital with a waived requirement for informed consent.

There are three main data files in CSV format included with this dataset:

all_uti_resist_labels.csv : Contains resistance testing results for the most common antibiotics used for UTI infections (nitrofurantoin (NIT), trimethoprim-sulfamethoxazole (SXT), ciprofloxacin (CIP), and levofloxacin (LVX)) for all specimens in our UTI cohort.

all_prescriptions.csv : Contains empiric clinician prescription selections for specimens in the uncomplicated UTI cohort only . By construction, our uncomplicated cohort is filtered to only contain specimens for which clinicians treated the infection with exactly one treatment in { NIT, SXT, CIP, LVX } in the empiric treatment window. We do not include prescriptions for the other specimens in the dataset, as clinicians may have treated other specimens with multiple antibiotics, or with antibiotics from outside this set.

all_uti_features.csv : Contains constructed features for all specimens. Also contains columns indicating membership of each specimen in training vs. test set and membership in the uncomplicated UTI cohort.

We also include a data dictionary file ( data_dictionary.csv ) for all of the columns in the files above. This data dictionary has five columns: file / column give the relevant file and column name, description gives additional information, and from / until indicate the window (if applicable) over which the feature is calculated. For instance, if from is 14 and until is 7, this indicates that the feature is calculated over the window of 14 days prior to specimen collection, up to 7 days prior to specimen collection. All windows are inclusive.

example_id : Unique specimen ID used to link between files.

NIT : Binary indicator of resistance to nitrofurantoin ( 1 if resistant).

SXT : Binary indicator of resistance to trimethoprim-sulfamethoxazole ( 1 if resistant).

CIP : Binary indicator of resistance to ciprofloxacin ( 1 if resistant).

LVX : Binary indicator of resistance to levofloxacin ( 1 if resistant).

is_train : Used to denote membership in training set (2007-13).

uncomplicated : Used to denote membership in uncomplicated UTI cohort.

Note that if no test result is available for a given antibiotic in (NIT, SXT, CIP, LVX), then the corresponding column will be empty.

example_id : Unique specimen ID used to link between files.

prescription : Observed empiric prescription (one of NIT,SXT,CIP,LVX).

is_train : Used to denote membership in training set (2007-13).

This section contains a detailed descriptions of the feature columns found in all_uti_features.csv .

This section also includes notes on how missing data is handled, when it is not implicit in the definition: For instance, most features are binary indicators, with a 1 indicates the presence of an observed element (e.g., a previous infection) and a 0 indicates that an element was not observed, and covers cases where data might be missing.

First, we note that the following columns are included in this file, which are defined similarly as in the other files:

example_id : Unique specimen ID used to link between files.

is_train : Used to denote membership in training set (2007-13).

uncomplicated : Used to denote membership in uncomplicated UTI cohort.

Each feature in this category conveys basic demographic information:

demographics - age : Patient age (in years) at time of specimen collection, calculated using recorded date of birth. All ages >= 90 are clipped and set to 90. There are no missing values for this feature.

demographics - is_white : Binary indicator for whether patient is white ( 1 ) or non-white ( 0 ). If race is not recorded (which occurs in 3% of specimens), this feature is 0 .

demographics - is_veteran : Binary indicator for whether patient is a veteran ( 1 ) or non-veteran ( 0 ). If veteran status is not recorded, this feature is 0 .

Each feature in this category is a binary indicator for whether a patient had a resistant test result to a particular antibiotic in a specified time window preceding the current specimen. These column names are of the form:

micro - prev resistance [ANTIBIOTIC] [TIME WINDOW] .

For each antibiotic, we construct binary features for prior resistance in the 14, 30, 90, and 180 days preceding specimen collection, as well as any record of prior resistance to this treatment (in which case ALL is used for [TIME WINDOW]). Previous resistance within fewer than 7 days is excluded from these features, to prevent label leakage.

Antibiotic names are given as abbreviations, in accordance with those established by the American Society for Microbiology ( link ).

Note that a 0 for these variables implicitly includes instances where data is missing. For instance, a 0 for micro - prev resistance SXT 90 could indicate that an antibiotic resistance test was done and that the infection was found to be susceptible, or that no test results exist for this patient in that time window.

Each feature in this category is a binary indicator for whether a patient was treated with a particular antibiotic or class of antibiotic in a specified time window preceding the current specimen. These column names are of the form:

medication [TIME WINDOW] - [ANTIBIOTIC] .

ab subtype [TIME WINDOW] - [ANTIBIOTIC SUBCLASS] .

ab class [TIME WINDOW] - [ANTIBIOTIC CLASS] .

For each antibiotic, we construct features for prior exposure in the 7, 14, 30, 90, and 180 days preceding specimen collection, as well as any record of prior exposure to this treatment (in which case ALL is used for [TIME WINDOW]). Previous exposure within fewer than 2 days is excluded from these features, to prevent leakage of the empiric treatment decision.

Each feature in this category is a binary indicator for whether a patient was previously infected with a specific pathogen in a time window preceding the current specimen. These column names are of the form:

micro - prev organism [PATHOGEN NAME] [TIME WINDOW] .

For each pathogen of interest, we construct features for prior infection in the 14, 30, 90, and 180 days preceding specimen collection. Prior infecting organisms within fewer than 7 days are excluded from these features, to prevent leakage of the current infecting organism.

Each feature in this category is a binary indicator for whether a patient was previously diagnosed with a given comorbidity in a time window preceding the current specimen. We use the comorbidities that comprise the Elixhauser Comorbidity Index [Quan et al. 2015], and extracted these from ICD-9 and ICD-10 codes using the icd package in R. These column names are of the form:

comorbidity [TIME WINDOW] - [COMORBIDITY NAME] .

For each comorbidity of interest, we construct features for prior infection in the 7, 14, 30, 90, and 180 days preceding specimen collection. This includes comorbidities recorded up until the date of specimen collection (inclusive).

Each feature in this category is a binary indicator for whether the current specimen was collected in a specific department of the hospital; there is a feature for collection in inpatient (IP) settings, outpatient (OP) settings, ER, or the ICU. These binary features are included as:

Note that due to the filtering and merging of different specimens (see "Filtering and Merging of Specimens" in the methods section) into a single sample, it is possible to see multiple hospital departments for the same infection.

When no hospital department is recorded, all of these features will be 0 .

We define the colonization pressure of an antibiotic as the rate of resistance to that agent within a specified location and time period. We compute the colonization pressure for a given specimen as the proportion of all urinary specimens resistant to an antibiotic in the period ranging from 7 days before to 90 days before the date of specimen collection.

We compute colonization pressure at three location hierarchies, across 25 antibiotics. These column names are of the form:

selected micro - colonization pressure [ANTIBIOTIC] 90 - [granular level] : Resistance rate across specimens collected at the same floor/ward/clinic.

selected micro - colonization pressure [ANTIBIOTIC] 90 - [higher level] : Resistance rate across specimens collected at the same hospital (MGH or BWH) and department type (inpatient, outpatient, ICU, ER).

selected micro - colonization pressure [ANTIBIOTIC] 90 - [overall] : Resistance rate across all specimens.

Antibiotic names are given as abbreviations, in accordance with those established by the American Society for Microbiology ( link ).

When there are no previous visits to the given location in the given time window, these features will default to 0 .

We also include a feature for whether or not a patient has been to a skilled nursing facility in the past 7, 14, 30, and 90 days. Thus custom feature is included as:

These are defined as either of the following: (a) CPT code in the range 99304-99318, or (b) "nursing facility" included in the procedure description.

All specimens in this dataset are from the urinary tract. However, some patients have other specimens collected (on the same day as the urinary specimen) from other infection sites. We encode this information using the binary features included as:

Each feature in this category is a binary indicator for whether a patient previously received a specific procedure in a time window preceding the current specimen. For each procedure of interest, we construct binary indicators for the presence of each procedure in the window of 0 - 180 days preceding specimen collection. This includes procedures up until the date of specimen collection (inclusive).

procedure 180 - had cvc : Placement of a central venous catheter (CVC), defined as either (a) CPT code in 36555-36598, (b) ICD9 code 38.97 or in 999.31-999.33, or (c) "central venous catheter" included in the procedure description.

procedure 180 - had surgery : Any surgical procedure, defined as either (a) CPT code in 10021-69990, or (b) "surgery" or "surgical" included in the procedure description.

procedure 180 - had mechanical ventilation : Mechanical ventilation, defined as "ventilation" included in the procedure description.

procedure 180 - had hemodialysis : Hemodialysis, defined as either (a) CPT code in 90935-90940 or (b) "hemodialysis" but not "than hemodialysis" included in the procedure description.

procedure 180 - had parenteral nutrition : Parenteral nutrition, defined as "parenteral" and "nutrition" included (in that order) in the procedure description.

Note: The uncomplicated UTI cohort is defined to exclude any specimen where any of these features are present in the past 90 days. Hence, these features should be interpreted as giving information on the window of 91-180 days for uncomplicated UTIs.

This dataset is a de-identified version of the dataset used in Kanjilal et al [3]. Detailed documentation is hosted on the project website clinicalml.org/data/amr-dataset , which also contains links to publications and software that make use of this dataset.

This work was supported by a Massachusetts General Hospital – Massachusetts Institute of Technology Grand Challenges Award (S.K., M.O., S.B., H.Z) and a National Science Foundation CAREER award #1350965 (S.B., D.S.). This work was also supported in part by Office of Naval Research Award No. N00014-17-1-2791 (M.O.). Finally, this work was also conducted with the support of a KL2 award (an appointed KL2 award) from Harvard Catalyst (S.K.) | The Harvard Clinical and Translational Science Center (National Center for Advancing Translational Sciences, National Institutes of Health Award KL2 TR002542). The content is solely the responsibility of the authors and does not necessarily represent the official views of Harvard Catalyst, Harvard University and its affiliated academic healthcare centers, or the National Institutes of Health.

The authors declare no conflicts of interest

H. Quan et al., “Coding algorithms for defining comorbidities in ICD-9-CM and ICD-10 Administrative Data,” Med. Care, vol. 43, no. 11, 2005.

CLSI. M100 performance standards for antimicrobial susceptibility testing. 2017.

Kanjilal S., Oberst M., Boominathan S., Zhou H., Hooper D.C., Sontag D. (2020). A decision algorithm to promote outpatient antimicrobial stewardship for uncomplicated urinary tract infection. Science Translational Medicine, Volume 12, Issue 568. http://doi.org/10.1126/scitranslmed.aay5067

4 publications cite this project.
    The most recent are listed below.

Prevalence of Antimicrobial Resistance Among the WHO’s AWaRe Classified Antibiotics Used to Treat Urinary Tract Infections in Diabetic Women Ahmad Hamdan, Mohannad Natheef AbuHaweeleh, Leena Al-Qassem et al. Antibiotics ,
        2024.

TransAMR: An Interpretable Transformer Model for Accurate Prediction of Antimicrobial Resistance Using Antibiotic Administration Data Mukunthan Tharmakulasingam, Wenwu Wang, Michael Kerby et al. IEEE Access ,
        2023.

Personalized antibiograms for machine learning driven antibiotic selection Conor K. Corbin, Lillian Sung, Arhana Chattopadhyay et al. Communications Medicine ,
        2022.

Probing automated treatment of urinary tract infections for bias Garrett H. Yoon, Vincent J. Major. ACM International Conference on Bioinformatics, Computational Biology, and Health Informatics (ACM-BCB) ,
        2021.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

sign the data use agreement for the project
