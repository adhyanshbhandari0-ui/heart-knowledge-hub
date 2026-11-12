# RadQA

**Source:** https://physionet.org/content/radqa/1.0.0

---

RadQA: A Question Answering Dataset to Improve Comprehension of Radiology Reports

Soni, S., & Roberts, K. (2022). RadQA: A Question Answering Dataset to Improve Comprehension of Radiology Reports (version 1.0.0). PhysioNet . RRID:SCR_007345. https://doi.org/10.13026/ckkp-6y19

Soni, S., Gudala, M., Pajouhi, A., & Roberts, K. (2022, June). RadQA: A Question Answering Dataset to Improve Comprehension of Radiology Reports. In Proceedings of the Thirteenth Language Resources and Evaluation Conference (pp. 6250-6259). https://aclanthology.org/2022.lrec-1.672

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

We present a radiology question answering dataset, RadQA, with 3074 questions posed against radiology reports and annotated with their corresponding answer spans (resulting in a total of 6148 question-answer evidence pairs) by physicians. The questions are manually created using the clinical referral section of the reports that take into account the actual information needs of ordering physicians and eliminate bias from seeing the answer context (and, further, organically create unanswerable questions). The answer spans are marked within the Findings and Impressions sections of a report. The dataset aims to satisfy the complex clinical requirements by including complete (yet concise) answer phrases (which are not just entities) that can span multiple lines. In published work, we conducted a thorough analysis of the proposed dataset by examining the broad categories of disagreement in annotation (providing insights on the errors made by humans) and the reasoning requirements to answer a question (uncovering the huge dependence on medical knowledge for answering the questions). In that work, the best-performing transformer language model achieved an F1 of 63.55 on the test set. However, the top human-level performance on this dataset is 90.31 (with an average human performance of 84.52), which demonstrates the challenging nature of RadQA that leaves ample scope for future method research.

Machine reading comprehension (MRC) has been widely explored to better comprehend unstructured text, by enabling machines to answer specific questions given a textual passage [1]. Much of these pursuits are powered by neural models and since a well-constructed dataset is pivotal to building a suitable model (for a given requirement, domain, or task) there is an explosion of MRC datasets in recent years [2]. However, little work is drawn toward the clinical domain to build challenging MRC datasets for improving comprehension of the semantically complex and diverse electronic health record (EHR) data.

The current MRC datasets for unstructured EHR data fall short of many important considerations in order to build an advanced model for the task. Most of these datasets are too small (to build advanced models) [3] or publicly unavailable (making them nonexistent for building any models) [4] or both [5,6]. Additionally, the questions for most of these datasets are collected in a manner that induces bias and does not reflect real-world user needs, including for an available dataset where the users are shown candidate questions (with answers) for reference [7]. Lastly, one of the “large” EHR MRC datasets, emrQA [8], has gained much traction. However, the variety in emrQA is severely limited due to templatization, as is also found in a separate systematic analysis of emrQA’s MRC data. Furthermore, almost all existing datasets for EHR MRC use discharge summaries as documents. However, other types of clinical texts such as radiology reports (that have vastly different semantic content and vocabulary) are markedly underrepresented in the MRC task.

We propose RadQA, a new EHR MRC dataset, that aims to overcome the issues with the existing resources for the MRC task in the clinical domain. The questions reflect the true information needs of clinicians ordering radiology reports (as the queries are inspired by the clinical referral section of the radiology reports). The answers are oftentimes present in the form of phrases or span multiple lines (as opposed to only multi-word answer entities in available MRC datasets), fulfilling the clinical information needs. The questions require a wide variety of reasoning and domain knowledge to answer, which makes it a challenging dataset for training advanced models

We source the radiology reports (used as documents) for our dataset from the MIMIC-III database [9] . We sample a realistic set of reports by selecting the documents at the patient level, i.e., we first sampled 100 patients and then included all the 1009 associated radiology reports in our dataset for annotations. We further divide our data of 100 patients into training, development, and testing splits in the ratio of 8:1:1, respectively.

The ordering physicians include their requirements in the form of a clinical referral that is sent to the radiologist along with the radiographs. The annotators were asked to create questions thinking about both implicit and explicit information needs expressed by the referral section. Our annotators possess the medical knowledge to understand both the types of information needs in the referral and thus were able to incorporate those needs into their created questions.

Two annotators independently constructed questions for all the reports in our dataset. All the questions are associated with the report whose clinical referral section was used while constructing them. Finally, the questions are deduplicated at the report level.

For marking answers, the annotators were shown the whole radiology report (including the referral) along with the corresponding set of questions. There are two main sections in radiology reports, namely, Findings and Impressions. We tasked the annotators to annotate answer spans in the report text, at most one span each in the Findings and Impressions sections. We instructed them to annotate the shortest possible span that answers a question to the point. Specifically, the selected answer span should be sufficient by itself to answer the question but, simultaneously, it should not contain any additional information that is not required by the question.

Because the questions are not constructed after viewing the full report text or deciding an answer in advance, they may not have direct answers in the report. Further, owing to the question creation phase, all the questions in our dataset are not required to have answers in the report. All the answers are marked by two annotators independently and reconciled at regular intervals.

