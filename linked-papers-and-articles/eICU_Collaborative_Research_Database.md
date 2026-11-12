# eICU Collaborative Research Database

**Source:** https://physionet.org/content/eicu-crd/2.0

---

Tom Pollard , Alistair Johnson , Jesse Raffa , Leo Anthony Celi , Omar Badawi , Roger Mark

Pollard, T., Johnson, A., Raffa, J., Celi, L. A., Badawi, O., & Mark, R. (2019). eICU Collaborative Research Database (version 2.0). PhysioNet . RRID:SCR_007345. https://doi.org/10.13026/C2WM1R

The eICU Collaborative Research Database, a freely available multi-center database for critical care research. Pollard TJ, Johnson AEW, Raffa JD, Celi LA, Mark RG and Badawi O. Scientific Data (2018). DOI: http://dx.doi.org/10.1038/sdata.2018.178 . https://www.nature.com/articles/sdata2018178

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

The eICU Collaborative Research Database is a multi-center database comprising deidentified health data associated with over 200,000 admissions to ICUs across the United States between 2014-2015. The database includes vital sign measurements, care plan documentation, severity of illness measures, diagnosis information, and treatment information. Data is collected through the Philips eICU program, a critical care telehealth program that delivers information to caregivers at the bedside.

Philips Healthcare has developed an eICU telehealth system for critically ill patients, which provides 24 hour support for caregivers at the bedside. It is a supplement — not a replacement — to the bedside team, and the data utilized by the remote caregivers is archived for research purposes. Here we describe the eICU Collaborative Research Database, a multi-center intensive care unit database covering over 200,000 admissions to ICUs monitored by eICU Programs across the United States. The database is deidentified, and includes vital sign measurements, care plan documentation, APACHE severity of illness measures, and diagnosis information and treatment details.

The eICU Collaborative Research Database is populated with data from a combination of many critical care units throughout the continental United States. Patients were selected for inclusion in the public database, by first identifying hospital discharges between 2014 and 2015. The proportion of index stays in each hospital from the full private data repository was used to perform a stratified sample of patient index stays based upon hospital. A small proportion of patients only had stays in step down units or low acuity units, and these stays were removed. The database comprises over 200 thousand patient unit encounters for over 139 thousand unique patients admitted between 2014 and 2015. Patients were admitted to one of 335 units at 208 hospitals located throughout the US.

All tables are deidentified to meet the safe harbor provision of the US Health Insurance Portability and Accountability Act (HIPAA). These provisions include the removal of all protected health information. Hospital and unit identifiers have also been removed to protect the privacy of contributing organizations. The schema was established in collaboration with Privacert (Cambridge, MA), who certified the re-identification risk as meeting safe harbor standards (HIPAA Certification no. 1031219-2).

Data include vital signs, laboratory measurements, medications, APACHE components, care plan information, admission diagnosis, patient history, time-stamped diagnoses from a structured problem list, and similarly chosen treatments. Data from each patient is collected into a common warehouse only if certain “interfaces” are available. Each interface is used to transform and load a certain type of data: vital sign interfaces incorporate vital signs, laboratory interfaces provide measurements on blood samples, and so on. It is important to be aware that different care units may have different interfaces in place, and that the lack of an interface will result in no data being available for a given patient, even if those measurements were made in reality. The data is provided as a relational database, comprising multiple tables joined by keys.

Accessing the data requires proof of completion of a course on human research and signing of a data use agreement. By sharing the data publicly, we seek to foster collaboration in secondary analysis of electronic health records. Detailed documentation is available online at: https://eicu-crd.mit.edu/. Jupyter Notebooks are shared alongside documentation to demonstrate analysis and exploration of the data. A collaboratively developed codebase for working with the data is available at: https://github.com/mit-lcp/eicu-code.

The eICU Collaborative Research Database (eICU-CRD) is provided through the work of researchers at the MIT Laboratory for Computational Physiology, Philips Healthcare, and our collaborators. We have limited resources and cannot provide individual support to researchers worldwide, so we encourage researchers to work together as a community. If you are seeking advice for a specific question, we would suggest raising an issue on the eICU Code Repository: https://github.com/mit-lcp/eicu-code/issues

The authors would like to thank the Philips eICU Research Institute and Philips Healthcare for contribution of the data. The authors would also like to thank Andrew A. Kramer for insightful comments regarding the data and Dina Demner-Fushman for helpful feedback on the deidentification process.

The work was supported by grants NIH-R01-EB017205, NIH-R01-EB001659, and NIH-R01-GM104987 from the National Institutes of Health. The MIT Laboratory for Computational Physiology received funding from Philips Healthcare to undertake work on the database described in this paper. O.B. is an employee of Philips Healthcare.

Pollard TJ, Johnson AEW, Raffa JD, Celi LA, Mark RG and Badawi O. The eICU Collaborative Research Database, a freely available multi-center database for critical care research. Scientific Data (2018). DOI: http://dx.doi.org/10.1038/sdata.2018.178.

121 publications cite this project.
    The most recent are listed below.

Aggregate results for a comparative study of 48-hour ICU readmission definitions Yuxuan Zhang. Zenodo (CERN European Organization for Nuclear Research) ,
        2026.

Delayed Hyperbilirubinemia Is Associated with Mortality in Hypoxic Hepatitis across Shock Etiologies: derivation and independent validation in two critical care databases Hideya Itagaki, Tomoyuki Endo.
        
        2026.

Predicting Persistent Creatinine Elevation After the First Recorded ICU Furosemide Event in Acute Heart Failure: A Retrospective Cohort Study Shuting Kong, Yibin Pan. Research Square ,
        2026.

Reproducible code for a comparative study of 48-hour ICU readmission definitions Yuxuan Zhang. Zenodo (CERN European Organization for Nuclear Research) ,
        2026.

A 13-Variable Hour-24 Model for 7-Day ICU Mortality in Neurocritical Care: Strong Cross-Database Discrimination with Unit-Level Calibration Differences Shuaijia Zeng, Zhang Xiaodong, Xing Cao et al. Research Square ,
        2026.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

sign the data use agreement for the project
