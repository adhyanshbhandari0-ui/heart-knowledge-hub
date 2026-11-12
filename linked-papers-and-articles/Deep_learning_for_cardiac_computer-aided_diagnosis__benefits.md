# Deep learning for cardiac computer-aided diagnosis: benefits, issues & solutions

**Source:** http://mhealth.amegroups.com/article/view/17021/17339

---

Deep learning for cardiac computer-aided diagnosis: benefits, issues & solutions

According to the World Health Organization (WHO), in 2015, cardiovascular diseases represented 31% of all global deaths ( 1 ), with ischemic heart disease often cited as the leading cause of death worldwide. Furthermore, public health statistics have shown an increase of patients with some form of cardiovascular disease in countries with low or middle gross national income ( 2 ). Although serious and often life threatening, cardiovascular disease in individuals can be managed clinically as a chronic condition, and treated with medications, diet, and regular monitoring of specific health indicators. Risk factors are fairly well defined and lifestyle changes can mitigate some risks. The motivation to prevent and manage heart disease has spurred development of numerous mHealth applications for consumer use, some of which have been scientifically assessed for efficacy ( 3 ). In this paper, we provide an overview of telemedicine and mHealth technologies applied in rural healthcare settings, using one form of cardiovascular disease for context. Additionally, we discuss the need for computer-aided diagnosis (CADx) as well as the implementation of machine and deep learning techniques in these systems. Finally, we explore the issues and solutions associated with using deep learning algorithms for medical applications.

Coronary artery disease, a common type of heart disease, occurs from the build-up of plaque within arteries that supply blood to the heart muscles. As an artery is gradually obstructed, blood flow to the heart muscles is reduced, which impairs heart motion. This is referred to as myocardial ischemia. When irreversible damage is done to the heart muscles due to partial or complete blockage of an artery, myocardial infarction, also known as a heart attack, occurs.

The heart is divided into four chambers, the upper receiving chambers (right and left atria), and the lower pumping chambers [right and left ventricle (LV)]. De-oxygenated blood is collected in the right atrium and is pumped to the lungs by the right ventricle for the oxygenation process. The oxygenated blood returns to the heart by entering the left atrium and is distributed to all parts of the body by the LV. The LV is the biggest chamber of the heart and one of the most important due to its function. Because of this, it is also typically responsible for heart failure. Throughout the progression of coronary artery disease, wall motion abnormalities would begin to appear, which can be detected via the use of echocardiography ( 4 ). These flaws can be diagnosed with LV measurements and scoring of wall motions. Therefore, it is essential to continuously monitor the LV as prolonged damage will affect function, size and shape.

Echocardiography is a common heart imaging technique which captures ultrasound videos of distinct cardiac views, the structures within, and their movements. It is an important tool for morphological and functional assessment of the heart, and can be utilized to diagnose cardiac diseases associated with motion abnormalities ( 5 ). Moreover, quantitative assessments such as left ventricular ejection fraction and cardiac output can be measured by an echocardiogram ( 6 ). Numerous factors contribute to the dominance of echocardiography as the preferred cardiac imaging method. The creation of portable ultrasound devices, spurred by technological advancements have enabled the use of echocardiography in diverse scenarios such as health missions to rural areas of developing nations ( 7 ). Compared with other imaging modalities, ultrasound has no known adverse effects and does not expose patients to radiation or contrast agents ( 4 ). Also, it is the most cost efficient and sustainable imaging technology in comparison to computed tomography, magnetic resonance imaging and nuclear perfusion imaging ( 8 ). Lastly, echocardiography can be performed in real time with the benefit of having a low acquisition duration ( 9 ). The integration of echocardiography with telemedicine and mHealth applications have proven to be quite effective in rural healthcare scenarios for capturing and transmitting heart imagery, thereby permitting diagnosis and remote monitoring, as well as alleviating the need for patients to travel from distant areas to a clinician’s location.

Rural healthcare, telemedicine & mobile health (mHealth)

There is a strong need for diagnostic imaging to accurately treat patients who are located in developing countries ( 10 ). Healthcare is most deficient in rural or remote areas because of issues such as absence or shortage of electricity and telecommunication services, lack of treatment services and medical specialists, low per capita income, basic infrastructure, and severe weather conditions ( 11 ). Compared to urban communities, the rural population possesses higher death and disease rates as well as health disparities due to insufficient medical care ( 12 ).

A viable solution to this predicament is telemedicine, which involves the delivery of health care and sharing of medical knowledge to sites located at a distance from the provider ( 13 ). Research has shown that telemedicine can enable access to specialized services in regions with scarce infrastructure, increase information availability and improve retention of physicians in remote areas, and impact the rural economy by decreasing costs ( 14 , 15 ). The methods to conduct telemedicine can be divided into two categories, namely synchronous (real-time) and asynchronous (store-and-forward). The approach chosen depends on the data that needs to be transmitted, availability of telecommunications resources, and the urgency of response ( 16 ). Synchronous applications require high bandwidth usage as data transmission in the form of video and audio occurs in real time while an examination is being performed ( 15 ). A general example would be a video conference call between doctor and patient. Conversely, asynchronous applications collect, store and forward information such as images, text or audio without the need for either parties to be simultaneously present ( 17 ). An example asynchronous application is emailing of medical images and waiting for a subsequent diagnostic reply. Regardless of the selected methods, mobile devices such as compact medical equipment, smartphones, and laptops, play an important role in bridging the gap between distant locations.

