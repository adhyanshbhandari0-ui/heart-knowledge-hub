# CardIO framework for deep research of electrocardiograms

**Source:** https://medium.com/data-analysis-center/cardio-framework-for-deep-research-of-electrocardiograms-2a38a0673b8e

---

Machine learning for Oil and Gas Exploration. Advanced methods to locate oil deposits

CardIO framework for deep research of electrocardiograms

This article introduces a framework that allows to build end-to-end machine learning models for deep research of electrocardiograms and provides ready-to-use methods for heart diseases detection. You will learn

CardIO is an open-source Python framework. With CardIO you can

calculate heart beat rate and find other standard ECG characteristics

efficiently work with large datasets that do not even fit into memory

easily arrange new custom actions into pipelines

build, train and test custom models for deep research

… and do everything under a single API! You can get the repository here and immediately start using it. The repository contains comprehensive documentation and a set of IPython Notebook tutorials .

Conceptually CardIO is based on a very simple and natural approach:

input dataset can be indefinitely large, so we split it into batches and process data batch by batch

describe workflow as a sequence of actions (e.g. load data —data preprocessing — train model)

run the workflow once for the whole dataset.

Important note is that CardIO does not provide pretrained models since ECG data vary a lot according to cardiac monitoring devices. Instead of it CardIO provides reproducible workflows for model training. Results presented in this article were obtained with the QT Database and PhysioNet short single lead ECG database .

CardIO has been elaborated for processing of electrocardiograms (ECG).

In short ECG shows how your heart is beating. Every muscular movement is accompanied with some electrical impulse. Cardiac monitors measure integrated impulse and thus produce the well known signal pattern that consists of regular peaks and waves.

To be specific let’s get some dataset of ECGs and play with it (all examples of code given below are combined in a single IPython Notebook available here ). After cloning CardIO repository you will find a dataset with 6 examples of ECG in folder cardio/tests/data.

ECG data are typically stored in wfdb format. Each ECG record consists of several files that contain signal itself, signal meta information (e.g. sample rate), annotanion and signal calibration specifications. These files have common filename which is a record name (e.g. ‘A00001’) but different extensions (.hea, .dat etc).

CardIO does not load the whole dataset directly into memory, instead it stores only indices of dataset items. Indices can be easily composed from filenames of individual ECG records:

Check that all ECG record names are in list of indices:

We should obtain a list [‘A00001’, ‘A00002’, ‘A00004’, ‘A00005’, ‘A00008’, ‘A00013’]. Then we create a dataset of ECG records. It contains indices and class with batch actions :

From dataset we can generate batches of any size. Let’s generate batch of size two:

However, batch still contains nothing but indices. Action load loads data into batch:

It’s time to look at short segment of signal with index ‘A00001’:

Cardiac signal has a clear quasi periodic structure. Every cycle here is a single heart beat. The more similar cycles are the more regular heart rhythm is and risk of heart diseases is relative low. In contrast, deviations from normal rhythm may indicate heart diseases.

In the next step we will show how CardIO helps to analyze ECG.

Calculate ECG characteristics with CardIO

It is common to isolate and measure a number of features in ECG that are schematically given in the figure below (figure source: Wikipedia ).

The most prominent feature is a so-called R-peak. Counting a number of R-peaks one obtains heart beat rate. Normally it lies between 60 and 100 beats per minute. In normal ECG R-peak precedes S-peak and T-wave and follows after P-wave and Q-peak. This structure should regularly repeat every cardiac cycle.

CardIO has built-in pipelines for calculation of ECG characteristics. With the framework you can

calculate heart beat rate and length of ECG segments.

To demonstrate how this works we consider pipeline hmm_predict_pipeline that makes segmentation of ECG into QRS intervals, T-waves and P-waves . To get results we simply pass ECG dataset into the pipeline and run calculation:

This will iterate over the whole dataset and perform successively all actions and signal transformations required for segmentation (see details in Part 2 ). Figure below shows the result.

Under the hood the pipeline contains a list of actions:

In the same manner you can define another list of actions. This will be your custom pipeline . You have not to limit yourself by a list of built-in actions since pipelines may include any custom action. So CardIO allows creation any pipeline you need for research!

Proper interpretation of ECG signal is vitally important for heart disease recognition. Machine learning models may help in this process.

While the normal ECG pattern seems to be quite simple, the deviations from it obtain very and very different forms. Standard features mentioned above can be absent at all, or appear irregularly, or appear in a random order and so on and so on… Such a complex nature of ECG requires high qualification from cardiologists, however, its misinterpretation is always probable.

CardIO has a built-in model for recognition of atrial fibrillation (AF) that is one of the most common heart disorder. For detection of any other disease Framework allows to easily create, train and test custom models . Moreover, several model can be trained simultaneously. The process is as simple as run pipeline.

Let’s consider how CardIO estimates a probability of atrial fibrillation in ECG.

Atrial fibrillation is characterized by a number of changes in ECG. Most remarkable symptoms are irregularly irregular rhythm of ECG, absence of P-waves, absence of an isoelectric baseline, presence of flutter-like waves.

CardIO AF detection model receives short segments of ECG signal and returns probability of AF. Hidden logic on how this model was trained and detailed architecture are discussed in Part 3 . Here we only demonstrate how to use this model for AF prediction:

Prediction list assigned to variable pred contains probability of AF as well as estimated confidence (details are clarified in Part 3 ). We consider only predicted AF probability:

We obtain probabilities 0.02, 0.02, 0.87, 0.61, 0.03, 0.02 that correspond to ECGs with indices ‘A00001’, ‘A00002’, ‘A00004’, ‘A00005’, ‘A00008’, ‘A00013’. One can conclude that signal ‘A00001’ is unlikely to have AF (probability is 0.02) while signal ‘A00004’ has AF with high probability 0.87.

Under the hood of dirichlet_predict_pipeline contains a list of actions:

These actions import pretrained model, preprocess data and make predictions. In the same manner CardIO allows to create custom models and custom training and predicting pipelines.

CardIO has a general framework for any model. Framework is defined in BaseModel class that contains build, load, train, save and predict methods. Depending on the backend you prefer general methods should be connected with corresponding backend methods. Once it is done and model architecture is built, you can include model methods directly in pipeline . If you write a model with Tensorflow then you simply exploit provided TFModel class. Thus in most cases you only need to specify a model architecture.

Batch is a core concept of CardIO. You may have an enormous amount of data that does not even fit into memory, but splitting data into batches one can easily iterate over the whole dataset. Ordinary iterating in GPU/CPU architectures looks as follows:

We can note that very often CPU and GPU are unused and do nothing. CardIO resolves such issue and gives boosting due to prefetch. While one batch is being processed on GPU (typically during model training), several other batches are being preprocessed on CPU. This constantly utilizes power of GPU and CPU and makes computations fast. The figure below shows the benefit from prefetch.

One can notice that with prefetch we process 2 times more batches in comparison with non-prefetch mode. Of course, in practice things are more complicated, however, by varying depth of prefetch (how many batches are loaded and preprocessed in CPU) you can obtain evident boosting!

Summing up, CardIO provides convenient framework to do research in ECG and related areas of signal analysis. With CardIO you can build end-to-end research workflow that includes

preprocess steps, where you apply built-in or custom actions on data

definition of model (this can be neural network, bayesian model, etc)

training and testing of the models (here you can play with several models simultaneously, e.g. choosing the best one).

To test the workflow you simply pass data into it and let it run. You should not bother about the total data size. CardIO splits it into batches of appropriate size and iterates over the whole dataset. Moreover, you can be sure that CardIO fully utilizes GPU/CPU power due to prefetch. This makes the process really fast and efficient.

That’s not all. Now you can train the models for ECG segmentation and predicting atrial fibrillation . Hopefully you will find inspiring ideas for your own research!

Machine learning for Oil and Gas Exploration. Advanced methods to locate oil deposits
