# How AI based arrhythmia detector can explain its decisions

**Source:** https://medium.com/mawi-band/how-ai-based-arrhythmia-detector-can-explain-its-decisions-b4f433faa4a2

---

We are creating methods for democratization of heart big data collection and analysis to detect diseases at early symptomless stages

How AI based arrhythmia detector can explain its decisions

In the past several years, Deep learning is getting one of the most important topics in AI. Its invasion has started from computer vision, particularly, ImageNet competition. Further, the state of the art CV methods was successfully applied for medical images. The most known examples are Kaggle Diabetic Retinopathy Detection and National Institutes of Health Chest X-Ray datasets.

Later, researchers applied Deep learning methods to another kind of medical data — medical signal and sequences. The first examples of these biomedical signals that come to our mind at once are called electrocardiogram (ECG). Initially, doctors and data scientists used to extract specific crucial points called QRS-complex (shown below) from each heartbeat and heart rate variability (HRV) features to perform disease detection.

Raw signal meant to be redundant and too expensive for shallow ML methods. However, segments of ECG with certain short length perfectly fitted for Convolutional Neural Networks. So, Stanford ML Group introduced an outstanding paper called Cardiologist-Level Arrhythmia Detection With Convolutional Neural Networks . They used Deep Residual Network which classified short-term electrocardiogram fragments and achieved human-quality arrhythmia detection. Besides, ML scientists tackled some other cardiological problems like myocardial infarction detection where also succeeded.

However, to apply them in real medical practice, algorithms have to receive certification, like Arterys (Medical Imagine Cloud AI) did this year. A key requirement is to provide a real necessity and right interpretation of the results.

As well known, contemporary Deep Learning models are working as black/grey boxes providing just strongly typed output. Fortunately, there are some approaches that can provide the significance of features for each input sample. Literature and scientific papers call them attribution, interpretation or justification. Let’s explore them.

First and most intuitive way to inspect a behavior of the model, is to take a correctly predicted test sample and modify certain feature (or set of features) by removing, masking or altering them. Then running a forward pass on the new input, measuring the difference with the original output. This method was called perturbation. As far as current neural network architectures do not allow to explicitly remove a feature without preliminary preparation, a logical way to overcome that is to simulate absence of information. A chosen feature assigns to a baseline, in our case we used 0, as a canonical one, however it can be selected specifically.

The second approach requires only single forward and backward pass through the network because it uses gradients to calculate an attribution for given sample. These methods are called Backpropagation based. The intuition can be comprehensively explained on a simple linear model. To identify the importance of features we have to multiply the input vector by model weights. After sorting the obtained vector with the descending order, we may observe the most valuable features for the model at the beginning of obtained vector. As far as we can calculate a local linear approximation of the (nonlinear) deep network, by calculating the gradient for particular input sample, we also can apply early mentioned model explanation method to deep networks. Intuitively, it was called Gradient*Input and has some modifications like Integrated Gradient, Layer-wise Relevance Propagation and DeepLIFT. They are different by a manner of calculation of importance values, but quite universal for literally all types of neural networks. More comprehensive explanation you can find in this paper . There are also methods like Grad-CAM, Deconvolutional Network, Guided Backpropagation, however, they are designed for specific architectures.

In MAWI we develop a lot of different neural network-based models for raw ECG signal analysis. It includes relatively straightforward applications as arrhythmia or some other disease detection to signal annotation, filtering, and augmentation. Recently we were showing our solution for atrial fibrillation (AF) detection based on neural networks to the doctors and although they were impressed with the accuracy, they were wondering why our model diagnoses ECG like this, how do we explain it? Reviewers also underlined, that it’s crucial for their practice to understand and explain the judgments of any intelligent assistant, but without math heavy justifications.

The main idea of this article was to introduce you a CNN model justification for Atrial Fibrillation task. For this purpose, I’ve selected a well-known MIT-BIH Atrial Fibrillation Database from Physionet. It contains 23 records of 22 people, each more than 6 hours long, 5 records were removed from the dataset because of the low quality and presence of the inseparable noise. Each record contains a labeled fragment of Atrial Fibrillation, Atrial Flutter, and Normal sinus rhythm. In this case, I focused only on solving a binary classification task by distinguishing an Atrial Fibrillation from the Normal sinus rhythm.

For the CNN I’ve chosen ResNet topology that already proved itself in ECG classification tasks as well as in CV and researchers or practitioners often use it as some kind of golden standard today. Considering data preprocessing, I prefer standard FIR filter that eliminated baseline and power line noise. To prevent subject overfitting and make everything “fair”, I’ve performed a classification in a user-independent manner, which picking one subject record for testing and using remaining records for training.