Telesonography, a subtype of telemedicine, involves the guidance of a novice sonographer in ultrasound acquisition, and the interpretation of ultrasound imagery by a remote expert through the use of mobile devices ( 18 ). Numerous researchers have experimented with real-time streaming applications whereby an ultrasound machine, connected to a computer, streams the video feed to offsite devices ( 17 , 19 ). Among these works, many have focused on the feasibility of video streaming to mobile phones and tablets ( 20 , 21 ), while others concentrated on the viability of different internet connection types ( 22 , 23 ). Results show that conducting remote guidance and interpretation on mobile devices connected to low bandwidth networks are possible. Though image quality and transmission speeds would be inferior due to slower internet connectivity ( 20 , 24 ). Despite this, evaluations were not significantly affected and transmitted images maintained their clinical value ( 21 ).

mHealth, which is the use of mobile devices for health care services, is a rapidly evolving field that has grown in tandem with telemedicine. It has been utilized for various applications such as treatment compliance, data collection, disease surveillance and prevention, point-of-care support and emergency response ( 25 ). Several studies have demonstrated the positive impacts of mHealth projects towards developing nations. These benefits include, widening access to healthcare services particularly for remote communities, lowering service costs for financially challenged or resource scarce areas, promoting the dissemination of health education thereby improving disease monitoring and treatment, as well as supporting health providers by providing efficient portable tools ( 26 , 27 ). Telecommunication technologies, especially mobile phones have contributed greatly to the successful implementation of mHealth initiatives. The popularity of smartphones to the global population, its computing capabilities and affordability have made it an effective tool for disseminating health care ( 28 , 29 ).

mHealth cardiology applications have generally been utilized for the following purposes: monitoring, self-management, reporting, adherence and rehabilitation. The majority of research has focused on monitoring systems which aim to detect abnormalities in patients through the integration of mobile technologies in their daily life ( 30 , 31 ). For instance, the pairing of a wireless heart monitor to a smartphone, and data transmission over mobile telecommunications networks would provide physicians a constant stream of reports regarding a patient’s status ( 27 , 32 , 33 ). Additionally, through the use of mobile or web based applications, interaction between physician and patient can be achieved on a consistent basis regardless of distance between both parties ( 34 , 35 ). Studies have shown that mHealth applications can achieve similar utility in urban and rural settings ( 36 ), increase patient adherence towards therapy and rehabilitation ( 37 , 38 ), and successfully identify and manage health deteriorations ( 39 ). Although preliminary testing demonstrates the potential of mHealth, results are still inadequate due to the limited number of trials that have been performed ( 28 , 40 ).

Despite its potential, telemedicine and mHealth faces several issues when applied to rural areas. First of all, the availability and speed of an internet connection can be a limiting factor to the quality of exchanged information as well as the timeliness of vital answers ( 10 , 41 ). The poor quality or lack of mobile telecommunication infrastructures, and limited power supplies are serious impediments to the usage of mobile devices ( 42 , 43 ). Even with the appropriate technologies and infrastructures, the acquisition and interpretation of imagery are highly user-dependent and require a certain level of expertise, which may not be available in geographically isolated areas ( 17 , 19 ). In the case of echocardiography, physicians are required to undergo a long training process which has a steep learning curve ( 44 , 45 ). Furthermore, during interpretation, image quality can be affected by speckle noise, low contrast and signal dropouts which interfere with diagnosis ( 9 , 46 ). Apart from that, the complex spatio-temporal motion of the heart can cause difficulties in interpretation ( 5 ). Lastly, after evaluation, high inter- and intra-observer variations as well as subjective interpretations can occur, even for experts ( 47 ). The current echocardiography workflow consisting of examination, image analysis, final integration and reporting, can be a time-consuming and inefficient process ( 48 ). Besides that, the obstacles mentioned above play a part in influencing the overall health outcomes. Because of this, there is a critical need for automated systems capable of providing diagnostic assistance, decision support and objective interpretation ( 49 ). In telemedicine or mHealth scenarios where the absence of medical expertise and telecommunications infrastructures are prevalent, CADx systems can potentially overcome these issues.

CADx systems are capable of assisting physicians during the interpretation and diagnosis of medical imagery. CADx systems can be divided into low complexity and sophisticated systems. Low complexity systems offer only disease or non-disease diagnosis while sophisticated systems are able to diagnose different stages of diseases ( 2 ). A CADx system normally consists of four phases, which are image acquisition and pre-processing, segmentation or region-of-interest selection, feature extraction and classification ( 49 ). Following the acquisition of medical imagery, frames are normally pre-processed to remove visual abnormalities and improve diagnostic quality. Next, depending on the purpose of classification, segmentation is performed to properly delineate objects or areas of importance. Features are then extracted from these regions for the purposes of training learning algorithms. Once properly trained, the CADx system would be able to provide disease classifications for new patient data. As mentioned earlier, the diagnosis of a disease is highly dependent on a physician’s subjective interpretation. CADx systems can reduce this subjectivity by offering precise tools capable of improving diagnosis and providing quantitative support for decision making ( 50 ).

