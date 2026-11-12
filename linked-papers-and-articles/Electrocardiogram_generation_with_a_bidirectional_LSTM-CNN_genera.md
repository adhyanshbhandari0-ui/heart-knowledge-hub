# Electrocardiogram generation with a bidirectional LSTM-CNN generative adversarial network

**Source:** https://www.nature.com/articles/s41598-019-42516-z

---

Thank you for visiting nature.com. You are using a browser version with limited support for CSS. To obtain
            the best experience, we recommend you use a more up to date browser (or turn off compatibility mode in
            Internet Explorer). In the meantime, to ensure continued support, we are displaying the site without styles
            and JavaScript.

Electrocardiogram generation with a bidirectional LSTM-CNN generative adversarial network

You have full access to this open access article

Heart disease is a malignant threat to human health. Electrocardiogram (ECG) tests are used to help diagnose heart disease by recording the heart’s activity. However, automated medical-aided diagnosis with computers usually requires a large volume of labeled clinical data without patients' privacy to train the model, which is an empirical problem that still needs to be solved. To address this problem, we propose a generative adversarial network (GAN), which is composed of a bidirectional long short-term memory(LSTM) and convolutional neural network(CNN), referred as BiLSTM-CNN,to generate synthetic ECG data that agree with existing clinical data so that the features of patients with heart disease can be retained. The model includes a generator and a discriminator, where the generator employs the two layers of the BiLSTM networks and the discriminator is based on convolutional neural networks. The 48 ECG records from individuals of the MIT-BIH database were used to train the model. We compared the performance of our model with two other generative models, the recurrent neural network autoencoder(RNN-AE) and the recurrent neural network variational autoencoder (RNN-VAE). The results showed that the loss function of our model converged to zero the fastest. We also evaluated the loss of the discriminator of GANs with different combinations of generator and discriminator. The results indicated that BiLSTM-CNN GAN could generate ECG data with high morphological similarity to real ECG recordings.

A hybrid deep learning algorithm for ECG-based heart disease classification

Hybrid CNN-BLSTM architecture for classification and detection of arrhythmia in ECG signals

KT-CBHNET: a spatio-temporal deep learning framework for interpretable ECG signal classification for cardiovascular disease prediction

Deep Learning Techniques for ECG Signal Analysis

Cardiovascular diseases are the leading cause of death throughout the world. Approximately 32.1% of the annual global deaths reported in 2015 were related with cardiovascular diseases 1 . Due to increases in work stress and psychological issues, the incidences of cardiovascular diseases have kept growing among young people in recent years. As an effective method, Electrocardiogram (ECG) tests, which provide a diagnostic technique for recording the electrophysiological activity of the heart over time through the chest cavity via electrodes placed on the skin 2 , have been used to help doctors diagnose heart diseases. However, as vast volumes of ECG data are generated each day and continuously over 24-hour periods 3 , it is really difficult to manually analyze these data, which calls for automatic techniques to support the efficient diagnosis of heart diseases.

Machine learning is employed frequently as an artificial intelligence technique to facilitate automated analysis. Many machine learning techniques have been applied to medical-aided diagnosis, such as support vector machines 4 , decision trees 5 , random conditional fields 6 , and recently developed deep learning methods 7 . However, most of these methods require large amounts of labeled data for training the model, which is an empirical problem that still needs to be solved. For example, large volumes of labeled ECG data are usually required as training samples for heart disease classification systems. Moreover, when machine learning approaches are applied to personalized medicine research, such as personalized heart disease research, the ECGs are often categorized based on the personal features of the patients, such as their gender and age. Thus, the problems caused by lacking of good ECG data are exacerbated before any subsequent analysis. Furthermore, maintaining the privacy of patients is always an issue that cannot be igored. However, the personal information and private clinical data obtained from patients are still likely to be illegally leaked. An optimal solution is to generate synthetic data without any private details to satisfy the requirements for research.

Hence, it is very necessary to develop a suitable method for producing practical medical samples for disease research, such as heart disease. Several previous studies have investigated the generation of ECG data. McSharry et al . proposed a dynamic model based on three coupled ordinary differential equations 8 , where real synthetic ECG signals can be generated by specifying heart rate or morphological parameters for the PQRST cycle. Clifford et al . used a nonlinear model to generate 24-hour ECG, blood pressure, and respiratory signals with realistic linear and nonlinear clinical characteristics 9 . Cao et al. designed an ECG system for generating conventional 12-lead signals 10 . However, most of these ECG generation methods are dependent on mathematical models to create artificial ECGs, and therefore they are not suitable for extracting patterns from existing ECG data obtained from patients in order to generate ECG data that match the distributions of real ECGs.

The generative adversarial network (GAN) proposed by Goodfellow in 2014 is a type of deep neural network that comprises a generator and a discriminator 11 . The generator produces data based on the noise data sampled from a Gaussian distribution, which is fitted to the real data distribution as accurately as possible. The inputs for the discriminator are real data and the results produced by the generator, where the aim is to determine whether the input data are real or fake. During the training process, the generator and the discriminator play a zero-sum game until they converge. GAN has been shown to be an efficient method for generating data, such as images.

