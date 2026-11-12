# Cardiologist-level arrhythmia detection and classification in ambulatory electrocardiograms using a deep neural network

**Source:** https://www.nature.com/articles/s41591-018-0268-3

---

Thank you for visiting nature.com. You are using a browser version with limited support for CSS. To obtain
            the best experience, we recommend you use a more up to date browser (or turn off compatibility mode in
            Internet Explorer). In the meantime, to ensure continued support, we are displaying the site without styles
            and JavaScript.

A Publisher Correction to this article was published on 24 January 2019

Computerized electrocardiogram (ECG) interpretation plays a critical role in the clinical ECG workflow 1 . Widely available digital ECG data and the algorithmic paradigm of deep learning 2 present an opportunity to substantially improve the accuracy and scalability of automated ECG analysis. However, a comprehensive evaluation of an end-to-end deep learning approach for ECG analysis across a wide variety of diagnostic classes has not been previously reported. Here, we develop a deep neural network (DNN) to classify 12 rhythm classes using 91,232 single-lead ECGs from 53,549 patients who used a single-lead ambulatory ECG monitoring device. When validated against an independent test dataset annotated by a consensus committee of board-certified practicing cardiologists, the DNN achieved an average area under the receiver operating characteristic curve (ROC) of 0.97. The average F 1 score, which is the harmonic mean of the positive predictive value and sensitivity, for the DNN (0.837) exceeded that of average cardiologists (0.780). With specificity fixed at the average specificity achieved by cardiologists, the sensitivity of the DNN exceeded the average cardiologist sensitivity for all rhythm classes. These findings demonstrate that an end-to-end deep learning approach can classify a broad range of distinct arrhythmias from single-lead ECGs with high diagnostic performance similar to that of cardiologists. If confirmed in clinical settings, this approach could reduce the rate of misdiagnosed computerized ECG interpretations and improve the efficiency of expert human ECG interpretation by accurately triaging or prioritizing the most urgent conditions.

This is a preview of subscription content, access via your institution

Access Nature and 54 other Nature Portfolio journals

Get Nature+, our best-value online-access subscription

Receive 12 print issues and online access

Prices may be subject to local taxes which are calculated during checkout

Two-dimensional ECG-based cardiac arrhythmia classification using DSE-ResNet

A hybrid deep learning network for automatic diagnosis of cardiac arrhythmia based on 12-lead ECG

An explainable deep learning framework for trustworthy arrhythmia detection from ECG signals

Deep Learning Techniques for ECG Signal Analysis

The test dataset used to support the findings of this study is publicly available at https://irhythm.github.io/cardiol_test_set without restriction. Restrictions apply to the availability of the training dataset, which was used under license from iRhythm Technologies, Inc. for the current study. iRhythm Technologies, Inc. will consider requests to access the training data on an individual basis. Any data use will be restricted to noncommercial research purposes, and the data will only be made available on execution of appropriate data use agreements.

24 January 2019 In the version of this article originally published, the x axis labels in Fig. 1a were incorrect. The labels originally were ‘Specificity,’ but should have been ‘1 – Specificity.’ Also, the x axis label in Fig. 2b was incorrect. It was originally ‘DNN predicted label,’ but should have been ‘Average cardiologist label.’ The errors have been corrected in the PDF and HTML versions of this article.

In the version of this article originally published, the x axis labels in Fig. 1a were incorrect. The labels originally were ‘Specificity,’ but should have been ‘1 – Specificity.’ Also, the x axis label in Fig. 2b was incorrect. It was originally ‘DNN predicted label,’ but should have been ‘Average cardiologist label.’ The errors have been corrected in the PDF and HTML versions of this article.

Schläpfer, J. & Wellens, H. J. Computer-interpreted electrocardiograms: benefits and limitations. J. Am. Coll. Cardiol. 70 , 1183–1192 (2017). Article PubMed Google Scholar

Schläpfer, J. & Wellens, H. J. Computer-interpreted electrocardiograms: benefits and limitations. J. Am. Coll. Cardiol. 70 , 1183–1192 (2017).

LeCun, Y., Bengio, Y. & Hinton, G. Deep learning. Nature 521 , 436–444 (2015). Article CAS PubMed Google Scholar