Smartphones are particularly useful for the task of acquiring and processing images. As technology improves, hardware components such as digital displays and cameras are constantly being upgraded ( 51 ). Some works have successfully embedded mobile devices with CADx systems for the purpose of identifying specific diseases. For example, researchers investigating the detection of retinal diseases combined a smartphone and microscopic lens to perform eye examinations and disease diagnosis ( 52 ). By capturing retinal images and analyzing them, normal or infected conditions could be identified. Similar research involving the detection of ultrasound kidney abnormalities also made use of a smartphone camera and machine learning algorithms for diagnostic analysis ( 53 ). In both cases, the disease detection rates were competitive with accuracies above 80%.

The clinical and system benefits of tools such as CADx are maximized when coupled with machine learning techniques, which are an assortment of mathematical algorithms capable of identifying patterns in data and performing predictions on new information ( 54 ). In general, machine learning techniques are divided into supervised learning, unsupervised learning and reinforcement learning ( 55 ). In supervised learning, labelled inputs and outputs are provided for training, with the goal of predicting new data. On the other hand, unsupervised learning does not require any labelled inputs nor desired outputs. Instead, it focuses on discovering naturally occurring patterns within the given data. Reinforcement learning involves interactions with a changing environment whereby feedback is received in the form of rewards or punishments, and answers are found through trial and error. Out of the three techniques, supervised learning is the most widely used ( 56 ). The role of machine learning in the field of medicine, particularly cardiology, has been covered in several papers ( 57 , 58 ). Various supervised learning algorithms including support vector machines, decision trees, random forests, k-nearest neighbors, and others, have been applied to problems ranging from image analysis, prediction, diagnosis and treatment of heart disease ( 57 ). For example, many works have utilized machine learning algorithms to discover and rank features ( 49 ) as well as segment heart walls and analyze their motion patterns ( 59 , 60 ) in an effort to determine the lack or presence of abnormalities. Automated systems like CADx can gain incremental improvements in accuracy and reliability by employing these methods, though they may be constrained by their ability to process raw data.

The creation of conventional machine learning systems require careful engineering and substantial expert knowledge to design feature extractors capable of transforming raw data into suitable representations for classification ( 61 ). Furthermore, the engineering process is a time-consuming effort and features are often low-level since prior knowledge is hand-crafted ( 62 ). In recent years, deep learning has emerged as the leading technique for computer vision and imaging tasks. Deep learning is a class of machine learning algorithms that use supervised or unsupervised strategies to automatically learn features through the implementation of multi-layered hierarchies for the purpose of classification ( 63 ). Compared to traditional machine learning techniques, deep learning has the potential to change the modelling of CADx systems. Cheng et al. ( 64 ), discussed a 3-fold advantage as follows. With deep learning, features can be directly uncovered without the effort of explicitly defining them. These deep learning discovered features may surpass those found with conventional means. Furthermore, feature interaction and hierarchy can be simultaneously maintained within the deep neural network architecture, which would lead to the simplification of the feature selection process. Finally, feature extraction, selection and classification can be jointly optimized within the same architecture.

An important component of deep learning algorithms is the artificial neural network (ANN). ANNs are information processing systems composed of multiple interconnected elements which cooperate to perform parallel processing in an effort to solve a particular problem ( 65 ). In visual tasks where raw features are not individually interpretable, ANNs have achieved a high level of success as a result of their ability to learn hierarchical representations ( 66 ). One type of ANN, convolutional neural network (CNN), has produced many accomplishments in detection, segmentation and recognition of objects and regions within images ( 61 ). A CNN comprises of multiple layers with neurons that process portions of an input image. The outputs of these neurons are tiled to form an overlap, which provides a filtered representation of the original image. This process is repeated for each layer, until the final output, which is typically the probabilities of predicted classes. The training of a CNN requires many iterations to optimize network parameters. During each iteration, a batch of samples are chosen at random from the input training set and undergoes forward-propagation through the network layers. In order to achieve optimal results, parameters within the network are updated through back-propagation to minimize a cost function. Once trained, a network can be applied on new or unseen data to obtain predictions. The main advantages of CNNs, can be summarized as follows. Features can be automatically learned from a training set without the need for expert knowledge or hard-coding ( 67 , 68 ). Additionally, it has been demonstrated that the extracted features are relatively robust to image transformations or variations ( 63 , 67 ). Finally, research has shown that CNNs outperform traditional image classification methods and can achieve state-of-the-art results ( 67 , 69 ). The application of deep learning techniques for general and healthcare ( 70 - 72 ) purposes have been reviewed by various researchers. In the field of medical imaging, CNNs have been mainly utilized for detection, segmentation and classification ( 71 ). These tasks make up part of the CADx process flow as discussed before.

Despite its benefits, deep learning and CNN models face certain complications during training. A large amount of training data is required to avoid the over-fitting problem ( 73 , 74 ). In the medical field, this is a challenging requirement as expert annotation is costly and disease specific datasets are rare ( 70 , 75 ). When a dataset is imbalanced, predictions are biased towards the majority samples, thus leading to over-fitting ( 76 ). A commonly used method to reduce over-fitting is through the implementation of data augmentation to artificially enlarge a dataset using label-preserving transformations ( 77 , 78 ). Data augmentation, which can be applied during training or testing, perturbs an image through transformations such as cropping or flipping, in order to generate additional samples in the dataset ( 79 ). Many tests have proven that data augmentation improves classification accuracy ( 77 , 79 ), though there are cases where a reduction in accuracy occurs instead ( 80 ). Medical images that are acquired at fixed viewpoints or infrequently experience variations of angles may encounter reduced performance due to added noise created from augmented data. A further step to handling limited training data is by performing transfer learning which applies knowledge learned from a previous task to a new task ( 74 ). The availability of big data repositories, though dissimilar, has made transfer learning a suitable choice for pretraining and adapting CNNs for the medical imaging domain ( 75 , 81 ). Additionally, research has shown that transfer learning can be exploited in data scarce scenarios even when the knowledge transferred is derived from unrelated domains such as natural images ( 73 , 82 ).

