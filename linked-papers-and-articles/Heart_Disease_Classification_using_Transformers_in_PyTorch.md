# Heart Disease Classification using Transformers in PyTorch

**Source:** https://towardsdatascience.com/heart-disease-classification-using-transformers-in-pytorch-8dbd277e079

---

Heart disease is an important problem and deep learning solves problems. Transformers are the future: what happens when we combine everything?

In this article, a classification system for Atrial Fibrillation (AF) using electrocardiogram (ECG/ EKG) data will be implemented and discussed. The classification system will be binary (Normal Sinus Rhythm, AF) and will be based on a transformer network using the PyTorch framework. The structure of this article will be as follows, first the problem at hand, as well as the data used, will be introduced, secondly, the technical details of the network will be presented, thirdly the implementation of the network and training will be presented, lastly, a presentation of the results and discussion will follow. The repository for this project can be found here: https://github.com/bh1995/AF-classification .

Learn this step by step with the interactive Machine Learning roadmap .

Atrial Fibrillation Classification Problem

Heart disease is amongst the leading causes of death globally [1]. Heart diseases often cause an irregularity in heart behavior called an arrhythmia. Among all types of arrhythmia, Atrial Fibrillation (AF) is the most common cardiac arrhythmia and it is estimated to be prevalent in the range of 2% to 4% of the population; with the prevalence expected to increase linearly in the future as the average age of the population increases. Given the current statistics, there is an approximate probability of 37% for any given individual of European descent to suffering from AF over the span of their lifetime [2]. A standard heart monitoring technology is the electrocardiogram (ECG/ EKG), it monitors the electrical signals in a heart and as such can be very useful for clinicians to diagnose arrhythmias. The aim of this project is to utilize real, publicly available, ECG data that has been labeled by clinicians to train a deep learning model.

The data used in this project come from multiple sources, namely from the China Physiological Signal Challenge 2018 (CPSC2018)[3], St Petersburg INCART 12-lead Arrhythmia Database [4], Georgia 12-Lead ECG Challenge Database (CinC2020)[5], PhysioNet Computing in Cardiology Challenge 2017 (CinC2017) dataset [5], Contextual Arrhythmia Database (CACHET-CADB)[6].

The data sources used have collected their ECG data at various sampling rates, and using different devices (some use a Holter monitor others hospital grade 12-lead ECG), this leads to the nature of each data source is slightly different. To increase the learning capabilities of the deep learning model, it is wise to process all data in a normalizing way. In this project, a bandpass filter (FIR-filter) was used on all signals such that only frequencies in the range of [0.5, 40] are kept. The signals are also resampled to a rate of 300 Hz, and separated into individual segments of 10 seconds in length (thus each input to the model is a one dimensional array with a length of 3000 data points). Each 10 second segment is then normalized such that all values lie between 0 and 1. The figures below show two original (raw) signals (one AF and one normal) and the same two signals after pre-processing.

The signal plots in the first image show a standard, clear 10 second long ECG recording. The y-axis of the plots represents voltage difference and the x-axis sampling rate which is in our case 300 Hz. As seen from the plots, the voltage of a given person's heart varies compared to another. For us humans, it is clear to look for a pattern on the x-axis instead of looking at the amplitude on the y-axis. However, a deep learning model computes features in an unbiased way and as such will naively use all information given (even though the amplitude is generally irrelevant for arrhythmia classification). This is why it is extremely important to normalize the data to a given interval (ex. [-1,1] or [0,1]). The figure above shows an example of AF, this can be seen from the irregular spacing between some of the heartbeats. This case is a "simple" example as even amateurs can clearly see the abnormality of the AF signal.

The full dataset used in this project can be downloaded via the link . The data is all pre-processed and is saved as an array in a .h5 file format. The code snippet below shows an example of how the dataset can be loaded.

Two models are tested in this project, they both follow the same fundamental architecture but use different inputs. The first uses the pre-processed ECG signal as its only input, whereas the second model uses the pre-processed ECG signal, as well as the so called RRI (RR-interval) for that signal. The RRI is the estimated time in seconds between a heartbeat and the consecutive heartbeat. The RRI is computed by estimating the R-peak (middle position of each heartbeat) in the signal using the Pan-Tompkins algorithm [10], and then using the following equation,