LeCun, Y., Bengio, Y. & Hinton, G. Deep learning. Nature 521 , 436–444 (2015).

Holst, H., Ohlsson, M., Peterson, C. & Edenbrandt, L. A confident decision support system for interpreting electrocardiograms. Clin. Physiol. 19 , 410–418 (1999). Article CAS PubMed Google Scholar

Holst, H., Ohlsson, M., Peterson, C. & Edenbrandt, L. A confident decision support system for interpreting electrocardiograms. Clin. Physiol. 19 , 410–418 (1999).

Schlant, R. C. et al. Guidelines for electrocardiography. A report of the American College of Cardiology/American Heart Association Task Force on assessment of diagnostic and therapeutic cardiovascular procedures (Committee on Electrocardiography). J. Am. Coll. Cardiol. 19 , 473–481 (1992). Article CAS PubMed Google Scholar

Schlant, R. C. et al. Guidelines for electrocardiography. A report of the American College of Cardiology/American Heart Association Task Force on assessment of diagnostic and therapeutic cardiovascular procedures (Committee on Electrocardiography). J. Am. Coll. Cardiol. 19 , 473–481 (1992).

Shah, A. P. & Rubin, S. A. Errors in the computerized electrocardiogram interpretation of cardiac rhythm. J. Electrocardiol. 40 , 385–390 (2007). Article PubMed Google Scholar

Shah, A. P. & Rubin, S. A. Errors in the computerized electrocardiogram interpretation of cardiac rhythm. J. Electrocardiol. 40 , 385–390 (2007).

Guglin, M. E. & Thatai, D. Common errors in computer electrocardiogram interpretation. Int. J. Cardiol. 106 , 232–237 (2006). Article PubMed Google Scholar

Guglin, M. E. & Thatai, D. Common errors in computer electrocardiogram interpretation. Int. J. Cardiol. 106 , 232–237 (2006).

Poon, K., Okin, P. M. & Kligfield, P. Diagnostic performance of a computer-based ECG rhythm algorithm. J. Electrocardiol. 38 , 235–238 (2005). Article PubMed Google Scholar

Poon, K., Okin, P. M. & Kligfield, P. Diagnostic performance of a computer-based ECG rhythm algorithm. J. Electrocardiol. 38 , 235–238 (2005).

Amodei, D. et al. Deep Speech 2: end-to-end Speech recognition in English and Mandarin. In Proc. 33rd International Conference on Machine Learning, 173–182 (2016).

Amodei, D. et al. Deep Speech 2: end-to-end Speech recognition in English and Mandarin. In Proc. 33rd International Conference on Machine Learning, 173–182 (2016).

He, K., Zhang, X., Ren, S. & Sun, J. Delving deep into rectifiers: surpassing human-level performance on ImageNet classification. In Proc. International Conference on Computer Vision, 1026–1034 (IEEE, 2015).

He, K., Zhang, X., Ren, S. & Sun, J. Delving deep into rectifiers: surpassing human-level performance on ImageNet classification. In Proc. International Conference on Computer Vision, 1026–1034 (IEEE, 2015).

Silver, D. et al. Mastering the game of Go with deep neural networks and tree search. Nature 529 , 484–489 (2016). Article CAS PubMed Google Scholar

Silver, D. et al. Mastering the game of Go with deep neural networks and tree search. Nature 529 , 484–489 (2016).

Gulshan, V. et al. Development and validation of a deep learning algorithm for detection of diabetic retinopathy in retinal fundus photographs. JAMA 316 , 2402–2410 (2016). Article PubMed Google Scholar

Gulshan, V. et al. Development and validation of a deep learning algorithm for detection of diabetic retinopathy in retinal fundus photographs. JAMA 316 , 2402–2410 (2016).

Esteva, A. Dermatologist-level classification of skin cancer with deep neural networks. Nature 542 , 115–118 (2017). Article CAS PubMed Google Scholar

Esteva, A. Dermatologist-level classification of skin cancer with deep neural networks. Nature 542 , 115–118 (2017).

