# 
    "\n",
    "Once you have a raw EDA signal in the shape of a vector (i.e., a one-dimensional array), or a list, you can use [eda_process()

**Source:** https://neuropsychology.github.io/NeuroKit/functions/eda.html

---

Convenience function that automatically processes electrodermal activity (EDA) signal.

eda_signal ( Union[list, np.array, pd.Series] ) – The raw EDA signal.

eda_signal ( Union[list, np.array, pd.Series] ) – The raw EDA signal.

sampling_rate ( int ) – The sampling frequency of "eda_signal" (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of "eda_signal" (in Hz, i.e., samples/second).

method ( str ) – The processing pipeline to apply. Can be one of "biosppy" or "neurokit" (default).

method ( str ) – The processing pipeline to apply. Can be one of "biosppy" or "neurokit" (default).

report ( str ) – The filename of a report containing description and figures of processing
(e.g. "myreport.html" ). Needs to be supplied if a report file
should be generated. Defaults to None . Can also be "text" to
just print the text in the console without saving anything.

report ( str ) – The filename of a report containing description and figures of processing
(e.g. "myreport.html" ). Needs to be supplied if a report file
should be generated. Defaults to None . Can also be "text" to
just print the text in the console without saving anything.

**kwargs – Other arguments to be passed to specific methods. This includes amplitude_min (relative SCR amplitude threshold, default 0.1 )
forwarded to eda_peaks() . For more information, see eda_methods() .

**kwargs – Other arguments to be passed to specific methods. This includes amplitude_min (relative SCR amplitude threshold, default 0.1 )
forwarded to eda_peaks() . For more information, see eda_methods() .

signals ( DataFrame ) – A DataFrame of same length as "eda_signal" containing the following
columns: EDA_Raw : The raw signal. EDA_Clean : The cleaned signal. EDA_Tonic : The tonic component of the signal, or the Tonic Skin Conductance Level (SCL). EDA_Phasic : The phasic component of the signal, or the Phasic Skin Conductance Response (SCR). SCR_Onsets : The samples at which the onsets of the peaks occur, marked as “1” in a list of zeros. SCR_Peaks : The samples at which the peaks occur, marked as “1” in a list of zeros. SCR_Height : The SCR amplitude of the signal including the Tonic component. Note that cumulative effects of close-occurring SCRs might lead to an underestimation of the amplitude. SCR_Amplitude : The SCR amplitude of the signal excluding the Tonic component. SCR_RiseTime : The time taken for SCR onset to reach peak amplitude within the SCR. SCR_Recovery : The samples at which SCR peaks recover (decline) to half amplitude, marked as “1” in a list of zeros. info ( dict ) – A dictionary containing the information of each SCR peak (see eda_findpeaks() ),
as well as the signals’ sampling rate.

signals ( DataFrame ) – A DataFrame of same length as "eda_signal" containing the following
columns: EDA_Raw : The raw signal. EDA_Clean : The cleaned signal. EDA_Tonic : The tonic component of the signal, or the Tonic Skin Conductance Level (SCL). EDA_Phasic : The phasic component of the signal, or the Phasic Skin Conductance Response (SCR). SCR_Onsets : The samples at which the onsets of the peaks occur, marked as “1” in a list of zeros. SCR_Peaks : The samples at which the peaks occur, marked as “1” in a list of zeros. SCR_Height : The SCR amplitude of the signal including the Tonic component. Note that cumulative effects of close-occurring SCRs might lead to an underestimation of the amplitude. SCR_Amplitude : The SCR amplitude of the signal excluding the Tonic component. SCR_RiseTime : The time taken for SCR onset to reach peak amplitude within the SCR. SCR_Recovery : The samples at which SCR peaks recover (decline) to half amplitude, marked as “1” in a list of zeros.

signals ( DataFrame ) – A DataFrame of same length as "eda_signal" containing the following
columns:

EDA_Tonic : The tonic component of the signal, or the Tonic Skin Conductance Level (SCL).

EDA_Tonic : The tonic component of the signal, or the Tonic Skin Conductance Level (SCL).

EDA_Phasic : The phasic component of the signal, or the Phasic Skin Conductance Response (SCR).

EDA_Phasic : The phasic component of the signal, or the Phasic Skin Conductance Response (SCR).

SCR_Onsets : The samples at which the onsets of the peaks occur, marked as “1” in a list of zeros.

SCR_Onsets : The samples at which the onsets of the peaks occur, marked as “1” in a list of zeros.

SCR_Peaks : The samples at which the peaks occur, marked as “1” in a list of zeros.

SCR_Peaks : The samples at which the peaks occur, marked as “1” in a list of zeros.

SCR_Height : The SCR amplitude of the signal including the Tonic component. Note that cumulative effects of close-occurring SCRs might lead to an underestimation of the amplitude.

SCR_Height : The SCR amplitude of the signal including the Tonic component. Note that cumulative effects of close-occurring SCRs might lead to an underestimation of the amplitude.

SCR_Amplitude : The SCR amplitude of the signal excluding the Tonic component.

SCR_Amplitude : The SCR amplitude of the signal excluding the Tonic component.

SCR_RiseTime : The time taken for SCR onset to reach peak amplitude within the SCR.

SCR_RiseTime : The time taken for SCR onset to reach peak amplitude within the SCR.

SCR_Recovery : The samples at which SCR peaks recover (decline) to half amplitude, marked as “1” in a list of zeros.

SCR_Recovery : The samples at which SCR peaks recover (decline) to half amplitude, marked as “1” in a list of zeros.

info ( dict ) – A dictionary containing the information of each SCR peak (see eda_findpeaks() ),
as well as the signals’ sampling rate.

info ( dict ) – A dictionary containing the information of each SCR peak (see eda_findpeaks() ),
as well as the signals’ sampling rate.

eda_simulate , eda_clean , eda_phasic , eda_findpeaks , eda_plot

Perform EDA analysis on either epochs (event-related analysis) or on longer periods of data
such as resting-state data.

data ( Union[dict, pd.DataFrame] ) – A dictionary of epochs, containing one DataFrame per epoch, usually obtained via epochs_create , or a DataFrame containing all epochs, usually obtained via epochs_to_df . Can also take a DataFrame of processed signals from a longer period of
data, typically generated by eda_process or bio_process . Can also take a dict
containing sets of separate periods of data.

data ( Union[dict, pd.DataFrame] ) – A dictionary of epochs, containing one DataFrame per epoch, usually obtained via epochs_create , or a DataFrame containing all epochs, usually obtained via epochs_to_df . Can also take a DataFrame of processed signals from a longer period of
data, typically generated by eda_process or bio_process . Can also take a dict
containing sets of separate periods of data.

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).
Defaults to 1000Hz.

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).
Defaults to 1000Hz.

