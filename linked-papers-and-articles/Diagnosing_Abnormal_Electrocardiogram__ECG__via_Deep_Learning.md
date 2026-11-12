# Diagnosing Abnormal Electrocardiogram (ECG) via Deep Learning

**Source:** https://www.intechopen.com/online-first/diagnosing-abnormal-electrocardiogram-ecg-via-deep-learning

---

Home > Books > Practical Applications of Electrocardiogram

Diagnosing Abnormal Electrocardiogram (ECG) via Deep Learning

Submitted: 02 October 2018 Reviewed: 27 February 2019 Published: 03 April 2019

Practical Applications of Electrocardiogram

Total Chapter Downloads on intechopen.com

In this chapter, we investigate the most recent automatic detecting algorithms on abnormal electrocardiogram (ECG) in a variety of cardiac arrhythmias. We present typical examples of a medical case study and technical applications related to diagnosing ECG, which include (i) a recently patented data classifier on the basis of deep learning model, (ii) a deep neural network scheme to diagnose variable types of arrhythmia through wearable ECG monitoring devices, and (iii) implementation of the health cloud platform, which consists of automatic detection, data mining, and classifying via the Android terminal module. Our work establishes a cross-area study, which relates artificial intelligence (AI), deep learning, cloud computing on huge amount of data to minishape ECG monitoring devices, and portable interaction platforms. Experimental results display the technical advantages such as saving cost, better reliability, and higher accuracy of deep learning-based models in contrast to conventional schemes on cardiac diagnosis.

Xin Gao * Department of Electrical and Computer Engineering, The University of Arizona, Tucson, AZ, USA

Department of Electrical and Computer Engineering, The University of Arizona, Tucson, AZ, USA

*Address all correspondence to: xgao1985@email.arizona.edu

Statistical reports indicated that the leading cause of death in the world comes from cardiovascular diseases [ 9 , 20 ]. The World Health Organization (WHO) reported that the total number of deaths from cardiovascular diseases in 2012 was approximately 17.5 million, compared with 17.7 million in 2015, and this number has been increasing every year [ 1 , 3 , 9 ]. With the accelerating pace of life, more and more young people suffer from great pressure related to work, and completely ignore physical examinations, which increases the risk of sudden death [ 9 ]. Hence, monitoring ECG and performing automatic diagnosis become particularly important. In cardiology, the electrical actions of a human’s heart are simply and painlessly recorded by electrocardiogram (ECG) via single or multiple-lead detections [ 8 , 20 ]. The real-time ECG sequence of a patient represents one of the most useful clinical diagnostic features on cardiovascular diseases, reflecting the electrophysiological activity of cardiac excitement, and indicating great importance on the aspects of basic heart functions and related pathological research [ 12 ]. Meanwhile, ECG is of crucial importance for analyzing and identifying various arrhythmias, which reflect the degree of myocardial damage, the corresponding development process, and the functional structure of both atria and ventricles [ 3 , 12 ]. A few research scholars have related medical evidence of ECG toward arrhythmias with the latest experimental study, see [ 3 , 4 , 12 , 23 , 29 ], and the references therein.

Typical anomaly behaviors in ECG refer to irregular heartbeats, which are often recognized as sinus arrhythmia, ectopic tachycardia, cardiac flutter and tremor, and heart block [ 12 ]. The ectopic tachycardia is also known as premature contraction, standing for the most common types of cardiac arrhythmias. Classification of arrhythmias can be in accordance with a cardiac pacemaker and the conduction process [ 9 , 12 ]: abnormal pacemakers may lead to arrhythmias and fluctuated heart rates, including atrial fibrillation, ventricular fibrillation (either sinus, supraventricular, or ventricular), tachycardia and bradycardia; abnormal cardiac conduction system results into heart blocks such as atrioventricular block and intraventricular block, etc. Atrioventricular block takes place in the atrioventricular node, the His bundle and its branches, while ventricular conduction block occurs in the left and right bundle branches. Specifically, no obvious symptoms appear in left bundle branch block, while coronary and rheumatic heart diseases as well as acute myocardial infarction often accompany right bundle branch block. Healthy people come along with occasional atrial premature beats, while ventricular premature beats are often associated with some kind of organic lesion. Several distortions on QRS wave and ST segments could appear in those cardiac arrhythmias [ 12 ].

Previously reported medications and medical procedures such as pacemaker insertion and surgery offer well-established treatments for most arrhythmias; meanwhile, a large quantity of signal and image processing algorithms as well as sensor devices provided useful tools on electrocardiogram-assisted diagnosis [ 8 , 18 , 20 , 26 , 31 , 32 ]. Recently, many researchers have been devoting themselves on computer-aided ECG analysis, where the technical developments are enriched from the booming growth on machine learning and deep learning algorithms [ 6 , 9 , 11 , 13 , 14 , 15 , 16 , 17 , 21 , 24 , 25 , 27 , 30 , 33 , 35 , 36 , 37 ]. Their methodology of study is broadly categorized as conventional machine learning and deep learning. Traditional machine learning schemes are greatly affected by data, which demands complex preprocessing such as noise removal and data normalization. Besides, it is also vulnerable to over-extract unnecessary features, requiring filter design and sorting out redundant features, and then finally input another algorithm for classification [ 10 , 16 , 19 , 21 , 25 , 26 , 27 , 28 ]. While good effects on recognition got achieved, the overall procedure is more complicated than those of the deep learning schemes [ 1 , 6 , 9 , 14 , 17 , 21 , 25 , 27 ]. Hence, previous machine learnings are no longer suitable to be embedded into mobile devices or perform real-time analysis [ 15 ].