Deep learning algorithms can be optimized through the tuning of hyperparameters such as learning rate, network architectures, activation functions and more. These parameters are essential for controlling learning behavior and must be determined before the training process ( 83 ). The act of choosing ideal hyperparameters is a long and tedious process as many values are interdependent and require multiple trials to refine ( 84 , 85 ). Furthermore, many experts still rely on their own technical savvy to manually determine appropriate values ( 86 ). Because of this, several automated hyperparameter optimization methods were created. The works focused on enhancing different factors ranging from prediction accuracy ( 85 ), speed of parameter selection ( 84 , 86 ), and ranking of hyperparameters ( 83 ). Evaluations have demonstrated that hyperparameter values chosen by these algorithms can yield higher accuracy rates compared to experts. Moreover, the time needed for parameter optimization is continually decreasing.

The popularity of deep learning can be attributed to the tremendous increase of computational processing power in the form of graphics processing units (GPU) as well as the lowered hardware costs ( 87 , 88 ). Although this is so, substantial computational and memory resources are still necessary to ensure timely completion of the CNN training process ( 70 , 75 ). Likewise, when adapted for use on mobile devices, the requirements for training and running deep learning algorithms are magnified to a greater extent ( 72 ). A typical solution is for the mobile device to offload execution to powerful cloud servers by exchanging training data and output results. In normal circumstances where telecommunications infrastructures are available, this could be a viable choice. But as discussed earlier, rural locations may not possess the foundations necessary to accomplish cloud computing. Additionally, even with available communications networks, cloud-based options may potentially expose private data, consume significant bandwidth and deplete mobile battery reserves ( 89 - 91 ). Research has therefore been undertaken to enable local processing on mobile devices with the goal of alleviating computational requirements ( 89 - 91 ), reducing power consumption ( 92 - 94 ) and ensuring privacy ( 95 ). Experimental results indicate that it is possible to efficiently execute deep learning models on mobile processors while maintaining low energy usage.

The above issues regarding data preparation, hyperparameter optimization and mobile deep learning are especially important in the context of telemedicine and mHealth. As previously discussed, medical datasets can be difficult to acquire and may not necessarily be suited for training in its raw form. Take for instance a scenario where echocardiogram videos are collected from a hospital which routinely conducts heart screenings for all their patients. In this situation, it is likely that a greater number of patients have normal echocardiograms as opposed to abnormal ones. As a consequence of the imbalance, classification models generated from the raw data may overfit to the majority class. This would lead to an increase of false negative detections where abnormal hearts are classified as normal instead. It is therefore essential to correctly prepare data for training through the application of suitable augmentation and transfer learning techniques.

Another concern towards the training process is the selection of network architectures and parameters. These variables can significantly affect the accuracy, sensitivity (true positive rate) and specificity (true negative rate) of resulting models. Since the intention is to accurately classify the presence of diseases, it is imperative that models are sufficiently sensitive and specific to correctly identify unhealthy patients as abnormal while ensuring healthy patients are not misclassified. The optimization of hyperparameters is consequently indispensable considering the liabilities and risks involved if a misdiagnosis were to occur.

Embedding deep learning algorithms into telemedicine and mHealth CADx applications would bring about many benefits in terms of diagnostic capabilities and usability. The potency of CNNs for automated visual analysis can be applied to rural healthcare scenarios where medical expertise is absent. A novice physician with a smartphone need only capture videos or images, and then utilize the installed CADx system to obtain diagnostic assistance, decision support and objective interpretation. Moreover, with recent advancements of mobile deep learning, portable systems running on smartphones can facilitate the delivery of healthcare services in various remote settings. Because of these factors, the need to decrease computation time and reduce power consumption is crucial to ensuring ubiquitous medical support.

The deployment of rural healthcare services in the form of telemedicine and mHealth applications is sorely needed. Diverse solutions comprised of portable medical equipment and mobile technologies have been created to address the deficiencies encountered in remote settings. In addition to that, CADx systems have also been utilized for assistive interpretation and diagnosis of medical imagery. The implementation of machine and deep learning algorithms to these systems would bring numerous benefits to both physician and patient. In the case of deep learning, the accuracy, sensitivity and specificity of these systems may equal or even surpass human experts. Furthermore, the advancement of mobile technologies would expedite the proliferation of healthcare services to those residing in impoverished regions. This in turn could then lead to the further decline of death and disease rates of the global population.

This research was supported by the Swinburne Sarawak Postgraduate Research Studentship (SPRS). The authors wish to acknowledge the Sarawak General Hospital for providing assistance and medical domain knowledge regarding cardiovascular diseases.

