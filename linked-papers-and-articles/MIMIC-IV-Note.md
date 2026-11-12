# MIMIC-IV-Note

**Source:** https://physionet.org/content/mimic-iv-note/2.2

---

MIMIC-IV-Note: Deidentified free-text clinical notes

Alistair Johnson , Tom Pollard , Steven Horng , Leo Anthony Celi , Roger Mark

Johnson, A., Pollard, T., Horng, S., Celi, L. A., & Mark, R. (2023). MIMIC-IV-Note: Deidentified free-text clinical notes (version 2.2). PhysioNet . RRID:SCR_007345. https://doi.org/10.13026/1n74-ne17

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

The advent of large, open access text databases has driven advances in state-of-the-art model performance in natural language processing (NLP). The relatively limited amount of clinical data available for NLP has been cited as a significant barrier to the field's progress. Here we describe MIMIC-IV-Note: a collection of deidentified free-text clinical notes for patients included in the MIMIC-IV clinical database. MIMIC-IV-Note contains 331,794 deidentified discharge summaries from 145,915 patients admitted to the hospital and emergency department at the Beth Israel Deaconess Medical Center in Boston, MA, USA. The database also contains 2,321,355 deidentified radiology reports for 237,427 patients. All notes have had protected health information removed in accordance with the Health Insurance Portability and Accountability Act (HIPAA) Safe Harbor provision. All notes are linkable to MIMIC-IV providing important context to the clinical data therein. The database is intended to stimulate research in clinical natural language processing and associated areas.

Free-text notes are integral to the care provided to patients in most health systems. Although digital information systems with structured forms for input have proliferated over the last few decades, providers continue to rely on free-text notes to communicate amongst themselves, relay important health related information to patients, and document information related to care plans [1]. For researchers, free-text notes are an important source of information for understanding a patient's clinical course. Investigations into public views on the use of patient data for research broadly suggest that there is a willingness to share data where it is for the common good [2]. This trend is held when considering free-text notes in particular [3, 4]. Despite both public and researcher desire to improve health through processing of clinical notes, lack of access to shared clinical text has slowed down progress [5]. The cost and complexity with deidentifying clinical text is often the major barrier to the creation of clinical text datasets. In contrast, the broad use of MIMIC-III for clinical natural language processing and demonstrates the potential for these datasets once deidentified. Recent advances in natural language processing have dramatically improved the capabilities of text processing models for a variety of tasks including named entity recognition. These improvements have been demonstrated to carry over to the deidentification of free-text notes, which can be cast as a named entity recognition task [6]. The advances of automatic deidentification of free-text clinical notes has made sharing of clinical notes for research possible in a manner that protects patient privacy and maximizes public benefit.

All inclusion criteria for MIMIC-IV also apply to MIMIC-IV-Note. In general, only notes occurring within one year of a patient encounter are included in the database, where an encounter is defined as an emergency department or hospital stay. Free-text notes were acquired from the hospital system and deidentified using a custom rule-based approach combined with a neural network trained for deidentification. Annotations from the two approaches were unioned, and identified instances of protected health information (PHI) were removed from the notes. Each instance of PHI was replaced with exactly three underscores. Previous work identified the sensitivity of the approach to be 99.9% for radiology reports [7]. A manual review of discharge summaries was also conducted, with no PHI found.

There are four tables in the dataset: discharge , discharge_detail , radiology , and radiology_detail . In general the name of the table refers to the domain of the note, and tables with a _detail suffix are entity-attribute-value tables with additional information relating to the free-text notes. Each table contains a note_id which uniquely identifies a note and is composed with the subject_id, the abbreviated note domain, and a sequential integer.

The discharge table contains discharge summaries for hospitalizations. Discharge summaries are long form narratives which describe the reason for a patient’s admission to the hospital, their hospital course, and any relevant discharge instructions. The discharge_detail table contains auxiliary information associated with discharge summaries, including a deidentified placeholder for the authors of the discharge summaries.

The radiology table contains free-text radiology reports associated with radiography imaging. Radiology reports cover a variety of imaging modalities: x-ray, computed tomography, magnetic resonance imaging, ultrasound, and so on. Free-text radiology reports are semi-structured and usually follow a consistent template for a given imaging protocol. For example, chest x-rays typically have four sections: indication, comparison, findings, and impression.