For some of the deep learning-based schemes [ 1 , 9 , 13 , 14 , 15 , 17 , 25 , 27 ], it is not only unnecessary to perform accurate denoising on the data, but also automatically extract the features in order to achieve the expected ideal recognition results. Common training modes of algorithmic ECG diagnosis usually compose single lead and multilead [ 9 ]. Multilead data combined with multichannel neural network algorithms (MCNN) are capable of achieving considerably good results; however, their shortcomings display on the relatively larger training parameters of models and much longer training time, which increases the difficulties to realize real-time monitoring associated with the existing mobile devices [ 9 , 10 , 31 , 32 ]. Comparing to single-lead ECG data processing, the performance of recognition by multilead can be achieved with satisfactory, i.e., using the AlexNet structure, while the weakness lies on that these methods were regarded as relatively out of date [ 9 ].

The remainder of this chapter is organized as follows. In Section 2, several typical algorithms are briefly described on how deep learning-based light-quantity level algorithms recognize ECG data, and how the principles of deep learning are related on accurately diagnosing cardiac arrhythmia. Section 3 introduces a recently patented ECG data classifier with deep learning-based model. The automatic ECG arrhythmia diagnosing system and Android health cloud platform are referenced in Section 4. The last Section 5 prospects the progress on cross-area study of artificial intelligence-(AI)-related ECG diagnosis and draws our conclusions.

2. Deep learning theory and automatic ECG diagnosis

Since ECG periodically reflects the variations on electrical activities of a human’s heart and real-time monitoring indicates parallel processing on amazing amount of data, automatic ECG diagnosis calls for efficient classification techniques on extracting unsupervised data features in practical ways. Many previous statistical signal processing or machine learning schemes utilize some dimensional reduction methods (i.e., linear discriminate analysis (LDA), independent component analysis (ICA), principle component analysis (PCA), etc.) to release the complexity issues, while it is the fact that practically most of the feature selection schemes are still dependent on human labor [ 9 ]. Deep learning is developed from artificial neural networks to simulate the input and output of neurons and the process of excitatory transmission of signals [ 9 , 21 , 25 ]. While early neural network (perceptron) only aimed to solve the linear separable problem, deep learning models connect some hidden layer(s) with an activation function between the input and output layers to obtain multilayer perceptions (MLP) [ 9 ]. Expanded cascades on the hidden layer of neurons indicate that the ability of network learning is deepened, and hence, any arbitrary continuous function of arbitrary complexity was proved to be effectively approached (in any level of accuracy), given an expression of a functional model, while the by-products turn to be increased network parameters and difficulty on training [ 9 ].

Two representative training methods in deep learning-based ECG diagnosis include the back-propagation (BP) algorithm and deep belief network (DBN) [ 1 , 8 , 28 ], where the former still fails to overcome the error dissipation effect in the process of back-propagation, and the latter is suitable for layer-by-layer unsupervised learning via using a small portion of labeled samples for global optimization; for feature learning, DBN makes full use of unlabeled data and reduces the cost via the strategy of “pretraining and minor tuning” [ 9 ]. Other applicable deep network structures applied in latest works on automatic ECG analysis comprise fundamental or variation schemes related to classical MLP, convolutional neural networks (CNN), and recurrent neural networks (RNN) [ 9 , 22 ]. A schematic diagram of CNN-based arrhythmia classification is displayed in Figure 1 [ 9 ].

A schematic diagram of CNN-based automatic arrhythmia classification from ECG [ 9 ].

A schematic diagram of CNN-based automatic arrhythmia classification from ECG [ 9 ].

The three basic features of CNN, known as locally receptive field, shared weights and pooling, are reflected inside of the input and output layers in Figure 1 as depicted above [ 9 ]: the convolutional layer exploits sample information fragments in the form of moving windows (locally acceptable domain) to continuously learn the entire information of samples, and traverse to obtain multiple feature maps by weight sharing, which is the convolution layer. The pool layer performs data compression on the feature map of convolutional layer in order to simplify its output. Frequently used max-pool operation filters out all redundant values except the maximum value in the sample region, and then transforms the data to improve the algorithmic robustness. The upper fully layer corresponds to the network output, and the combination of convolution layer, and pool layer can also be inserted with full layers to acquire middle outputs. Since diagnosing ECG is also a task of time series analysis, its information is mainly expressed by the spatial structure, and the information output by each channel of the multilead ECG is not identically the same. The chest V1 lead signal and the limb II lead signal are both inputs into the neural network, and the output layer performs classification on different types of arrhythmia [ 9 ].