Conflicts of Interest : The authors have no conflicts of interest to declare.

WHO. Cardiovascular diseases (CVDs). Available online: http://www.who.int/mediacentre/factsheets/fs317/en/

Faust O, Acharya UR, Sudarshan VK, et al. Computer aided diagnosis of Coronary Artery Disease, Myocardial Infarction and carotid atherosclerosis using ultrasound images: A review. Phys Med 2017;33:1-15. [ Crossref ] [ PubMed ]

National Institutes of Health. Consumer use of mHealth for prevention of cardiovascular disease: Where the science stands. Available online: https://obssr.od.nih.gov/consumer-use-of-mhealth-for-prevention-of-cardiovascular-disease-where-the-science-stands/

Spencer KT, Kimura BJ, Korcarz CE, et al. Focused cardiac ultrasound: recommendations from the American Society of Echocardiography. J Am Soc Echocardiogr 2013;26:567-81. [ Crossref ] [ PubMed ]

Beymer D, Syeda-Mahmood T. Cardiac disease recognition in echocardiograms using spatio-temporal statistical models. 30th Annual International Conference of the IEEE. 20-25 Aug, 2008; Vancouver, BC, Canada. IEEE, 2008.

Wu H, Huynh TT, Souvenir R. Motion factorization for echocardiogram classification. 11th International Symposium. 29 Apr-02 May, 2014; Beijing, China. IEEE, 2014.

Singh S, Bansal M, Maheshwari P, et al. American Society of Echocardiography: Remote Echocardiography with Web-Based Assessments for Referrals at a Distance (ASE-REWARD) Study. J Am Soc Echocardiogr 2013;26:221-33. [ Crossref ] [ PubMed ]

Gladding PA, Cave A, Zareian M, et al. Open access integrated therapeutic and diagnostic platforms for personalized cardiovascular medicine. J Pers Med 2013;3:203-37. [ Crossref ] [ PubMed ]

Sudarshan VK, Acharya UR, Ng EY, et al. Data mining framework for identification of myocardial infarction stages in ultrasound: A hybrid feature extraction paradigm (PART 2). Comput Biol Med 2016;71:241-51. [ Crossref ] [ PubMed ]

Sutherland JE, Sutphin D, Redican K, et al. Telesonography: foundations and future directions. J Ultrasound Med 2011;30:517-22. [ Crossref ] [ PubMed ]

Graziplene LR. Creating Telemedicine-Based Medical Networks for Rural and Frontier Areas. IBM Center for The Business of Government 2009. Available online: http://observgo.uquebec.ca/observgo/fichiers/71490_Telemedicine.pdf

Bodenheimer T, Pham HH. Primary care: current problems and proposed solutions. Health Aff (Millwood) 2010;29:799-805. [ Crossref ] [ PubMed ]

Pattichis CS, Kyriacou E, Voskarides S, et al. Wireless telemedicine systems: an overview. IEEE, 2002;44:143-53.

Martínez A, Villarroel V, Seoane J, et al. Rural telemedicine for primary healthcare in developing countries. IEEE, 2004;23:13-22.

Steele R, Lo A. Telehealth and ubiquitous computing for bandwidth-constrained rural and remote areas. Pers Ubiquitous Comput 2013;17:533-43. [ Crossref ]

Smith AC, Bensink M, Armfield N, et al. Telemedicine and rural health care applications. J Postgrad Med 2005;51:286-93. [ PubMed ]

Ferreira AC, O'Mahony E, Oliani AH, et al. Teleultrasound: historical perspective and clinical application. Int J Telemed Appl 2015;2015:306259.

McBeth P, Crawford I, Tiruta C, et al. Help is in your pocket: the potential accuracy of smartphone- and laptop-based remotely guided resuscitative telesonography. Telemed J E Health 2013;19:924-30. [ Crossref ] [ PubMed ]

Pian L, Gillman LM, McBeth PB, et al. Potential Use of Remote Telesonography as a Transformational Technology in Underresourced and/or Remote Settings. Emerg Med Int 2013;2013:986160.

Choi BG, Mukherjee M, Dala P, et al. Interpretation of remotely downloaded pocket-size cardiac ultrasound images on a web-enabled smartphone: validation against workstation evaluation. J Am Soc Echocardiogr 2011;24:1325-30. [ Crossref ] [ PubMed ]

Kim C, Hur J, Kang BS, et al. Can an Offsite Expert Remotely Evaluate the Visual Estimation of Ejection Fraction via a Social Network Video Call? J Digit Imaging 2017. [Epub ahead of print]. [ Crossref ] [ PubMed ]

Adambounou K, Adjenou V, Salam AP, et al. A low-cost tele-imaging platform for developing countries. Front Public Health 2014;2:135. [ Crossref ] [ PubMed ]

Crawford I, McBeth PB, Mitchelson M, et al. How to set up a low cost tele-ultrasound capable videoconferencing system with wide applicability. Crit Ultrasound J 2012;4:13. [ Crossref ] [ PubMed ]

Liteplo AS, Noble VE, Attwood BH. Real-time video streaming of sonographic clips using domestic internet networks and free videoconferencing software. J Ultrasound Med 2011;30:1459-66. [ Crossref ] [ PubMed ]

Littman-Quinn R, Chandra A, Schwartz A, et al. mHealth applications for telemedicine and public health intervention in Botswana. IST-Africa Conference Proceedings. 11-13 May, 2011; Gaborone, Botswana. IEEE, 2011.