Poungponsri, S. & Yu, X. An adaptive filtering approach for electrocardiogram (ECG) signal noise reduction using neural networks. Neurocomputing 117 , 206–213 (2013). Article Google Scholar

Poungponsri, S. & Yu, X. An adaptive filtering approach for electrocardiogram (ECG) signal noise reduction using neural networks. Neurocomputing 117 , 206–213 (2013).

Ochoa, A., Mena, L. J. & Felix, V. G. Noise-tolerant neural network approach for electrocardiogram signal classification. In Proc. 3rd International Conference on Compute and Data Analysis, 277–282 (Association for Computing Machinery, 2017).

Ochoa, A., Mena, L. J. & Felix, V. G. Noise-tolerant neural network approach for electrocardiogram signal classification. In Proc. 3rd International Conference on Compute and Data Analysis, 277–282 (Association for Computing Machinery, 2017).

Mateo, J. & Rieta, J. J. Application of artificial neural networks for versatile preprocessing of electrocardiogram recordings. J. Med. Eng. Technol. 36 , 90–101 (2012). Article CAS PubMed Google Scholar

Mateo, J. & Rieta, J. J. Application of artificial neural networks for versatile preprocessing of electrocardiogram recordings. J. Med. Eng. Technol. 36 , 90–101 (2012).

Pourbabaee, B., Roshtkhari, M. J. & Khorasani, K. Deep convolutional neural networks and learning ECG features for screening paroxysmal atrial fibrillation patients. IEEE Trans. Syst. Man Cybern. Syst. 99 , 1–10 (2017). Google Scholar

Pourbabaee, B., Roshtkhari, M. J. & Khorasani, K. Deep convolutional neural networks and learning ECG features for screening paroxysmal atrial fibrillation patients. IEEE Trans. Syst. Man Cybern. Syst. 99 , 1–10 (2017).

Javadi, M., Arani, S. A., Sajedin, A. & Ebrahimpour, R. Classification of ECG arrhythmia by a modular neural network based on mixture of experts and negatively correlated learning. Biomed. Signal Process. Control 8 , 289–296 (2013). Article Google Scholar

Javadi, M., Arani, S. A., Sajedin, A. & Ebrahimpour, R. Classification of ECG arrhythmia by a modular neural network based on mixture of experts and negatively correlated learning. Biomed. Signal Process. Control 8 , 289–296 (2013).

Acharya, U. R. et al. A deep convolutional neural network model to classify heartbeats. Comput. Biol. Med. 89 , 389–396 (2017). Article PubMed Google Scholar

Acharya, U. R. et al. A deep convolutional neural network model to classify heartbeats. Comput. Biol. Med. 89 , 389–396 (2017).

Banupriya, C. V. & Karpagavalli, S. Electrocardiogram beat classification using probabilistic neural network. In Proc. Machine Learning: Challenges and Opportunities Ahead 31–37 (2014).

Banupriya, C. V. & Karpagavalli, S. Electrocardiogram beat classification using probabilistic neural network. In Proc. Machine Learning: Challenges and Opportunities Ahead 31–37 (2014).

Al Rahhal, M. M. et al. Deep learning approach for active classification of electrocardiogram signals. Inf. Sci. (NY) 345 , 340–354 (2016). Article Google Scholar

Al Rahhal, M. M. et al. Deep learning approach for active classification of electrocardiogram signals. Inf. Sci. (NY) 345 , 340–354 (2016).

Acharya, U. R. et al. Automated detection of arrhythmias using different intervals of tachycardia ECG segments with convolutional neural network. Inf. Sci. (NY) 405 , 81–90 (2017). Article Google Scholar

Acharya, U. R. et al. Automated detection of arrhythmias using different intervals of tachycardia ECG segments with convolutional neural network. Inf. Sci. (NY) 405 , 81–90 (2017).

Zihlmann, M., Perekrestenko, D. & Tschannen, M. Convolutional recurrent neural networks for electrocardiogram classification. Comput. Cardiol. https://doi.org/10.22489/CinC.2017.070-060 (2017).

Zihlmann, M., Perekrestenko, D. & Tschannen, M. Convolutional recurrent neural networks for electrocardiogram classification. Comput. Cardiol. https://doi.org/10.22489/CinC.2017.070-060 (2017).