While applying deep learning theory in automatic ECG diagnosis and arrhythmia classification, in addition to BP algorithm, CNN and fully connected feedforward neural network (FCFNN), the gradient descent training algorithm also suggests a feasible candidate [ 9 , 22 ]. In the optimization process of training, the follow-up methods such as target function selection, dropout technique, and Nesterov impulse update are capable of improving the training efficiency and reduce the probability of over-fitting on sequential processing of ECG data [ 9 , 22 ]. Regarding to RNN as mentioned above, its variation model named as long-short-term memory (LSTM) [ 18 , 22 ] had been applied to classify arrhythmia, where the two share the same network structure, while the neurons in hidden layer got replaced with loop-connected memory units [ 18 ]. A standard memory unit contains single/multiple self-connected memory unit and three multiplication units (input/output gates and forgotten gate). Among the consecutive operations of “write,” “read,” and “reset,” the forgotten gate offers a self-reset scheme for memory units, which is crucial to demand LSTM to “forgot” the previously loaded tasks [ 18 ]. A single cell-unit-based classical LSTM memory unit model is depicted in Figure 2a , and the schematic diagram of LSTM-based arrhythmia classification model is shown in Figure 2b .

LSTM-based single cell-unit model and schematic diagram for arrhythmia classification [ 18 ].

LSTM-based single cell-unit model and schematic diagram for arrhythmia classification [ 18 ].

The LSTM-based model represents another deep learning scheme on diagnosing abnormal ECG and performing automatic arrhythmia classification [ 18 ]. With an input layer and two hidden layers, it cascades the SoftMax classifier as the last layer, which comprises five nodes that correspondingly stands for N, S, V, F, and Q [ 18 ]. Preprocessed ECG segments were taken as input data into LSTM to proceed with layer-to-layer feature learning and mapping, then the deep-level ECG signal features were sent to SoftMax classifier to perform training, from which the acquired weights follow-up with the initialization step and weight optimization step by BP algorithm so as to converge into the global optimal of LSTM network model, and finally achieve the goal of arrhythmia classification [ 18 , 22 ]. The LSTM model overcame the dependence of traditional features on ECG signals, solved the problem of gradient elimination that early neural networks occur, and achieved data mining on the distinctive deep features behind large pool of ECG data via the proposed self-learning style [ 18 ].

In 2017, computer scientists in Stanford University claimed that they have developed a deep learning scheme on accurate diagnosing various types of arrhythmia, which achieved the grading level of diagnosing as high as professional cardiologists [ 2 , 38 ]. Such kind of deep learning-based schemes can sieve irregular heartbeats from sequential data of several hours. It is common to view arrhythmia from ECG, while doctors often supply patients with portable ECG that consecutively monitors their heartbeats since portable wearing devices are able to generate data in hundreds of hours [ 2 ]. Research scholars and a heartbeat monitoring company named as IRhythm have been working together to investigate accurate detection of deep CNN models toward large amount of concentrated, irregular ECG data [ 34 , 38 , 39 ]. It was claimed by these scholars that their proposed algorithm performed much better comparing to professional cardiologists when diagnosing 13 different types of arrhythmia [ 2 ]. Benefited from accelerating diagnosis and improving treatments, the algorithmic accuracy even exceeds those obtained by cardiological doctors. Besides, their ECG algorithm was expected to help people in remote areas gain some assistance from cardiological experts: performing some kind of anomaly detection, associated with processing various types of anomalous arrhythmia in high precision [ 2 , 38 ]. Applying their algorithm to monitor ECG of potential arrhythmia patients can be imaged in the following scenarios: when patients first come to see the doctor in office, if the wearable ECG device does not detect any problem, doctors would possibly allow the potential patient to use portable devices and monitor heartbeats consecutively for 2 weeks; hence, the crossover range of time generating data by the device is longer than 300 hours. After the second appointment, doctors may analysis the data of every second to discover any hint on arrhythmia [ 2 ].

Analyzing arrhythmia was in fact a data processing problem, as was found by Dr. Andrew Ng, a well-known artificial intelligence (AI) expert leading Stanford’s machine learning team, where the deep learning algorithm they developed aims to diagnose different types of arrhythmias from ECG inputs [ 2 ]. Cooperating with companies, which provide wearable rhythm monitoring equipment, about 36,000 ECG data samples were acquired to train a deep neural network model, which was later proved to be more accurate than a cardiologist in diagnosing arrhythmias, and performs even better than a doctor in most cases [ 2 , 38 ]. Their trained 34-layer CNN model is depicted in Figure 3 , where a single-lead wearable heart device monitors ECG, and the objective is oriented on correct detection of the sinus rhythm (SINUS) and atrial fibrillation (AFIB). The input after preactivation, followed by 33 convolution layers in cascades, one fully connected layer at the last and a SoftMax, contributed the entire architecture of this trained deep neural network [ 38 ].

The trained 34-layer CNN on arrhythmia detection on time-series ECG of random length [ 38 ].