Aranda-Jan CB, Mohutsiwa-Dibe N, Loukanova S. Systematic review on what works, what does not work and why of implementation of mobile health (mHealth) projects in Africa. BMC Public Health 2014;14:188. [ Crossref ] [ PubMed ]

Kirtava Z, Gegenava T, Gegenava M. mHealth for cardiac patients telemonitoring and integrated care. e-Health Networking, Applications & Services (Healthcom), 2013 IEEE 15th International Conference. 9-12 Oct, 2013; Lisbon, Portugal. IEEE, 2013.

Cajita MI, Gleason KT, Han HR. A Systematic Review of mHealth-Based Heart Failure Interventions. J Cardiovasc Nurs 2016;31:E10-22. [ Crossref ] [ PubMed ]

Perera C, Chakrabarti R. The utility of mHealth in Medical Imaging. J Mob Technol Med 2013;2:4-6. [ Crossref ]

Martínez-Pérez B, de la Torre-Díez I, López-Coronado M, et al. Mobile apps in cardiology JMIR Mhealth Uhealth 2013;1:e15.  review. [ Crossref ] [ PubMed ]

Jain PK, Tiwari AK. Heart monitoring systems--a review. Comput Biol Med 2014;54:1-13. [ Crossref ] [ PubMed ]

Hickey KT, Biviano AB, Garan H, et al. Evaluating the Utility of Mhealth ECG Heart Monitoring for the Detection and Management of Atrial Fibrillation in Clinical Practice. J Atr Fibrillation 2017;9:16-20.

Kitsiou S, Thomas M, Marai GE, et al. Development of an innovative mHealth platform for remote physical activity monitoring and health coaching of cardiac rehabilitation patients. Biomedical & Health Informatics (BHI), 2017 IEEE EMBS International Conference on. 16-19 Feb, 2017; Orlando, FL, USA. IEEE, 2017.

Modre-Osprian R, Hayn D, Kastner P, et al. Mhealth Supporting Dynamic Medication Management during Home Monitoring of Heart Failure Patients. Biomed Tech (Berl) 2013. [Epub ahead of print].

Alnosayan N, Lee E, Alluhaidan A, et al. MyHeart: An intelligent mHealth home monitoring system supporting heart failure self-care. e-Health Networking, Applications and Services (Healthcom), 2014 IEEE 16th International Conference. 15-18 Oct, 2014; Natal, Brazil. IEEE, 2014.

de Garibay VG, Fernández MA, de la Torre-Díez I, et al. Utility of a mHealth App for Self-Management and Education of Cardiac Diseases in Spanish Urban and Rural Areas. J Med Syst 2016;40:186. [ Crossref ] [ PubMed ]

Beatty AL, Fukuoka Y, Whooley MA. Using mobile technology for cardiac rehabilitation: a review and framework for development and evaluation. J Am Heart Assoc 2013;2:e000568. [ Crossref ] [ PubMed ]

Park LG, Howie-Esquivel J, Chung ML, et al. A text messaging intervention to promote medication adherence for patients with coronary heart disease: a randomized controlled trial. Patient Educ Couns 2014;94:261-8. [ Crossref ] [ PubMed ]

Alnosayan N, Chatterjee S, Alluhaidan A, et al. Design and Usability of a Heart Failure mHealth System: A Pilot Study. JMIR Hum Factors 2017;4:e9. [ Crossref ] [ PubMed ]

Pfaeffli Dale L, Dobson R, Whittaker R, et al. The effectiveness of mobile-health behaviour change interventions for cardiovascular disease self-management: A systematic review. Eur J Prev Cardiol 2016;23:801-17. [ Crossref ] [ PubMed ]

Balasingam M, Sivalingam B. Future of Tele-echocardiography. GSTF J Nurs Health Care 2015;3:200-5.

Brian RM, Ben-Zeev D. Mobile health (mHealth) for mental health in Asia: objectives, strategies, and limitations. Asian J Psychiatr 2014;10:96-100. [ Crossref ] [ PubMed ]

Chigona W, Nyemba M, Metfula A. A review on mHealth research in developing countries. J Commun Inform 2013;9.

Bosch JG, Nijland F, Mitchell SC, et al. Computer-aided diagnosis via model-based shape analysis: automated classification of wall motion abnormalities in echocardiograms. Acad Radiol 2005;12:358-67. [ Crossref ] [ PubMed ]

Knackstedt C, Bekkers SC, Schummers G, et al. Fully Automated Versus Standard Tracking of Left Ventricular Ejection Fraction and Longitudinal Strain: The FAST-EFs Multicenter Study. J Am Coll Cardiol 2015;66:1456-66. [ Crossref ] [ PubMed ]

Belous G, Busch A, Rowlands D. Segmentation of the Left Ventricle from Ultrasound Using Random Forest with Active Shape Model. Artificial Intelligence, Modelling and Simulation (AIMS), 2013 1st International Conference. 3-5 Dec, 2013; Kota Kinabalu, Malaysia. IEEE, 2013.

Fung G, Qazi M, Krishnan S, et al. Sparse classifiers for Automated HeartWall Motion Abnormality Detection. Machine Learning and Applications, 2005. Proceedings. Fourth International Conference on. 15-17 Dec, 2005; Los Angeles, CA, USA. IEEE, 2005.

