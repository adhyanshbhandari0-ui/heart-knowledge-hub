# ECG arrhythmia classification using a 2-D convolutional neural network

**Source:** https://medium.com/datadriveninvestor/ecg-arrhythmia-classification-using-a-2-d-convolutional-neural-network-33aa586bad67

---

empowerment through data, knowledge, and expertise. Join DDI community at https://join.datadriveninvestor.com

ECG arrhythmia classification using a 2-D convolutional neural network

According to the World Health Organization (WHO), cardiovascular diseases (CVDs) are the number one cause of death today. Over 17.7 million people died from CVDs in the year 2017 all over the world which is about 31% of all deaths, and over 75% of these deaths occur in low and middle income countries. Arrhythmia is a representative type of CVD that refers to any irregular change from the normal heart rhythms. There are several types of arrhythmia including atrial fibrillation, premature contraction, ventricular fibrillation, and tachycardia. Although single arrhythmia heartbeat may not have a serious impact on life, continuous arrhythmia beats can result in fatal circumstances. For example, prolonged premature ventricular contraction (PVCs) beats occasionally turn into a ventricular tachycardia (VT) or ventricular fibrillation (VF) beats which can immediately lead to heart failure. Thus, it is important to periodically monitor the heart rhythms to manage and prevent the CVDs. Electrocardiogram (ECG) is a non-invasive medical tool that displays the rhythm and status of the heart. Therefore, automatic detection of irregular heart rhythms from ECG signals is a significant task in the field of cardiology.

In this post, I have implemented this paper https://arxiv.org/pdf/1804.06812.pdf in which we classify ECG into seven categories, one being normal and the other six being different types of arrhythmia using deep two-dimensional CNN with grayscale ECG images. By transforming one-dimensional ECG signals into two-dimensional ECG images, noise filtering and feature extraction are no longer required. This is important since some of ECG beats are ignored in noise filtering and feature extraction. In addition, training data can be enlarged by augmenting the ECG images which results in higher classification accuracy. Data augmentation is hard to be applied in 1-d signals since the distortion of 1-d ECG signal could downgrade the performance of the classifier. However, augmenting two-dimensional ECG images with different cropping methods helps the CNN model to train with different viewpoints of the single ECG images. Using ECG image as an input data of the ECG arrhythmia classification also benefits in the sense of robustness.

I have used the MIT-BIH arrhythmia database for the CNN model training and testing as has been mentioned in the paper. The MIT-BIH arrhythmia Database contains 48 half-hour excerpts of two-channel ambulatory ECG recordings, obtained from 47 subjects studied by the BIH arrhythmia laboratory between 1975 and 1979. For each record there are three files: 1. Annotation file 2. Signals file 3. Header file.

In this implementation, I have used the lead2 signals. The get_records() function in the code snippet below creates a list of all the records in the dataset. The beat_annotations() function finds the indices of the beats belonging to a particular category (In the code below, I have found the indices of Normal beats). The segmentation() function is used to segment the beats of each category.

Since the CNN model handles two-dimensional image as an input data, ECG signals are transformed into ECG images during the ECG data pre-processing step. With these obtained ECG images, classification of seven ECG types is performed in CNN classifier step. The seven classes are: Atrial Premature Contraction, Normal, Left Bundle Branch Block, Paced Beat, Premature Ventricular Contraction, Right Bundle Branch Block and Ventricular Escape Beat.

I have transformed ECG signals into ECG images by plotting each ECG beat. I first detected the R-peaks in ECG signals using Biosppy module of Python. Once the R-peaks have been found, to segment a beat, I took the present R-peak and the last R-peak, took half of the distance between the two and included those signals in the present beat. Similarly I did this for the next beat.

To convert these segmented signals into images, I have used Matplotlib and OpenCV . Since, in ECG signals, colors are of not any importance, I have converted them to grayscale images.

Join Medium for free to get updates from this writer.

Data augmentation means increasing the number of data points. In terms of images, it may mean that increasing the number of images in the dataset. We can achieve both high specificity and sensitivity by augmenting and balancing input data. I have augmented six ECG arrhythmia beats (PVC, PAB, RBB, LBB, APC, VEB) with nine different cropping methods: left top, center top, right top, center left, center, center right, left bottom, center bottom, and right bottom. Each cropping method results in two of three sizes of an ECG image, that is 96 x 96. Then, these augmented images are resized to the original size which is 128 x 128.

The architecture of the CNN model is the same as has been used in this paper: https://arxiv.org/pdf/1804.06812.pdf . An 11 layer model has been used. The main structure of the model is very similar to VGGNet. The CNN model uses Xavier initialization for all the layers. For the activation function, they have used exponential linear units(ELU) unlike ReLU, that has been used in VGGNet.

For validation, I have used skLearn’s train_test_split to divide the training and test set. There were 352295 images in the Training set and 44041 images in the Test set. This model has achieved an accuracy of 99.31 on the given Test set.

I have deployed the model on my local server, thanks to this Github repo . In this web app we can either select segmented ECG beats or a CSV file of raw ECG signals to get the corresponding output. Here are some screenshots of the app.

After choosing the CSV file and clicking on Predict, for each segmented beat we get the class it belongs to as well as the sample range. For eg: in the first beat that ranges from sample number 175 to sample number 235, the output is Premature Ventricular Contraction.

https://github.com/mtobeiyf/keras-flask-deploy-webapp

https://www.physionet.org/physiobank/database/mitdb/

Thanks for reading. Do clap, if you liked it.

Senior Research Engineer @ A*STAR, Singapore

empowerment through data, knowledge, and expertise. Join DDI community at https://join.datadriveninvestor.com