The trained 34-layer CNN on arrhythmia detection on time-series ECG of random length [ 38 ].

Research scholars discovered that many types of arrhythmia are similar on occurrence, while their differences are trivial; however, it has a great impact on how to deal with a specific arrhythmia: for instance, two types of arrhythmias were known as secondary atrioventricular block and showed very similar appearance, while one requires no treatment and the other urges immediate observation [ 2 , 12 , 22 ]. Their research products are not only able to discover signs of arrhythmia, but also expose different types of arrhythmia with unprecedented high precision [ 22 ]. The advantage of this deep CNN-based algorithm lies that it never become exhausted and continuously performs immediate diagnosis of arrhythmia, which further benefits patients who are unable to see a cardiologist in remote areas or a developing country [ 2 ]. When a potentially fatal heart rhythm appears in high-risk groups, one who wears a daily-used rhythm monitoring device will immediately respond and notify emergency personnel to aid the individual(s) with professional arrhythmia diagnosis [ 2 , 38 ].

3. Automatic ECG diagnosis via deep learning: lightweight classifier

Among the architecture model of deep learning-based schemes on automatic ECG diagnosis, reducing the computational cost, network parameters and training difficulties, will represent crucial problems. In order to solve these issues mentioned above, research scholars have been seeking for an ideal technical solution. A deep learning research lab in Zhengzhou University established a lightweight algorithm on automatic ECG data diagnosis, in which the elements on technical realization are displayed as below [ 40 ]: the objective is to provide a deep learning-based lightweight algorithm for identifying ECG data, which aims at the deficiencies of the current techniques. This invention takes along with a technical plan of identifying the ECG data based on deep learning, which includes the following steps [ 40 ]:

Step 1: Perform rough extraction of data features. The extracted ECG data are conveyed through a standard convolution layer

Step 2: Pass the rough extracted data features through a pooling layer max-pooling, then send these features to the core Lite module to extract deep-level data features

Step 3: Send the deep-level data features through a pooling layer max-pooling, then the two full-connection layers, named as dense, will receive these features by turns and perform purification

Step 4: Transmit the purified data features to the classifier function and proceed with outputs after feature classification.

A flowchart on the operating procedures with respect to this invention is depicted in Figure 4 , and the diagram of its core module, the deep learning-based light weight algorithm, is shown in Figure 5 .

The flowchart of automatic ECG classifier.

The flowchart of automatic ECG classifier.

Core modules of deep-learning based lightweight algorithm.

Core modules of deep-learning based lightweight algorithm.

Regarding to the core module as proposed on invention, the max-pooling layer plays an anti-overfitting effect in the entire structure model and ensures the classification accuracy. The activation function of each convolutional layer including the fully connected layer is named as LeakReLU [ 40 ]. When performing the optimization step by the Adam optimizer, the learning rate was set as 0.001. The specific setting parameters of this algorithmic model are presented as below.

Based on the analysis as described above, the activation functions of each convolutional layer and fully connected layer are implemented by LeakReLU, while the model is optimized using the Adam optimizer [ 40 ]: the learning rate is set as 0.001. In Step 1, the convolution kernel of the standard convolutional layer is set as 1 × 5 with step size of 1; the convolution kernel size of the pooled layer max-pooling is set as 1 × 2, with step size of 2; the convolution kernel size of the squeeze convolution layer and the first standard convolution layer are both set as 1 × 1 with step size of 1; similarly, with the same step size, convolution kernels of the second and third standard convolutional layers are set as 1 × 2 and 1 × 3, respectively; the convolution kernels of the depthwise convolutional layers match the same size with their follow-up standard convolution layers, their step sizes are set as 1; and the convolution kernel of the pointwise convolution layer is also set as 1 × 1 with step size of 1.

In Step 2, the function of core module lite is to install the squeeze convolution layer on compressing feature data outputted by the upper layer; after the layer of squeezed convolutions, the standard convolutions of three different channels were set to extract data features of different local sizes; the rough data features are transmitted through a depthwise convolution layer and a pointwise convolution layer after the second and the third standard convolutional layers; a residual connection is also constructed on the terminal right side of the squeeze convolution layer; finally, the outputs of filter concatenation are performed after the first standard convolution layer, pointwise convolution layer, and the residual connections [ 40 ].

It should be noted that the standard convolution layer in the invented automatic ECG classifier, performs a conventional convolution operation, which is named as standard convolutional layer for distinctions; the compression convolution layer is obtained by compressing the amount of feature data in the upper layer so as to reduce the computational load for convolution operation of the next layer. For example, if the upper layer outputs 10 feature data and the compressed convolution layer sets up five convolution kernels, then 5 feature data will be released, which means the input of next layer has five feature data. Deep convolution and pointwise convolution actually divide the ordinary standard convolution operation into two steps [ 40 ]: the first step is to exploit the deep convolution layer to perform convolution operations separately on each feature data of the previous layer, which indicates that a convolution kernel only convolves one feature data. In the second step, the pointwise convolution, which is the 1 × 1 convolution kernel, performs feature combination operations on the output after deep convolution.