method ( str ) – Can be one of "event-related" for event-related analysis on epochs, or "interval-related" for analysis on longer periods of data. Defaults to "auto" where
the right method will be chosen based on the mean duration of the data ( "event-related" for duration under 10s).

method ( str ) – Can be one of "event-related" for event-related analysis on epochs, or "interval-related" for analysis on longer periods of data. Defaults to "auto" where
the right method will be chosen based on the mean duration of the data ( "event-related" for duration under 10s).

DataFrame – A dataframe containing the analyzed EDA features. If event-related analysis is conducted,
each epoch is indicated by the Label column. See eda_eventrelated() and eda_intervalrelated() docstrings for details.

bio_process , eda_process , epochs_create , eda_eventrelated , eda_intervalrelated

Example 1: Data for event-related analysis

Example 1: Data for event-related analysis

Visualize electrodermal activity (EDA) data

eda_signals ( DataFrame ) – DataFrame obtained from eda_process() .

eda_signals ( DataFrame ) – DataFrame obtained from eda_process() .

info ( dict ) – The information Dict returned by eda_process() . Defaults to None .

info ( dict ) – The information Dict returned by eda_process() . Defaults to None .

static ( bool ) – If True, a static plot will be generated with matplotlib.
If False, an interactive plot will be generated with plotly.
Defaults to True.

static ( bool ) – If True, a static plot will be generated with matplotlib.
If False, an interactive plot will be generated with plotly.
Defaults to True.

See ecg_plot() for details on how to access the figure, modify the size and save it.

Simulate Electrodermal Activity (EDA) signal

Generate an artificial (synthetic) EDA signal of a given duration and sampling rate.

duration ( int ) – Desired recording length in seconds.

duration ( int ) – Desired recording length in seconds.

sampling_rate ( int ) – The desired sampling rate (in Hz, i.e., samples/second). Defaults to 1000Hz.

sampling_rate ( int ) – The desired sampling rate (in Hz, i.e., samples/second). Defaults to 1000Hz.

length ( int ) – The desired length of the signal (in samples). Defaults to None.

length ( int ) – The desired length of the signal (in samples). Defaults to None.

noise ( float ) – Noise level (amplitude of the laplace noise). Defaults to 0.01.

noise ( float ) – Noise level (amplitude of the laplace noise). Defaults to 0.01.

scr_number ( int ) – Desired number of skin conductance responses (SCRs), i.e., peaks. Defaults to 1.

scr_number ( int ) – Desired number of skin conductance responses (SCRs), i.e., peaks. Defaults to 1.

drift ( float or list ) – The slope of a linear drift of the signal. Defaults to -0.01.

drift ( float or list ) – The slope of a linear drift of the signal. Defaults to -0.01.

random_state ( None, int, numpy.random.RandomState or numpy.random.Generator ) – Seed for the random number generator. See for misc.check_random_state for further information.

random_state ( None, int, numpy.random.RandomState or numpy.random.Generator ) – Seed for the random number generator. See for misc.check_random_state for further information.

random_state_distort ( {‘legacy’, ‘spawn’}, None, int, numpy.random.RandomState or numpy.random.Generator ) – Random state to be used to distort the signal. If "legacy" , use the same random state used to
generate the signal (discouraged as it creates dependent random streams). If "spawn" , spawn
independent children random number generators from the random_state argument. If any of the other types,
generate independent children random number generators from the random_state_distort provided (this
allows generating multiple version of the same signal distorted by different random noise realizations).

