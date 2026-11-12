# CardIO documentation

**Source:** https://analysiscenter.github.io/cardio/index.html

---

CardIO is designed to build end-to-end machine learning models for deep research of electrocardiograms.

load and save signal in various formats (wfdb, DICOM, EDF, etc)

calculate heart rate and other ECG characteristics

perform complex processing like fourier and wavelet transformations

recognize heart diseases (e.g. atrial fibrillation)

efficiently work with large datasets that do not even fit into memory

build, train and test neural networks and other machine learning models

CardIO is based on Dataset . You might benefit from reading its documentation . However, it is not required, especially at the beginning.

CardIO has three modules: core , models and pipelines .

core module contains EcgBatch and EcgDataset classes. EcgBatch defines how ECGs are stored and includes actions for ECG processing. These actions might be used to build multi-staged workflows that can also involve machine learning models. EcgDataset is a class that stores indices of ECGs and generates batches of type EcgBatch .

models module provides several ready to use models for important problems in ECG analysis:

how to detect specific features of ECG like R-peaks, P-wave, T-wave, etc

how to recognize heart diseases from ECG, for example, atrial fibrillation

pipelines module contains predefined workflows to

train a model and perform an inference to detect PQ, QT, QRS segments and calculate heart rate

train a model and perform an inference to find probabilities of heart diseases, in particular, atrial fibrillation

Here is an example of pipeline that loads ECG signals, makes preprocessing and trains a model for 50 epochs:

CardIO module is in the beta stage. Your suggestions and improvements are very welcome.

When cloning repo from GitHub use flag --recursive to make sure that Dataset submodule is also cloned:

Please cite CardIO in your publications if it helps your research.

Welcome to CardIO’s documentation! About CardIO Contents Basic usage Installation Installation as a python package Installation as a project repository Citing CardIO

Installation Installation as a python package Installation as a project repository