In this study, we propose a novel model for automatically learning from existing data and then generating ECGs that follow the distribution of the existing data so the features of the existing data can be retained in the synthesized ECGs. Our model is based on a GAN architecture which is consisted of a generator and a discriminator. In the generator part, the inputs are noise data points sampled from a Gaussian distribution. We build up two layers of bidirectional long short-term memory (BiLSTM) networks 12 , which has the advantage of selectively retaining the history information and current information. Moreover, to prevent over-fitting, we add a dropout layer. In the discriminator part, we classify the generated ECGs using an architecture based on a convolutional neural network (CNN). The discriminator includes two pairs of convolution-pooling layers as well as a fully connected layer, a softmax layer, and an output layer from which a binary value is determined based on the calculated one-hot vector. We used the MIT-BIH arrhythmia data set 13 for training. The results indicated that our model worked better than the other two methods, the deep recurrent neural network-autoencoder (RNN-AE) 14 and the RNN-variational autoencoder (RNN-VAE) 15 .

The GAN is a deep generative model that differs from other generative models such as autoencoder in terms of the methods employed for generating data and is mainly comprised of a generator and a discriminator. The generator produces data based on sampled noise data points that follow a Gaussian distribution and learns from the feedback given by the discriminator. The discriminator learns the probability distribution of the real data and gives a true-or-false value to judge whether the generated data are real ones. The two sub-models comprising the generator and discriminator reach a convergence state by playing a zero-sum game. Figure 1 illustrates the architecture of GAN.

The solution obtained by GAN can be viewed as a min-max optimization process. The objective function is:

where D is the discriminator and G is the generator. When the distribution of the real data is equivalent to the distribution of the generated data, the output of the discriminator can be regarded as the optimal result.

GAN has been successfully applied in several areas such as natural language processing 16 , 17 , latent space learning 18 , morphological studies 19 , and image-to-image translation 20 .

Recurrent neural network has been widely used to solve tasks of processing time series data 21 , speech recognition 22 , and image generation 23 . Recently, it has also been applied to ECG signal denoising and ECG classification for detecting obstructions in sleep apnea 24 . RNN typically includes an input layer, a hidden layer, and an output layer, where the hidden state at a certain time t is determined by the input at the current time as well as by the hidden state at a previous time:

where f and g are the activation functions, x t and o t are the input and output at time t , respectively, h t is the hidden state at time t , W { ih,hh,ho } represent the weight matrices that connect the input layer, hidden layer, and output layer, and b { h,o } denote the basis of the hidden layer and output layer.

RNN is highly suitable for short-term dependent problems but is ineffective in dealing with long-term dependent problems. The long short-term memory (LSTM) 25 and gated recurrent unit (GRU) 26 were introduced to overcome the shortcomings of RNN, including gradient expansion or gradient disappearance during training. The LSTM is a variation of an RNN and is suitable for processing and predicting important events with long intervals and delays in time series data by using an extra architecture called the memory cell to store previously captured information. LSTM has been applied to tasks based on time series data such as anomaly detection in ECG signals 27 . However, LSTM is not part of the generative models and no studies have employed LSTM to generate ECG data yet. The GRU is also a variation of an RNN, which combines the forget gate and input gate into an update gate to control the amount of information considered from previous time flows at the current time. The reset gate of the GRU is used to control how much information from previous times is ignored. GRUs have been applied in some areas in recent years, such as speech recognition 28 .

The autoencoder and variational autoencoder (VAE) are generative models proposed before GAN. Besides used for generating data 29 , they were utilized to dimensionality reduction 30 , 31 .

RNN-AE is an expansion of the autoencoder model where both the encoder and decoder employ RNNs. The encoder outputs a hidden latent code d , which is one of the input values for the decoder. In contrast to the encoder, the output and hidden state of the decoder at the current time depend on the output at the current time and the hidden state of the decoder at the previous time as well as on the latent code d . The goal of RNN-AE is to make the raw data and output for the decoder as similar as possible. Figure 2 illustrates the RNN-AE architecture 14 .

VAE is a variant of autoencoder where the decoder no longer outputs a hidden vector, but instead yields two vectors comprising the mean vector and variance vector. A skill called the re-parameterization trick 32 is used to re-parameterize the random code z as a deterministic code, and the hidden latent code d is obtained by combining the mean vector and variance vector:

where μ is the mean vector, σ is the variance vector, and ε ~ N (0, 1).

RNN-VAE is a variant of VAE where a single-layer RNN is used in both the encoder and decoder. This model is suitable for discrete tasks such as sequence-to-sequence learning and sentence generation.

To the best of our knowledge, there is no reported study adopting the relevant techniques of deep learning to generate or synthesize ECG signals, but there are some related works on the generation of audio and classic music signals.

Methods for generating raw audio waveforms were principally based on the training autoregressive models, such as Wavenet 33 and SampleRNN 34 , both of them using conditional probability models, which means that at time t each sample is generated according to all samples at previous time steps. However, autoregressive settings tend to result in slow generation because the output audio samples have to be fed back into the model once each time, while GAN is able to avoid this disadvantage by constantly adversarial training to make the distribution of generated results and real data as approximate as possible.

Mogren et al . proposed a method called C-RNN-GAN 35 and applied it on a set of classic music. In their work, tones are represented as quadruplets of frequency, length, intensity and timing. Both the generator and the discriminator use a deep LSTM layer and a fully connected layer. Inspired by their work, in our research, each point sampled from ECG is denoted by a one-dimensional vector of the time-step and leads. Donahue et al . applied WaveGANs 36 from aspects of time and frequency to audio synthesis in an unsupervised background. WaveGAN uses a one-dimensional filter of length 25 and a great up-sampling factor. However, it is essential that these two operations have the same number of hyper parameters and numerical calculations. According to the above analysis, our architecture of GAN will adopt deep LSTM layers and CNNs to optimize generation of time series sequence.