Tajik AJ. Machine Learning for Echocardiographic Imaging: Embarking on Another Incredible Journey. J Am Coll Cardiol 2016;68:2296-8. [ Crossref ] [ PubMed ]

Vidya KS, Ng EY, Acharya UR, et al. Computer-aided diagnosis of Myocardial Infarction using ultrasound images with DWT, GLCM and HOS methods: A comparative study. Comput Biol Med 2015;62:86-93. [ Crossref ] [ PubMed ]

Tsai D-Y. Comparison of four computer-aided diagnosis schemes for automated discrimination of myocardial heart disease. Signal Processing Proceedings, 2000. WCCC-ICSP 2000. 5th International Conference. 21-25 Aug, 2000; Beijing, China. IEEE, 2000.

Bolster NM, Giardini ME, Livingstone IA, et al. How the smartphone is driving the eye-health imaging revolution. Expert Rev Ophthalmol 2014;9:475-85. [ Crossref ]

Bourouis A, Feham M, Hossain MA, et al. An intelligent mobile based decision support system for retinal disease diagnosis. Decis Sup Syst 2014;59:341-50. [ Crossref ]

Vaish P, Bharath R, Rajalakshmi P, et al. Smartphone based automatic abnormality detection of kidney in ultrasound images. e-Health Networking, Applications and Services (Healthcom), 2016 IEEE 18th International Conference. 14-16 Sept, 2016; Munich, Germany. IEEE, 2016.

Slomka PJ, Dey D, Sitek A, et al. Cardiac imaging: working towards fully-automated machine analysis & interpretation. Expert Rev Med Devices 2017;14:197-212. [ Crossref ] [ PubMed ]

Qiu J, Wu Q, Ding G, et al. A survey of machine learning for big data processing. EURASIP J Adv Signal Process 2016;2016:67.

Jordan MI, Mitchell TM. Machine learning: Trends, perspectives, and prospects. Science 2015;349:255-60. [ Crossref ] [ PubMed ]

Krittanawong C, Zhang H, Wang Z, et al. Artificial Intelligence in Precision Cardiovascular Medicine. J Am Coll Cardiol 2017;69:2657-64. [ Crossref ] [ PubMed ]

Safdar S, Zafar S, Zafar N, et al. Machine learning based decision support systems (DSS) for heart disease diagnosis: a review. Artif Intell Rev 2017.1-27.

Balaji G, Subashini T, Chidambaram N. Detection of Heart Muscle Damage from Automated Analysis of Echocardiogram Video. IETE J Res 2015;61:236-43. [ Crossref ]

Shalbaf A, Behnam H, Alizade-Sani Z, et al. Automatic classification of left ventricular regional wall motion abnormalities in echocardiography images using nonrigid image registration. J Digit Imaging 2013;26:909-19. [ Crossref ] [ PubMed ]

LeCun Y, Bengio Y, Hinton G. Deep learning. Nature 2015;521:436-44. [ Crossref ] [ PubMed ]

Antony J, McGuinness K, O’Connor NE, et al. Quantifying Radiographic Knee Osteoarthritis Severity using Deep Convolutional Neural Networks. 2016. Available online: https://arxiv.org/abs/1609.02469

Chen XW, Lin X. Big Data Deep Learning: Challenges and Perspectives. IEEE Access 2014;2:514-25.

Cheng JZ, Ni D, Chou YH, et al. Computer-Aided Diagnosis with Deep Learning Architecture: Applications to Breast Lesions in US Images and Pulmonary Nodules in CT Scans. Sci Rep 2016;6:24454. [ Crossref ] [ PubMed ]

Macukow B. Neural Networks – State of Art, Brief History, Basic Models and Architecture. Springer International Publishing Switzerland, 2016:3-14.

Lipton ZC, Berkowitz J, Elkan C. A Critical Review of Recurrent Neural Networks for Sequence Learning. 2015. Available online: https://arxiv.org/abs/1506.00019

Gao X, Li W, Loomes M, et al. A fused deep learning architecture for viewpoint classification of echocardiography. Inform Fusion 2017;36:103-13. [ Crossref ]

Tran PV. A Fully Convolutional Neural Network for Cardiac Segmentation in Short-Axis MRI. 2016. Available online: https://arxiv.org/abs/1604.00494

Khan SA, Yong SP. An Evaluation of Convolutional Neural Nets for Medical Image Anatomy Classification. Advances in Machine Learning and Signal Processing. Springer International Publishing Switzerland, 2016:293-303.

Greenspan H, van Ginneken B, Summers RM. Guest Editorial Deep Learning in Medical Imaging: Overview and Future Promise of an Exciting New Technique. IEEE Trans Med Imaging 2016;35:1153-9. [ Crossref ]

Litjens G, Kooi T, Bejnordi BE, et al. A Survey on Deep Learning in Medical Image Analysis. 2017. Available online: https://arxiv.org/abs/1702.05747

Miotto R, Wang F, Wang S, et al. Deep learning for healthcare: review, opportunities and challenges. Brief Bioinform 2017. [Epub ahead of print]. [ Crossref ] [ PubMed ]

Ravishankar H, Sudhakar P, Venkataramani R, et al. Understanding the Mechanisms of Deep Transfer Learning for Medical Images. 2017. Available online: https://arxiv.org/abs/1704.06040