By adopting the invented deep learning-based lightweight algorithm and through the setting of a core module, this model is trained to guarantee a certain accuracy in absence of demanding much computational cost. In contrast to other detection algorithms, the proposed scheme takes less time, displays faster prediction, and reduces personal consumption. The well-trained software platform can be embedded into a wearable ECG device or the mobile phone terminals to classify and monitor the collected ECG data, and triggers an alarm in case an abnormality is encountered. The embedded device is not only free of spending extra time affecting daily work, but also arouses people to pay enough attention on cardiac abnormalities and regularly perform physical examination; hence, the incidence of heart disease can be significantly reduced [ 40 ].

Comparing to the existing methods, this deep learning-based lightweight algorithm on invention has substantive features and significant advances, which can be specifically referred as [ 40 ]: Core module stands for an innovative design module of structural fusion, which combines multilayer convolution kernel structure of the famous GoogleNet, the compressive convolution idea of SqueezeNet, and the depth-pointwise convolution on parameter reduction of MobileNets. By implementing the classical AlexNet network structure, the entire framework was designed to ensure the stability of algorithmic model. Compared with other algorithms, this invented model does not require many computational parameters while ensures certain recognition effects; it also has the capacity on automatically realizing the processing of sequential ECG data on limited network resources or running memory.

Core module stands for an innovative design module of structural fusion, which combines multilayer convolution kernel structure of the famous GoogleNet, the compressive convolution idea of SqueezeNet, and the depth-pointwise convolution on parameter reduction of MobileNets. By implementing the classical AlexNet network structure, the entire framework was designed to ensure the stability of algorithmic model.

Core module stands for an innovative design module of structural fusion, which combines multilayer convolution kernel structure of the famous GoogleNet, the compressive convolution idea of SqueezeNet, and the depth-pointwise convolution on parameter reduction of MobileNets. By implementing the classical AlexNet network structure, the entire framework was designed to ensure the stability of algorithmic model.

Compared with other algorithms, this invented model does not require many computational parameters while ensures certain recognition effects; it also has the capacity on automatically realizing the processing of sequential ECG data on limited network resources or running memory.

Compared with other algorithms, this invented model does not require many computational parameters while ensures certain recognition effects; it also has the capacity on automatically realizing the processing of sequential ECG data on limited network resources or running memory.

As specified by several steps mentioned above, the lightweight algorithm for identifying ECG data based on deep learning can be realized via uniprocessors in parallel computing, in which the convolution manner of each convolution layer is convolution of one-dimensional ECG data [ 40 ]. Brief notation on implementation is presented as follows: x [ n ] and y [ n ] denote the input and the output sequences, respectively; h [ n ] represents the convolution kernel weight sequence, h [ −k ] represents the inversion of the h [ k ] sequence, h [ N − k ] indicates that h [ −k ] is moved by n points; m stands for the length of input sequence, while the length of output sequence is expressed as len( x [ n ]) + len( h [ n ]) − 1. Because the classifier function is a SoftMax function classifying five types of ECG data, each type of ECG data is recorded as a neuron in the SoftMax function, which appears in the form as a product of the upper neuron output and the weight of SoftMax function connected to the upper neuron [ 40 ]. Hence, by constructing the loss function and the linear regression model, the output probability of each neuron and each neural unit can be modeled through vector calculus and probabilistic interpretation, which finally achieves the prediction value of output.

To sum up, the technical invention [ 40 ] provides a deep learning-based lightweight algorithm for automatic ECG data identification and diagnosis, where its procedure consists of extracting the extracted ECG data through a standard convolution layer, and performing rough extraction of data features; while a feature is passed through a max-pooling layer, the core module is sent to the kernel lite module to extract deep data features. Note that after passing the deep data features through a pooled layer max-pooling, those features will be sequentially loaded into two fully connected layers named as dense, in which purification is performed on the hierarchical data features; in the next step, the classifier function takes responsibility for feature classification on the output of purified data features. Compared with other similar schemes on automatic ECG diagnosis [ 5 , 7 , 16 , 27 , 31 , 36 ], the invented lightweight algorithm has been released from requiring large set of calculation parameters but still ensures constant accuracy on recognition effects, which is able to realize parallel processing of ECG data despite of limited network resources or running memory on GPU [ 40 ].

4. Automatic detection system for arrhythmias and the Android health cloud platform