We propose a GAN-based model for generating ECGs. Our model comprises a generator and a discriminator. The input to the generator comprises a series of sequences where each sequence is made of 3120 noise points. The output is a generated ECG sequence with a length that is also set to 3120. The input to the discriminator is the generated result and the real ECG data, and the output is D ( x ) ∈ {0, 1}. In the training process, G is initially fixed and we train D to maximize the probability of assigning the correct label to both the realistic points and generated points. We then train G to minimize log(1 − D ( G ( z ))). The objective function is described by Eq. 5 :

where N is the number of points, which is 3120 points for each sequence in our study, and θ and ϕ represent the set of parameters.

As CNN does not have recurrent connections like forgetting units as in LSTM or GRU, the training process of the models with CNN-based discriminator is often faster, especially in the case of long sequence data modeling. CNN has achieved excellent performance in sequence classification such as the text or voice sorting 37 . Many successful deep learning methods applied to ECG classification and feature extraction are based on CNN or its variants. Therefore, the CNN discriminator is nicely suitable to the ECG sequences data modeling.

A series of noise data points that follow a Gaussian distribution are fed into the generator as a fixed length sequence. We assume that each noise point can be represented as a d -dimensional one-hot vector and the length of the sequence is T . Thus, the size of the input matrix is T × d .

The generator comprises two BiLSTM layers, each having 100 cells. A dropout layer is combined with a fully connected layer. The architecture of the generator is shown in Fig. 3 .

The current hidden state depends on two hidden states, one from forward LSTM and the other from backward LSTM. Eqs 6 and 7 are used to calculate the hidden states from two parallel directions and Eq. 9 calculates the output of the first BiLSTM layer at time t :

where the output depends on \({\overrightarrow{h}}_{t}\) and \({\overleftarrow{h}}_{t}\) , and h 0 is initialized as a zero vector.

Similarly, we obtain the output at time t from the second BiLSTM layer:

To prevent slow gradient descent due to parameter inflation in the generator, we add a dropout layer and set the probability to 0.5 38 . The output layer is a two-dimensional vector where the first element represents the time step and the second element denotes the lead.

The architecture of discriminator is illustrated in Fig. 4 . The pair of red dashed lines on the left denote a type of mapping indicating the position where a filter is moved, and those on the right show the value obtained by using the convolution operation or the pooling operation.

Structure of the CNN in the discriminator.

The sequence comprising ECG data points can be regarded as a time series sequence (a normal image requires both a vertical convolution and a horizontal convolution) rather than an image, so only one-dimensional (1-D) convolution need to be involved. We assume that an input sequence x 1 , x 2 , … x T comprises T points, where each is represented by a d -dimensional vector. We set the size of filter to h *1, the size of the stride to k*1 ( k ≪ h ), and the number of the filters to M . Therefore, the output size from the first convolutional layer is M * [( T − h )/ k + 1] * 1. The window for the filter is:

where 1 ≤ k * i + 1 ≤ T − h + 1 and h ≤ k * i − k + h ≤ T ( i ∈ [1, ( T − h )/ k + 1]).

The returned convolutional sequence c = [ c 1 , c 2 , … c i , …] with each c i is calculated as

where \(w\in {{\mathbb{R}}}^{h\times d}\) a shared weight matrix, and f represents a nonlinear activation function.

The successor layer is the max pooling layer with a window size of a*1 and stride size of b*1 . Each output from pooling p j for the returned pooling result sequence p = [ p 1 , p 2 , … p j …] is:

After conducting double pairs of operations for convolution and pooling, we add a fully connected layer that connects to a softmax layer, where the output is a one-hot vector. The two elements in the vector represent the probability that the input is true or false. The function of the softmax layer is:

In Table 1 , C1 layer is a convolutional layer, with the size of each filter 120*1, the number of filters is 10 and the size of stride is 5*1. The output size of C1 is calculated by:

where ( W , H ) represents the input volume size (1*3120*1), F and S denote the size of kernel filters and length of stride respectively, and P is the amount of zero padding and it is set to 0. Thus, the output size of C1 is 10*601*1.

In Table 1 , the P1 layer is a pooling layer where the size of each window is 46*1 and size of stride is 3*1. The output size of P1 is computed by:

where ( W , H ) represents the input volume size (10*601*1), F and S denote the size of each window and the length of stride respectively. Thus, calculated by Eq. 17 , the output size of P1 is 10*186*1.

The computational principle of parameters of convolutional layer C2 and pooling layer P2 is the same as that of the previous layers. It needs to be emphasized that the amount of kernels filters of C2 is set to 5 factitiously. With pairs of convolution-pooling operations, we get the output size as 5*10*1. A fully connected layer which contains 25 neurons connects with P2. The last layer is the softmax-output layer, which outputs the judgement of the discriminator.

In the experiment, we used a computer with an Intel i7-7820X (8 cores) CUP, 16 GB primary memory, and a GeForce GTX 1080 Ti graphics processing unit (GPU). The operating system is Ubuntu 16.04LTS. We implemented the model by using Python 2.7, with the package of PyTorch and NumPy. Compared to the static platform, the established neural network in PyTorch is dynamic. The result of the experiment is then displayed by Visdom, which is a visual tool that supports PyTorch and NumPy.

