# HiRID

**Source:** https://physionet.org/content/hirid/1.1.1

---

HiRID, a high time-resolution ICU dataset

Martin Faltys , Marc Zimmermann , Xinrui Lyu , Matthias Hüser , Stephanie Hyland , Gunnar Rätsch , Tobias Merz

New on PhysioNet: the HiRID critical care dataset (June 5, 2020, 12:29 p.m.) We are pleased to announce the release of the HiRID critical care dataset, developed as part of a collaboration between Bern University Hospital and the Swiss Federal Institute of Technology (ETH). HiRID is a freely accessible critical care dataset containing data relating to more than 33 thousand admissions to the Department of Intensive Care Medicine of the Bern University Hospital, Switzerland, an interdisciplinary 60-bed unit admitting >6,500 patients per year.

We are pleased to announce the release of the HiRID critical care dataset, developed as part of a collaboration between Bern University Hospital and the Swiss Federal Institute of Technology (ETH). HiRID is a freely accessible critical care dataset containing data relating to more than 33 thousand admissions to the Department of Intensive Care Medicine of the Bern University Hospital, Switzerland, an interdisciplinary 60-bed unit admitting >6,500 patients per year.

Faltys, M., Zimmermann, M., Lyu, X., Hüser, M., Hyland, S., Rätsch, G., & Merz, T. (2021). HiRID, a high time-resolution ICU dataset (version 1.1.1). PhysioNet . RRID:SCR_007345. https://doi.org/10.13026/nkwc-js72

Hyland, S.L., Faltys, M., Hüser, M. et al. Early prediction of circulatory failure in the intensive care unit using machine learning. Nat Med 26, 364–373 (2020). https://doi.org/10.1038/s41591-020-0789-4 https://doi.org/10.1038/s41591-020-0789-4

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

HiRID is a freely accessible critical care dataset containing data relating to almost 34 thousand patient admissions to the Department of Intensive Care Medicine of the Bern University Hospital, Switzerland (ICU), an interdisciplinary 60-bed unit admitting >6,500 patients per year. The ICU offers the full range of modern interdisciplinary intensive care medicine for adult patients. The dataset was developed in cooperation between the Swiss Federal Institute of Technology (ETH) Zürich, Switzerland and the ICU.

The dataset contains de-identified demographic information and a total of 681 routinely collected physiological variables, diagnostic test results and treatment parameters from almost 34 thousand admissions during the period from January 2008 to June 2016. Data is stored with a uniquely high time resolution of one entry every two minutes.

Critical illness is characterized by the presence or risk of developing life-threatening organ dysfunction. Critically ill patients are typically cared for in intensive care units (ICUs), which specialize in providing continuous monitoring and advanced therapeutic and diagnostic technologies. This dataset was collected during routine care at the Department of Intensive Care Medicine of the Bern University Hospital, Switzerland (ICU), an interdisciplinary 60-bed unit admitting >6,500 patients per year. It was initially extracted to support a study on the early prediction of circulatory failure in the intensive care unit using machine learning [1].  The latest documentation for the dataset is available at hirid.intensivecare.ai [2].

The HiRID database contains a large selection of all routinely collected data relating to patient admissions to the Department of Intensive Care Medicine of the Bern University Hospital, Switzerland (ICU). The data was extracted from the ICU Patient Data Management System which is used to prospectively register patient health information, measurements of organ function parameters, results of laboratory tests and treatment parameters from ICU admission to discharge.

Measurements and settings of medical devices such as mechanical ventilation

Measurements and settings of medical devices such as mechanical ventilation

Observations by health care providers e.g.: GCS, RASS, urine and other fluid output

Observations by health care providers e.g.: GCS, RASS, urine and other fluid output

HiRID has a higher time resolution than other published datasets, most importantly for bedside monitoring with most parameters recorded every 2 minutes.

To ensure the anonymization of individuals in the data set, we followed the procedures successfully applied for the MIMIC-III and AmsterdamUMCdb dataset, which adopted the Health Insurance Portability and Accountability Act (HIPAA) Safe Harbor requirements and, in the case of AmsterdamUMCdb, also the European Union's General Data Protection Regulation (GDPR) standards [3,4].

Removal of all eighteen identifying data elements listed in HIPAA

Removal of all eighteen identifying data elements listed in HIPAA

Dates were shifted by a random offset such that the admission date lies between 2100 and 2200. We made sure to preserve the seasonality, time of day and the day of week.

Dates were shifted by a random offset such that the admission date lies between 2100 and 2200. We made sure to preserve the seasonality, time of day and the day of week.

Patient age, height and weight are binned into bins of size 5. For patient age, the max bin is 90 years and contains also all older patients.

Patient age, height and weight are binned into bins of size 5. For patient age, the max bin is 90 years and contains also all older patients.

Measurements and medications with changing units over time were standardized to the latest unit used. This standardization was necessary to make a conclusion about estimated admission times, based on the units used in a specific patient, impossible.

Measurements and medications with changing units over time were standardized to the latest unit used. This standardization was necessary to make a conclusion about estimated admission times, based on the units used in a specific patient, impossible.

k-anonymization was applied on patient age, weight, height and sex.

k-anonymization was applied on patient age, weight, height and sex.

The institutional review board (IRB) of the Canton of Bern approved the study. The need for obtaining informed patient consent was waived owing to the retrospective and observational nature of the study.