where Rn is the given peak and fs is the frequency (sampling rate). To keep a set length of the input RRI sequence to the model, the first 10 of the total RRIs are used and zero padded if less than 10 are found.

The model used in the project was inspired by the work of [8]. The model is comprised of the following modules: 1) an embedding network made up of a series of convolutional layers, 2) a stacking of transformer encoder layers, 3) a classification head comprised of a series of fully connected layers. The code for the model architecture and model training can be found here .

Embedding : The embedding network applies one dimensional convolutions to the original ECG signal, this results in a sequence of embedded representations ( x[0], ..., x[n] ). These embedded representations are summed together with positional encodings ( p[0], ..., p[n] ) to represent the order of each sequence, as done in the original transformer paper [7]. The result is a positional encoded embedding, e = ( x[0]+p[0], ..., x[n]+p[n] ) which then is used as input to the stacked transformer encoder layers module.

Transformer encoder layers: The transformer module consists of a stacking of transformer encoder layers, where each encoder consists of a multi-headed self-attention mechanism sublayer, after trial and error it was found that a number of four encoder layers and heads produced good results. Again, after trail and error, the embedding dimension within the encoder was chosen to be 64 and the dimension of the feed forward network within the encoder layers to be 512 . The output of the transformer module is a tensor of attention weights with the shape, [Sequence length, Batch size, Embedding]. The output must be transformed in some way such that it be fed into the classification head module, i.e. it needs to be transformed to the shape [Batch size, Embedding]. Two methods were tried, the first being to simply take the average of the tensor on the sequence dimension and the second to use a self attention pooling layer as suggested in work by [9]. Both methods showed good performance, however, the utilization of a self attention pooling layer produced the best results. The self attention pooling layer is applied to the output of the transformer module which produces an embedding that is a learned average of the features in the encoder sequence.

Classification head: The output from the self attention pooling is used as input to the final classification head to produce the logits used for prediction. The final classification head is two fully connected layers with a single dropout layer in between.

The model was trained using binary cross entropy as a loss function, and the AdamW algorithm as the optimizer ( β1=0.9, β2=0.98, ε=10^(-9) ). An initial learning rate of 10^(-3) was used and a learning scheduler was used to decrease the learning rate by 5% every five epochs starting after the first 30 epochs. The dataset has a total of 52 370, 10 second long ECG signals, where the ratio of Normal to AF labels is approximately even. 85% (44 514) of the dataset was randomly selected to be used for training and the remaining 15% (7 855) was used for testing. A batch size of 10 was used and training was done using a Tesla P100 GPU in a cloud computing environment.

The results for both models will be presented below, first the model which uses only the raw ECG signal followed by the model using the raw ECG signal as well as the RRIs for that signal.

As seen in the plots below, the model showed consistent learning over epochs, without any considerable overfitting. Test accuracy is also seen to grow consistently. Since this task is a binary classification of disease, sensitivity and specificity is arguably a better metric of performance. The sensitivity and specificity on the test data at the end of training were 85.6 and 92.7 respectively. The training time was about 178 seconds per epoch.

When RRI features were used during training/ inference, the model performance increased. The plot below showcases that the model shows clear signs of overfitting, however, this overfitting does not negatively affect model accuracy on the test data over epochs. The sensitivity and specificity on the test data at the end of training was, 96.9 and 95.6 respectively. The training time was about 1550 seconds per epoch.

It is clear from the results that the transformer encoder based network works well in classifying AF in 10 second long ECG signals. It is also clear that using RRI features provides a large improvement in performance of the model at the cost of a nearly nine fold increase in training and inference time. This time increase is attributed to the fact that the Pan-Tompkins algorithm used to perform R-peak detection is slow.

[1] Heart disease and stroke statistics 2018 update: A report from the American Heart Association. American Heart Association, 1, 2018.