We used the MIT-BIH arrhythmia data set provided by the Massachusetts Institute of Technology for studying arrhythmia in our experiments. We downloaded 48 individual records for training. Each record comprised three files, i.e., the header file, data file, and annotation file. Each data file contained about 30 minutes of ECG data. In each record, a single ECG data point comprised two types of lead values; in this work, we only selected one lead signal for training:

where x t represents the ECG points at time step t sampled at 360 Hz, \({x}_{t}^{\alpha }\) is the first sampling signal value, and \({x}_{t}^{\beta }\) is the second one. Both were divided by 200 to calculate the corresponding lead value. The number of ECG data points in each record was calculated by multiplying the sampling frequency (360 Hz) and duration of each record for about 650,000 ECG data points. Therefore, we used 31.2 million points in total.

First, we compared the GAN with RNN-AE and RNN-VAE. All of the models were trained for 500 epochs using a sequence of 3120 points, a mini-batch size of 100, and a learning rate of 10 −5 . The loss of the GAN was calculated with Eq. 5 and the loss of RNN-AE was calculated as:

where θ is the set of parameters, N is the length of the ECG sequence, x i is the i th point in the sequence, which is the input of for the encoder, and y i is the i th point in the sequence, which is the output from the decoder.

where \({p}_{\theta }(\overrightarrow{z})\) is usually a standard prior N ~ (0, 1), \({q}_{\varphi }(\overrightarrow{z}|x)\) is the encoder, \({p}_{\theta }(x|\overrightarrow{z})\) is the decoder, and θ and ϕ are the sets of parameters for the decoder and encoder, respectively.

We extended the RNN-AE to LSTM-AE, RNN-VAE to LSTM-VAE, and then compared the changes in the loss values of our model with these four different generative models. Figure 5 shows the training results, where the loss of our GAN model was the minimum in the initial epoch, whereas all of the losses of the other models were more than 20. After 200 epochs of training, our GAN model converged to zero while other models only started to converge. At each stage, the value of the loss function of the GAN was always much smaller than the losses of the other models obviously.

We then compared the results obtained by the GAN models with those using a CNN, MLP (Multi-Layer Perceptron), LSTM, and GRU as discriminators, which we denoted as BiLSTM-CNN, BiLSTM-GRU, BiLSTM-LSTM, and BiLSTM-MLP, respectively. Each model was trained for 500 epochs with a batch size of 100, where the length of the sequence comprised a series of ECG 3120 points and the learning rate was 1 × 10 −5 . Figure 6 shows the losses calculated of the four GAN discriminators using Eq. 5 .

Loss of each type of discriminator. The four lines represent the discriminators based mainly on the structure with the CNN (red line), MLP (green line), LSTM (orange line), and GRU (blue line). ( a–d ) Represent the results after 200, 300, 400, and 500 epochs of training.

Figure 6 shows that the loss with the MLP discriminator was minimal in the initial epoch and largest after training for 200 epochs. The loss with the discriminator in our model was slightly larger than that with the MLP discriminator at the beginning, but it was obviously less than those of the LSTM and GRU discriminators. Eventually, the loss converged rapidly to zero with our model and it performed the best of the four models.

Finally, we used the models obtained after training to generate ECGs by employing the GAN with the CNN, MLP, LSTM, and GRU as discriminators. The dim for the noise data points was set to 5 and the length of the generated ECGs was 400. Figure 7 shows the ECGs generated with different GANs.

Results generated using different discriminator structures. ( a–d ) Represent the results obtained when the discriminator used the CNN, GRU, MLP, and LSTM respectively.

Figure 7 shows that the ECGs generated by our proposed model were better in terms of their morphology. We found that regardless of the number of time steps, the ECG curves generated using the other three models were warped up at the beginning and end stages, whereas the ECGs generated with our proposed model were not affected by this problem.

We then evaluated the ECGs generated by four trained models according to three criteria. The distortion quantifies the difference between the original signal and the reconstructed signal. We evaluated the difference between the real data and the generated points with the percent root mean square difference (PRD) 39 , which is the most widely used distortion measurement method.

The generated points were first normalized by:

where x [ n ] is the n th real point, \(\widehat{{x}_{[n]}}\) is the n th generated point, and N is the length of the generated sequence.

The root mean square error (RMSE) 39 reflects the stability between the original data and generated data, and it was calculated as:

The Fréchet distance (FD) 40 is a measure of similarity between curves that takes into consideration the location and ordering of points along the curves, especially in the case of time series data. A lower FD usually stands for higher quality and diversity of generated results.

Let P be the order of points along a segment of realistic ECG curve, and Q be the order of points along a segment of a generated ECG curve: \(\sigma (P)=({u}_{1},\,{u}_{2},\,\mathrm{...}\,{u}_{p})\) , \(\sigma (Q)=({\nu }_{1},\,{\nu }_{2},\,\mathrm{...}\,{\nu }_{q})\) . Then we can get a sequence which consists of couple of points: \(\{({u}_{{a}_{1}},{v}_{{b}_{1}}),\,\mathrm{...}({u}_{{a}_{m}},{v}_{{b}_{m}})\}\) . The length \(||d||\) of this sequence is computed by:

where d represents the Euclidean distance. Essentially, we have \({a}_{i+1}={a}_{i}\) or \({a}_{i+1}={a}_{i}+1\) and \({b}_{i+1}={b}_{i}\) as prerequisites.

Finally, the discrete Fréchet distance is calculated as:

Table 2 shows that our model has the smallest metric values about PRD, RMSE and FD compared with other generative models.