Shie CK, Chuang CH, Chou CN, et al. Transfer representation learning for medical image analysis. Engineering in Medicine and Biology Society (EMBC), 2015 37th Annual International Conference of the IEEE. 25-29 Aug, 2015; Milan, Italy. IEEE, 2015.

Tajbakhsh N, Shin JY, Gurudu SR, et al. Convolutional Neural Networks for Medical Image Analysis: Full Training or Fine Tuning? IEEE Trans Med Imaging 2016;35:1299-312. [ Crossref ] [ PubMed ]

Setio AA, Ciompi F, Litjens G, et al. Pulmonary Nodule Detection in CT Images: False Positive Reduction Using Multi-View Convolutional Networks. IEEE Trans Med Imaging 2016;35:1160-9. [ Crossref ] [ PubMed ]

Krizhevsky A, Sutskever I, Hinton GE. ImageNet Classification with Deep Convolutional Neural Networks. Advances in Neural Information Processing Systems 25. Neural Information Processing Systems, 2012.

Arevalo J, González FA, Ramos-Pollán R, et al. Representation learning for mammography mass lesion classification with convolutional neural networks. Comput Methods Programs Biomed 2016;127:248-57. [ Crossref ] [ PubMed ]

Chatfield K, Simonyan K, Vedaldi A, et al. Return of the Devil in the Details: Delving Deep into Convolutional Nets. 2014. Available online: https://arxiv.org/abs/1405.3531

Yu Y, Lin H, Yu Q, et al. Modality Classification for Medical Images using Multiple Deep Convolutional Neural Networks. J Comput Inf Syst 2015;11:5403-13.

Weiss K, Khoshgoftaar TM, Wang D. A survey of transfer learning. J Big Data 2016;3:9. [ Crossref ]

Moradi M, Gur Y, Wang H, et al. A hybrid learning approach for semantic labeling of cardiac CT slices and recognition of body position. Biomedical Imaging (ISBI), 2016 IEEE 13th International Symposium. 13-16 April, 2016; Prague, Czech Republic. IEEE, 2016.

Jia D, Wang R, Xu C, et al. QIM: Quantifying Hyperparameter Importance for Deep Learning. In: Gao G, Qian D, Gao X, et al. editors. Network and Parallel Computing. Springer, Cham, 2016.

Ilievski I, Akhtar T, Feng J, et al. Efficient Hyperparameter Optimization for Deep Learning Algorithms Using Deterministic RBF Surrogates. Thirty-First AAAI Conference on Artificial Intelligence. 2017.

Li Z, Jin L, Yang C, et al. Hyperparameter search for deep convolutional neural network using effect factors. Signal and Information Processing (ChinaSIP), 2015 IEEE China Summit and International Conference. 12-15 July, 2015; Chengdu, China. IEEE, 2015.

Domhan T, Springenberg JT, Hutter F. Speeding up automatic hyperparameter optimization of deep neural networks by extrapolation of learning curves. IJCAI’15 Proceedings of the 24th International Conference on Artificial Intelligence. 2015:3460-8.

Deng L. Three classes of deep learning architectures and their applications: a tutorial survey. APSIPA Trans Signal Inf Process 2012.

Zeiler MD, Fergus R. Visualizing and Understanding Convolutional Networks. In: Fleet D, Pajdla T, Schiele B, et al. editors. Computer Vision – ECCV 2014. Springer, Cham, 2014:818-33.

Chen CF, Lee GG, Sritapan V, et al. Deep Convolutional Neural Network on iOS Mobile Devices. Signal Processing Systems (SiPS), 2016 IEEE International Workshop. 26-28 Oct, 2016; Dallas, TX, USA. IEEE, 2016.

Huynh LN, Balan RK, Lee Y. DeepSense: A GPU-based Deep Convolutional Neural Network Framework on Commodity Mobile Devices. Proceedings of the 2016 Workshop on Wearable Systems and Applications. ACM, 2016:25-30.

Lane ND, Bhattacharya S, Georgiev P, et al. DeepX: A Software Accelerator for Low-Power Deep Learning Inference on Mobile Devices. Information Processing in Sensor Networks (IPSN), 2016 15th ACM/IEEE International Conference. 11-14 April, 2016; Vienna, Austria. IEEE, 2016.

Georgiev P, Lane ND, Mascolo C, et al. Accelerating Mobile Audio Sensing Algorithms through On-Chip GPU Offloading. Proceedings of the 15th Annual International Conference on Mobile Systems, Applications, and Services. ACM, 2017:306-18.

Lane ND, Georgiev P, Qendro L. Deepear: robust smartphone audio sensing in unconstrained acoustic environments using deep learning. Proceedings of the 2015 ACM International Joint Conference on Pervasive and Ubiquitous Computing. ACM, 2015:283-94.

Rizvi ST, Cabodi G, Patti D, et al. GPGPU Accelerated Deep Object Classification on a Heterogeneous Mobile Platform. Electronics 2016;5:88. [ Crossref ]

Ossia SA, Shamsabadi AS, Taheri A, et al. A Hybrid Deep Learning Architecture for Privacy-Preserving Mobile Analytics. 2017. Available online: https://arxiv.org/abs/1703.02952

Your session has expired. Please sign in again.
