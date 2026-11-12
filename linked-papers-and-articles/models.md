# ``models``

**Source:** https://analysiscenter.github.io/cardio/modules/models.html

---

This is a place where ECG models live. You can write your own model or exploit provided models .

We have two built-in models suited to classify whether ECG signal is normal or pathological, and a model to annotate segments of ECG signal (e.g., P-wave).

This model is used to perform ECG classification. However, instead of predicting class probabilities themselves, the model predicts parameters of the Dirichlet distribution over these probabilities. This is done in order to get model’s confidence in its prediction, which varies from 0 (absolutely sure) to 1 (absolutely unsure). You can read more about the model in this article .

The high-level architecture of the network is shown in the figure below.

Hidden Markov Model is used to annotate ECG signal. This allows to calculate a number of parameters important for diagnosing.
This model allows to detect P and T waves; Q, R, S peaks; PQ and ST segments.

It has a total of 19 states, which makes a good compromise on complexity versus performance of the model. There will be 3 states for the ISO, P-wave, and QRS-complex models; 2 states for the PQ and ST segment models; 6 states for the T-wave. The mapping of them to the segments of ECG signal can  be found in cardio.batch.ecg_batch_tools submodule.

Also, as you can see in the picture below, we introduce direct transition from last ISO state to first PQ state, thus enabling possibility of absent P-wave.

FFT model learns to classify ECG signals using signal spectrum. At first step it convolves signal with a number of 1D kernels.
Then for each channel it applies fast fourier transform.
The result is considered as 2D image and is processed with a number of Inception2 blocks
to resulting output, which is a predicted class. See below the model architecture:

We applied this model to arrhythmia prediction from single-lead ECG. Train pipeline we used for the fft model looks as follows:

To learn more about existing models and building new ones, refer to the tutorial .

Models DirichletModel HMModel FFTModel Learn more API