Xiong, Z., Zhao, J. & Stiles, M. K. Robust ECG signal classification for detection of atrial fibrillation using a novel neural network. Comput. Cardiol. https://doi.org/10.22489/CinC.2017.066-138 (2017).

Xiong, Z., Zhao, J. & Stiles, M. K. Robust ECG signal classification for detection of atrial fibrillation using a novel neural network. Comput. Cardiol. https://doi.org/10.22489/CinC.2017.066-138 (2017).

Clifford, G. et al. AF classification from a short single lead ECG recording: the PhysioNet/Computing in Cardiology Challenge 2017. Comput. Cardiol. https://doi.org/10.22489/CinC.2017.065-469 (2017).

Clifford, G. et al. AF classification from a short single lead ECG recording: the PhysioNet/Computing in Cardiology Challenge 2017. Comput. Cardiol. https://doi.org/10.22489/CinC.2017.065-469 (2017).

Teijeiro, T., Garcia, C. A., Castro, D. & Felix, P. Arrhythmia classification from the abductive interpretation of short single-lead ECG records. Comput. Cardiol. https://doi.org/10.22489/CinC.2017.166-054 (2017).

Teijeiro, T., Garcia, C. A., Castro, D. & Felix, P. Arrhythmia classification from the abductive interpretation of short single-lead ECG records. Comput. Cardiol. https://doi.org/10.22489/CinC.2017.166-054 (2017).

Goldberger, A. L. et al. PhysioBank, PhysioToolkit, and PhysioNet: components of a new research resource for complex physiologic signals. Circulation 101 , E215–E220 (2000). CAS PubMed Google Scholar

Goldberger, A. L. et al. PhysioBank, PhysioToolkit, and PhysioNet: components of a new research resource for complex physiologic signals. Circulation 101 , E215–E220 (2000).

Turakhia, M. P. et al. Diagnostic utility of a novel leadless arrhythmia monitoring device. Am. J. Cardiol. 112 , 520–524 (2013). Article PubMed Google Scholar

Turakhia, M. P. et al. Diagnostic utility of a novel leadless arrhythmia monitoring device. Am. J. Cardiol. 112 , 520–524 (2013).

Hand, D. J. & Till, R. J. A simple generalisation of the area under the ROC curve for multiple class classification problems. Mach. Learn. 45 , 171–186 (2001). Article Google Scholar

Hand, D. J. & Till, R. J. A simple generalisation of the area under the ROC curve for multiple class classification problems. Mach. Learn. 45 , 171–186 (2001).

Smith, M. D. et al. in Best Care at Lower Cost: the Path to Continuously Learning Health Care in America (National Academies Press,: Washington, 2012).

Smith, M. D. et al. in Best Care at Lower Cost: the Path to Continuously Learning Health Care in America (National Academies Press,: Washington, 2012).

Lyon, A., Mincholé, A., Martínez, J. P., Laguna, P. & Rodriguez, B. Computational techniques for ECG analysis and interpretation in light of their contribution to medical advances. J. R. Soc. Interface 15 , pii: 20170821 (2018). Article Google Scholar

Lyon, A., Mincholé, A., Martínez, J. P., Laguna, P. & Rodriguez, B. Computational techniques for ECG analysis and interpretation in light of their contribution to medical advances. J. R. Soc. Interface 15 , pii: 20170821 (2018).

Carrara, M. et al. Heart rate dynamics distinguish among atrial fibrillation, normal sinus rhythm and sinus rhythm with frequent ectopy. Physiol. Meas. 36 , 1873–1888 (2015). Article PubMed Google Scholar

Carrara, M. et al. Heart rate dynamics distinguish among atrial fibrillation, normal sinus rhythm and sinus rhythm with frequent ectopy. Physiol. Meas. 36 , 1873–1888 (2015).

Zhou, X., Ding, H., Ung, B., Pickwell-MacPherson, E. & Zhang, Y. Automatic online detection of atrial fibrillation based on symbolic dynamics and Shannon entropy. Biomed. Eng. Online 13 , 18 (2014). Article PubMed PubMed Central Google Scholar