We can see that the FD metric values of other four generative models fluctuate around 0.950. The RMSE and PRD of these models are much smaller than that of the BiLSTM-CNN GAN. This indicates that except for RNN-AE, the corresponding PRD and RMSE of LSTM-AE, RNN-VAE, LSTM-VAE are fluctuating between 145.000 to 149.000, 0.600 to 0.620 respectively because of their similar architectures. Based on the results shown in Table 2 , we can conclude that our model is the best in generating ECGs compared with different variants of the autocoder. Table 3 shows that our proposed model performed the best in terms of the RMSE, PRD and FD assessment compared with different GANs.

Table 3 demonstrated that the ECGs obtained using our model were very similar to the standard ECGs in terms of their morphology. In addition, the LSTM and GRU are both variations of RNN, so their RMSE and PRD values were very similar.

From the results listed in Tables 2 and 3 , we can see that both of RMSE and FD values are between 0 and 1. Under the BiLSTM-CNN GAN, we separately set the length of the generated sequences and obtain the corresponding evaluation values. It is well known that under normal circumstances, the average heart rate is 60 to 100 in a second. Therefore, the normal cardiac cycle time is between 0.6 s to 1 s. Based on the sampling rate of the MIT-BIH, the calculated length of a generated ECG cycle is between 210 and 360. Figure 8 shows the results of RMSE and FD by different specified lengths from 50–400. From Fig. 8 , we can conclude that the quality of generation is optimal when the generated length is 250 (RMSE: 0.257 , FD: 0.728 ).

Results of RMSE and FD by different specified lengths.

To address the lack of effective ECG data for heart disease research, we developed a novel deep learning model that can generate ECGs from clinical data without losing the features of the existing data. Our model is based on the GAN, where the BiLSTM is used as the generator and the CNN is used as the discriminator. After training with ECGs, our model can create synthetic ECGs that match the data distributions in the original ECG data. Our model performed better than other two deep learning models in both the training and evaluation stages, and it was advantageous compared with other three generative models at producing ECGs. The ECGs synthesized using our model were morphologically similar to the real ECGs.

Wang, H. et al . Global, regional, and national life expectancy, all-cause mortality, and cause-specific mortality for 249 causes of death, 1980–2015: a systematic analysis for the Global Burden of Disease Study 2015. The Lancet 388 (10053), 1459–1544, https://doi.org/10.1016/S0140-6736(16)31012-1 (2016). Article Google Scholar

Wang, H. et al . Global, regional, and national life expectancy, all-cause mortality, and cause-specific mortality for 249 causes of death, 1980–2015: a systematic analysis for the Global Burden of Disease Study 2015. The Lancet 388 (10053), 1459–1544, https://doi.org/10.1016/S0140-6736(16)31012-1 (2016).

Lilly, L. S. Pathophysiology of heart disease: a collaborative project of medical students and faculty. Lippincott Williams & Wilkins , (2015).

Lilly, L. S. Pathophysiology of heart disease: a collaborative project of medical students and faculty. Lippincott Williams & Wilkins , (2015).

George, S. et al . Computerized extraction of electrocardiograms from continuous 12‐ lead holter recordings reduces measurement variability in a thorough QT study. The Journal of Clinical Pharmacology 52 (12), 1891–1900, https://doi.org/10.1177/0091270011430505 (2012). Article CAS PubMed Google Scholar

George, S. et al . Computerized extraction of electrocardiograms from continuous 12‐ lead holter recordings reduces measurement variability in a thorough QT study. The Journal of Clinical Pharmacology 52 (12), 1891–1900, https://doi.org/10.1177/0091270011430505 (2012).

Kampouraki, A., Manis, G. & Nikou, C. Heartbeat time series classification with support vector machines. IEEE Transactions on Information Technology in Biomedicine 13 (4), 512–518, https://doi.org/10.1109/TITB.2008.2003323 (2009). Article PubMed Google Scholar

Kampouraki, A., Manis, G. & Nikou, C. Heartbeat time series classification with support vector machines. IEEE Transactions on Information Technology in Biomedicine 13 (4), 512–518, https://doi.org/10.1109/TITB.2008.2003323 (2009).

Zhang, L., Peng, H. & Yu, C. An approach for ECG classification based on wavelet feature extraction and decision tree. In International Conference on Wireless Communications and Signal Processing (WCSP) , 1–4, https://doi.org/10.1109/WCSP.2010.5633782 (2010).

Zhang, L., Peng, H. & Yu, C. An approach for ECG classification based on wavelet feature extraction and decision tree. In International Conference on Wireless Communications and Signal Processing (WCSP) , 1–4, https://doi.org/10.1109/WCSP.2010.5633782 (2010).

Wei, Q. et al . Disease named entity recognition by combining conditional random fields and bidirectional recurrent neural networks. Database 10 , 1–8, https://doi.org/10.1093/database/baw140 (2016). Article Google Scholar

Wei, Q. et al . Disease named entity recognition by combining conditional random fields and bidirectional recurrent neural networks. Database 10 , 1–8, https://doi.org/10.1093/database/baw140 (2016).

Benali, R., Reguig, F. B. & Slimane, Z. H. Automatic classification of heartbeats using wavelet neural network. Journal of medical systems 36 , 883–892, https://doi.org/10.1007/s10916-010-9551-7 (2012). Article PubMed Google Scholar

Benali, R., Reguig, F. B. & Slimane, Z. H. Automatic classification of heartbeats using wavelet neural network. Journal of medical systems 36 , 883–892, https://doi.org/10.1007/s10916-010-9551-7 (2012).