[2] 2020 ESC Guidelines for the diagnosis and management of atrial fibrillation developed in collaboration with the European Association for Cardio-Thoracic Surgery (EACTS): The Task Force for the diagnosis and management of atrial fibrillation of the European Society of Cardiology (ESC) Developed with the special contribution of the European Heart Rhythm Association (EHRA) of the ESC. European Heart Journal, 08 2020. ehaa612.

[3] F. F. Liu, C. Y. Liu*, L. N. Zhao, X. Y. Zhang, X. L. Wu, X. Y. Xu, Y. L. Liu, C. Y. Ma, S. S. Wei, Z. Q. He, J. Q. Li and N. Y. Kwee. An open access database for evaluating the algorithms of ECG rhythm and morphology abnormal detection. Journal of Medical Imaging and Health Informatics, 2018, 8(7): 1368–1373.

[4] Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220.

[5] Perez Alday EA, Gu A, Shah AJ, Robichaux C, Wong AI, Liu C, Liu F, Rad AB, Elola A, Seyedi S, Li Q, Sharma A, Clifford GD , Reyna MA . Classification of 12-lead ECGs: the PhysioNet/Computing in Cardiology Challenge 2020. Physiol Meas. 41 (2020).

[6] Devender Kumar, Sadasivan Puthusserypady, and Jakob Eyvind Bardram. CACHET-CADB. 5 May 2021. https://doi.org/10. 11583/DTU.14547264.v1.

[7] Vaswani, A., Brain, G., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin,I. Attention Is All You Need, .arXiv:1706.03762v5.

[8] A. Natarajan, et al .. A Wide and Deep Transformer Neural Network for 12-Lead ECG Classification. 2020 Computing in Cardiology , 2020, pp. 1–4, doi: 10.22489/CinC.2020.107.

[9] Safari, P., India, M., & Hernando, J.. Self-attention encoding and pooling for speaker recognition, .arXiv:2008.01077v1.

[10] J. Pan and W. J. Tompkins. A Real-Time QRS Detection Algorithm. IEEE Transactions on Biomedical Engineering , vol. BME-32, no. 3, pp. 230–236, March 1985, doi: 10.1109/TBME.1985.325532.

Upgrading and rebuilding the host Deep Learning Things went South fast after my last all Night hack David Moore January 23, 2021 13 min read

Things went South fast after my last all Night hack

Untangling AI systems Machine Learning How physics can help us understand neural networks Javier Marín Valenzuela October 26, 2024 13 min read

How physics can help us understand neural networks

Staying Motivated For Your Data Science Career Artificial Intelligence We Can Stay Motivated for the Long Run. Kurtis Pykes June 24, 2020 7 min read

Staying Motivated For Your Data Science Career

Machine Learning: How does it work; and more importantly, Why does it work? Artificial Intelligence Essence of ML and Hoeffding's inequality Venkatesh K August 23, 2020 7 min read

Machine Learning: How does it work; and more importantly, Why does it work?

Fast Anomaly Detection in Images With Python Machine Learning How I improved speed by 10x Anthony Cavin June 28, 2022 7 min read

Fast Anomaly Detection in Images With Python

Latest picks: A Better Way To Vote Machine Learning Your daily dose of data science TDS Editors February 4, 2021 1 min read

Data Lake Change Data Capture (CDC) using Apache Hudi on Amazon EMR - Part 2-Process Artificial Intelligence Easily process data changes over time from your database to Data Lake using Apache Hudi on Amazon EMR Manoj Kukreja October 22, 2020 5 min read

Data Lake Change Data Capture (CDC) using Apache Hudi on Amazon EMR - Part 2-Process

Easily process data changes over time from your database to Data Lake using Apache Hudi on Amazon EMR

Hot dog or Not Hot dog Deep Learning Trying out well-known CNN models with Tensorflow 2 to help Jian Yang Sanjay Chouhan September 7, 2021 7 min read

Trying out well-known CNN models with Tensorflow 2 to help Jian Yang

The Most Important Data Science Project Artificial Intelligence The Project every Data Scientist must do Kurtis Pykes July 9, 2020 7 min read
