# MURA (musculoskeletal radiographs)

**Source:** https://stanfordmlgroup.github.io/competitions/mura

---

MURA ( mu sculoskeletal ra diographs) is a large dataset of bone X-rays. Algorithms are tasked with determining whether an X-ray study is normal or abnormal.

Musculoskeletal conditions affect more than 1.7 billion people worldwide, and are the most common cause of severe, long-term pain and disability, with 30 million emergency department visits annually and increasing. We hope that our dataset can lead to significant advances in medical imaging technologies which can diagnose at the level of experts, towards improving healthcare access in parts of the world where access to skilled radiologists is limited.

MURA is one of the largest public radiographic image datasets. We're making this dataset available to the community and hosting a competition to see if your models can perform as well as radiologists on the task.

MURA uses a hidden test set for official evaluation of models. Teams submit their executable code on Codalab, which is then run on a test set that is not publicly readable. Such a setup preserves the integrity of the test results.

Here's a tutorial walking you through official evaluation of your model. Once your model has been evaluated officially, your scores will be added to the leaderboard.

Will your model perform as well as radiologists in detecting abnormalities in musculoskeletal X-rays?

MURA is a dataset of musculoskeletal radiographs consisting of 14,863 studies from 12,173 patients, with a total of 40,561 multi-view radiographic images. Each belongs to one of seven standard upper extremity radiographic study types: elbow, finger, forearm, hand, humerus, shoulder, and wrist. Each study was manually labeled as normal or abnormal by board-certified radiologists from the Stanford Hospital at the time of clinical radiographic interpretation in the diagnostic radiology environment between 2001 and 2012.

To evaluate models and get a robust estimate of radiologist performance, we collected additional labels from six board-certified Stanford radiologists on the test set, consisting of 207 musculoskeletal studies. The radiologists individually retrospectively reviewed and labeled each study in the test set as a DICOM file as normal or abnormal in the clinical reading room environment using the PACS system. The radiologists have 8.83 years of experience on average ranging from 2 to 25 years. We randomly chose 3 of these radiologists to create a gold standard, defined as the majority vote of labels of the radiologists.

Our baseline uses a 169-layer convolutional neural network to detect and localize abnormalities. The model takes as input one or more views for a study of an upper extremity. On each view, our 169-layer convolutional neural network predicts the probability of abnormality. We compute the overall probability of abnormality for the study by taking the arithmetic mean of the abnormality probabilities output by the network for each image. The model makes the binary prediction of abnormal if the probability of abnormality for the study is greater than 0.5.

The network uses a Dense Convolutional Network architecture, which connects each layer to every other layer in a feed-forward fashion to make the optimization of deep networks tractable. We replace the final fully connected layer with one that has a single output, after which we apply a sigmoid nonlinearity. We use Class Activation Maps to visualize the parts of the radiograph which contribute most to the model's prediction of abnormality.

We evaluated our baseline on the Cohen’s kappa statistic, which expresses the agreement of the model with the gold standard. Baseline performance is comparable to radiologist performance in detecting abnormalities on finger studies and equivalent on wrist studies. However, baseline performance is lower than best radiologist performance in detecting abnormalities on elbow, forearm, hand, humerus, shoulder studies, and overall, indicating that the task is a good challenge for future research.

Find the dataset on the Stanford AIMI website .

MURA: Large Dataset for Abnormality Detection in Musculoskeletal Radiographs.

Pranav Rajpurkar*, Jeremy Irvin*, Aarti Bagul, Daisy Ding, Tony Duan, Hershel Mehta, Brandon Yang, Kaylie Zhu, Dillon Laird, Robyn L. Ball, Curtis Langlotz, Katie Shpanskaya, Matthew P. Lungren, Andrew Y. Ng

If you have questions about our work,
contact us at our google group .
