# article

**Source:** https://medium.com/data-analysis-center/annotating-ecg-signals-with-hidden-markov-model-56f8b9abd83a

---

Machine learning for Oil and Gas Exploration. Advanced methods to locate oil deposits

Annotating ECG signals with Hidden Markov Model

And yet, many of us spoil their health in pursuit of money, which usually spent afterwards in attempt to return what was lost. This is a very common problem in developed countries, and almost everyone is exposed to harmful effects. Athletes are doing anything to reach and go beyond their limits; programmers and office workers suffer from absence of activity and long hours spend in front of the laptops; managers and executives are subjects of constant stress; retirees have health issues associated with advanced age, often aggravated by lack of medical care or it’s improper quality. Chineese proverb says, “The best time to plant a tree was 20 years age. The second best time is now”. This can be applied to our lifestyle too: the sooner you start monitor your health and take appropriate actions, the better.

Latest advances in technology have brought to the market a variety of devices for health monitoring. There are gadgets that can record ECG, track your sleep patterns and daily activity, estimate stress levels, monitor blood pressure, respiration rate, and even blood oxygenation. Not even mentioning such boring and familiar to everyone things like weight and body temperature trackers.

All these gadgets are able to generate hundreds of megabytes of unique data, but little to none of them have any tools for interpretation of this data. The data itself is useless — real value for users like you and me is in the fast and comprehensive analysis of this unique information: in finding patters specific to each user, in discovering abnormalities that may indicate some disease, in forecasting possible health issues a user may encounter.

How to analyze the data you’ve collected?

Development of such analytical software is no longer prerogative of a small group of companies — there are many startups, little companies and even single developers that create medical software to solve specific health-related issues using medical data from gadgets. For example, Phillips , Concept to clinic , Viome and others. This drastic shift became possible due to two insiping trends: first, advances in open-source movement that allows anyone to obtain, modify and share software; second, spread of the idea of open data, which implies that data should be freely available to everyone to use and republish as they wish, without restrictions from copyright, patents or other mechanisms of control.

For example, one interested in analysis of cardiological data could make use of CardIO , an open-source framework for preprocessing and deep analysis of medical data. You can learn more about this framework from its’ documentation . Another useful tool is PhysioBank , a part of the research resource for physiologic data called PhysioNet . PhysioBank offers free access to a large collection of annotated digitalized physiologic signals and time series. These two resources are enough to create a simple script to calculate heart rate and some other cardiological parameters using ECG signal.

PhysioBank contains over 90K recordings, organized in more than 80 databases. To calculate heart rate, one needs to find duration between R-peaks on ECG recording. Among other parameters that cardiologists find helpful in diagnosing are durations of PQ interval (also called PR), QRS complex and QT interval. To learn a model to find P-wave, QRS complex and T-wave on ECG recording you can use QT Databse.

The QT Database contains a total of 105 fifteen-minute ECG recordings. It includes signals which were chosen to represent a wide variety of QRS and ST-T morphologies, in order to challenge QT detection algorithms with real-world variability. Within each record, between 30 and 100 representative beats were manually annotated by cardiologists, who identified the P-wave, QRS-complex and the T-wave. You can find more comprehensive description of the QT Database in this publication .

Hidden Markov Models are statistical models in which the system being modeled is assumed to be a Markov process with unobserved, or hidden, states. To simplify, the modeled system can be observed in some states, and with some probability it can make a transition from one state to another. In general, modeler does not know what are those states, but has to assume number of them.

In out task we will map segments of the ECG signal to the states of the HMM. On the image to the left you can see eight segments of ECG signal: ISO, P, PQ, Q, R, S, ST, T. Those segments will correspond to the states of HMM as shown in the picture below:

In our model, though, we will expand number of possible states to nineteen. This will make a good compromise on complexity versus performance of the model. There will be 3 states for the ISO, P-wave, and QRS-complex models; 2 states for the PQ and ST segment models; 6 states for the T-wave. Also, we introduce direct transition from last ISO state to first PQ state, thus enabling possibility of absent P-wave.

This section and the following ones contain code snippets and visualizations. You can find full code in the form of the jupyter notebook here .

When a data scientist has some prior knowledge about the system, she can introduce initial parameters to the HMM as a starting point. Since we have an annotated dataset, we can use it to provide some extra information for the model by generatin new features. So, we need to:

Let’s write template pipeline, link it to the dataset and run:

Using data from pipeline variables annsamps , anntypes and wavelets we can calculate initial parameters and plug them in the configuration of the model, as you will see in the next section.

First, to train the model we need to define its’ configuration, and here we’ll use initial parameters that were calculated in the previous step:

Next step is to create a pipeline for training. This pipeline includes the following actions:

Preprocess data — make wavelet transformation

The pipeline described above looks like this:

After you’ve run the dataset though the pipeline, you can save the model with this line of code:

To perform testing we should modify the config to load pretrained model:

The next move is to write a pipeline composed of the following:

Calculation of ECG parameters, such as HR

Finally, using values from the pipeline variable, we can plot the results of the annotation and calculate heart rate.

On this first example you can see annotation of the two-lead ECG signal. Green areas highlight P-wave, blue areas are for T-wave and red areas show QRS complex:

The second example shows similar signal, but it has less accurate annotation of P-wave:

Using CardIO you can implement some interesting models by yourself. For example, in this tutorial we did not consider U-wave, which in some cases appear on ECG signal and which is annotated in QT Database — you can build HMM that includes this segment too. Also, in this tutorial the model has been trained only on the first lead, and you can train a model on both leads to increase performance.

Another promising and interesting direction — disease detection using ECG signals. If you are eager to dive into this field, check out a tutorial on how to build probabilistic models to detect atrial fibrillation .

Or, if you want to learn more about CardIO, its’ possibilities and use cases, you can look at the paper where CardIO is introduced .

Machine learning for Oil and Gas Exploration. Advanced methods to locate oil deposits