The overall data is available in two states: as raw data and/or as pre-processed data. Additionally there are three reference tables for variable lookup.

variable reference (*hirid_variable_reference.csv*) - reference table for variables (for raw stage)

variable reference (*hirid_variable_reference.csv*) - reference table for variables (for raw stage)

ordinal variable reference (*ordinal_vars_ref.csv*) - reference table for categorical/ordinal variables for string value lookup

ordinal variable reference (*ordinal_vars_ref.csv*) - reference table for categorical/ordinal variables for string value lookup

pre-processed variable reference (*hirid_variable_reference_preprocessed.csv*) - reference table for variables (for merged and imputed stage)

pre-processed variable reference (*hirid_variable_reference_preprocessed.csv*) - reference table for variables (for merged and imputed stage)

The raw data was only processed if this was necessary for patient de-identification and otherwise left unchanged compared to the original source. The source data contains the complete set of available variables (685 variables). It consists of the following tables:

The pre-processed data consists of intermediary pipeline stages from the accompanying publication by Hyland et al [1]. Source variables representing the same clinical concepts were merged into one meta-variable per concept. The data contains the 18 most predictive meta-variables only, as defined in our publication. Two different stages of the pipeline are available

Merged stage source variables are merged into meta-variables by clinical concepts e.g. non-opioid-analgesics. The time grid is left unchanged and is sparse.

Merged stage source variables are merged into meta-variables by clinical concepts e.g. non-opioid-analgesics. The time grid is left unchanged and is sparse.

Imputed stage the data from the merged stage is down sampled to a five-minute time grid. The time grid is filled with imputed values. The imputation strategy is complex and is discussed in the original publication.

Imputed stage the data from the merged stage is down sampled to a five-minute time grid. The time grid is filled with imputed values. The imputation strategy is complex and is discussed in the original publication.

The code used to generate these stages can be found in this GitHub repository under the preprocessing folder [5].

The pre-processed data is intended mainly as a quick way to jump-start a project or for use in a proof of concept. We recommend using the source data whenever possible for regular projects. It is the most flexible form and contains the complete set of variables in the original time resolution.

Data is available in two formats: CSV for wide compatibility and Apache Parquet for convenience and performance.

Since the data sets are fairly large, they are split into partitions, such that they can be processed in parallel in a straightforward way. The lookup table mapping patient id to partition id is provided in the file named {data_set}_index.csv along with the data. The partitions are aligned between the different data sets and tables, such that the data of a patient can always be found in the partition with the same id. Note however, that a patient may not occur in all data sets, e.g. a patient might be missing in the preprocessed data, because a patient didn't meet the demographic criteria to be included in the study.

The dataset treats each ICU admission uniquely and it is not possible to identify multiple ICU admissions as originating from the same patient. For each ICU (re-)admission a unique "Patient ID" is generated.

The schemata of every table can be found in the *schemata.pdf* file.

As the database contains detailed information regarding the clinical care of patients, it must be treated with appropriate care and respect.

Researchers are required to formally request access via PhysioNet. To be granted access, the user has to be a credentialed PhysioNet user, digitally sign the Data Use Agreement and provide a specific research question.

Changes from version 1.0: - Introduction of the discharge status (alive/dead/unknown) as a column in the general table - Corrected an issue with the unit of Troponin (Variable ID: 24000538, 24000806). Now all measurements have ng/l as unit. Some measurements had a wrong unit before.

The authors declare no conflicts of interest

HiRID GitHub Repository. http://github.com/ratschlab/circEWS/

AmsterdamUMCdb website and documentation. https://amsterdammedicaldatascience.nl/

HiRID Database website and documentation. https://hirid.intensivecare.ai/

Johnson, A., Pollard, T., Shen, L., Lehman, L., Feng, M., Ghassemi, M., Moody, B., Szolovits, P., Celi, L., & Mark, R. (2016). MIMIC-III, a freely accessible critical care database. Scientific data, 3, 160035.

Hyland, S.L., Faltys, M., Hüser, M. et al. Early prediction of circulatory failure in the intensive care unit using machine learning. Nat Med 26, 364–373 (2020). https://doi.org/10.1038/s41591-020-0789-4

523 publications cite this project.
    The most recent are listed below.

Medical status forecasting with Markov feature engineering for autocorrelated categorical response variable Xin Zhao, Chaozhi Yu, Xiaokai Nie. Computational Statistics ,
        2026.

Real-Time Machine Learning Model to Predict Cardiac Arrest Within 12 Hours in Critically Ill Patients (DeepiCARS): A Confirmatory Trial and External Validation Ukdong Gim, Leerang Lim, Kyung-Jae Cho et al. Diagnostics ,
        2026.

Development and Validation of a Mixture-of-Experts–Based Model for Postoperative In-Hospital Mortality Risk Assessment: Multicenter Retrospective Study Shixin Huang, Jinhong Xia, Xixi Nie et al. Journal of Medical Internet Research ,
        2026.

Beyond Structured Vitals: Semantic-Temporal Alignment for Full-Record ICU Risk Forecasting Zhichong Zheng, Xiaohang Nie, Xueqi Wang et al. ACM International Conference on Information and Knowledge Management (CIKM) ,
        2026.

Compact clinical features capturing organ history for dynamic prediction of organ deterioration in sepsis Luomeng Wang, Jialin Song, Marina Vereshchako et al. medRxiv ,
        2026.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

submit a request to the authors to use the data for your project
