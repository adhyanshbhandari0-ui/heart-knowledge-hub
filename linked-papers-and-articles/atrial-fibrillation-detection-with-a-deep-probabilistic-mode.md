# atrial-fibrillation-detection-with-a-deep-probabilistic-model-1239f69eff6c

**Source:** https://medium.com/data-analysis-center/atrial-fibrillation-detection-with-a-deep-probabilistic-model-1239f69eff6c

---

Machine learning for Oil and Gas Exploration. Advanced methods to locate oil deposits

Atrial fibrillation detection with a deep probabilistic model

Atrial fibrillation (also called AF or AFib) is the most common heart arrhythmia, occurring in about 2% of the world’s population. It is associated with significant mortality and morbidity from heart failure, dementia and stroke. The early AF identification is an essential part of preventing the development of heart diseases, but it is a challenging task due to its episodic nature and similarity to many other abnormal rhythms.

Fortunately, with CardIO framework you can easily create a deep machine learning model for atrial fibrillation detection. This article is structured as follows: we start with the dataset description, then present the model architecture, as well as training and testing pipelines with classification metrics and, finally, we analyze model’s confidence in its predictions.

If you are not already familiar with CardIO, take a quick look at the documentation page and tutorials first.

We use the PhysioNet dataset for model training and testing. It is a set of single-lead ECGs collected from portable heart monitoring devices. All ECGs were classified by a single expert into 4 classes:

Further, we will drop all noisy signals and focus on solving a two-class classification problem: atrial fibrillation against normal and other rhythms.

For this learning task a convolutional neural network would do the trick, since they are very well suited for signal processing. However, instead of predicting atrial fibrillation probability itself, the model will predict parameters of the beta distribution over this probability. This is done in order to get model’s confidence in its prediction which will be discussed later in this section.

The network consists of ResNet-like blocks with two convolutional layers per block. The first convolution in some blocks subsamples its input by a factor of 2, in this case the corresponding shortcut connection is downsampled by the same factor with a max pooling operation. If the number of channels produced by the last convolution in a block differs from the number of channels in the block’s input, then a 1x1 convolution is applied to the shortcut connection just before the addition operation.

The high-level architecture of the network is shown in the figure below. Note that batch normalization is applied before each activation.

A more detailed description of the model can be found in the DirichletModelBase class . It is called this way because it can also be used for multiclass classification, while the Dirichlet distribution generalizes the beta distribution to a multivariate case.

The model is trained on fixed-size crops from ECG signals by minimizing the negative beta log likelihood. Each crop is labeled with the original signal’s class. This approach may result in data mislabeling, but we haven’t faced significant troubles with the training procedure.

Making a prediction in such a model is not so straightforward. A new ECG signal can have an arbitrary length, while the network is trained on fixed-size crops. Therefore, an algorithm for multiple predictions aggregation is needed.

Let’s denote the signal generating process by X , the atrial fibrillation probability by t and the vector of the beta distribution parameters by α . Consider the conditional distribution of t given X :

Here, we assume that X is an ergodic process . In this case, samples from p(α|X) may be replaced by network’s outputs for consequent non-overlapping crops from the original signal.

So, the distribution over atrial fibrillation probability can be approximately modelled by the mixture of beta distributions with equal weights. The mean of the mixture provides a point estimate of this probability.

Now consider the variance of an arbitrary random variable whose values lie between 0 and 1. As follows from the definition, it is bounded below by 0. It is also bounded above by 0.25 – the variance of a Bernoulli random variable with equal probabilities of 0 and 1.

We will take the variance of the mixture divided by this maximal variance as model’s uncertainty in a given signal’s class. If it equals zero, the model is absolutely sure in its prediction: all the probability mass is concentrated in one point. If it equals one, the model is absolutely unsure.

data loading, preprocessing (e.g. flipping) and augmentation (e.g. resampling)

Let’s create a template pipeline, then link it to our training dataset and run:

The figure below shows the training loss for 1000 epochs:

As we can see, training loss almost reaches a plateau by the end of the training.

Testing pipeline is almost identical to the training one. The differences lie in the absence of signal resampling and the modified segmentation procedure. Notice, that the model is imported from the training pipeline, rather than being constructed from scratch:

Take a look at the confusion matrix and precision, recall and F1-score for both classes:

The model misclassifies 33 patients with atrial fibrillation and 25 patients with normal and other rhythms. All other patients were classified correctly.

We’ve already obtained good classification performance. Let’s see if we can do even better.

As discussed above, in addition to class probabilities the model returns its uncertainty in the prediction, which varies from 0 (absolutely sure) to 1 (absolutely unsure). The figure below illustrates the histogram of model’s uncertainty in classifying testing dataset:

As can be seen, the model is very often confident in its predictions. Often, but not always.

Compare the classification performance for the full testing dataset with the classification performance for 90% most certain predictions:

We can observe a significant increase in precision, recall and F1-score for the atrial fibrillation class. Now only 16 signals were misclassified.

This means that the chosen uncertainty measure actually reflects model’s uncertainty in its prediction.

First, let’s look at the healthy person’s ECG. The signal is shown on the left plot. Note that it has a clear quasi periodic structure. The right plot shows the pdf of the mixture of beta distributions with atrial fibrillation probability plotted on the horizontal axis. The model is absolutely certain in the absence of AF: almost all the probability density is concentrated around 0.

And now comes an ECG with irregular structure, which may be caused by a disease or some measurement errors. The probability density on the right plot is almost equally concentrated around 0 and 1. This is an example of an uncertain prediction.

To summarize, in this article you’ve learned how to:

build a deep probabilistic model for atrial fibrillation detection in just a few lines of code with CardIO framework

significantly increase the classification performance by filtering out uncertain predictions

You can find more information about CardIO framework in the documentation and tutorials .

Here you can learn more about ECG processing and CardIO framework features.

If you are interested in ECG signal segmentation, take a look at this article , where a hidden Markov model is used to detect P waves, QRS complexes and T waves.

Machine learning for Oil and Gas Exploration. Advanced methods to locate oil deposits