While the current methods on network medical treatments are often restricted to the interactions between doctors and patients via modern communication tools, it is neither possible to establish mutual trust nor collect real-time data. Hence, wearable ECG monitoring systems and applicable software platforms (typically integrated into Android terminal modules in a cellphone, for daily use) are calling for proposal. Recently, the health cloud platform for arrhythmia detection [ 9 ] and the ThingSpeak cloud computing platform [ 41 ] on classifying and diagnosing ECG had been proposed to solve some prior problems at different levels. Utilizing deep learning tools and the intelligent information integration platform named as the Internet of Things (IoT) [ 9 , 41 ], a new follow-up mode of automatic heart monitoring system was developed for real-time remote services among doctors and patients in a long term. The system established a cloud platform on health inquiry, providing medical data management services for online patients. Aiming at reducing potential risks for cardiovascular diseases, this platform offers online assessment, diagnosis, and rehabilitation guidance by relevant doctors [ 9 ]. Regarding to offline services, this system relies on existing medical-level biosensors to construct terminals on signal acquisition and processing [ 9 ]. For real-time ECG sequence, it provides functions such as collection, exhibition, and analytical monitoring of basic physiological parameters, and constructs a communication platform for doctors and patients with respect to their practical demands. The deep learning-based detection algorithm was integrated into the arrhythmia automatic diagnosis system within the module of health monitoring control, which performs real-time remote surveillance and outputs feedbacks on the ECG signals collected by the biosensors [ 9 ].

The system hardware mainly comprises a monitor system and an Android terminal [ 9 ]: a monitor system module is responsible for measuring and collecting data of vital signs such as ECG, blood pressure and body temperature, etc., then transmitting real-time data to the Android terminal module via serial port or Bluetooth and thereby completing the tasks of uploading data and synchronous exhibition, followed by performing automatic diagnosis (including real-time analysis) of possible arrhythmia data in the ECG sequence. The hardware of system monitor module adopts PM6750 for medical signal processing. RK3188 development motherboard with quad-core Cortex-A9 processor was chosen for hardware design on the Android terminal module. Original ECG data were sent to the terminal through the monitoring devices where the mode of asynchronous serial port transmission is applied, no parity bit exists, and the baud rate is 115,200 Baud. According to the protocol, Android terminal module parses the restored signal data including waveforms, heart rate and breathing, styles of single-lead or multilead, filtering, and signal gain. The parsed data can be uploaded to the cloud platform and saved as private health data for each client. Historical data can be viewed by each individual at any time through the browser to provide health channels and follow-up support on clinical treatments [ 9 ]. While ThingSpeak employed similar datasets on MIT database for ECG data, the proposed online monitoring system displays comparable outputs on ECG signals using principle component analysis (PCA), which is depicted in Figure 6 [ 41 ]. The online MATLAB programs are running through the ThingSpeak IoT cloud for automatic ECG data analysis, which enables doctors to monitor, diagnose, and improve the health of patients [ 41 ]; meanwhile, the call for emergency service ensures local first-aid institutions to respond at prompt time in order to minimize any risk issues in absence of proper treatments [ 9 , 41 ].

In another scenario on the workflow of system, the automatic arrhythmia detection system starts with a network of bio-sensors, where the input signals follow the arranged entry to the bio-data acquisition module followed by the control module on health monitoring, and then uploaded into the cardiovascular health cloud platform for data analysis in Android systems [ 9 ]. Those mobile devices provide supplemental aid on building up virtual human models in digital physiological bases, simulating medical plans on treatment and predicting potential risks on disease. With the helpful support of remote clinical diagnosis in collaboration of artificial intelligence-based solutions such as electronic health and digital medicine plans, the comprehensive online medical cloud platform will come into reality very soon [ 9 ]. For broader applications on biomedical data management and access, Navale and Bourne [ 42 ] proposed a conceptual framework to show how the data producers, consumers and repositories got integrated via a cloud-based platform; meanwhile, the open data and analytics must follow the principle of findable, accessible, interoperable and reusable (FAIR) to upgrade the discovery and innovation of knowledge. The architecture-based conceptual framework was depicted in Figure 7 , where API stands for applicable programming interface [ 42 ].

The proposed ThingSpeak online monitoring system for ECG analytics using PCA [ 41 ].

The proposed ThingSpeak online monitoring system for ECG analytics using PCA [ 41 ].

The architecture of conceptual framework on cloud-based platform: variable data types flow between producers and consumers in support of the FAIR principle and in demands of different data level needs [ 42 ].

The architecture of conceptual framework on cloud-based platform: variable data types flow between producers and consumers in support of the FAIR principle and in demands of different data level needs [ 42 ].

In this chapter, we have established a study on deep learning theory related to automatic diagnosis on abnormal electrocardiogram (ECG). We briefly introduced the most recent automatic detecting schemes such as convolutional neural networks (CNN), recurrent neural networks (RNN) [ 9 , 22 , 34 , 39 ], and its variation of long-short-term memory (LSTM) model [ 18 , 22 ], which aims on analyzing different types of cardiac arrhythmias. We presented an investigation of practical examples and applications of deep learning on automatic ECG diagnosis [ 5 , 7 , 16 , 27 , 31 , 36 ], which consists of a deep learning-based lightweight classifier on ECG data identification, deep belief network (DBN) [ 1 , 8 , 28 ] on diagnosing cardiac arrhythmia via wearable ECG monitoring devices, and a health cloud platform on automatic ECG detection, data mining and classification. We combined the theoretical concepts of artificial intelligence (AI)-oriented topics such as deep learning, big data health cloud platform to real medical applications, i.e., minishape ECG monitoring devices [ 9 , 41 ], domestic cardiac arrhythmia analyzer [ 40 ], automatic ECG diagnosis on Android terminal modules [ 9 ] and the conceptual framework on managing and accessing biomedical data [ 42 ]. Technical advantages such as low-power consumption, higher accuracy, better reliability, and cost saving on the links of feasible software/hardware implementations to automatic cardiac arrhythmia diagnosis prospects broader applications of deep learning on ECG and other data analytics on medical imaging.

