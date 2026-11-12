# neurokit2

**Source:** https://pypi.python.org/pypi/neurokit2

---

The Python Toolbox for Neurophysiological Signal Processing.

pip install neurokit2 Copy PIP instructions

The Python Toolbox for Neurophysiological Signal Processing

NeuroKit2 is a user-friendly package providing easy access to advanced biosignal processing routines.
Researchers and clinicians without extensive knowledge of programming or biomedical signal processing
can analyze physiological data with only two lines of code .

If you’re not sure what to do, read our installation guide .

NeuroKit2 is the most welcoming project with a large community of contributors with all levels of programming expertise. But the package is still far from being perfect! Thus, if you have some ideas for improvement , new features , or just want to learn Python and do something useful at the same time, do not hesitate and check out the following guide:

Also, if you have developed new signal processing methods or algorithms and you want to increase their usage, popularity, and citations , get in touch with us to eventually add them to NeuroKit. A great opportunity for the users as well as the original developers!

You have spotted a mistake ? An error in a formula or code? OR there is just a step that seems strange and you don’t understand? Please let us know! We are human beings, and we’ll appreciate any inquiry.

Click on the links above and check out our tutorials:

Simulate Artificial Physiological Signals

Simulate Artificial Physiological Signals

Analyze Respiratory Rate Variability (RRV)

Analyze Respiratory Rate Variability (RRV)

Extract and Visualize Individual Heartbeats

Extract and Visualize Individual Heartbeats

Don’t know which tutorial is suited for your case? Follow this flowchart:

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

a comprehensive review of the most up-to-date HRV indices

a discussion of their significance in psychological research and practices

a discussion of their significance in psychological research and practices

a step-by-step guide for HRV analysis using NeuroKit2

a step-by-step guide for HRV analysis using NeuroKit2

Compute HRV indices using Python Time domain : RMSSD, MeanNN, SDNN, SDSD, CVNN, etc. Frequency domain : Spectral power density in various frequency bands (Ultra low/ULF, Very low/VLF, Low/LF, High/HF, Very high/VHF), Ratio of LF to HF power, Normalized LF (LFn) and HF (HFn), Log transformed HF (LnHF). Nonlinear domain : Spread of RR intervals (SD1, SD2, ratio between SD2 to SD1), Cardiac Sympathetic Index (CSI), Cardial Vagal Index (CVI), Modified CSI, Sample Entropy (SampEn).

Time domain : RMSSD, MeanNN, SDNN, SDSD, CVNN, etc.

Time domain : RMSSD, MeanNN, SDNN, SDSD, CVNN, etc.

Frequency domain : Spectral power density in various frequency bands (Ultra low/ULF, Very low/VLF, Low/LF, High/HF, Very high/VHF), Ratio of LF to HF power, Normalized LF (LFn) and HF (HFn), Log transformed HF (LnHF).

Frequency domain : Spectral power density in various frequency bands (Ultra low/ULF, Very low/VLF, Low/LF, High/HF, Very high/VHF), Ratio of LF to HF power, Normalized LF (LFn) and HF (HFn), Log transformed HF (LnHF).

Nonlinear domain : Spread of RR intervals (SD1, SD2, ratio between SD2 to SD1), Cardiac Sympathetic Index (CSI), Cardial Vagal Index (CVI), Modified CSI, Sample Entropy (SampEn).

Nonlinear domain : Spread of RR intervals (SD1, SD2, ratio between SD2 to SD1), Cardiac Sympathetic Index (CSI), Cardial Vagal Index (CVI), Modified CSI, Sample Entropy (SampEn).

Delineate the QRS complex of an electrocardiac signal (ECG) including P-peaks, T-peaks, as well as their onsets and offsets.

Delineate the QRS complex of an electrocardiac signal (ECG) including P-peaks, T-peaks, as well as their onsets and offsets.

Signal processing functionalities Filtering : Using different methods. Detrending : Remove the baseline drift or trend. Distorting : Add noise and artifacts.

Detrending : Remove the baseline drift or trend.

Detrending : Remove the baseline drift or trend.

Complexity (Entropy, Fractal Dimensions, …)

Optimize complexity parameters (delay tau , dimension m , tolerance r )

Optimize complexity parameters (delay tau , dimension m , tolerance r )