We adjudicated the annotated answers frequently in order to ensure the quality of our dataset. For the first 100 reports, we reconciled in batches of 10, giving both annotators sufficient time to ramp up on the annotation scheme. Afterward, we reconciled in batches of 100 reports. We calculate inter-annotator agreement using the F1 measure.

We reconciled all the answer spans down to one unique answer for our training split. For the dev and test splits, however, as long as both the annotated spans answered the question at hand, we kept both answers in the dataset. This facilitates a natural development and evaluation of models which respects the presence of more than one way of answering a question

The following is an example report in the dataset with a question and its answers in both the Findings and Impressions sections of Radiology Reports.

INDICATION: XX year old male with status post recent STE MI. Now with increasing edema and shortness of breath.

AP supine single view of the chest is compared to [**2101-3-24**].

FINDINGS: The heart is enlarged in size but stable in the interval. Mediastinal contour is unchanged. There is upper zone redistribution of the pulmonary artery vasculature. Perihilar haziness as well as diffuse bilateral pulmonary opacities. These findings are consistent with acute CHF. There are also bilateral pleural effusions. There is barium in the left colon from previous contrast study.

IMPRESSION: 1. Findings consistent with pulmonary edema due to CHF. 2. Bilateral pleural effusions.

The dataset is formatted as a json file which follows the structure of SQuAD, a popular open-domain MRC dataset. The following excerpt from the dataset file contains annotations for the above example question-answer pairs.

The dataset is split into training, development, and testing sets at the patient level (in the ratio of 8:1:1) for a realistic evaluation. The following files are included.

The descriptive statistics of the sampled radiology reports and those in MIMIC-III (after removing outlier patients) are presented below. The top modalities are determined separately after filtering out the report types with proportions less than 0.1%.

Following are the descriptive statistics of RadQA (with emrQA for comparison). Lengths are in tokens. UnAns – Unanswerable. Med – Median.

The RadQA dataset can be used to train machine comprehension models to enable answering a question given a radiology report text. The dataset contains predefined training, development, and testing splits, making it easier to compare the results.

The authors have no ethical concerns to declare.

This work was supported by the U.S. National Library of Medicine, National Institutes of Health, (R00LM012104); the National Institute of Biomedical Imaging and Bioengineering (R21EB029575); and UTHealth Innovation for Cancer Prevention Research Training Program Predoctoral Fellowship (CPRIT RP210042).

The authors have no conflicts of interest to declare.

Zeng C, Li S, Li Q, Hu J, Hu J. A Survey on Machine Reading Comprehension—Tasks, Evaluation Metrics and Benchmark Datasets. Appl Sci. 2020 Jan;10(21):7640.

Dzendzik D, Foster J, Vogel C. English Machine Reading Comprehension Datasets: A Survey. In: Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing. Online and Punta Cana, Dominican Republic: Association for Computational Linguistics; 2021. p. 8784–804.

Fan J. Annotating and Characterizing Clinical Sentences with Explicit Why-QA Cues. In: Proceedings of the 2nd Clinical Natural Language Processing Workshop. Minneapolis, Minnesota, USA: Association for Computational Linguistics; 2019. p. 101–6.

Raghavan P, Patwardhan S, Liang JJ, Devarakonda MV. Annotating Electronic Medical Records for Question Answering. arXiv:180506816. 2018 May 17.

Yue X, Jimenez Gutierrez B, Sun H. Clinical Reading Comprehension: A Thorough Analysis of the emrQA Dataset. In: Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics. Online: Association for Computational Linguistics; 2020. p. 4474–86.

Oliveira LES, Schneider ETR, Gumiel YB, Luz MAP da, Paraiso EC, Moro C. Experiments on Portuguese Clinical Question Answering. In: Britto A, Valdivia Delgado K, editors. Intelligent Systems. Cham: Springer International Publishing; 2021. p. 133–45. (Lecture Notes in Computer Science).

Yue X, Zhang XF, Yao Z, Lin S, Sun H. CliniQG4QA: Generating Diverse Questions for Domain Adaptation of Clinical Question Answering. ArXiv201016021 Cs. 2020 Nov 4.

Pampari A, Raghavan P, Liang J, Peng J. emrQA: A Large Corpus for Question Answering on Electronic Medical Records. In: EMNLP. Brussels, Belgium: Association for Computational Linguistics; 2018. p. 2357–68.

Johnson AEW, Pollard TJ, Shen L, Lehman L wei H, Feng M, Ghassemi M, et al. MIMIC-III, a freely accessible critical care database. Sci Data. 2016 May 24;3(1):160035.

3 publications cite this project.
    The most recent are listed below.

Exploring the Trade-Offs: Unified Large Language Models vs Local Fine-Tuned Models for Highly-Specific Radiology NLI Task Zihao Wu, Lu Zhang, Chao Cao et al. IEEE Transactions on Big Data ,
        2025.

Towards Efficient Methods in Medical Question Answering using Knowledge Graph Embeddings Saptarshi Sengupta, Connor Heaton, Suhan Cui et al. IEEE International Conference on Bioinformatics and Biomedicine (BIBM) ,
        2024.

StatMetaQA: A dataset for closed domain question answering in Indonesian statistical metadata Nur Rachmawati, Evi Yulianti. Data in Brief ,
        2024.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

sign the data use agreement for the project