For illustration, I’ve used users record 04746 from the dataset (image below) from which sampled 5-second signal fragments with 1-second overlapping. As a result, 19526 of Atrial fibrillation and 17236 of normal sinus rhythm samples were obtained.

For training, I’ve randomly sampled 50,000 five-second fragments for each class obtaining a balanced dataset of 100,000 elements. Finally, the obtained elements were normalized and split for training and validation in ratio 90 to 10 correspondingly. After training I’ve obtained accuracies around 99.39 and 98.98 on test and validation set accordingly.

Atrial fibrillation is the most spread type of the heart arrhythmia. It may cause stroke, cardiovascular morbidity and mortality. Moreover, according to a Global Burden of Disease 2010 Study , 33.5 million people worldwide suffer from AF with 5 million new cases each year. And the most terrifying thing, that it’s very hard to detect during raw medical check-up. Even long-term Holter diagnostics do not always succeed. However, in MAWI we are working with the frequent short on-demand records, collected using our ECG-band. In the majority of cases, they are more efficient for conventional atrial fibrillation diagnostics, as reported in the given study . But how do doctors distinguish this disease and which patterns they are looking for?

Practitioners found that atrial fibrillation is based on several symptoms. Here is a quote from an awesome cardiological book, that truly describes features of atrial fibrillation.

“This irregularly irregular appearance of QRS complexes in the absence of discrete P waves is the key to identify atrial fibrillation. The wavelike forms that may often be seen on close inspection of the undulating baseline called fibrillation waves”.

So there are three main points that cardiologists are looking for:

The P wave in the ECG represents atrial depolarization, which starts spreading electrical signal through the heart.

• Presence of waveform artifacts between two QRS complexes

Instead of these nice looking waves heart with AF has small so called f-waves, that actually are these fibrillations, disorganized electrical activity instead of P waves.

Since we’re talking about arrhythmia, not rhythmic beat intervals are also very important signs of atrial fibrillation.

Now comes the most interesting. I’ve applied both perturbation and backpropagation-based methods on the trained network and obtained amusing results. On the plots below, points (or a set of points) depicted from blue in blue to red color, depending on how weakly or strongly they were involved in model decision making (red for strong and blue for weak).

First, just let’s take a look, how perturbation method called “Occlusion” (first plot), backpropagation based methods “gradient*input” and “Integrated Gradient”. On a sample with a normal rhythm, both methods accurately pointed to the present P-waves, which is an opposite feature to AF. Also, I have to point, that significant points found using the Integrated Gradient method are placed on each R-peak which can be interpreted as learned normal heartbeat rhythm.

This algorithm strongly emphasizes on present P waves.

This one emphasizes on present P waves as well.

Seems like this method also pays attention to regularity of the beats rhythm and underlines R peaks.

Here are couple of other interesting examples, where algorithm visualizes more the regularity of heart rhythm:

Note: the thickness of lines on the “Occlusion” plots is bigger, comparing to examples for gradient-based methods. It happens because a particular signal fragment for “Occlusion” was removed to calculate an importance value, whereas other methods importance values were calculated for each point.

In the case of samples with AF , explanation results are also meaningful. All used methods are pointing to the artifacts that were placed on the interbeat intervals, which is also a clinical feature.

As we can see, the neural network considers R peaks (because the rhythm is irregular) and fibrillations instead of P waves.

Here are some more representative examples.

To summarize, our results look pretty impressive, right? We are expanding these solutions to other diseases and symptoms and they always show correspondence with human-based priors. It is very interesting, because it shows, that in the area of understanding our heart people have already done the major work and our algorithm could just “repeat” it and understand the same patterns. On the other hand, neural network required just a dataset and 10 minutes of training, while human beings were studying cardiology for years and still share their experience from generation to generation.

On the other hand, we also have to conclude, that these explanations still need some human supervision and more friendly visualization. Another important issue that we have noticed — classifier (at least binary one) tends to visualize features that are present in one of the classes (as present P waves and “good” rhythm in our case) and everything else kind of supposed to be considered as a second class. It has to be taken into account while delivering this kind of systems to the clients.

We hope that you enjoyed this article because it showed you what neural networks really train and that we can trust their decisions (at least to some extent) and the functional of the MAWI band. We will keep working on explaining inner behavior of our AI algorithms and all the latest updates you may find on this blog page. So, you’re welcome to like, share, subscribe, leave some comments below. Cheers.

We are creating methods for democratization of heart big data collection and analysis to detect diseases at early symptomless stages