McSharry, P. E. et al . A dynamical model for generating synthetic electrocardiogram signals. IEEE Transactions on Biomedical Engineering 50 , 289–294, https://doi.org/10.1109/TBME.2003.808805 (2003). Article PubMed Google Scholar

McSharry, P. E. et al . A dynamical model for generating synthetic electrocardiogram signals. IEEE Transactions on Biomedical Engineering 50 , 289–294, https://doi.org/10.1109/TBME.2003.808805 (2003).

Clifford, G. & McSharry, P. Generating 24-hour ECG, BP and respiratory signals with realistic linear and nonlinear clinical characteristics using a nonlinear model. Computers in Cardiology , 709–712, https://doi.org/10.1109/CIC.2004.1443037 (2004).

Clifford, G. & McSharry, P. Generating 24-hour ECG, BP and respiratory signals with realistic linear and nonlinear clinical characteristics using a nonlinear model. Computers in Cardiology , 709–712, https://doi.org/10.1109/CIC.2004.1443037 (2004).

Cao, H. et al . Design and evaluation of a novel wireless three-pad ECG system for generating conventional 12-lead signals. the Fifth International Conference on Body Area Networks , 84–90, https://doi.org/10.1145/2221924.2221942 (2010).

Cao, H. et al . Design and evaluation of a novel wireless three-pad ECG system for generating conventional 12-lead signals. the Fifth International Conference on Body Area Networks , 84–90, https://doi.org/10.1145/2221924.2221942 (2010).

Goodfellow, I. J. et al . Generative adversarial networks. Advances in Neural Information Processing Systems 3 , 2672–2680, https://arxiv.org/abs/1406.2661 (2014). Google Scholar

Goodfellow, I. J. et al . Generative adversarial networks. Advances in Neural Information Processing Systems 3 , 2672–2680, https://arxiv.org/abs/1406.2661 (2014).

Yao, Y. & Huang, Z. Bi-directional LSTM recurrent neural network for Chinese word segmentation. International Conference on Neural Information Processing , 345–353, https://arxiv.org/abs/1602.04874 (2016).

Yao, Y. & Huang, Z. Bi-directional LSTM recurrent neural network for Chinese word segmentation. International Conference on Neural Information Processing , 345–353, https://arxiv.org/abs/1602.04874 (2016).

Torres-Alegre, S. et al . Artificial Metaplasticity: Application to MITBIH Arrhythmias Database. Artificial Computation in Biology and Medicine, Springer International Publishing (2015).

Torres-Alegre, S. et al . Artificial Metaplasticity: Application to MITBIH Arrhythmias Database. Artificial Computation in Biology and Medicine, Springer International Publishing (2015).

Cho, K. et al . Learning phrase representations using RNN encoder--decoder for statistical machine translation. Empirical Methods in Natural Language Processing , 1724–1734, https://arxiv.org/abs/1406.1078 (2014).

Cho, K. et al . Learning phrase representations using RNN encoder--decoder for statistical machine translation. Empirical Methods in Natural Language Processing , 1724–1734, https://arxiv.org/abs/1406.1078 (2014).

Kingma, D. P. & Welling, M. Auto-encoding variational Bayes. International Conference on Learning Representations , 1–14, https://arxiv.org/abs/1312.6114 (2014).

Kingma, D. P. & Welling, M. Auto-encoding variational Bayes. International Conference on Learning Representations , 1–14, https://arxiv.org/abs/1312.6114 (2014).

Press, O. et al . Language generation with recurrent generative adversarial networks without pre-training. the 1st Workshop on Learning to Generate Natural Language at ICML 2017 , 1–5, https://arxiv.org/abs/1706.01399 (2017).

Press, O. et al . Language generation with recurrent generative adversarial networks without pre-training. the 1st Workshop on Learning to Generate Natural Language at ICML 2017 , 1–5, https://arxiv.org/abs/1706.01399 (2017).

Li, J. et al . Adversarial learning for neural dialogue generation. Empirical Methods in Natural Language Processing , 2157–2169, https://arxiv.org/abs/1701.06547 (2017).

Li, J. et al . Adversarial learning for neural dialogue generation. Empirical Methods in Natural Language Processing , 2157–2169, https://arxiv.org/abs/1701.06547 (2017).

Chen, X. et al . InfoGAN: interpretable representation learning by information maximizing generative adversarial nets. Advances in Neural Information Processing Systems , 2180–2188, https://arxiv.org/abs/1606.03657 (2016).

Chen, X. et al . InfoGAN: interpretable representation learning by information maximizing generative adversarial nets. Advances in Neural Information Processing Systems , 2180–2188, https://arxiv.org/abs/1606.03657 (2016).

Wang, Z. et al . Defo-Net: Learning body deformation using generative adversarial networks. International Conference on Robotics and Automation , https://arxiv.org/abs/1804.05928 , 2440–2447 (2018).

Wang, Z. et al . Defo-Net: Learning body deformation using generative adversarial networks. International Conference on Robotics and Automation , https://arxiv.org/abs/1804.05928 , 2440–2447 (2018).

Zhu J. et al . Unpaired image-to-image translation using cycle-consistent adversarial networks. International Conference on Computer Vision , 2242–2251, https://doi.org/10.1109/iccv.2017.244 (2017).