The radiology_detail table provides information associated with the imaging study. Current Procedural Terminology (CPT) codes, exam names, and links between parent reports and addendums are available in the table.

The notes are distributed as comma separated value (CSV) files. Each row corresponds to a unique note and has been assigned a unique note_id.

We have created an open source repository for the sharing of code and discussion of the database, referred to as the MIMIC Code Repository [8, 9]. The code repository provides a mechanism for shared discussion and analysis of all versions of MIMIC, including MIMIC-IV-Note.

MIMIC-IV-Note v2.2 was released in January 2023. Changes were only made to the project meta-data.

MIMIC-IV-Note v2.1 was the first publicly available version of the database.

The collection of patient information and creation of the research resource was reviewed by the Institutional Review Board at the Beth Israel Deaconess Medical Center, who granted a waiver of informed consent and approved the data sharing initiative.

Makam AN, Lanham HJ, Batchelor K, Samal L, Moran B, Howell-Stampley T, Kirk L, Cherukuri M, Santini N, Leykum LK, Halm EA. Use and satisfaction with key functions of a common commercial electronic health record: a survey of primary care providers. BMC medical informatics and decision making. 2013 Dec;13(1):1-7.

Stockdale J, Cassell J, Ford E. “Giving something back”: A systematic review and ethical enquiry into public views on the use of patient data for research in the United Kingdom and the Republic of Ireland. Wellcome open research. 2018;3.

Ford E, Stockdale J, Jackson R, Cassell J. For the greater good? Patient and public attitudes to use of medical free text data in research. International Journal of Population Data Science. 2017;1(1).

Ford E, Oswald M, Hassan L, Bozentko K, Nenadic G, Cassell J. Should free-text data in electronic medical records be shared for research? A citizens’ jury study in the UK. Journal of medical ethics. 2020 Jun 1;46(6):367-77.

Chapman WW, Nadkarni PM, Hirschman L, D'avolio LW, Savova GK, Uzuner O. Overcoming barriers to NLP for clinical text: the role of shared tasks and the need for additional creative solutions. Journal of the American Medical Informatics Association. 2011 Sep 1;18(5):540-3.

Johnson AE, Pollard TJ, Berkowitz SJ, Greenbaum NR, Lungren MP, Deng CY, Mark RG, Horng S. MIMIC-CXR, a de-identified publicly available database of chest radiographs with free-text reports. Scientific data. 2019 Dec 12;6(1):1-8.

Johnson AE, Bulgarelli L, Pollard TJ. Deidentification of free-text medical records using pre-trained bidirectional transformers. InProceedings of the ACM Conference on Health, Inference, and Learning 2020 Apr 2 (pp. 214-221).

Johnson AE, Stone DJ, Celi LA, Pollard TJ. The MIMIC Code Repository: enabling reproducibility in critical care research. Journal of the American Medical Informatics Association. 2018 Jan;25(1):32-9.

117 publications cite this project.
    The most recent are listed below.

Labeling Clinical Notes With Large Language Models: Retrospective Benchmarking Study Pritam Mukherjee, Michael Nazmifar, Vivek Batheja et al. Journal of Medical Internet Research ,
        2026.

MIMIC-Note-Extract: A Large-Scale Structured Dataset Extracted from MIMIC-IV-Note Discharge Summaries Kristian Schwethelm, Jonas Kuntzer, Conrad Ketzer et al. arXiv (Cornell University) ,
        2026.

Understanding clinical reasoning variability in medical large language models: a mechanistic interpretability study Mirage Modi, Jordan Edward Krull, Timothy D. Gauntner et al. npj Digital Medicine ,
        2026.

Blood pressure history improves near-term hypotension prediction and reassessment prioritisation in sepsis Luomeng Wang, Jiajun Zhu, Rongyang Zhou et al. medRxiv ,
        2026.

K-MIMIC and the next stage of multimodal critical care data Sangseok Lee. Korean Journal of Anesthesiology ,
        2026.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

sign the data use agreement for the project
