# Parallel use of a convolutional neural network and bagged tree ensemble for the classification of Holter ECG

**Source:** https://iopscience.iop.org/article/10.1088/1361-6579/aad9ee

---

The aim of the Institute of Physics and Engineering in Medicine (IPEM) is to promote the advancement of physics and engineering applied to medicine and biology for the public benefit. Its members are professionals working in healthcare, education, industry and research.

IPEM publishes scientific journals and books and organises conferences to disseminate knowledge and support members in their development. It sets and advises on standards for the practice, education and training of scientists and engineers working in healthcare to secure an effective and appropriate workforce.

Parallel use of a convolutional neural network and bagged tree ensemble for the classification of Holter ECG

Filip Plesinger , Petr Nejedly , Ivo Viscor , Josef Halamek and Pavel Jurak

Published 12 September 2018 • © 2018 Institute of Physics and Engineering in Medicine. All rights, including for text and data mining, AI training, and similar technologies, are reserved. Physiological Measurement , Volume 39 , Number 9 Focus on detection of arrhythmia and noise from cardiovascular data Citation Filip Plesinger et al 2018 Physiol. Meas. 39 094002 DOI 10.1088/1361-6579/aad9ee

Institute of Scientific Instruments of the Czech Academy of Sciences, Brno, Czechia

Institute of Scientific Instruments of the Czech Academy of Sciences, Brno, Czechia

Institute of Scientific Instruments of the Czech Academy of Sciences, Brno, Czechia

Institute of Scientific Instruments of the Czech Academy of Sciences, Brno, Czechia

Institute of Scientific Instruments of the Czech Academy of Sciences, Brno, Czechia

820 Total downloads 0 Video abstract views

The automated detection of arrhythmia in a Holter ECG signal is a challenging task due to its complex clinical content and data quantity. It is also challenging due to the fact that Holter ECG is usually affected by noise. Such noise may be the result of the regular activity of patients using the Holter ECG—partially unplugged electrodes, short-time disconnections due to movement, or disturbances caused by electric devices or infrastructure. Furthermore, regular patient activities such as movement also affect the ECG signals and, in connection with artificial noise, may render the ECG non-readable or may lead to misinterpretation of the ECG.

Objective : In accordance with the PhysioNet/CinC Challenge 2017, we propose a method for automated classification of 1-lead Holter ECG recordings. Approach : The proposed method classifies a tested record into one of four classes—‘normal’, ‘atrial fibrillation’, ‘other arrhythmia’ or ‘too noisy to classify’. It uses two machine learning methods in parallel. The first—a bagged tree ensemble (BTE)—processes a set of 43 features based on QRS detection and PQRS morphology. The second—a convolutional neural network connected to a shallow neural network (CNN/NN)—uses ECG filtered by nine different filters (8×  envelograms, 1×  band-pass). If the output of CNN/NN reaches a specific level of certainty, its output is used. Otherwise, the BTE output is preferred.

Main results : The proposed method was trained using a reduced version of the public PhysioNet/CinC Challenge 2017 dataset (8183 records) and remotely tested on the hidden dataset on PhysioNet servers (3658 records). The method achieved F1 test scores of 0.92, 0.82 and 0.74 for normal recordings, atrial fibrillation and recordings containing other arrhythmias, respectively. The overall F1 score measured on the hidden test-set was 0.83. Significance : This F1 score led to shared rank #2 in the follow-up PhysioNet/CinC Challenge 2017 ranking.

The computer you are using is not registered by an institution with a subscription to this article. Please choose
            one of the options below.

Purchase this article from our trusted document delivery partners.

To gain access to this content, please complete the Recommendation
                    Form and we will follow up with your librarian or Institution on your behalf.

For corporate researchers we can also follow up directly with your R&D manager, or the information
                    management contact at your company. Institutional subscribers have access to the current volume, plus a
                    10-year back file (where available).

MSc Medical Physics with Radiobiology University of Oxford, Department of Oncology

Assistant Professor of Physics - Tenure Track Georgia Southern University

2027 SURF Vacancy Announcements are open! National Institute of Standards and Technology (NIST) - Gaithersburg and Boulder