1. Altan G, Allahverdi N, Kutlu Y. A multistage deep learning algorithm for detecting arrhythmia. 1st International Conference on Computer Applications & Information Security (ICCAIS). Riyadh: 2018. pp. 1-5; DOI: 10.1109/CAIS.2018.8441942

2. Anonymous. Professors in Stanford University of USA developed a new algorithm on diagnosing 13 types of arrhythmias. Journal of Practical Electrocardiology. 2017; 26 (4):246

3. Behzadi M, Joukar S, Beik A. Opioids and cardiac arrhythmia: a literature review. Medical Principles and Practice. 2018; 27 :401-414

4. Bravo-Valenzuela NJ, Rocha LA, Nardozza LMM, Júnior EA. Fetal cardiac arrhythmias: current evidence. Annals of Pediatric Cardiology. May-Aug 2018; 11 (2):148-163

5. Chen KM, Powers LS, Roveda JM. Noise-invariant component analysis for wearable sensor based electrocardiogram monitoring system. SM Journal of Biomedical Engineering. 2018; 4 (1):1025

6. Chen YM, Gao X. The latest progress of deep learning. Computer Science and Applications. 2018; 8 (4):565-571. DOI: 10.12677/csa.2018.84064

7. Fan XM, Yao QH, Cai YP, Miao F, Sun FM, Li Y. Multi-scaled fusion of deep convolutional neural networks for screening atrial fibrillation from single lead short ECG recordings. IEEE Journal of Biomedical and Health Informatics. 2018; 22 (6):1744-1753

8. Gao X. Non-invasive detection and compression of fetal electrocardiogram. Interpreting Cardiac Electrograms – From Skin to Endocardium, 2017:53-74. http://dx.doi.org/10.5772/intechopen.69920

9. Gao Y. Deep learning based automatic detection of arrhythmia and its applications. Thesis in Shandong University of Science and Technology, 2016:1-61

10. Hu S, Wei HX, Chen YD, Tan JD. A real-time cardiac arrhythmia classification system with wearable sensor networks. Sensors. 2012; 12 :12844-12869. DOI:10.3390/s120912844

11. Hu X, Yu ZB. Diagnosis of mesothelioma with deep learning. Oncology Letters. Oct 2018:1-8. DOI: 10.3892/ol.2018.9761

12. Hsing MJ, Hsia HH, Cardiac Arrhythmias. 2010:341-374. DOI: 10.1007/978-0-387-77452-7_19

13. Isin A, Ozdalili S. Cardiac arrhythmia detection using deep learning. Procedia Computer Science. 2017; 120 :268-275

14. Jin LP, Dong J. Deep learning research on clinical electrocardiogram analysis. China Science: Information Science. 2015; 45 (3):398-416

15. Jin LP, Dong J. Normal versus abnormal ECG classification by the aid of deep learning. Artificial Intelligence – Emerging Trends and Applications. InTech Open; 2018. pp. 295-315

16. Kamaleswaran R, Mahajan R, Akbilgic O. A robust deep convolutional neural network for the classification of abnormal cardiac rhythm using varying length single lead electrocardiogram. Physiological Measurement. Jan 2018:1-12. DOI: 10.1088/1361-6579/aaaa9d

17. Lee YN, Kwon JM, Lee YH, Park HH, Cho H, Park JS. Deep learning in the medical domain: predicting cardiac arrest using deep learning. Acute and Critical Care. 2018; 33 (3):117-120

18. Li X. Research of arrhythmia classification based on LSTM. Thesis in Lanzhou University. 2018:1-58

19. Kalidas V, Tamil LS. Cardiac arrhythmia classification using multi-modal signal analysis. Physiological Measurement. 2016; 37 :1253-1272. DOI: 10.1088/0967-3334/37/8/1253

20. Kalra A, Lowe A, Al-Jumaily A. Critical review of electrocardiography measurement systems and technology. Nov 2018. DOI: 10.1088/1361-6501/aaf2b7

21. Krishna MM, Neelima M, Harshali M, Rao MVG. Image classification using deep learning. International Journal of Engineering & Technology. 2018; 7 (2.7):614-617

22. Oh SL, Ng EYK, Tan RS, Acharya UR. Automated diagnosis of arrhythmia using combination of CNN and LSTM techniques with variable length heart beats. Computers in Biology and Medicine. June 2018. pp. 1-24. DOI: 10.1016/j.compbiomed.2018.06.002

23. Papadopoulos CH, Oikonomidis D, Lazaris E, Nihoyannopoulos P. Echocardiography and cardiac arrhythmias, Hellenic Journal of Cardiology. 2017:1-10. https://doi.org/10.1016/j.hjc.2017.11.017