Zhou, X., Ding, H., Ung, B., Pickwell-MacPherson, E. & Zhang, Y. Automatic online detection of atrial fibrillation based on symbolic dynamics and Shannon entropy. Biomed. Eng. Online 13 , 18 (2014).

Article PubMed PubMed Central Google Scholar

Hong, S. et al. ENCASE: an ENsemble ClASsifiEr for ECG Classification using expert features and deep neural networks. Comput. Cardiol. https://doi.org/10.22489/CinC.2017.178-245 (2017).

Hong, S. et al. ENCASE: an ENsemble ClASsifiEr for ECG Classification using expert features and deep neural networks. Comput. Cardiol. https://doi.org/10.22489/CinC.2017.178-245 (2017).

Nahar, J., Imam, T., Tickle, K. S. & Chen, Y. P. Computational intelligence for heart disease diagnosis: a medical knowledge driven approach. Expert Syst. Appl. 40 , 96–104 (2013). Article Google Scholar

Nahar, J., Imam, T., Tickle, K. S. & Chen, Y. P. Computational intelligence for heart disease diagnosis: a medical knowledge driven approach. Expert Syst. Appl. 40 , 96–104 (2013).

Cubanski, D., Cyganski, D., Antman, E. M. & Feldman, C. L. A neural network system for detection of atrial fibrillation in ambulatory electrocardiograms. J. Cardiovasc. Electrophysiol. 5 , 602–608 (1994). Article CAS PubMed Google Scholar

Cubanski, D., Cyganski, D., Antman, E. M. & Feldman, C. L. A neural network system for detection of atrial fibrillation in ambulatory electrocardiograms. J. Cardiovasc. Electrophysiol. 5 , 602–608 (1994).

Andreotti, F., Carr, O., Pimentel, M. A. F., Mahdi, A. & De Vos, M. Comparing feature-based classifiers and convolutional neural networks to detect arrhythmia from short segments of ECG. Comput. Cardiol. https://doi.org/10.22489/CinC.2017.360-239 (2017).

Andreotti, F., Carr, O., Pimentel, M. A. F., Mahdi, A. & De Vos, M. Comparing feature-based classifiers and convolutional neural networks to detect arrhythmia from short segments of ECG. Comput. Cardiol. https://doi.org/10.22489/CinC.2017.360-239 (2017).

Xu, S. S., Mak, M. & Cheung, C. Towards end-to-end ECG classification with raw signal extraction and deep neural networks. IEEE J. Biomed. Health Informatics 14 , 1 (2018). Article Google Scholar

Xu, S. S., Mak, M. & Cheung, C. Towards end-to-end ECG classification with raw signal extraction and deep neural networks. IEEE J. Biomed. Health Informatics 14 , 1 (2018).

Ong, S. L., Ng, E. Y. K., Tan, R. S. & Acharya, U. R. Automated diagnosis of arrhythmia using combination of CNN and LSTM techniques with variable length heart beats. Comput. Biol. Med. 102 , 278–287 (2018). Article Google Scholar

Ong, S. L., Ng, E. Y. K., Tan, R. S. & Acharya, U. R. Automated diagnosis of arrhythmia using combination of CNN and LSTM techniques with variable length heart beats. Comput. Biol. Med. 102 , 278–287 (2018).

Shashikumar, S. P., Shah, A. J., Clifford, G. D. & Nemati, S. Detection of paroxysmal atrial fibrillation using attention-based bidirectional recurrent neural networks. In Proc. 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, 715–723 (Association for Computing Machinery, 2018).

Shashikumar, S. P., Shah, A. J., Clifford, G. D. & Nemati, S. Detection of paroxysmal atrial fibrillation using attention-based bidirectional recurrent neural networks. In Proc. 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, 715–723 (Association for Computing Machinery, 2018).

Xia, Y., Wulan, N., Wang, K. & Zhang, H. Detecting atrial fibrillation by deep convolutional neural networks. Comput. Biol. Med. 93 , 84–92 (2018). Article PubMed Google Scholar

Xia, Y., Wulan, N., Wang, K. & Zhang, H. Detecting atrial fibrillation by deep convolutional neural networks. Comput. Biol. Med. 93 , 84–92 (2018).