Zhu J. et al . Unpaired image-to-image translation using cycle-consistent adversarial networks. International Conference on Computer Vision , 2242–2251, https://doi.org/10.1109/iccv.2017.244 (2017).

Hüsken, M. & Stagge, P. Recurrent neural networks for time series classification. Neurocomputing 50 , 223–235, https://doi.org/10.1016/S0925-2312(01)00706-8 (2003). Article MATH Google Scholar

Hüsken, M. & Stagge, P. Recurrent neural networks for time series classification. Neurocomputing 50 , 223–235, https://doi.org/10.1016/S0925-2312(01)00706-8 (2003).

Graves, A. et al . Speech recognition with deep recurrent neural networks. International Conference on Acoustics, Speech, and Signal Processing , 6645–6649, https://doi.org/10.1109/ICASSP.2013.6638947 (2013).

Graves, A. et al . Speech recognition with deep recurrent neural networks. International Conference on Acoustics, Speech, and Signal Processing , 6645–6649, https://doi.org/10.1109/ICASSP.2013.6638947 (2013).

Gregor, K. et al . Draw: A recurrent neural network for image generation. International Conference on Machine Learning , 1462–1471, https://arxiv.org/abs/1502.04623 (2015).

Gregor, K. et al . Draw: A recurrent neural network for image generation. International Conference on Machine Learning , 1462–1471, https://arxiv.org/abs/1502.04623 (2015).

Cheng, M. et al . Recurrent neural network based classification of ecg signal features for obstruction of sleep apnea detection. IEEE International Conference on Computational Science and Engineering (CSE) and Embedded and Ubiquitous Computing (EUC) , 199–202, https://doi.org/10.1109/CSEEUC.2017.220 (2017).

Cheng, M. et al . Recurrent neural network based classification of ecg signal features for obstruction of sleep apnea detection. IEEE International Conference on Computational Science and Engineering (CSE) and Embedded and Ubiquitous Computing (EUC) , 199–202, https://doi.org/10.1109/CSEEUC.2017.220 (2017).

Hochreiter, S. & Schmidhuber, J. Long short-term memory. Neural Computation 9 , 1735–1780, https://doi.org/10.1162/neco.1997.9.8.1735 (1997). Article CAS PubMed Google Scholar

Hochreiter, S. & Schmidhuber, J. Long short-term memory. Neural Computation 9 , 1735–1780, https://doi.org/10.1162/neco.1997.9.8.1735 (1997).

Chung, J. et al . Gated feedback recurrent neural networks. International Conference on Machine Learning , 2067–2075, https://arxiv.org/abs/1502.02367 (2015).

Chung, J. et al . Gated feedback recurrent neural networks. International Conference on Machine Learning , 2067–2075, https://arxiv.org/abs/1502.02367 (2015).

Chauhan, S. & Vig, L. Anomaly detection in ECG time signals via deep long short-term memory networks. IEEE International Conference on Data Science and Advanced Analytics (DSAA) , 1–7, https://doi.org/10.1109/DSAA.2015.7344872 (2015).

Chauhan, S. & Vig, L. Anomaly detection in ECG time signals via deep long short-term memory networks. IEEE International Conference on Data Science and Advanced Analytics (DSAA) , 1–7, https://doi.org/10.1109/DSAA.2015.7344872 (2015).

Ravanelli, M. et al . Light gated recurrent units for speech recognition. IEEE Transactions on Emerging Topics in Computational Intelligence 2 , 92–102, https://doi.org/10.1109/tetci.2017.2762739 (2018). Article Google Scholar

Ravanelli, M. et al . Light gated recurrent units for speech recognition. IEEE Transactions on Emerging Topics in Computational Intelligence 2 , 92–102, https://doi.org/10.1109/tetci.2017.2762739 (2018).

Bowman, S. R. et al . Generating sentences from a continuous space. Conference on Computational Natural Language Learning , 10–21, https://doi.org/10.18653/v1/K16-1002 (2016).

Bowman, S. R. et al . Generating sentences from a continuous space. Conference on Computational Natural Language Learning , 10–21, https://doi.org/10.18653/v1/K16-1002 (2016).

Wang, J., He, H. & Prokhorov, D. V. A folded neural network autoencoder for dimensionality reduction. Procedia Computer Science 13 , 120–127, https://doi.org/10.1016/j.procs.2012.09.120 (2012). Article CAS Google Scholar

Wang, J., He, H. & Prokhorov, D. V. A folded neural network autoencoder for dimensionality reduction. Procedia Computer Science 13 , 120–127, https://doi.org/10.1016/j.procs.2012.09.120 (2012).

Zabalza, J. et al . Novel segmented stacked autoencoder for effective dimensionality reduction and feature extraction in hyperspectral imaging. Neurocomputing 185 , 1–10, https://doi.org/10.1016/j.neucom.2015.11.044 (2016). Article Google Scholar

Zabalza, J. et al . Novel segmented stacked autoencoder for effective dimensionality reduction and feature extraction in hyperspectral imaging. Neurocomputing 185 , 1–10, https://doi.org/10.1016/j.neucom.2015.11.044 (2016).

Kingma, D. P. et al . Variational dropout and the local reparameterization trick. Advances in Neural Information Processing Systems , 2575–2583, https://arxiv.org/abs/1506.02557 (2015).

Kingma, D. P. et al . Variational dropout and the local reparameterization trick. Advances in Neural Information Processing Systems , 2575–2583, https://arxiv.org/abs/1506.02557 (2015).

