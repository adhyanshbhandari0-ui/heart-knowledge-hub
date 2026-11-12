# Classifying Heart Sounds Challenge

**Source:** http://www.peterjbentley.com/heartchallenge

---

Background Task Overview Downloads About Data Test Procedure Important Dates

Peter Bentley , Glenn Nordehn , Miguel Coimbra , Shie Mannor , Rita Getz

According to the World Health Organisation, cardiovascular diseases (CVDs) are the number one cause of death globally: more people die annually from CVDs than from any other cause. An estimated 17.1 million people died from CVDs in 2004, representing 29% of all global deaths. Of these deaths, an estimated 7.2 million were due to coronary heart disease. Any method which can help to detect signs of heart disease could therefore have a significant impact on world health. This challenge is to produce methods to do exactly that. Specifically, we are interested in creating the first level of screening of cardiac pathologies both in a Hospital environment by a doctor (using a digital stethoscope) and at home by the patient (using a mobile device).

The problem is of particular interest to machine learning researchers as it involves classification of audio sample data, where distinguishing between classes of interest is non-trivial. Data is gathered in real-world situations and frequently contains background noise of every conceivable type. The differences between heart sounds corresponding to different heart symptoms can also be extremely subtle and challenging to separate. Success in classifying this form of data requires extremely robust classifiers. Despite its medical significance, to date this is a relatively unexplored application for machine learning.

Data has been gathered from two sources: (A) from the general public via the iStethoscope Pro iPhone app, provided in Dataset A , and (B) from a clinic trial in hospitals using the digital stethoscope DigiScope, provided in Dataset B .

The first challenge is to produce a method that can locate S1(lub) and S2(dub) sounds within audio data, segmenting the Normal audio files in both datasets. To enable your machine learning method to learn we provide the exact location of S1 and S2 sounds for some of the audio files. You need to use them to identify and locate the S1 and S2 sounds of all the heartbeats in the unlabelled group. The locations of sounds are measured in audio samples for better precision. Your method must use the same unit.

The task is to produce a method that can classify real heart audio (also known as âbeat classificationâ) into one of four categories for Dataset A:

You may tackle either or both of these challenges. If you can solve the first challenge, the second will be considerably easier! The winner of each challenge will be the method best able to segment and/or classify two sets of unlabelled data into the correct categories after training on both datasets provided below. The creator of the winning method will receive a WiFi 32Gb iPad as the prize, awarded at a workshop at AISTATS 2012.

After downloading the data, please register your interest to participate in the challenge by clicking here .

Dataset A, containing 176 files in WAV format, organized as:

The same datasets are also available in aif format:

Segmentation data (updated 23 March 2012), giving locations of S1 and S2 sounds in Atraining_normal: Atraining_normal_seg.csv

Dataset B, containing 656 files in WAV format, organized as:

The same datasets are also available in aif format:

Segmentation data, giving locations of S1 and S2 sounds in Btraining_normal: Btraining_normal_seg.csv

Evaluation Scripts plus full details of the metrics and test procedure you must use in order to measure the effectiveness of your methods are available here: Evaluation.zip

Challenge 1 involves segmenting the audio files in Atraining_normal.zip and Btraining_normal.zip using the training segmentations provided above.

Challenge 2 involves correctly labelling the sounds in Aunlabelledtest.zip and Bunlabelledtest.zip

Please use the following citation if the data is used:

@misc{pascal-chsc-2011, author = "Bentley, P. and Nordehn, G. and Coimbra, M. and Mannor, S.", title = "The {PASCAL} {C}lassifying {H}eart {S}ounds {C}hallenge 2011 {(CHSC2011)} {R}esults", howpublished = "http://www.peterjbentley.com/heartchallenge/index.html"}

The audio files are of varying lengths, between 1 second and 30 seconds (some have been clipped to reduce excessive noise and provide the salient fragment of the sound).

Most information in heart sounds is contained in the low frequency components, with noise in the higher frequencies. It is common to apply a low-pass filter at 195 Hz. Fast Fourier transforms are also likely to provide useful information about volume and frequency over time. More domain-specific knowledge about the difference between the categories of sounds is provided below.

Normal Category In the Normal category there are normal, healthy heart sounds. These may contain noise in the final second of the recording as the device is removed from the body. They may contain a variety of background noises (from traffic to radios). They may also contain occasional random noise corresponding to breathing, or brushing the microphone against clothing or skin. A normal heart sound has a clear âlub dub, lub dubâ pattern, with the time from âlubâ to âdubâ shorter than the time from âdubâ to the next âlubâ (when the heart rate is less than 140 beats per minute). Note the temporal description of âlubâ and âdubâ locations over time in the following illustration:

â¦lubâ¦â¦â¦.dubâ¦â¦â¦â¦â¦. lubâ¦â¦â¦.dubâ¦â¦â¦â¦â¦. lubâ¦â¦â¦.dubâ¦â¦â¦â¦â¦. lubâ¦â¦â¦.dubâ¦

In medicine we call the lub sound "S1" and the dub sound "S2". Most normal heart rates at rest will be between about 60 and 100 beats (âlub dubâs) per minute. However, note that since the data may have been collected from children or adults in calm or excited states, the heart rates in the data may vary from 40 to 140 beats or higher per minute. Dataset B also contains noisy_normal data - normal data which includes a substantial amount of background noise or distortion. You may choose to use this or ignore it, however the test set will include some equally noisy examples .

Murmur Category Heart murmurs sound as though there is a âwhooshing, roaring, rumbling, or turbulent fluidâ noise in one of two temporal locations: (1) between âlubâ and âdubâ, or (2) between âdubâ and âlubâ. They can be a symptom of many heart disorders, some serious. There will still be a âlubâ and a âdubâ. One of the things that confuses non-medically trained people is that murmurs happen between lub and dub or between dub and lub; not on lub and not on dub. Below, you can find an asterisk* at the locations a murmur may be.

â¦lub..****...dubâ¦â¦â¦â¦â¦. lub..****..dub â¦â¦â¦â¦â¦. lub..****..dub â¦â¦â¦â¦â¦. lub..****..dub â¦

â¦lubâ¦â¦â¦.dubâ¦******â¦.lubâ¦â¦â¦. dubâ¦******â¦.lub â¦â¦â¦. dubâ¦******â¦.lub â¦â¦â¦.dubâ¦

Dataset B also contains noisy_murmur data - murmur data which includes a substantial amount of background noise or distortion. You may choose to use this or ignore it, however the test set will include some equally noisy examples

Extra Heart Sound Category (Dataset A) Extra heart sounds can be identified because there is an additional sound, e.g. a âlub-lub dubâ or a âlub dub-dubâ. An extra heart sound may not be a sign of disease.  However, in some situations it is an important sign of disease, which if detected early could help a person.  The extra heart sound is important to be able to detect as it cannot be detected by ultrasound very well. Below, note the temporal description of the extra heart sounds:

â¦lub.lubâ¦â¦â¦.dubâ¦â¦â¦..â¦â¦â¦. lub. lubâ¦â¦â¦.dubâ¦â¦â¦â¦â¦.lub.lubâ¦â¦..â¦â¦.dubâ¦â¦.

â¦lubâ¦â¦â¦. dub.dubâ¦â¦â¦â¦â¦â¦â¦.lub.â¦â¦â¦.dub.dubâ¦â¦â¦â¦â¦â¦â¦.lubâ¦â¦..â¦â¦.dub. dubâ¦â¦

Artifact Category (Dataset A) In the Artifact category there are a wide range of different sounds, including feedback squeals and echoes, speech, music and noise. There are usually no discernable heart sounds, and thus little or no temporal periodicity at frequencies below 195 Hz. This category is the most different from the others. It is important to be able to distinguish this category from the other three categories, so that someone gathering the data can be instructed to try again .

â¦........lubâ¦â¦â¦.dubâ¦â¦â¦..â¦â¦â¦. lub. â¦â¦â¦..â¦â¦â¦.dubâ¦â¦â¦â¦â¦.lub.lubâ¦â¦..â¦â¦.dubâ¦â¦. or â¦lubâ¦â¦â¦. dub......â¦â¦â¦â¦â¦â¦â¦.lub.â¦â¦â¦â¦â¦â¦â¦dub.dubâ¦â¦â¦â¦â¦â¦â¦.lubâ¦â¦..â¦â¦.dub.â¦â¦

To allow systems to be comparable, there are some guidelines that we would like participants to follow:

Domain-specific knowledge as provided in this document may be freely used to enhance the performance of the systems.

We provide both training and test data sets, but labels are omitted for the test data. We require the results to be produced in a specific format in a text file. A scoring script is provided for participants to evaluate their data on the results for both test and training data.

We expect to see results for both the training and test sets in the submissions. We also require the code for the method, which needs to include instructions for executing the system, to enable us to validate the submitted results if necessary.

See the evaluation scripts in the downloads section for details of how accuracy of your results can be calculated. You must use this script to enable each system to be compared.