He, K., Zhang, X., Ren, S. & Sun, J. Identity mappings in deep residual networks. In Proc. European Conference on Computer Vision, 630–645 (Springer, 2016).

He, K., Zhang, X., Ren, S. & Sun, J. Identity mappings in deep residual networks. In Proc. European Conference on Computer Vision, 630–645 (Springer, 2016).

Ioffe, S. & Szegedy, C. Batch normalization: accelerating deep network training by reducing internal covariate shift. In Proc. International Conference on Machine Learnin g, 448–456 (2015).

Ioffe, S. & Szegedy, C. Batch normalization: accelerating deep network training by reducing internal covariate shift. In Proc. International Conference on Machine Learnin g, 448–456 (2015).

He, K., Zhang, X., Ren, S. & Sun, J. Deep residual learning for image recognition. In Proc. IEEE Conference on Computer Vision and Pattern Recognition, 770–778 (IEEE, 2016).

He, K., Zhang, X., Ren, S. & Sun, J. Deep residual learning for image recognition. In Proc. IEEE Conference on Computer Vision and Pattern Recognition, 770–778 (IEEE, 2016).

Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I. & Salakhutdinov, R. Dropout: a simple way to prevent neural networks from overfitting. J. Mach. Learn. Res. 15 , 1929–1958 (2014). Google Scholar

Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I. & Salakhutdinov, R. Dropout: a simple way to prevent neural networks from overfitting. J. Mach. Learn. Res. 15 , 1929–1958 (2014).

Kingma, D. P. & Ba, J. L. Adam: a method for stochastic optimization. In Proc. International Conference on Learning Representations 1–15 (2015).

Kingma, D. P. & Ba, J. L. Adam: a method for stochastic optimization. In Proc. International Conference on Learning Representations 1–15 (2015).

Hochreiter, S. & Schmidhuber, J. Long short-term memory. Neural Comput. 9 , 1735–1780 (1997). Article CAS PubMed Google Scholar

Hochreiter, S. & Schmidhuber, J. Long short-term memory. Neural Comput. 9 , 1735–1780 (1997).

Fawcett, T. An introduction to ROC analysis. Pattern Recognit. Lett. 27 , 861–874 (2006). Article Google Scholar

Fawcett, T. An introduction to ROC analysis. Pattern Recognit. Lett. 27 , 861–874 (2006).

Hanley, J. A. & McNeil, B. J. A method of comparing the areas under receiver operating characteristic curves derived from the same cases. Radiology 148 , 839–843 (1983). Article CAS PubMed Google Scholar

Hanley, J. A. & McNeil, B. J. A method of comparing the areas under receiver operating characteristic curves derived from the same cases. Radiology 148 , 839–843 (1983).

Saito, T. & Rehmsmeier, M. The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. PLoS ONE 10 , e0118432 (2015). Article PubMed PubMed Central Google Scholar

Saito, T. & Rehmsmeier, M. The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. PLoS ONE 10 , e0118432 (2015).

Article PubMed PubMed Central Google Scholar

iRhythm Technologies, Inc. provided financial support for the data annotation in this work. M.H. and C.B. are employees of iRhythm Technologies, Inc. A.Y.H. was funded by an NVIDIA fellowship. G.H.T. received support from the National Institutes of Health (K23 HL135274). The only financial support provided by iRhythm Technologies, Inc. for this study was for the data annotation. Data analysis and interpretation was performed independently from the sponsor. The corresponding author had full access to all the data in the study and had final responsibility for the decision to submit for publication.

These authors contributed equally: Awni Y. Hannun, Pranav Rajpurkar, Masoumeh Haghpanahi, Geoffrey H. Tison.

These authors contributed equally: Awni Y. Hannun, Pranav Rajpurkar, Masoumeh Haghpanahi, Geoffrey H. Tison.

Department of Computer Science, Stanford University, Stanford, CA, USA Awni Y. Hannun, Pranav Rajpurkar & Andrew Y. Ng

Department of Computer Science, Stanford University, Stanford, CA, USA

Awni Y. Hannun, Pranav Rajpurkar & Andrew Y. Ng