random_state_distort ( {‘legacy’, ‘spawn’}, None, int, numpy.random.RandomState or numpy.random.Generator ) – Random state to be used to distort the signal. If "legacy" , use the same random state used to
generate the signal (discouraged as it creates dependent random streams). If "spawn" , spawn
independent children random number generators from the random_state argument. If any of the other types,
generate independent children random number generators from the random_state_distort provided (this
allows generating multiple version of the same signal distorted by different random noise realizations).

array – Vector containing the EDA signal.

ecg_simulate , rsp_simulate , emg_simulate , ppg_simulate

Bach, D. R., Flandin, G., Friston, K. J., & Dolan, R. J. (2010). Modelling event-related skin
conductance responses. International Journal of Psychophysiology, 75(3), 349-356.

Bach, D. R., Flandin, G., Friston, K. J., & Dolan, R. J. (2010). Modelling event-related skin
conductance responses. International Journal of Psychophysiology, 75(3), 349-356.

Preprocess Electrodermal Activity (EDA) signal

This function cleans the EDA signal by removing noise and smoothing the signal with different methods.

NeuroKit : Default methods. Low-pass filter with a 3 Hz cutoff frequency and a 4th order
Butterworth filter. Note thaht if the sampling rate is lower than 7 Hz (as it is the case
with some signals recorded by wearables such as Empatica), the filtering is skipped (as there
is no high enough frequency to remove).

NeuroKit : Default methods. Low-pass filter with a 3 Hz cutoff frequency and a 4th order
Butterworth filter. Note thaht if the sampling rate is lower than 7 Hz (as it is the case
with some signals recorded by wearables such as Empatica), the filtering is skipped (as there
is no high enough frequency to remove).

BioSPPy : More aggresive filtering than NeuroKit’s default method. Low-pass filter with a
5 Hz cutoff frequency and a 4th order Butterworth filter.

BioSPPy : More aggresive filtering than NeuroKit’s default method. Low-pass filter with a
5 Hz cutoff frequency and a 4th order Butterworth filter.

eda_signal ( Union[list, np.array, pd.Series] ) – The raw EDA signal.

eda_signal ( Union[list, np.array, pd.Series] ) – The raw EDA signal.

