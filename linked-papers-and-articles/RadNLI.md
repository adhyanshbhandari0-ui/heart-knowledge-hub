# RadNLI

**Source:** https://physionet.org/content/radnli-report-inference/1.0.0

---

RadNLI: A natural language inference dataset for the radiology domain

Yasuhide Miura , Yuhao Zhang , Emily Tsai , Curtis Langlotz , Dan Jurafsky

Miura, Y., Zhang, Y., Tsai, E., Langlotz, C., & Jurafsky, D. (2021). RadNLI: A natural language inference dataset for the radiology domain (version 1.0.0). PhysioNet . RRID:SCR_007345. https://doi.org/10.13026/mmab-c762

Miura, Y., Zhang, Y., Tsai, E., Langlotz, C., & Jurafsky, D. (2021). Improving Factual Completeness and Consistency of Image-to-Text Radiology Report Generation. In Proceedings of NAACL-HLT 2021. https://www.aclweb.org/anthology/2021.naacl-main.416/

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

The problem of natural language inference (NLI) determines whether a natural language hypothesis can be justifiably inferred from a natural language premise. NLI has attracted researchers to benchmark it in a number of settings including medical ones. While NLI datasets such as the MedNLI dataset exist for the clinical domain, systems trained with them do not generalize well to applications that require understanding of radiology reports. We therefore introduce an NLI dataset in the radiology domain, in which NLI information is annotated on sentences drawn from radiology reports. Sentence pairs in our dataset are sampled from MIMIC-CXR and we annotated them with NLI labels by two experts: one medical expert and one computer science expert. Each pair is annotated twice, swapping its premise and hypothesis, resulting in 960 pairs. The set is then split in half, resulting in 480 pair for a validation set and 480 pairs for a test set. We confirmed that a BERT-based NLI model trained with a distant supervision approach can achieve the accuracy of 77.8% on this test set.

Natural language inference (NLI) in natural language processing is the task determining a systems ability to understand language beyond simple word or character matches. Recently, NLI has achieved attention for evaluating the factual correctness in natural language generation (NLG) [1, 2]. An important new application of NLG is to build assistive systems that take radiology images of a patient and generate a textual report describing clinical observations in the images. While NLI datasets such as the MedNLI dataset [3] exist for the clinical domain, systems trained with them do not generalize well to applications that require understanding of radiology reports.

Automatic radiology report generation systems have achieved promising performance as measured by widely used NLG metrics such as CIDEr and BLEU. However, reports that achieve high performance on these NLG metrics are not always factually complete or consistent. To improve the factual consistency of generated reports, we have worked to construct an NLI dataset that can be used to evaluate the performance of an NLI model in the radiology domain. Sentence pairs in our dataset are sampled from MIMIC-CXR [4,5] and we annotated them with NLI labels by two experts: one medical expert and one computer science expert. We confirmed that a BERT-based NLI model [6] trained with a distant supervision approach can achieve the accuracy of 77.8% on this test set [7].

We sampled 480 sentence pairs that satisfy the following conditions from the validation section of MIMIC-CXR [2,3]:

Two sentences ( s 1 s_1 and s 2 s_2 ) have s i m ( s 1 , s 2 ) ≥ 0.5 sim(s_1, s_2) \ge 0.5

Two sentences ( s 1 s_1 and s 2 s_2 ) have s i m ( s 1 , s 2 ) ≥ 0.5 sim(s_1, s_2) \ge 0.5

MedNLI labels are equally distributed over three labels: entailment, neutral, and contradiction

MedNLI labels are equally distributed over three labels: entailment, neutral, and contradiction

We used BERTScore [8] as the above similarity function sim . These conditions are introduced to reduce neutral pairs since most pairs will be neutral with random sampling. The sampled pairs are annotated twice—swapping their premise and hypothesis—by two experts: one medical expert and one computer science expert. For pairs that the two annotators disagreed, the labels are decided by discussion between the two labelers and one additional computer science expert. The resulting 960 bidirectional pairs are split in half to give 480 pairs for a validation set and 480 pairs for a test set. More detailed descriptions of the dataset construction process can be found in the original publication [7].

radnli_dev_v1.jsonl : The development set.

Each line in the development/test set is a json consisting of the following keys:

gold_label : The NLI label in one of entailment, contradiction, or neutral.

The three NLI labels are defined as followings:

entailment : The hypothesis can be inferred from the premise.

contradiction : The hypothesis can NOT be inferred from the premise.

neutral : The inference relation of the premise and the hypothesis is undetermined.

An example of the dataset is shown below:

The ifcc-code folder contains a snapshot of the code used in our associated paper entitled "Improving Factual Completeness and Consistency of Image-to-text Radiology Report Generation" [7]. The latest version of this code can be found on GitHub [9].

This dataset may be useful for researchers seeking to explore computer assisted generation of imaging reports. In an associated paper, we demonstrate a promising method for generating such reports [7]. Code for reproducing the paper is provided in the ifcc-code folder and is also available on GitHub [9]. Please refer to the MIMIC-CXR Database (v2.0.0) for the source data for the annotations [4,5].

The authors have no conflicts of interest to declare.

Falke, T., Ribeiro, L., Utama, P., Dagan, I., & Gurevych, I. (2019). Ranking Generated Summaries by Correctness: An Interesting but Challenging Application for Natural Language Inference. In Proceedings of ACL 2019.

Maynez, J., Narayan, S., Bohnet, B., & McDonald, R. (2020). On Faithfulness and Factuality in Abstractive Summarization. In Proceedings of ACL 2020.

Romanov, A., & Shivade, C. (2018). Lessons from Natural Language Inference in the Clinical Domain. In Proceedings of EMNLP 2018.

Johnson, A., Pollard, T., Berkowitz, S., Greenbaum, N., Lungren, M., Deng, C., Mark, R., & Horng, S. (2019). MIMIC-CXR, a de-identified publicly available database of chest radiographs with free-text reports. Scientific Data, 6.

Johnson, A., Pollard, T., Mark, R., Berkowitz, S., & Horng, S. (2019). MIMIC-CXR Database (version 2.0.0). PhysioNet. https://doi.org/10.13026/C2JT1Q.

Devlin, J., Chang, M., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. In Proceedings of NAACL-HLT 2019.

Miura, Y., Zhang, Y., Tsai, E., Langlotz, C., & Jurafsky, D. (2021). Improving Factual Completeness and Consistency of Image-to-Text Radiology Report Generation. In Proceedings of NAACL-HLT 2021. https://www.aclweb.org/anthology/2021.naacl-main.416.pdf

Zhang, T., Kishore, V., Wu, F., Weinberger, K., & Artzi, Y. (2020). BERTScore: Evaluating text generation with BERT. In ICLR 2020.

Code for "Improving Factual Completeness and Consistency of Image-to-text Radiology Report Generation". https://github.com/ysmiura/ifcc [Accessed: 25 June 2021]]

sign the data use agreement for the project
