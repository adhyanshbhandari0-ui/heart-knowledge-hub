# Cardiologist-Level Arrhythmia Detection With Convolutional Neural Networks

**Source:** https://stanfordmlgroup.github.io/projects/ecg

---

Cardiologist-Level Arrhythmia Detection With Convolutional Neural Networks

Pranav Rajpurkar*, Awni Hannun*, Masoumeh Haghpanahi, Codie Bourn, and Andrew Ng

A collaboration between Stanford University and iRhythm Technologies

We develop a model which can diagnose irregular heart rhythms, also known as arrhythmias, from single-lead ECG signals better than a cardiologist.

Key to exceeding expert performance is a deep convolutional network which can map a sequence of ECG samples to a sequence of arrhythmia annotations along with a novel dataset two orders of magnitude larger than previous datasets of its kind.

We train a 34-layer convolutional neural network (CNN) to detect arrhythmias in arbitrary length ECG time-series.

The network takes as input a time-series of raw ECG signal, and outputs a sequence of label predictions. The 30 second long ECG signal is sampled at 200Hz, and the model outputs a new prediction once every second. We arrive at an architecture which is 33 layers of convolution followed by a fully connected layer and a softmax.

To make the optimization of such a deep model tractable, we use residual connections and batch-normalization. The depth increases both the non-linearity of the computation as well as the size of the context window for each classification decision.

We collect and annotate a dataset of 64,121 ECG records from 29,163 patients.

The ECG data is sampled at a frequency of 200 Hz and is collected from a single-lead, noninvasive and  continuous monitoring device called the Zio Patch (iRhythm Technologies) which has a wear period up to 14 days. Each ECG record in the training set is 30 seconds long and can contain more than one rhythm type. Each record is annotated by a clinical ECG expert: the expert highlights segments of the signal and marks it as corresponding to one of the 14 rhythm classes.

We collect a test set of 336 records from 328 unique patients. For the test set, ground truth annotations for each record were obtained by a committee of three board-certified cardiologists; there are three committees responsible for different splits of the test set. The cardiologists discussed each individual record as a group and came to a consensus labeling. For each record in the test set we also collect 6 individual annotations from cardiologists not participating in the group. This is used to assess performance of the model compared to an individual cardiologist.

The model outperforms the cardiologist average on both the Sequence and Set F1 metrics.

The Sequence F1 measures the average overlap between the prediction and the ground truth sequence labels, while the Set F1 measures the average overlap between the unique class labels from the prediction and those from the ground truth.

Mistakes made by the model are understandable

One of the most common confusions is between Ectopic Atrial Rhythm (EAR) and the sinus rhythm (SINUS). The main distinguishing criteria for this rhythm is an irregular P wave. This can be subtle to detect especially when the P wave has a small amplitude or when noise is present in the signal.

Similarly, Supraventricular Tachycardia (SVT) and Atrial Fibrillation (AFIB) are often confused with Atrial Flutter (AFL) which is understandable given that they are all atrial arrhythmias. Idioventricular Rhythm (IVR) is sometimes mistaken as Ventricular Tachycardia (VT), which again makes sense given that the two only differ in heart-rate and are difficult to distinguish close to the 100 beats per minute delineation.

Given that more than 300 million ECGs are recorded annually, high-accuracy diagnosis from ECG can save expert clinicians and cardiologists considerable time and decrease the number of misdiagnoses. Furthermore, we hope that this technology coupled with low-cost ECG devices enables more widespread use of the ECG as a diagnostic tool in places where access to a cardiologist is difficult.