sampling_rate ( int ) – The sampling frequency of rsp_signal (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of rsp_signal (in Hz, i.e., samples/second).

method ( str ) – The processing pipeline to apply. Can be one of "neurokit" (default), "biosppy" , or "none" .

method ( str ) – The processing pipeline to apply. Can be one of "neurokit" (default), "biosppy" , or "none" .

array – Vector containing the cleaned EDA signal.

eda_simulate , eda_findpeaks , eda_process , eda_plot

Electrodermal Activity (EDA) Decomposition into Phasic and Tonic Components

Decompose the Electrodermal Activity (EDA) into two components, namely Phasic and Tonic , using different methods including cvxEDA (Greco, 2016) or Biopac’s Acqknowledge
algorithms.

High-pass filtering : Method implemented in Biopac’s Acqknowledge. The raw EDA signal
is passed through a high pass filter with a cutoff frequency of 0.05 Hz
(cutoff frequency can be adjusted by the cutoff argument).

High-pass filtering : Method implemented in Biopac’s Acqknowledge. The raw EDA signal
is passed through a high pass filter with a cutoff frequency of 0.05 Hz
(cutoff frequency can be adjusted by the cutoff argument).

Median smoothing : Method implemented in Biopac’s Acqknowledge. The raw EDA signal is
passed through a median value smoothing filter, which removes areas of rapid change. The
phasic component is then calculated by subtracting the smoothed signal from the original.
This method is computationally intensive and the processing time depends on the smoothing
factor, which can be controlled by the as smoothing_factor argument, set by default to 4 seconds. Higher values will produce results more rapidly.

Median smoothing : Method implemented in Biopac’s Acqknowledge. The raw EDA signal is
passed through a median value smoothing filter, which removes areas of rapid change. The
phasic component is then calculated by subtracting the smoothed signal from the original.
This method is computationally intensive and the processing time depends on the smoothing
factor, which can be controlled by the as smoothing_factor argument, set by default to 4 seconds. Higher values will produce results more rapidly.

cvxEDA : Convex optimization approach to EDA processing (Greco, 2016). Requires the cvxopt package ( > 1.3.0.1 ) to
be installed.

cvxEDA : Convex optimization approach to EDA processing (Greco, 2016). Requires the cvxopt package ( > 1.3.0.1 ) to
be installed.

SparsEDA : Sparse non-negative deconvolution (Hernando-Gallego et al., 2017).

SparsEDA : Sparse non-negative deconvolution (Hernando-Gallego et al., 2017).

sparsEDA was newly added thanks to this implementation . Help is needed to
double-check it, improve it and make it more concise and efficient. Also, sometimes it errors
for unclear reasons. Please help.

eda_signal ( Union[list, np.array, pd.Series] ) – The raw EDA signal.

eda_signal ( Union[list, np.array, pd.Series] ) – The raw EDA signal.

sampling_rate ( int ) – The sampling frequency of raw EDA signal (in Hz, i.e., samples/second). Defaults to 1000Hz.

sampling_rate ( int ) – The sampling frequency of raw EDA signal (in Hz, i.e., samples/second). Defaults to 1000Hz.

method ( str ) – The processing pipeline to apply. Can be one of "cvxEDA" , "smoothmedian" , "highpass" . Defaults to "highpass" .

method ( str ) – The processing pipeline to apply. Can be one of "cvxEDA" , "smoothmedian" , "highpass" . Defaults to "highpass" .

**kwargs ( dict ) – Additional arguments to pass to the specific method.

**kwargs ( dict ) – Additional arguments to pass to the specific method.

DataFrame – DataFrame containing the "Tonic" and the "Phasic" components as columns.

eda_simulate , eda_clean , eda_peaks , eda_process , eda_plot

Greco, A., Valenza, G., & Scilingo, E. P. (2016). Evaluation of CDA and CvxEDA Models. In
Advances in Electrodermal Activity Processing with Applications for Mental Health (pp. 35-43).
Springer International Publishing.

Greco, A., Valenza, G., & Scilingo, E. P. (2016). Evaluation of CDA and CvxEDA Models. In
Advances in Electrodermal Activity Processing with Applications for Mental Health (pp. 35-43).
Springer International Publishing.

Greco, A., Valenza, G., Lanata, A., Scilingo, E. P., & Citi, L. (2016). cvxEDA: A convex
optimization approach to electrodermal activity processing. IEEE Transactions on Biomedical
Engineering, 63(4), 797-804.

Greco, A., Valenza, G., Lanata, A., Scilingo, E. P., & Citi, L. (2016). cvxEDA: A convex
optimization approach to electrodermal activity processing. IEEE Transactions on Biomedical
Engineering, 63(4), 797-804.

Hernando-Gallego, F., Luengo, D., & Artés-Rodríguez, A. (2017). Feature extraction of
galvanic skin responses by nonnegative sparse deconvolution. IEEE journal of biomedical and
shealth informatics, 22(5), 1385-1394.

Hernando-Gallego, F., Luengo, D., & Artés-Rodríguez, A. (2017). Feature extraction of
galvanic skin responses by nonnegative sparse deconvolution. IEEE journal of biomedical and
shealth informatics, 22(5), 1385-1394.

Find Skin Conductance Responses (SCR) in Electrodermal Activity (EDA)

Identify Skin Conductance Responses (SCR) peaks in the phasic component of
Electrodermal Activity (EDA) with different possible methods, such as:

eda_phasic ( Union[list, np.array, pd.Series] ) – The phasic component of the EDA signal (from eda_phasic() ).

eda_phasic ( Union[list, np.array, pd.Series] ) – The phasic component of the EDA signal (from eda_phasic() ).

sampling_rate ( int ) – The sampling frequency of the EDA signal (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of the EDA signal (in Hz, i.e., samples/second).

method ( str ) – The processing pipeline to apply. Can be one of "neurokit" (default), "gamboa2008" , "kim2004" (the default in BioSPPy), "vanhalem2020" or "nabian2018" .

method ( str ) – The processing pipeline to apply. Can be one of "neurokit" (default), "gamboa2008" , "kim2004" (the default in BioSPPy), "vanhalem2020" or "nabian2018" .

amplitude_min ( float ) – Only used if method is "neurokit" or "kim2004" . Minimum threshold by which to
exclude SCRs (peaks) as relative to the largest amplitude in the signal.

amplitude_min ( float ) – Only used if method is "neurokit" or "kim2004" . Minimum threshold by which to
exclude SCRs (peaks) as relative to the largest amplitude in the signal.

info ( dict ) – A dictionary containing additional information, in this case the aplitude of the SCR, the
samples at which the SCR onset and the SCR peaks occur. Accessible with the keys "SCR_Amplitude" , "SCR_Onsets" , and "SCR_Peaks" respectively. It also contains the signals’ sampling rate. signals ( DataFrame ) – A DataFrame of same length as the input signal in which occurences of SCR peaks are marked
as “1” in lists of zeros with the same length as "eda_cleaned" . Accessible with the keys "SCR_Peaks" .

info ( dict ) – A dictionary containing additional information, in this case the aplitude of the SCR, the
samples at which the SCR onset and the SCR peaks occur. Accessible with the keys "SCR_Amplitude" , "SCR_Onsets" , and "SCR_Peaks" respectively. It also contains the signals’ sampling rate.

info ( dict ) – A dictionary containing additional information, in this case the aplitude of the SCR, the
samples at which the SCR onset and the SCR peaks occur. Accessible with the keys "SCR_Amplitude" , "SCR_Onsets" , and "SCR_Peaks" respectively. It also contains the signals’ sampling rate.

signals ( DataFrame ) – A DataFrame of same length as the input signal in which occurences of SCR peaks are marked
as “1” in lists of zeros with the same length as "eda_cleaned" . Accessible with the keys "SCR_Peaks" .

signals ( DataFrame ) – A DataFrame of same length as the input signal in which occurences of SCR peaks are marked
as “1” in lists of zeros with the same length as "eda_cleaned" . Accessible with the keys "SCR_Peaks" .

eda_simulate , eda_clean , eda_phasic , eda_process , eda_plot

Gamboa, H. (2008). Multi-modal behavioral biometrics based on hci and electrophysiology.
PhD ThesisUniversidade.

Gamboa, H. (2008). Multi-modal behavioral biometrics based on hci and electrophysiology.
PhD ThesisUniversidade.

Kim, K. H., Bang, S. W., & Kim, S. R. (2004). Emotion recognition system using short-term
monitoring of physiological signals. Medical and biological engineering and computing, 42(3),
419-427.

Kim, K. H., Bang, S. W., & Kim, S. R. (2004). Emotion recognition system using short-term
monitoring of physiological signals. Medical and biological engineering and computing, 42(3),
419-427.

van Halem, S., Van Roekel, E., Kroencke, L., Kuper, N., & Denissen, J. (2020).
Moments That Matter? On the Complexity of Using Triggers Based on Skin Conductance to Sample
Arousing Events Within an Experience Sampling Framework. European Journal of Personality.

van Halem, S., Van Roekel, E., Kroencke, L., Kuper, N., & Denissen, J. (2020).
Moments That Matter? On the Complexity of Using Triggers Based on Skin Conductance to Sample
Arousing Events Within an Experience Sampling Framework. European Journal of Personality.

Nabian, M., Yin, Y., Wormwood, J., Quigley, K. S., Barrett, L. F., & Ostadabbas, S. (2018). An
Open-Source Feature Extraction Tool for the Analysis of Peripheral Physiological Data. IEEE
journal of translational engineering in health and medicine, 6, 2800711.

Nabian, M., Yin, Y., Wormwood, J., Quigley, K. S., Barrett, L. F., & Ostadabbas, S. (2018). An
Open-Source Feature Extraction Tool for the Analysis of Peripheral Physiological Data. IEEE
journal of translational engineering in health and medicine, 6, 2800711.

Correct  Skin Conductance Responses (SCR) peaks

Low-level function used by "eda_peaks()" to correct the peaks found by "eda_findpeaks()" . Doesn’t do anything for now for EDA. See eda_peaks() for details.

peaks ( list or array or DataFrame or Series or dict ) – The samples at which the SCR peaks occur. If a dict or a DataFrame is passed,
it is assumed that these containers were obtained with "eda_findpeaks()" .

peaks ( list or array or DataFrame or Series or dict ) – The samples at which the SCR peaks occur. If a dict or a DataFrame is passed,
it is assumed that these containers were obtained with "eda_findpeaks()" .

onsets ( list or array or DataFrame or Series or dict ) – The samples at which the SCR onsets occur. If a dict or a DataFrame is passed,
it is assumed that these containers were obtained with "eda_findpeaks()" . Defaults to None.

onsets ( list or array or DataFrame or Series or dict ) – The samples at which the SCR onsets occur. If a dict or a DataFrame is passed,
it is assumed that these containers were obtained with "eda_findpeaks()" . Defaults to None.

height ( list or array or DataFrame or Series or dict ) – The samples at which the amplitude of the SCR peaks occur. If a dict or a DataFrame is
passed, it is assumed that these containers were obtained with "eda_findpeaks()" . Defaults to None.

height ( list or array or DataFrame or Series or dict ) – The samples at which the amplitude of the SCR peaks occur. If a dict or a DataFrame is
passed, it is assumed that these containers were obtained with "eda_findpeaks()" . Defaults to None.

info ( dict ) – A dictionary containing additional information, in this case the aplitude of the SCR, the
samples at which the SCR onset and the SCR peaks occur. Accessible with the keys "SCR_Amplitude" , "SCR_Onsets" , and "SCR_Peaks" respectively.

eda_simulate , eda_clean , eda_phasic , eda_findpeaks , eda_peaks , eda_process , eda_plot

Performs event-related EDA analysis on epochs

epochs ( Union[dict, pd.DataFrame] ) – A dict containing one DataFrame per event/trial,
usually obtained via "epochs_create()" , or a DataFrame
containing all epochs, usually obtained via "epochs_to_df()" .

epochs ( Union[dict, pd.DataFrame] ) – A dict containing one DataFrame per event/trial,
usually obtained via "epochs_create()" , or a DataFrame
containing all epochs, usually obtained via "epochs_to_df()" .

silent ( bool ) – If True, silence possible warnings.

silent ( bool ) – If True, silence possible warnings.

DataFrame – A dataframe containing the analyzed EDA features for each epoch, with each epoch indicated
by the Label column (if not present, by the Index column). The analyzed features consist
the following: EDA_SCR : indication of whether Skin Conductance Response (SCR) occurs following the event (1 if an SCR onset is present and 0 if absent) and if so, its corresponding peak amplitude, time of peak, rise and recovery time. If there is no occurrence of SCR, nans are displayed for the below features. EDA_Peak_Amplitude : The maximum amplitude of the phasic component of the signal. SCR_Peak_Amplitude : The peak amplitude of the first SCR in each epoch. SCR_Peak_Amplitude_Time : The timepoint of each first SCR peak amplitude. SCR_RiseTime : The risetime of each first SCR i.e., the time it takes for SCR to reach peak amplitude from onset. SCR_RecoveryTime : The half-recovery time of each first SCR i.e., the time it takes for SCR to decrease to half amplitude.

DataFrame – A dataframe containing the analyzed EDA features for each epoch, with each epoch indicated
by the Label column (if not present, by the Index column). The analyzed features consist
the following:

EDA_SCR : indication of whether Skin Conductance Response (SCR) occurs following the event (1 if an SCR onset is present and 0 if absent) and if so, its corresponding peak amplitude, time of peak, rise and recovery time. If there is no occurrence of SCR, nans are displayed for the below features.

EDA_SCR : indication of whether Skin Conductance Response (SCR) occurs following the event (1 if an SCR onset is present and 0 if absent) and if so, its corresponding peak amplitude, time of peak, rise and recovery time. If there is no occurrence of SCR, nans are displayed for the below features.

EDA_Peak_Amplitude : The maximum amplitude of the phasic component of the signal.

EDA_Peak_Amplitude : The maximum amplitude of the phasic component of the signal.

SCR_Peak_Amplitude : The peak amplitude of the first SCR in each epoch.

SCR_Peak_Amplitude : The peak amplitude of the first SCR in each epoch.

SCR_Peak_Amplitude_Time : The timepoint of each first SCR peak amplitude.

SCR_Peak_Amplitude_Time : The timepoint of each first SCR peak amplitude.

SCR_RiseTime : The risetime of each first SCR i.e., the time it takes for SCR to reach peak amplitude from onset.

SCR_RiseTime : The risetime of each first SCR i.e., the time it takes for SCR to reach peak amplitude from onset.

SCR_RecoveryTime : The half-recovery time of each first SCR i.e., the time it takes for SCR to decrease to half amplitude.

SCR_RecoveryTime : The half-recovery time of each first SCR i.e., the time it takes for SCR to decrease to half amplitude.

events_find , epochs_create , bio_process

Performs EDA analysis on longer periods of data (typically > 10 seconds), such as resting-state
data.

data ( Union[dict, pd.DataFrame] ) – A DataFrame containing the different processed signal(s) as different columns, typically
generated by eda_process() or bio_process() . Can also take a dict containing
sets of separately processed DataFrames.

data ( Union[dict, pd.DataFrame] ) – A DataFrame containing the different processed signal(s) as different columns, typically
generated by eda_process() or bio_process() . Can also take a dict containing
sets of separately processed DataFrames.

sampling_rate ( int ) – The sampling frequency of ecg_signal (in Hz, i.e., samples/second). Defaults to 1000.

sampling_rate ( int ) – The sampling frequency of ecg_signal (in Hz, i.e., samples/second). Defaults to 1000.

**kwargs – Other arguments to be passed to the functions.

**kwargs – Other arguments to be passed to the functions.

DataFrame – A dataframe containing the analyzed EDA features. The analyzed
features consist of the following: SCR_Peaks_N : The number of occurrences of Skin Conductance Response (SCR). SCR_Peaks_Amplitude_Mean : The mean amplitude of the SCR peak occurrences. EDA_Tonic_SD : The mean amplitude of the SCR peak occurrences. "EDA_Sympathetic" : see eda_sympathetic() (only computed if signal duration
> 64 sec). "EDA_Autocorrelation" : see eda_autocor() (only computed if signal duration
> 30 sec).

DataFrame – A dataframe containing the analyzed EDA features. The analyzed
features consist of the following:

SCR_Peaks_N : The number of occurrences of Skin Conductance Response (SCR).

SCR_Peaks_N : The number of occurrences of Skin Conductance Response (SCR).

SCR_Peaks_Amplitude_Mean : The mean amplitude of the SCR peak occurrences.

SCR_Peaks_Amplitude_Mean : The mean amplitude of the SCR peak occurrences.

EDA_Tonic_SD : The mean amplitude of the SCR peak occurrences.

EDA_Tonic_SD : The mean amplitude of the SCR peak occurrences.

"EDA_Sympathetic" : see eda_sympathetic() (only computed if signal duration
> 64 sec).

"EDA_Sympathetic" : see eda_sympathetic() (only computed if signal duration
> 64 sec).

"EDA_Autocorrelation" : see eda_autocor() (only computed if signal duration
> 30 sec).

"EDA_Autocorrelation" : see eda_autocor() (only computed if signal duration
> 30 sec).

Sympathetic Nervous System Index from Electrodermal activity (EDA)

Derived from Posada-Quintero et al. (2016), who argue that dynamics of the sympathetic component
of EDA signal is represented in the frequency band of 0.045-0.25Hz. Note that the Posada method
requires a signal of a least 64 seconds.

eda_signal ( Union[list, np.array, pd.Series] ) – The EDA signal (i.e., a time series) in the form of a vector of values.

eda_signal ( Union[list, np.array, pd.Series] ) – The EDA signal (i.e., a time series) in the form of a vector of values.

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

frequency_band ( list ) – List indicating the frequency range to compute the the power spectral density in.
Defaults to [0.045, 0.25].

frequency_band ( list ) – List indicating the frequency range to compute the the power spectral density in.
Defaults to [0.045, 0.25].

method ( str ) – Can be one of "ghiasi" or "posada" .

method ( str ) – Can be one of "ghiasi" or "posada" .

show ( bool ) – If True, will return a plot of the power spectrum of the EDA signal within the specified
frequency band.

show ( bool ) – If True, will return a plot of the power spectrum of the EDA signal within the specified
frequency band.

signal_filter , signal_power , signal_psd

dict – A dictionary containing the EDA sympathetic indexes, accessible by keys "EDA_Sympathetic" and "EDA_SympatheticN" (normalized, obtained by dividing EDA_Symp
by total power). EDA_Sympathetic : Derived from Posada-Quintero et al. (2016), who argue that dynamics of the sympathetic component of EDA signal is represented in the frequency band of 0.045-0.25Hz. EDA_SympatheticN : normalized version of “EDA_Sympathetic” obtained by dividing EDA_Sympathetic by total power

dict – A dictionary containing the EDA sympathetic indexes, accessible by keys "EDA_Sympathetic" and "EDA_SympatheticN" (normalized, obtained by dividing EDA_Symp
by total power).

EDA_Sympathetic : Derived from Posada-Quintero et al. (2016), who argue that dynamics of the sympathetic component of EDA signal is represented in the frequency band of 0.045-0.25Hz.

EDA_Sympathetic : Derived from Posada-Quintero et al. (2016), who argue that dynamics of the sympathetic component of EDA signal is represented in the frequency band of 0.045-0.25Hz.

EDA_SympatheticN : normalized version of “EDA_Sympathetic” obtained by dividing EDA_Sympathetic by total power

EDA_SympatheticN : normalized version of “EDA_Sympathetic” obtained by dividing EDA_Sympathetic by total power

Ghiasi, S., Grecol, A., Nardelli, M., Catrambonel, V., Barbieri, R., Scilingo, E., & Valenza,
G. (2018). A New Sympathovagal Balance Index from Electrodermal Activity and Instantaneous
Vagal Dynamics: A Preliminary Cold Pressor Study. 2018 40th Annual International Conference
of the IEEE Engineering in Medicine and Biology Society (EMBC). doi:10.1109/embc.2018.8512932

Ghiasi, S., Grecol, A., Nardelli, M., Catrambonel, V., Barbieri, R., Scilingo, E., & Valenza,
G. (2018). A New Sympathovagal Balance Index from Electrodermal Activity and Instantaneous
Vagal Dynamics: A Preliminary Cold Pressor Study. 2018 40th Annual International Conference
of the IEEE Engineering in Medicine and Biology Society (EMBC). doi:10.1109/embc.2018.8512932

Posada-Quintero, H. F., Florian, J. P., Orjuela-Cañón, A. D., Aljama-Corrales, T.,
Charleston-Villalobos, S., & Chon, K. H. (2016). Power spectral density analysis of
electrodermal activity for sympathetic function assessment. Annals of biomedical engineering,
44(10), 3124-3135.

Posada-Quintero, H. F., Florian, J. P., Orjuela-Cañón, A. D., Aljama-Corrales, T.,
Charleston-Villalobos, S., & Chon, K. H. (2016). Power spectral density analysis of
electrodermal activity for sympathetic function assessment. Annals of biomedical engineering,
44(10), 3124-3135.

Compute the autocorrelation measure of raw EDA signal i.e., the correlation between the time
series data and a specified time-lagged version of itself.

eda_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned EDA signal.

eda_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned EDA signal.

sampling_rate ( int ) – The sampling frequency of raw EDA signal (in Hz, i.e., samples/second). Defaults to 1000Hz.

sampling_rate ( int ) – The sampling frequency of raw EDA signal (in Hz, i.e., samples/second). Defaults to 1000Hz.

lag ( int ) – Time lag in seconds. Defaults to 4 seconds to avoid autoregressive
correlations approaching 1, as recommended by Halem et al. (2020).

lag ( int ) – Time lag in seconds. Defaults to 4 seconds to avoid autoregressive
correlations approaching 1, as recommended by Halem et al. (2020).

float – Autocorrelation index of the eda signal.

van Halem, S., Van Roekel, E., Kroencke, L., Kuper, N., & Denissen, J. (2020). Moments that
matter? On the complexity of using triggers based on skin conductance to sample arousing
events within an experience sampling framework. European Journal of Personality, 34(5),
794-807.

van Halem, S., Van Roekel, E., Kroencke, L., Kuper, N., & Denissen, J. (2020). Moments that
matter? On the complexity of using triggers based on skin conductance to sample arousing
events within an experience sampling framework. European Journal of Personality, 34(5),
794-807.

Calculate the number of change points using of the skin conductance signal in terms of mean
and variance.

This function is somewhat experimental, and improvements or discussions about it are
welcome.

eda_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned EDA signal.

eda_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned EDA signal.

penalty ( int ) – Defaults to an algorithm penalty of 10000, as recommended by Halem et al. (2020). See signal_changepoints() .

penalty ( int ) – Defaults to an algorithm penalty of 10000, as recommended by Halem et al. (2020). See signal_changepoints() .

show ( bool ) – Show the signal with the change points.

show ( bool ) – Show the signal with the change points.

van Halem, S., Van Roekel, E., Kroencke, L., Kuper, N., & Denissen, J. (2020). Moments that
matter? On the complexity of using triggers based on skin conductance to sample arousing
events within an experience sampling framework. European Journal of Personality, 34(5),
794-807.

van Halem, S., Van Roekel, E., Kroencke, L., Kuper, N., & Denissen, J. (2020). Moments that
matter? On the complexity of using triggers based on skin conductance to sample arousing
events within an experience sampling framework. European Journal of Personality, 34(5),
794-807.

Find Skin Conductance Responses (SCR) in Electrodermal Activity (EDA)

Low-level function used by eda_peaks() to identify Skin Conductance Responses (SCR) peaks in
the phasic component of Electrodermal Activity (EDA) with different possible methods. See eda_peaks() for details.

eda_phasic ( Union[list, np.array, pd.Series] ) – The phasic component of the EDA signal (from eda_phasic() ).

eda_phasic ( Union[list, np.array, pd.Series] ) – The phasic component of the EDA signal (from eda_phasic() ).

sampling_rate ( int ) – The sampling frequency of the EDA signal (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of the EDA signal (in Hz, i.e., samples/second).

method ( str ) – The processing pipeline to apply. Can be one of "neurokit" (default), "gamboa2008" , "kim2004" (the default in BioSPPy), "vanhalem2020" or "nabian2018" .

method ( str ) – The processing pipeline to apply. Can be one of "neurokit" (default), "gamboa2008" , "kim2004" (the default in BioSPPy), "vanhalem2020" or "nabian2018" .

amplitude_min ( float ) – Only used if “method” is "neurokit" or "kim2004" . Minimum threshold by which to
exclude SCRs (peaks) as relative to the largest amplitude in the signal.

amplitude_min ( float ) – Only used if “method” is "neurokit" or "kim2004" . Minimum threshold by which to
exclude SCRs (peaks) as relative to the largest amplitude in the signal.

info ( dict ) – A dictionary containing additional information, in this case the aplitude of the SCR, the
samples at which the SCR onset and the SCR peaks occur. Accessible with the keys "SCR_Amplitude" , "SCR_Onsets" , and "SCR_Peaks" respectively.

eda_simulate , eda_clean , eda_phasic , eda_fixpeaks , eda_peaks , eda_process , eda_plot

Gamboa, H. (2008). Multi-modal behavioral biometrics based on hci and electrophysiology.
PhD Thesis Universidade.

Gamboa, H. (2008). Multi-modal behavioral biometrics based on hci and electrophysiology.
PhD Thesis Universidade.

Kim, K. H., Bang, S. W., & Kim, S. R. (2004). Emotion recognition system using short-term
monitoring of physiological signals. Medical and biological engineering and computing, 42(3),
419-427.

Kim, K. H., Bang, S. W., & Kim, S. R. (2004). Emotion recognition system using short-term
monitoring of physiological signals. Medical and biological engineering and computing, 42(3),
419-427.

van Halem, S., Van Roekel, E., Kroencke, L., Kuper, N., & Denissen, J. (2020).
Moments That Matter? On the Complexity of Using Triggers Based on Skin Conductance to Sample
Arousing Events Within an Experience Sampling Framework. European Journal of Personality.

van Halem, S., Van Roekel, E., Kroencke, L., Kuper, N., & Denissen, J. (2020).
Moments That Matter? On the Complexity of Using Triggers Based on Skin Conductance to Sample
Arousing Events Within an Experience Sampling Framework. European Journal of Personality.

Nabian, M., Yin, Y., Wormwood, J., Quigley, K. S., Barrett, L. F., & Ostadabbas, S. (2018). An
Open-Source Feature Extraction Tool for the Analysis of Peripheral Physiological Data. IEEE
journal of translational engineering in health and medicine, 6, 2800711.

Nabian, M., Yin, Y., Wormwood, J., Quigley, K. S., Barrett, L. F., & Ostadabbas, S. (2018). An
Open-Source Feature Extraction Tool for the Analysis of Peripheral Physiological Data. IEEE
journal of translational engineering in health and medicine, 6, 2800711.

Any function appearing below this point is not explicitly part of the documentation and should be added. Please open an issue if there is one.