Den, Oord A. V. et al . Wavenet: a generative model for raw audio. the 9th ISCA Speech Synthesis Workshop , 1–15, https://arxiv.org/abs/1609.03499 (2016).

Den, Oord A. V. et al . Wavenet: a generative model for raw audio. the 9th ISCA Speech Synthesis Workshop , 1–15, https://arxiv.org/abs/1609.03499 (2016).

Mehri, S. et al . SampleRNN: an unconditional rnd-to-rnd neural audio generation model. International Conference on Learning Representations , 1–11, https://arxiv.org/abs/1612.07837 (2017).

Mehri, S. et al . SampleRNN: an unconditional rnd-to-rnd neural audio generation model. International Conference on Learning Representations , 1–11, https://arxiv.org/abs/1612.07837 (2017).

Mogren, O. C-RNN-GAN: Continuous recurrent neural networks with adversarial training. Advances in Neural Information Processing systems , 1–6, https://arxiv.org/abs/1611.09904 (2016).

Mogren, O. C-RNN-GAN: Continuous recurrent neural networks with adversarial training. Advances in Neural Information Processing systems , 1–6, https://arxiv.org/abs/1611.09904 (2016).

Donahue, C., McAuley, J. & Puckette, M. Synthesizing audio with GANs. the 6th International Conference on Learning Representations , 1–6, (2018).

Donahue, C., McAuley, J. & Puckette, M. Synthesizing audio with GANs. the 6th International Conference on Learning Representations , 1–6, (2018).

Kim, Y. Convolutional neural networks for sentence classification. Empirical Methods in Natural Language Processing , 1746–1751, https://doi.org/10.3115/v1/D14-1181 (2014).

Kim, Y. Convolutional neural networks for sentence classification. Empirical Methods in Natural Language Processing , 1746–1751, https://doi.org/10.3115/v1/D14-1181 (2014).

Gal, Y. & Ghahramani, Z. A theoretically grounded application of dropout in recurrent neural networks. Advances in Neural Information Processing Systems , 1027–1035, https://arxiv.org/abs/1512.05287 (2016).

Gal, Y. & Ghahramani, Z. A theoretically grounded application of dropout in recurrent neural networks. Advances in Neural Information Processing Systems , 1027–1035, https://arxiv.org/abs/1512.05287 (2016).

Almahamdy, M. & Riley, H. B. Performance study of different denoising methods for ECG signals. Procedia Computer Science 37 (37), 325–332, https://doi.org/10.1016/j.procs.2014.08.048 (2014). Article Google Scholar

Almahamdy, M. & Riley, H. B. Performance study of different denoising methods for ECG signals. Procedia Computer Science 37 (37), 325–332, https://doi.org/10.1016/j.procs.2014.08.048 (2014).

Aronov B. et al . Fréchet distance for curves, revisited. European Symposium on Algorithms , 52–63, https://doi.org/10.1007/11841036_8 (2006). Google Scholar

Aronov B. et al . Fréchet distance for curves, revisited. European Symposium on Algorithms , 52–63, https://doi.org/10.1007/11841036_8 (2006).

This study was supported by the National Natural Science Foundation of China (61303108, 61373094, and 61772355), Jiangsu College Natural Science Research Key Program (17KJA520004), Suzhou Key Industries Technological Innovation-Prospective Applied Research Project (SYG201804), and Program of the Provincial Key Laboratory for Computer Information Processing Technology (Soochow University) (KJS1524).

School of Computer Science and Technology, Soochow University, Suzhou, 215006, China Fei Zhu, Fei Ye & Quan Liu

School of Computer Science and Technology, Soochow University, Suzhou, 215006, China

Provincial Key Laboratory for Computer Information Processing Technology, Soochow University, Suzhou, 215006, China Fei Zhu

Provincial Key Laboratory for Computer Information Processing Technology, Soochow University, Suzhou, 215006, China

School of Computer Science and Engineering, Changshu Institute of Technology, Changshu, 215500, China Yuchen Fu

School of Computer Science and Engineering, Changshu Institute of Technology, Changshu, 215500, China

Institutes for Systems Genetics, West China Hospital, Sichuan University, Chengdu, 610041, China Bairong Shen

Institutes for Systems Genetics, West China Hospital, Sichuan University, Chengdu, 610041, China

Fei Zhu View author publications Search author on: PubMed Google Scholar

Fei Ye View author publications Search author on: PubMed Google Scholar

Yuchen Fu View author publications Search author on: PubMed Google Scholar

Quan Liu View author publications Search author on: PubMed Google Scholar

Bairong Shen View author publications Search author on: PubMed Google Scholar

F.Z. and F.Y. performed the computational analyses; F.Z. and Y.F. performed the validation work; F.Z., F.Y. and Q.L. wrote the manuscript; B.S. coordinated the study.

The authors declare no competing interests.

Publisher’s note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ .

Zhu, F., Ye, F., Fu, Y. et al. Electrocardiogram generation with a bidirectional LSTM-CNN generative adversarial network. Sci Rep 9 , 6734 (2019). https://doi.org/10.1038/s41598-019-42516-z

DOI : https://doi.org/10.1038/s41598-019-42516-z

DOI : https://doi.org/10.1038/s41598-019-42516-z

Anyone you share the following link with will be able to read this content:

Sorry, a shareable link is not currently available for this article.

Provided by the Springer Nature SharedIt content-sharing initiative

Sign up for the Nature Briefing: AI and Robotics newsletter — what matters in AI and robotics research, free to your inbox weekly.
