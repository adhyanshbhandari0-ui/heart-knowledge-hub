# README.rst

**Source:** https://github.com/neuropsychology/NeuroKit/blob/master/README.rst

---

The Python Toolbox for Neurophysiological Signal Processing

NeuroKit2 is a user-friendly package providing easy access to advanced biosignal processing routines.
Researchers and clinicians without extensive knowledge of programming or biomedical signal processing
can analyze physiological data with only two lines of code .

If you're not sure what to do, read our installation guide .

NeuroKit2 is the most welcoming project with a large community of contributors with all levels of programming expertise. But the package is still far from being perfect! Thus, if you have some ideas for improvement , new features , or just want to learn Python and do something useful at the same time, do not hesitate and check out the following guide:

Also, if you have developed new signal processing methods or algorithms and you want to increase their usage, popularity, and citations , get in touch with us to eventually add them to NeuroKit. A great opportunity for the users as well as the original developers!

You have spotted a mistake ? An error in a formula or code? OR there is just a step that seems strange and you don't understand? Please let us know! We are human beings, and we'll appreciate any inquiry.

Click on the links above and check out our tutorials:

Simulate Artificial Physiological Signals

Analyze Respiratory Rate Variability (RRV)

Extract and Visualize Individual Heartbeats

Don't know which tutorial is suited for your case? Follow this flowchart:

The NeuroKit2 paper can be found here 🎉 Additionally, you can get the reference directly from Python by running:

Let us know if you used NeuroKit2 in a publication! Open a new discussion (select the NK in publications category) and link the paper. The community would be happy to know about how you used it and learn about your research. We could also feature it once we have a section on the website for papers that used the software.

You can easily simulate artificial ECG (also 12-Lead multichannel ECGs ), PPG, RSP, EDA, and EMG signals to test your scripts and algorithms.

The analysis of physiological data usually comes in two types, event-related or interval-related .

This type of analysis refers to physiological changes immediately occurring in response to an event.
For instance, physiological changes following the presentation of a stimulus (e.g., an emotional stimulus) are indicated by
the dotted lines in the figure above. In this situation, the analysis is epoch-based.
An epoch is a short chunk of the physiological signal (usually < 10 seconds), that is locked to a specific stimulus and hence
the physiological signals of interest are time-segmented accordingly. This is represented by the orange boxes in the figure above.
In this case, using bio_analyze() will compute features like rate changes, peak characteristics, and phase characteristics.

This type of analysis refers to the physiological characteristics and features that occur over
longer periods of time (from a few seconds to days of activity). Typical use cases are either
periods of resting state, in which the activity is recorded for several minutes while the participant
is at rest, or during different conditions in which there is no specific time-locked event
(e.g., watching movies, listening to music, engaging in physical activity, etc.). For instance,
this type of analysis is used when people want to compare the physiological activity under different
intensities of physical exercise, different types of movies, or different intensities of
stress. To compare event-related and interval-related analysis, we can refer to the example figure above.
For example, a participant might be watching a 20s-long short film where particular stimuli of
interest in the movie appear at certain time points (marked by the dotted lines). While
event-related analysis pertains to the segments of signals within the orange boxes (to understand the physiological
changes pertaining to the appearance of stimuli), interval-related analysis can be
applied on the entire 20s duration to investigate how physiology fluctuates in general.
In this case, using bio_analyze() will compute features such as rate characteristics (in particular,
variability metrics) and peak characteristics.

Check-out our Heart Rate Variability in Psychology: A Review of HRV Indices and an Analysis Tutorial paper for:

a comprehensive review of the most up-to-date HRV indices

a discussion of their significance in psychological research and practices

a step-by-step guide for HRV analysis using NeuroKit2

Compute HRV indices using Python Time domain : RMSSD, MeanNN, SDNN, SDSD, CVNN, etc. Frequency domain : Spectral power density in various frequency bands (Ultra low/ULF, Very low/VLF, Low/LF, High/HF, Very high/VHF), Ratio of LF to HF power, Normalized LF (LFn) and HF (HFn), Log transformed HF (LnHF). Nonlinear domain : Spread of RR intervals (SD1, SD2, ratio between SD2 to SD1), Cardiac Sympathetic Index (CSI), Cardial Vagal Index (CVI), Modified CSI, Sample Entropy (SampEn).

Time domain : RMSSD, MeanNN, SDNN, SDSD, CVNN, etc.

Frequency domain : Spectral power density in various frequency bands (Ultra low/ULF, Very low/VLF, Low/LF, High/HF, Very high/VHF), Ratio of LF to HF power, Normalized LF (LFn) and HF (HFn), Log transformed HF (LnHF).

Nonlinear domain : Spread of RR intervals (SD1, SD2, ratio between SD2 to SD1), Cardiac Sympathetic Index (CSI), Cardial Vagal Index (CVI), Modified CSI, Sample Entropy (SampEn).

Delineate the QRS complex of an electrocardiac signal (ECG) including P-peaks, T-peaks, as well as their onsets and offsets.

Signal processing functionalities Filtering : Using different methods. Detrending : Remove the baseline drift or trend. Distorting : Add noise and artifacts.

Detrending : Remove the baseline drift or trend.

Complexity (Entropy, Fractal Dimensions, ...)

Optimize complexity parameters (delay tau , dimension m , tolerance r )

Compute complexity features Entropy : Sample Entropy (SampEn), Approximate Entropy (ApEn), Fuzzy Entropy (FuzzEn), Multiscale Entropy (MSE), Shannon Entropy (ShEn) Fractal dimensions : Correlation Dimension D2, ... Detrended Fluctuation Analysis

Entropy : Sample Entropy (SampEn), Approximate Entropy (ApEn), Fuzzy Entropy (FuzzEn), Multiscale Entropy (MSE), Shannon Entropy (ShEn)

Fractal dimensions : Correlation Dimension D2, ...

NeuroKit2 is one of the most welcoming packages for new contributors and users, as well as the fastest-growing package. So stop hesitating and hop on board 🤗

The authors do not provide any warranty. If this software causes your keyboard to blow up, your brain to liquefy, your toilet to clog or a zombie plague to break loose, the authors CANNOT IN ANY WAY be held responsible.
