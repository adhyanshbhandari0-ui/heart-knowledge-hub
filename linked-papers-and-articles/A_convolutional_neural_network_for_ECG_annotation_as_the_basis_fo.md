# A convolutional neural network for ECG annotation as the basis for classification of cardiac rhythms

**Source:** https://iopscience.iop.org/article/10.1088/1361-6579/aae304

---

The aim of the Institute of Physics and Engineering in Medicine (IPEM) is to promote the advancement of physics and engineering applied to medicine and biology for the public benefit. Its members are professionals working in healthcare, education, industry and research.

IPEM publishes scientific journals and books and organises conferences to disseminate knowledge and support members in their development. It sets and advises on standards for the practice, education and training of scientists and engineers working in healthcare to secure an effective and appropriate workforce.

A convolutional neural network for ECG annotation as the basis for classification of cardiac rhythms

Philipp Sodmann , Marcus Vollmer , Neetika Nath and Lars Kaderali

Published 24 October 2018 • © 2018 Institute of Physics and Engineering in Medicine. All rights, including for text and data mining, AI training, and similar technologies, are reserved. Physiological Measurement , Volume 39 , Number 10 Focus on detection of arrhythmia and noise from cardiovascular data Citation Philipp Sodmann et al 2018 Physiol. Meas. 39 104005 DOI 10.1088/1361-6579/aae304

Institute of Bioinformatics, University Medicine Greifswald, Greifswald, Germany

DZHK (German Center for Cardiological Research), partner site Greifswald, Greifswald, Germany

Institute of Bioinformatics, University Medicine Greifswald, Greifswald, Germany

DZHK (German Center for Cardiological Research), partner site Greifswald, Greifswald, Germany

Institute of Bioinformatics, University Medicine Greifswald, Greifswald, Germany

Institute of Bioinformatics, University Medicine Greifswald, Greifswald, Germany

DZHK (German Center for Cardiological Research), partner site Greifswald, Greifswald, Germany

1744 Total downloads 0 Video abstract views

Objective : Electrocardiography is the most common tool to diagnose cardiovascular diseases. Annotation, segmentation and rhythm classification of ECGs are challenging tasks, especially in the presence of atrial fibrillation and other arrhythmias. Our aim is to increase the accuracy of heart rhythm estimation by the use of extreme gradient boosting trees and the development of a deep convolutional neural network for ECG segmentation.

Approach : We trained a convolutional neural network with waveforms from PhysioNet databases to annotate QRS complexes, P waves, T waves, noise and interbeat ECG segments that characterize the essences of normal and irregular heart beats. We evaluated true positive rates, positive predictive values and mean absolute differences of our annotation based on reference annotations of the QT and MIT-BIH P-wave database. Moreover, we compared the results with standard QRS detectors and Ecgpuwave. Extreme gradient boosting trees were used to determine the heart rhythm based on hand-crafted features. More precisely, a noise estimation function was used in combination with heart rate and interval data. Furthermore we defined particular features based on ECG morphology, appearance of P waves and detection of irregular beats. We examined the feature importance and identified key features for normal sinus rhythm, atrial fibrillation, alternative rhythm and noisy recordings. The classification performance was evaluated externally using F 1 scores by applying the algorithm to the hidden test set provided by the PhysioNet/CinC Challenge 2017.

Main results : The true positive rate of the convolutional neural network in detection of manually revised R peaks in the QT database was and the positive predictive value was . The detection of P and T waves reached a true positive rate of and respectively, given a 50 ms tolerance when comparing the reference to the test annotation set. The rhythm classification performance reached an overall F 1 score of 0.82 when applying the algorithm to the hidden test set.

Significance : We achieved a shared rank #9 in the post-challenge phase of the PhysioNet/CinC Challenge 2017.

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