24. Pourbabaee B, Roshtkhari MJ, Khorasani K. Deep convolutional neural networks and learning ECG features for screening paroxysmal atrial fibrillation patients. IEEE Transactions on Systems, Man, and Cybernetics: Systems. 2018; 48 (12):2095-2104

25. Pyakillya B, Kazachenko N, Mikhailovsky N. Deep learning for ECG classification. Journal of Physics: Conf. Series. 2017; 913 :012004. DOI: 10.1088/1742-6596/913/1/012004

26. Rajagopal R, Ranganathan V. Critical evaluation of linear dimensionality reduction techniques for cardiac arrhythmia classification. Circuits and Systems. 2016; 7 :2603-2612

27. Sanninoa G, Pietroa GD. Deep learning approach for ECG-based heartbeat classification for arrhythmia detection. Journal of Future Generation Computer Systems. 2018

28. Savalia S, Emamian V. Cardiac arrhythmia classification by multi-layer perceptron and convolution neural networks. Bioengineering. 2018; 5 (35):1-12. DOI:10.3390/bioengineering5020035

29. Shahreyar M, Fahhoum R, Akinseye O, Bhandari S, Dang G, Khouzam RN. Severe sepsis and cardiac arrhythmias. Annuals of Translational Medicine. 2018; 6 (1). DOI: 10.21037/atm.2017.12.26

30. Sun TK, Bao R, Jiang DH, Wang K. Security technology of the big cloud data based on deep learning. Computer Science and Applications. 2015; 5 (9):336-342

31. Xia YF, Gao ZF, Zhang HL, Zhang HY, Li S. An automatic cardiac arrhythmia classification system with wearable electrocardiogram. IEEE Access. 2018. DOI: 10.1109/ACCESS.2018.2807700

32. Xia YF, Zhang HL, Xu L, Gao ZF, Zhang HY, Liu HF, Li S. An automatic cardiac arrhythmia classification system with wearable electrocardiogram. IEEE Access. 2018; 6 :165529-16538

33. Yap J, Yolland W, Tschandl P. Multimodal skin lesion classification using deep learning. Experimental Dermatology. 2018; 00 :1-7. https://doi.org/10.1111/exd.13777

34. Zhan YJ, Wang J, Shi JP, Cheng GL, Yao LL, Sun WD. Distinguishing cloud and snow in satellite images via deep convolutional network. IEEE Geoscience and Remote Sensing Letters. 2017; 14 (10):1485-1489

35. Zhang R, Li WP, Tong M. Review of deep learning. Information and Control. 2018; 47 (4):385-397

36. Zhong W, Liao LJ, Guo XM, Wang GL. A deep learning approach for fetal QRS complex detection, Physiological Measurement. 2018; 39 (4):045004(9pp). DOI: 10.1088/1361-6579/aab297

37. Zhu YL, Lu ST, Dai RC, Liu GY, Wang ZW. Power market price forecasting via deep learning. 44th Annual Conference of the IEEE. Washington DC, USA: Industrial Electronics Society (IECON); 21-23 Oct 2018. https://arxiv.org/abs/1809.08092

38. Rajpurkar P, Hannun AY, Haghpanahi M, Bourn C, Ng, AY. Cardiologist-level arrhythmia detection with convolutional neural networks. [Online] Available: arxiv.org/pdf/1707.01836.pdf

39. Ribeiro AH, Ribeiro MH, Paixão G, Oliveira D, Gomes PR, Canazart JA, Pifano M, Meira-Jr. W, Schön TB, Ribeiro AL. Automatic diagnosis of short-duration 12-lead ECG using a deep convolutional network. [Online] Available: arxiv.org/pdf/1811.12194.pdf

40. A deep learning-based lightweight algorithm for identifying ECG data. [Online] Available: http://www.xjishu.com/zhuanli/55/201810353923.html

41. Thingspeak cloud computing platform based ECG diagnose system. [Online] Available: http://www.researchgate.net/publication/328042628_Thingspeak_Cloud_Computing_Platform_Based_ECG_Diagnose_System

42. Navale V and Bourne PE. Cloud computing applications for biomedical science: a perspective. PLoS Computational Biology. 2018; 14 (6):e1006144. https://doi.org/10.1371/journal.pcbi.1006144

2. Deep learning theory and automatic ECG diagnosis

3. Automatic ECG diagnosis via deep learning: lightweight classifier

4. Automatic detection system for arrhythmias and the Android health cloud platform

By Azzedine Dliou, Samir Elouaham, Rachid Latif and Mostafa Laaboubi

Submitted: 02 October 2018 Reviewed: 27 February 2019 Published: 03 April 2019

© 2019 The Author(s). Licensee IntechOpen. This chapter is distributed under the terms of the Creative Commons Attribution 3.0 License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

IntechOpen Author/Editor? To get your discount, log in .

Discounts available on purchase of multiple copies. View rates

Local taxes (VAT) are calculated in later steps, if applicable.

Discover 2026 Nobel Laureate Francis Halzen’s chapter on IntechOpen >