Compute complexity features Entropy : Sample Entropy (SampEn), Approximate Entropy (ApEn), Fuzzy Entropy (FuzzEn), Multiscale Entropy (MSE), Shannon Entropy (ShEn) Fractal dimensions : Correlation Dimension D2, … Detrended Fluctuation Analysis

Entropy : Sample Entropy (SampEn), Approximate Entropy (ApEn), Fuzzy Entropy (FuzzEn), Multiscale Entropy (MSE), Shannon Entropy (ShEn)

Entropy : Sample Entropy (SampEn), Approximate Entropy (ApEn), Fuzzy Entropy (FuzzEn), Multiscale Entropy (MSE), Shannon Entropy (ShEn)

Fractal dimensions : Correlation Dimension D2, …

Fractal dimensions : Correlation Dimension D2, …

NeuroKit2 is one of the most welcoming packages for new contributors and users, as well as the fastest-growing package. So stop hesitating and hop on board 🤗

The authors do not provide any warranty. If this software causes your keyboard to blow up, your brain to liquefy, your toilet to clog or a zombie plague to break loose, the authors CANNOT IN ANY WAY be held responsible.

Author: Tam Pham, Zen Juen Lau, Jan C. Brammer, François Lespinasse

ECG EDA EMG NeuroKit2 PPG Python bodily signals physiology

Programming Language Python :: 3.10 Python :: 3.11 Python :: 3.12 Python :: 3.13 Python :: 3.14

Author: Tam Pham, Zen Juen Lau, Jan C. Brammer, François Lespinasse

ECG EDA EMG NeuroKit2 PPG Python bodily signals physiology

Programming Language Python :: 3.10 Python :: 3.11 Python :: 3.12 Python :: 3.13 Python :: 3.14

For a detailed explanation of source distributions (sdists) and built distributions (wheels), please see the package formats documentation .

Release files / neurokit2-0.3.0-py3-none-any.whl

Provenance describes where a file came from. On PyPI, provenance is shared via attestations , which provide a verifiable record of the build or publishing details. View details, limitations and caveats.

None of the files in this release were uploaded with provenance metadata.

PyPI is a repository for distributing packages, not a service for auditing them. While third-party security researchers and our staff do their best to detect and remove malicious packages, PyPI cannot guarantee the quality, security or suitability of any given package.

To learn more about protecting yourself from malicious actors, visit our package security documentation .

Release history Release notifications | RSS feed

Nov 1, 2026 2 release files No provenance

Mar 2, 2026 2 release files No provenance

Jul 8, 2025 2 release files No provenance

May 13, 2025 2 release files No provenance

Aug 16, 2024 2 release files No provenance

May 21, 2024 2 release files No provenance

Nov 6, 2023 2 release files No provenance

Sep 12, 2023 2 release files No provenance

Jul 9, 2023 2 release files No provenance

Apr 6, 2023 2 release files No provenance

Feb 9, 2023 2 release files No provenance

Nov 15, 2022 2 release files No provenance

Sep 8, 2022 2 release files No provenance

May 18, 2022 2 release files No provenance

Feb 18, 2022 2 release files No provenance

Feb 15, 2022 2 release files No provenance

Nov 12, 2021 2 release files No provenance

Aug 30, 2021 2 release files No provenance

Aug 24, 2021 2 release files No provenance

Jul 30, 2021 2 release files No provenance

May 24, 2021 2 release files No provenance

Mar 10, 2021 2 release files No provenance

Feb 8, 2021 2 release files No provenance

Nov 23, 2020 2 release files No provenance

Oct 25, 2020 2 release files No provenance

Aug 5, 2020 2 release files No provenance

Jul 9, 2020 2 release files No provenance

Jun 15, 2020 2 release files No provenance

Jun 6, 2020 2 release files No provenance

Jun 1, 2020 2 release files No provenance

May 31, 2020 2 release files No provenance

Mar 28, 2020 1 release file No provenance

Mar 22, 2020 1 release file No provenance

Mar 10, 2020 1 release file No provenance

Feb 24, 2020 1 release file No provenance

Feb 11, 2020 1 release file No provenance

Jan 24, 2020 1 release file No provenance

Dec 19, 2019 1 release file No provenance

Oct 29, 2019 1 release file No provenance

"PyPI", "Python Package Index", and the blocks logos are registered trademarks of the Python Software Foundation .