iRhythm Technologies Inc., San Francisco, CA, USA Masoumeh Haghpanahi & Codie Bourn

iRhythm Technologies Inc., San Francisco, CA, USA

Division of Cardiology, Department of Medicine, University of California San Francisco, San Francisco, CA, USA Geoffrey H. Tison

Division of Cardiology, Department of Medicine, University of California San Francisco, San Francisco, CA, USA

Department of Medicine and Center for Digital Health, Stanford University School of Medicine, Stanford, CA, USA Mintu P. Turakhia

Department of Medicine and Center for Digital Health, Stanford University School of Medicine, Stanford, CA, USA

Veterans Affairs Palo Alto Health Care System, Palo Alto, CA, USA Mintu P. Turakhia

Veterans Affairs Palo Alto Health Care System, Palo Alto, CA, USA

Awni Y. Hannun View author publications Search author on: PubMed Google Scholar

Pranav Rajpurkar View author publications Search author on: PubMed Google Scholar

Masoumeh Haghpanahi View author publications Search author on: PubMed Google Scholar

Geoffrey H. Tison View author publications Search author on: PubMed Google Scholar

Codie Bourn View author publications Search author on: PubMed Google Scholar

Mintu P. Turakhia View author publications Search author on: PubMed Google Scholar

Andrew Y. Ng View author publications Search author on: PubMed Google Scholar

M.H., A.Y.N., A.Y.H., and G.H.T. contributed to the study design. M.H. and C.B. were responsible for data collection. P.R. and A.Y.H. ran the experiments and created the figures. G.H.T., P.R., and A.Y.H. contributed to the analysis. G.H.T., A.Y.H., and M.P.T. contributed to the data interpretation and to the writing. G.H.T., M.P.T., and A.Y.N. advised and A.Y.N. was the senior supervisor of the project. All authors read and approved the submitted manuscript.

M.H. and C.B. are employees of iRhythm Technologies, Inc. G.H.T. is an advisor to Cardiogram, Inc. M.P.T. is a consultant to iRhythm Technologies, Inc. None of the other authors have potential conflicts of interest.

Publisher’s note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Extended Data Fig. 1 Deep Neural Network architecture.

Our deep neural network consisted of 33 convolutional layers followed by a linear output layer into a softmax. The network accepts raw ECG data as input (sampled at 200 Hz, or 200 samples per second), and outputs a prediction of one out of 12 possible rhythm classes every 256 input samples.

Extended Data Fig. 2 Receiver operating characteristic curves for deep neural network predictions on 12 rhythm classes.

Individual cardiologist performance is indicated by the red crosses and averaged cardiologist performance is indicated by the green dot. The line represents the ROC curve of model performance. AF-atrial fibrillation/atrial flutter; AVB- atrioventricular block; EAR-ectopic atrial rhythm; IVR-idioventricular rhythm; SVT-supraventricular tachycardia; VT-ventricular tachycardia. n = 7,544 where each of the 328 30-second ECGs received 23 sequence-level predictions.

Supplementary Information (download PDF )

Sensitivity, specificity and PPV values at different operating points as well as the individual and average cardiologist metrics for the arrhythmias in the figure.

Absolute confusions counts between arrhythmias for both the model and the cardiologists.

Sensitivity and specificity values at different operating points as well as the individual and average cardiologist metrics for all of the arrhythmias.

Hannun, A.Y., Rajpurkar, P., Haghpanahi, M. et al. Cardiologist-level arrhythmia detection and classification in ambulatory electrocardiograms using a deep neural network. Nat Med 25 , 65–69 (2019). https://doi.org/10.1038/s41591-018-0268-3

DOI : https://doi.org/10.1038/s41591-018-0268-3

DOI : https://doi.org/10.1038/s41591-018-0268-3

Anyone you share the following link with will be able to read this content:

Sorry, a shareable link is not currently available for this article.

Provided by the Springer Nature SharedIt content-sharing initiative

Artificial intelligence for the electrocardiogram

Screening for cardiac contractile dysfunction using an artificial intelligence–enabled electrocardiogram

Sign up for the Nature Briefing newsletter — what matters in science, free to your inbox daily.
