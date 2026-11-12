# rsp_process()

**Source:** https://neuropsychology.github.io/NeuroKit/functions/rsp.html

---

Convenience function that automatically processes a respiration signal with one of the
following methods:

rsp_signal ( Union[list, np.array, pd.Series] ) – The raw respiration channel (as measured, for instance, by a respiration belt).

rsp_signal ( Union[list, np.array, pd.Series] ) – The raw respiration channel (as measured, for instance, by a respiration belt).

sampling_rate ( int ) – The sampling frequency of rsp_signal() (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of rsp_signal() (in Hz, i.e., samples/second).

method ( str ) – The processing pipeline to apply. Can be one of "khodadad2018" (default)
or "biosppy" .

method ( str ) – The processing pipeline to apply. Can be one of "khodadad2018" (default)
or "biosppy" .

method_rvt ( str ) – The rvt method to apply. Can be one of "harrison2021" (default), "birn2006" or "power2020" .

method_rvt ( str ) – The rvt method to apply. Can be one of "harrison2021" (default), "birn2006" or "power2020" .

report ( str ) – The filename of a report containing description and figures of processing
(e.g. "myreport.html" ). Needs to be supplied if a report file
should be generated. Defaults to None . Can also be "text" to
just print the text in the console without saving anything.

report ( str ) – The filename of a report containing description and figures of processing
(e.g. "myreport.html" ). Needs to be supplied if a report file
should be generated. Defaults to None . Can also be "text" to
just print the text in the console without saving anything.

**kwargs – Other arguments to be passed to specific methods. For more information,
see rsp_methods() .

**kwargs – Other arguments to be passed to specific methods. For more information,
see rsp_methods() .

signals ( DataFrame ) – A DataFrame of same length as rsp_signal() containing the following columns: RSP_Raw : The raw signal. RSP_Clean : The raw signal. RSP_Peaks : The respiratory peaks (exhalation onsets) marked as “1” in a list of zeros. RSP_Troughs : The respiratory troughs (inhalation onsets) marked as “1” in a list of zeros. RSP_Rate : The breathing rate interpolated between inhalation peaks. RSP_Amplitude : The breathing amplitude interpolated between inhalation peaks. RSP_Phase : The breathing phase, marked by “1” for inspiration and “0” for expiration. RSP_Phase_Completion : The breathing phase completion, expressed in percentage (from 0 to 1), representing the stage of the current respiratory phase. RSP_RVT : Respiratory volume per time (RVT). info ( dict ) – A dictionary containing the samples at which inhalation peaks and exhalation troughs occur,
accessible with the keys "RSP_Peaks" , and "RSP_Troughs" respectively, as well as the
signals’ sampling rate.

signals ( DataFrame ) – A DataFrame of same length as rsp_signal() containing the following columns: RSP_Raw : The raw signal. RSP_Clean : The raw signal. RSP_Peaks : The respiratory peaks (exhalation onsets) marked as “1” in a list of zeros. RSP_Troughs : The respiratory troughs (inhalation onsets) marked as “1” in a list of zeros. RSP_Rate : The breathing rate interpolated between inhalation peaks. RSP_Amplitude : The breathing amplitude interpolated between inhalation peaks. RSP_Phase : The breathing phase, marked by “1” for inspiration and “0” for expiration. RSP_Phase_Completion : The breathing phase completion, expressed in percentage (from 0 to 1), representing the stage of the current respiratory phase. RSP_RVT : Respiratory volume per time (RVT).

signals ( DataFrame ) – A DataFrame of same length as rsp_signal() containing the following columns:

RSP_Peaks : The respiratory peaks (exhalation onsets) marked as “1” in a list of zeros.

RSP_Peaks : The respiratory peaks (exhalation onsets) marked as “1” in a list of zeros.

RSP_Troughs : The respiratory troughs (inhalation onsets) marked as “1” in a list of zeros.

RSP_Troughs : The respiratory troughs (inhalation onsets) marked as “1” in a list of zeros.

RSP_Rate : The breathing rate interpolated between inhalation peaks.

RSP_Rate : The breathing rate interpolated between inhalation peaks.

RSP_Amplitude : The breathing amplitude interpolated between inhalation peaks.

RSP_Amplitude : The breathing amplitude interpolated between inhalation peaks.

RSP_Phase : The breathing phase, marked by “1” for inspiration and “0” for expiration.

RSP_Phase : The breathing phase, marked by “1” for inspiration and “0” for expiration.

RSP_Phase_Completion : The breathing phase completion, expressed in percentage (from 0 to 1), representing the stage of the current respiratory phase.

RSP_Phase_Completion : The breathing phase completion, expressed in percentage (from 0 to 1), representing the stage of the current respiratory phase.

RSP_RVT : Respiratory volume per time (RVT).

RSP_RVT : Respiratory volume per time (RVT).

info ( dict ) – A dictionary containing the samples at which inhalation peaks and exhalation troughs occur,
accessible with the keys "RSP_Peaks" , and "RSP_Troughs" respectively, as well as the
signals’ sampling rate.

info ( dict ) – A dictionary containing the samples at which inhalation peaks and exhalation troughs occur,
accessible with the keys "RSP_Peaks" , and "RSP_Troughs" respectively, as well as the
signals’ sampling rate.

rsp_clean , rsp_findpeaks , signal_rate , rsp_amplitude , rsp_plot , rsp_phase , rsp_rvt , rsp_symmetry

Performs RSP analysis on either epochs (event-related analysis) or on longer periods of data such as resting-state data.

data ( dict or DataFrame ) – A dictionary of epochs, containing one DataFrame per epoch, usually obtained via epochs_create() , or a DataFrame containing all epochs, usually obtained via epochs_to_df() . Can also take a DataFrame of processed signals from a longer period
of data, typically generated by rsp_process() or bio_process() . Can also take
a dict containing sets of separate periods of data.

data ( dict or DataFrame ) – A dictionary of epochs, containing one DataFrame per epoch, usually obtained via epochs_create() , or a DataFrame containing all epochs, usually obtained via epochs_to_df() . Can also take a DataFrame of processed signals from a longer period
of data, typically generated by rsp_process() or bio_process() . Can also take
a dict containing sets of separate periods of data.

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second). Defaults to 1000Hz.

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second). Defaults to 1000Hz.

method ( str ) – Can be one of "event-related" for event-related analysis on epochs, or "interval-related" for analysis on longer periods of data. Defaults to "auto" where
the right method will be chosen based on the mean duration of the data ( "event-related" for duration under 10s).

method ( str ) – Can be one of "event-related" for event-related analysis on epochs, or "interval-related" for analysis on longer periods of data. Defaults to "auto" where
the right method will be chosen based on the mean duration of the data ( "event-related" for duration under 10s).

DataFrame – A dataframe containing the analyzed RSP features. If event-related analysis is conducted,
each epoch is indicated by the Label column. See rsp_eventrelated() and rsp_intervalrelated() docstrings for details.

bio_process , rsp_process , epochs_create , rsp_eventrelated , rsp_intervalrelated

Generate an artificial (synthetic) respiratory signal of a given duration
and rate.

duration ( int ) – Desired length of duration (s).

duration ( int ) – Desired length of duration (s).

sampling_rate ( int ) – The desired sampling rate (in Hz, i.e., samples/second).

sampling_rate ( int ) – The desired sampling rate (in Hz, i.e., samples/second).

length ( int ) – The desired length of the signal (in samples).

length ( int ) – The desired length of the signal (in samples).

noise ( float ) – Noise level (amplitude of the laplace noise).

noise ( float ) – Noise level (amplitude of the laplace noise).

respiratory_rate ( float ) – Desired number of breath cycles in one minute.

respiratory_rate ( float ) – Desired number of breath cycles in one minute.

method ( str ) – The model used to generate the signal. Can be "sinusoidal" for a simulation based on a
trigonometric sine wave that roughly approximates a single respiratory cycle. If "breathmetrics" (default), will use an advanced model desbribed by Noto, et al. (2018) .

method ( str ) – The model used to generate the signal. Can be "sinusoidal" for a simulation based on a
trigonometric sine wave that roughly approximates a single respiratory cycle. If "breathmetrics" (default), will use an advanced model desbribed by Noto, et al. (2018) .

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

rsp_clean , rsp_findpeaks , signal_rate , rsp_process , rsp_plot

array – Vector containing the respiratory signal.

Noto, T., Zhou, G., Schuele, S., Templer, J., & Zelano, C. (2018). Automated analysis of
breathing waveforms using BreathMetrics: A respiratory signal processing toolbox. Chemical Senses, 43(8), 583-597.

Noto, T., Zhou, G., Schuele, S., Templer, J., & Zelano, C. (2018). Automated analysis of
breathing waveforms using BreathMetrics: A respiratory signal processing toolbox. Chemical Senses, 43(8), 583-597.

rsp_signals ( DataFrame ) – DataFrame obtained from rsp_process() .

rsp_signals ( DataFrame ) – DataFrame obtained from rsp_process() .

info ( dict ) – The information Dict returned by rsp_process() . Defaults to None .

info ( dict ) – The information Dict returned by rsp_process() . Defaults to None .

static ( bool ) – If True, a static plot will be generated with matplotlib.
If False, an interactive plot will be generated with plotly.
Defaults to True.

static ( bool ) – If True, a static plot will be generated with matplotlib.
If False, an interactive plot will be generated with plotly.
Defaults to True.

See ecg_plot() for details on how to access the figure, modify the size and save it.

Clean a respiration signal using different sets of parameters, such as:

khodadad2018 : Second order 0.05-3 Hz bandpass Butterworth filter. Note that the
implementation differs from the referenced paper (see issue #950).

khodadad2018 : Second order 0.05-3 Hz bandpass Butterworth filter. Note that the
implementation differs from the referenced paper (see issue #950).

BioSPPy : Second order 0.1-0.35 Hz bandpass Butterworth filter followed by a constant
detrending).

BioSPPy : Second order 0.1-0.35 Hz bandpass Butterworth filter followed by a constant
detrending).

hampel : Applies a median-based Hampel filter by replacing values which are 3 (can be
changed via threshold ) mad() away from the rolling median.

hampel : Applies a median-based Hampel filter by replacing values which are 3 (can be
changed via threshold ) mad() away from the rolling median.

charlton2021 : Second order 1 Hz lowpass Butterworth filter. Note that is doesn’t include
the Tukey window step proposed in Charlton et al.

charlton2021 : Second order 1 Hz lowpass Butterworth filter. Note that is doesn’t include
the Tukey window step proposed in Charlton et al.

rsp_signal ( Union[list, np.array, pd.Series] ) – The raw respiration channel (as measured, for instance, by a respiration belt).

rsp_signal ( Union[list, np.array, pd.Series] ) – The raw respiration channel (as measured, for instance, by a respiration belt).

sampling_rate ( int, optional ) – The sampling frequency of rsp_signal() (in Hz, i.e., samples/second).

sampling_rate ( int, optional ) – The sampling frequency of rsp_signal() (in Hz, i.e., samples/second).

method ( str, optional ) – The processing pipeline to apply. Can be one of "khodadad2018" (default), "biosppy" or "hampel" .

method ( str, optional ) – The processing pipeline to apply. Can be one of "khodadad2018" (default), "biosppy" or "hampel" .

**kwargs – Other arguments to pass to the cleaning method.

**kwargs – Other arguments to pass to the cleaning method.

array – Vector containing the cleaned respiratory signal.

rsp_findpeaks , signal_rate , rsp_amplitude , rsp_process , rsp_plot

Khodadad, D., Nordebo, S., Müller, B., Waldmann, A., Yerworth, R., Becher, T., … & Bayford,
R. (2018). Optimized breath detection algorithm in electrical impedance tomography.
Physiological measurement, 39(9), 094001.

Khodadad, D., Nordebo, S., Müller, B., Waldmann, A., Yerworth, R., Becher, T., … & Bayford,
R. (2018). Optimized breath detection algorithm in electrical impedance tomography.
Physiological measurement, 39(9), 094001.

Power, J., Lynch, C., Dubin, M., Silver, B., Martin, A., Jones, R.,(2020)
Characteristics of respiratory measures in young adults scanned at rest,
including systematic changes and “missed” deep breaths.
NeuroImage, Volume 204, 116234

Power, J., Lynch, C., Dubin, M., Silver, B., Martin, A., Jones, R.,(2020)
Characteristics of respiratory measures in young adults scanned at rest,
including systematic changes and “missed” deep breaths.
NeuroImage, Volume 204, 116234

Charlton, P.H, et al. (2021). An impedance pneumography signal quality index: Design, assessment
and application to respiratory rate monitoring. Biomedical Signal Processing and Control, 65, 102339.

Charlton, P.H, et al. (2021). An impedance pneumography signal quality index: Design, assessment
and application to respiratory rate monitoring. Biomedical Signal Processing and Control, 65, 102339.

Compute respiratory amplitude given the raw respiration signal and its extrema. The standard method computes the amplitude as the difference between a peak and its preceding
trough, while the prepost method computes the amplitude as the average of the differences
of peak to its preceding and succeeding troughs (Cole, 2019).

rsp_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned respiration channel as returned by rsp_clean() .

rsp_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned respiration channel as returned by rsp_clean() .

peaks ( list or array or DataFrame or Series or dict ) – The samples at which the respiration peaks (exhalation onsets) occur. If a dict or a
DataFrame is passed, it is assumed that these containers were obtained
with rsp_findpeaks() .

peaks ( list or array or DataFrame or Series or dict ) – The samples at which the respiration peaks (exhalation onsets) occur. If a dict or a
DataFrame is passed, it is assumed that these containers were obtained
with rsp_findpeaks() .

troughs ( list or array or DataFrame or Series or dict ) – The samples at which the respiration troughs (inhalation onsets) occur. If a dict or a
is passed, it is assumed that these containers were obtained with rsp_findpeaks() .

troughs ( list or array or DataFrame or Series or dict ) – The samples at which the respiration troughs (inhalation onsets) occur. If a dict or a
is passed, it is assumed that these containers were obtained with rsp_findpeaks() .

method ( str ) – The method to use to compute the amplitude. Can be "standard" or "prepost" .

method ( str ) – The method to use to compute the amplitude. Can be "standard" or "prepost" .

interpolation_method ( str ) – Method used to interpolate the amplitude between peaks. See signal_interpolate() . "monotone_cubic" is chosen as the default interpolation method since it ensures monotone
interpolation between data point (i.e., it prevents physiologically implausible “overshoots”
or “undershoots” in the y-direction). In contrast, the widely used cubic spline
‘interpolation does not ensure monotonicity.

interpolation_method ( str ) – Method used to interpolate the amplitude between peaks. See signal_interpolate() . "monotone_cubic" is chosen as the default interpolation method since it ensures monotone
interpolation between data point (i.e., it prevents physiologically implausible “overshoots”
or “undershoots” in the y-direction). In contrast, the widely used cubic spline
‘interpolation does not ensure monotonicity.

array – A vector containing the respiratory amplitude.

rsp_clean , rsp_peaks , signal_rate , rsp_process , rsp_plot , rsp_symmetry

Cole, S., & Voytek, B. (2019). Cycle-by-cycle analysis of neural oscillations. Journal of
neurophysiology, 122(2), 849-861.

Cole, S., & Voytek, B. (2019). Cycle-by-cycle analysis of neural oscillations. Journal of
neurophysiology, 122(2), 849-861.

Identify extrema in a respiration (RSP) signal

This function runs rsp_findpeaks() and rsp_fixpeaks() to identify and process
peaks (exhalation onsets) and troughs (inhalation onsets) in a preprocessed respiration signal
using different sets of parameters, such as:

khodad2018 : Uses the parameters in Khodadad et al. (2018).

khodad2018 : Uses the parameters in Khodadad et al. (2018).

biosppy : Uses the parameters in BioSPPy’s resp() function.

biosppy : Uses the parameters in BioSPPy’s resp() function.

scipy Uses the scipy peak-detection function.

scipy Uses the scipy peak-detection function.

schafer2008 : Uses the count-orig algorithm proposed in Schafer et al. (2008).

schafer2008 : Uses the count-orig algorithm proposed in Schafer et al. (2008).

rsp_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned respiration channel as returned by rsp_clean() .

rsp_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned respiration channel as returned by rsp_clean() .

sampling_rate ( int ) – The sampling frequency of rsp_cleaned() (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of rsp_cleaned() (in Hz, i.e., samples/second).

method ( str ) – The processing pipeline to apply. Can be one of "khodadad2018" (default), "biosppy" , "scipy" , or "schafer2008" .

method ( str ) – The processing pipeline to apply. Can be one of "khodadad2018" (default), "biosppy" , "scipy" , or "schafer2008" .

**kwargs – Other arguments to be passed to the different peak finding methods. See rsp_findpeaks() .

**kwargs – Other arguments to be passed to the different peak finding methods. See rsp_findpeaks() .

info ( dict ) – A dictionary containing additional information, in this case the samples at which peaks
(exhalation onsets) and troughs (inhalation onsets) occur, accessible with the keys "RSP_Peaks" , and "RSP_Troughs" , respectively, as well as the signals’ sampling rate. peak_signal ( DataFrame ) – A DataFrame of same length as the input signal in which occurrences of peaks (exhalation
onsets) and troughs (inhalation onsets) are marked as “1” in lists of zeros with the same
length as rsp_cleaned() . Accessible with the keys "RSP_Peaks" and "RSP_Troughs" respectively.

info ( dict ) – A dictionary containing additional information, in this case the samples at which peaks
(exhalation onsets) and troughs (inhalation onsets) occur, accessible with the keys "RSP_Peaks" , and "RSP_Troughs" , respectively, as well as the signals’ sampling rate.

info ( dict ) – A dictionary containing additional information, in this case the samples at which peaks
(exhalation onsets) and troughs (inhalation onsets) occur, accessible with the keys "RSP_Peaks" , and "RSP_Troughs" , respectively, as well as the signals’ sampling rate.

peak_signal ( DataFrame ) – A DataFrame of same length as the input signal in which occurrences of peaks (exhalation
onsets) and troughs (inhalation onsets) are marked as “1” in lists of zeros with the same
length as rsp_cleaned() . Accessible with the keys "RSP_Peaks" and "RSP_Troughs" respectively.

peak_signal ( DataFrame ) – A DataFrame of same length as the input signal in which occurrences of peaks (exhalation
onsets) and troughs (inhalation onsets) are marked as “1” in lists of zeros with the same
length as rsp_cleaned() . Accessible with the keys "RSP_Peaks" and "RSP_Troughs" respectively.

rsp_clean , signal_rate , rsp_findpeaks , rsp_fixpeaks , rsp_amplitude , rsp_process , rsp_plot

Khodadad, D., Nordebo, S., Müller, B., Waldmann, A., Yerworth, R., Becher, T., … & Bayford,
R. (2018). Optimized breath detection algorithm in electrical impedance tomography.
Physiological measurement, 39(9), 094001.

Khodadad, D., Nordebo, S., Müller, B., Waldmann, A., Yerworth, R., Becher, T., … & Bayford,
R. (2018). Optimized breath detection algorithm in electrical impedance tomography.
Physiological measurement, 39(9), 094001.

Schafer, A. and Kratky K.W. (2008). Estimation of breathing rate from respiratory sinus arrhythmia:
comparison of various methods. Annals of Biomedical Engineering, 36(3), 476–85.

Schafer, A. and Kratky K.W. (2008). Estimation of breathing rate from respiratory sinus arrhythmia:
comparison of various methods. Annals of Biomedical Engineering, 36(3), 476–85.

Extract extrema in a respiration (RSP) signal

Low-level function used by rsp_peaks() to identify inhalation and exhalation onsets
(troughs and peaks respectively) in a preprocessed respiration signal using different sets of
parameters. See rsp_peaks() for details.

rsp_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned respiration channel as returned by rsp_clean() .

rsp_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned respiration channel as returned by rsp_clean() .

sampling_rate ( int ) – The sampling frequency of rsp_cleaned() (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of rsp_cleaned() (in Hz, i.e., samples/second).

method ( str ) – The processing pipeline to apply. Can be one of "khodadad2018" (default), "scipy" , "biosppy" , or "bettermann1996" .

method ( str ) – The processing pipeline to apply. Can be one of "khodadad2018" (default), "scipy" , "biosppy" , or "bettermann1996" .

amplitude_min ( float ) – Only applies if method is "khodadad2018" . Extrema that have a vertical distance smaller
than(outlier_threshold * average vertical distance) to any direct neighbour are removed as
false positive outliers. I.e., outlier_threshold should be a float with positive sign (the
default is 0.3). Larger values of outlier_threshold correspond to more conservative
thresholds (i.e., more extrema removed as outliers).

amplitude_min ( float ) – Only applies if method is "khodadad2018" . Extrema that have a vertical distance smaller
than(outlier_threshold * average vertical distance) to any direct neighbour are removed as
false positive outliers. I.e., outlier_threshold should be a float with positive sign (the
default is 0.3). Larger values of outlier_threshold correspond to more conservative
thresholds (i.e., more extrema removed as outliers).

peak_distance ( float ) – Only applies if method is "scipy" . Minimal distance between peaks. Default is 0.8
seconds.

peak_distance ( float ) – Only applies if method is "scipy" . Minimal distance between peaks. Default is 0.8
seconds.

peak_prominence ( float ) – Only applies if method is "scipy" . Minimal prominence between peaks. Default is 0.5.

peak_prominence ( float ) – Only applies if method is "scipy" . Minimal prominence between peaks. Default is 0.5.

info ( dict ) – A dictionary containing additional information, in this case the samples at which inhalation
onsets and exhalation onsets occur, accessible with the keys "RSP_Troughs" and "RSP_Peaks" , respectively.

rsp_clean , rsp_fixpeaks , rsp_peaks , signal_rate , rsp_amplitude , rsp_process , rsp_plot

Low-level function used by rsp_peaks() to correct the peaks found
by rsp_findpeaks() . Doesn’t do anything for now for RSP.
See rsp_peaks() for details.

peaks ( list or array or DataFrame or Series or dict ) – The samples at which respiration peaks (exhalation onsets) occur. If a dict or a DataFrame
is passed, it is assumed that these containers were obtained with rsp_findpeaks() .

peaks ( list or array or DataFrame or Series or dict ) – The samples at which respiration peaks (exhalation onsets) occur. If a dict or a DataFrame
is passed, it is assumed that these containers were obtained with rsp_findpeaks() .

troughs ( list or array or DataFrame or Series or dict ) – The samples at which respiration troughs (inhalation onsets) occur. If a dict or a
DataFrame is passed, it is assumed that these containers were obtained
with rsp_findpeaks() .

troughs ( list or array or DataFrame or Series or dict ) – The samples at which respiration troughs (inhalation onsets) occur. If a dict or a
DataFrame is passed, it is assumed that these containers were obtained
with rsp_findpeaks() .

info ( dict ) – A dictionary containing additional information, in this case the samples at which
inhalation onsets and exhalation onsets occur, accessible with the keys "RSP_Troughs" and "RSP_Peaks" , respectively.

rsp_clean , rsp_findpeaks , rsp_peaks , rsp_amplitude , rsp_process , rsp_plot

Compute respiratory phase (inspiration and expiration)

Finds the respiratory phase, labelled as 1 for inspiration and 0 for expiration.

peaks ( list or array or DataFrame or Series or dict ) – The samples at which the inhalation peaks occur. If a dict or a DataFrame is passed, it is
assumed that these containers were obtained with rsp_findpeaks() .

peaks ( list or array or DataFrame or Series or dict ) – The samples at which the inhalation peaks occur. If a dict or a DataFrame is passed, it is
assumed that these containers were obtained with rsp_findpeaks() .

troughs ( list or array or DataFrame or Series or dict ) – The samples at which the inhalation troughs occur. If a dict or a DataFrame is passed, it is
assumed that these containers were obtained with rsp_findpeaks() .

troughs ( list or array or DataFrame or Series or dict ) – The samples at which the inhalation troughs occur. If a dict or a DataFrame is passed, it is
assumed that these containers were obtained with rsp_findpeaks() .

desired_length ( int ) – By default, the returned respiration rate has the same number of elements as peaks . If
set to an integer, the returned rate will be interpolated between peaks over desired_length samples. Has no effect if a DataFrame is passed in as the peaks argument.

desired_length ( int ) – By default, the returned respiration rate has the same number of elements as peaks . If
set to an integer, the returned rate will be interpolated between peaks over desired_length samples. Has no effect if a DataFrame is passed in as the peaks argument.

pd.DataFrame – A DataFrame of same length as rsp_signal() containing the following columns: "RSP_Phase" : breathing phase, marked by “1” for inspiration and “0” for expiration. "RSP_Phase_Completion" : breathing phase completion, expressed in percentage (from 0
to 1), representing the stage of the current respiratory phase.

pd.DataFrame – A DataFrame of same length as rsp_signal() containing the following columns:

"RSP_Phase" : breathing phase, marked by “1” for inspiration and “0” for expiration.

"RSP_Phase" : breathing phase, marked by “1” for inspiration and “0” for expiration.

"RSP_Phase_Completion" : breathing phase completion, expressed in percentage (from 0
to 1), representing the stage of the current respiratory phase.

"RSP_Phase_Completion" : breathing phase completion, expressed in percentage (from 0
to 1), representing the stage of the current respiratory phase.

rsp_clean , rsp_peaks , rsp_amplitude , rsp_process , rsp_plot

rsp_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned respiration channel as returned by rsp_clean() .

rsp_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned respiration channel as returned by rsp_clean() .

troughs ( Union[list, dict, np.array, pd.Series, pd.DataFrame] ) – The respiration troughs (inhalation onsets) as returned by rsp_peaks() .
If None (default), inhalation onsets will be automatically identified from the rsp_clean() signal.

troughs ( Union[list, dict, np.array, pd.Series, pd.DataFrame] ) – The respiration troughs (inhalation onsets) as returned by rsp_peaks() .
If None (default), inhalation onsets will be automatically identified from the rsp_clean() signal.

sampling_rate ( int ) – The sampling frequency of rsp_cleaned() (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of rsp_cleaned() (in Hz, i.e., samples/second).

window ( int ) – The duration of the sliding window (in second). Default to 10 seconds.

window ( int ) – The duration of the sliding window (in second). Default to 10 seconds.

hop_size ( int ) – The number of samples between each successive window. Default to 1 sample.

hop_size ( int ) – The number of samples between each successive window. Default to 1 sample.

method ( str ) – Method can either be "trough" or "xcorr" . In "trough" method, respiratory rate
is calculated from the periods between successive inspirations (i.e., inhalation onsets/
troughs). In "xcorr" method, cross-correlations between the changes in respiration with
a bank of sinusoids of different frequencies are calculated to identify the principal
frequency of oscillation.

method ( str ) – Method can either be "trough" or "xcorr" . In "trough" method, respiratory rate
is calculated from the periods between successive inspirations (i.e., inhalation onsets/
troughs). In "xcorr" method, cross-correlations between the changes in respiration with
a bank of sinusoids of different frequencies are calculated to identify the principal
frequency of oscillation.

peak_method ( str ) – Method to identify successive respiratory inspirations, only relevant if method is "trough" . Can be one of "khodadad2018" (default) or "biosppy" .

peak_method ( str ) – Method to identify successive respiratory inspirations, only relevant if method is "trough" . Can be one of "khodadad2018" (default) or "biosppy" .

interpolation_method ( str ) – Method used to interpolate the rate between inhalation onsets.
See signal_interpolate() . "monotone_cubic" is chosen as the default
interpolation method since it ensures monotone interpolation between data points (i.e., it
prevents physiologically implausible “overshoots” or “undershoots” in the
y-direction). In contrast, the widely used cubic spline interpolation does not ensure
monotonicity.

interpolation_method ( str ) – Method used to interpolate the rate between inhalation onsets.
See signal_interpolate() . "monotone_cubic" is chosen as the default
interpolation method since it ensures monotone interpolation between data points (i.e., it
prevents physiologically implausible “overshoots” or “undershoots” in the
y-direction). In contrast, the widely used cubic spline interpolation does not ensure
monotonicity.

rsp_rate ( np.ndarray ) – Instantenous respiration rate.

Compute symmetry features of the respiration cycle, such as the Peak-Trough symmetry and the
Rise-Decay symmetry (see Cole, 2019). Note that the values for each cycle are interpolated to
the same length as the signal (and the first and last cycles, for which one cannot compute the
symmetry characteristics, are padded).

rsp_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned respiration channel as returned by rsp_clean() .

rsp_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned respiration channel as returned by rsp_clean() .

peaks ( list or array or DataFrame or Series or dict ) – The samples at which the inhalation peaks occur. If a dict or a DataFrame is passed, it is
assumed that these containers were obtained with rsp_findpeaks() .

peaks ( list or array or DataFrame or Series or dict ) – The samples at which the inhalation peaks occur. If a dict or a DataFrame is passed, it is
assumed that these containers were obtained with rsp_findpeaks() .

troughs ( list or array or DataFrame or Series or dict ) – The samples at which the inhalation troughs occur. If a dict or a DataFrame is passed, it is
assumed that these containers were obtained with rsp_findpeaks() .

troughs ( list or array or DataFrame or Series or dict ) – The samples at which the inhalation troughs occur. If a dict or a DataFrame is passed, it is
assumed that these containers were obtained with rsp_findpeaks() .

interpolation_method ( str ) – Method used to interpolate the amplitude between peaks. See signal_interpolate() . "monotone_cubic" is chosen as the default interpolation method since it ensures monotone
interpolation between data point (i.e., it prevents physiologically implausible “overshoots”
or “undershoots” in the y-direction). In contrast, the widely used cubic spline
‘interpolation does not ensure monotonicity.

interpolation_method ( str ) – Method used to interpolate the amplitude between peaks. See signal_interpolate() . "monotone_cubic" is chosen as the default interpolation method since it ensures monotone
interpolation between data point (i.e., it prevents physiologically implausible “overshoots”
or “undershoots” in the y-direction). In contrast, the widely used cubic spline
‘interpolation does not ensure monotonicity.

show ( bool ) – If True, show a plot of the symmetry features.

show ( bool ) – If True, show a plot of the symmetry features.

pd.DataFrame – A DataFrame of same length as rsp_signal() containing the following columns: "RSP_Symmetry_PeakTrough" "RSP_Symmetry_RiseDecay"

pd.DataFrame – A DataFrame of same length as rsp_signal() containing the following columns:

rsp_clean , rsp_peaks , rsp_amplitude , rsp_phase

Cole, S., & Voytek, B. (2019). Cycle-by-cycle analysis of neural oscillations. Journal of
neurophysiology, 122(2), 849-861.

Cole, S., & Voytek, B. (2019). Cycle-by-cycle analysis of neural oscillations. Journal of
neurophysiology, 122(2), 849-861.

Computes time domain and frequency domain features for Respiratory Rate Variability (RRV)
analysis.

rsp_rate ( array ) – Array containing the respiratory rate, produced by signal_rate() .

rsp_rate ( array ) – Array containing the respiratory rate, produced by signal_rate() .

troughs ( dict ) – The samples at which the inhalation onsets occur.
Dict returned by rsp_peaks() (Accessible with the key, "RSP_Troughs" ).
Defaults to None .

troughs ( dict ) – The samples at which the inhalation onsets occur.
Dict returned by rsp_peaks() (Accessible with the key, "RSP_Troughs" ).
Defaults to None .

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

show ( bool ) – If True , will return a Poincaré plot, a scattergram, which plots each breath-to-breath
interval against the next successive one. The ellipse centers around the average
breath-to-breath interval. Defaults to False .

show ( bool ) – If True , will return a Poincaré plot, a scattergram, which plots each breath-to-breath
interval against the next successive one. The ellipse centers around the average
breath-to-breath interval. Defaults to False .

silent ( bool ) – If False , warnings will be printed. Default to True .

silent ( bool ) – If False , warnings will be printed. Default to True .

DataFrame – DataFrame consisting of the computed RRV metrics, which includes: RRV_SDBB : The standard deviation of the breath-to-breath intervals. RRV_RMSSD : The root mean square of successive differences of the breath-to-breath intervals. RRV_SDSD : The standard deviation of the successive differences between adjacent breath-to-breath intervals. RRV_BBx : The number of successive interval differences that are greater than x seconds. RRV_pBBx : the proportion of breath-to-breath intervals that are greater than x seconds, out of the total number of intervals. RRV_VLF : Spectral power density pertaining to very low frequency band (i.e., 0 to .04 Hz) by default. RRV_LF : Spectral power density pertaining to low frequency band (i.e., .04 to .15 Hz) by default. RRV_HF : Spectral power density pertaining to high frequency band (i.e., .15 to .4 Hz) by default. RRV_LFHF : The ratio of low frequency power to high frequency power. RRV_LFn : The normalized low frequency, obtained by dividing the low frequency power by the total power. RRV_HFn : The normalized high frequency, obtained by dividing the low frequency power by total power. RRV_SD1 : SD1 is a measure of the spread of breath-to-breath intervals on the Poincaré plot perpendicular to the line of identity. It is an index of short-term variability. RRV_SD2 : SD2 is a measure of the spread of breath-to-breath intervals on the Poincaré plot along the line of identity. It is an index of long-term variability. RRV_SD2SD1 : The ratio between short and long term fluctuations of the breath-to-breath intervals (SD2 divided by SD1). RRV_DFA_alpha1 : The “short-term” fluctuation value generated from Detrended Fluctuation Analysis i.e. the root mean square deviation from the fitted trend of the breath-to-breath intervals. Will only be computed if mora than 160 breath cycles in the signal. RRV_DFA_alpha2 : The long-term fluctuation value. Will only be computed if mora than 640 breath cycles in the signal. RRV_ApEn : The approximate entropy of RRV, calculated by :func:`.entropy_approximate`. RRV_SampEn : The sample entropy of RRV, calculated by :func:`.entropy_sample`. MFDFA indices : Indices related to the multifractal spectrum .

DataFrame – DataFrame consisting of the computed RRV metrics, which includes:

RRV_SDBB : The standard deviation of the breath-to-breath intervals.

RRV_SDBB : The standard deviation of the breath-to-breath intervals.

RRV_RMSSD : The root mean square of successive differences of the breath-to-breath intervals.

RRV_RMSSD : The root mean square of successive differences of the breath-to-breath intervals.

RRV_SDSD : The standard deviation of the successive differences between adjacent breath-to-breath intervals.

RRV_SDSD : The standard deviation of the successive differences between adjacent breath-to-breath intervals.

RRV_BBx : The number of successive interval differences that are greater than x seconds.

RRV_BBx : The number of successive interval differences that are greater than x seconds.

RRV_pBBx : the proportion of breath-to-breath intervals that are greater than x seconds, out of the total number of intervals.

RRV_pBBx : the proportion of breath-to-breath intervals that are greater than x seconds, out of the total number of intervals.

RRV_VLF : Spectral power density pertaining to very low frequency band (i.e., 0 to .04 Hz) by default.

RRV_VLF : Spectral power density pertaining to very low frequency band (i.e., 0 to .04 Hz) by default.

RRV_LF : Spectral power density pertaining to low frequency band (i.e., .04 to .15 Hz) by default.

RRV_LF : Spectral power density pertaining to low frequency band (i.e., .04 to .15 Hz) by default.

RRV_HF : Spectral power density pertaining to high frequency band (i.e., .15 to .4 Hz) by default.

RRV_HF : Spectral power density pertaining to high frequency band (i.e., .15 to .4 Hz) by default.

RRV_LFHF : The ratio of low frequency power to high frequency power.

RRV_LFHF : The ratio of low frequency power to high frequency power.

RRV_LFn : The normalized low frequency, obtained by dividing the low frequency power by the total power.

RRV_LFn : The normalized low frequency, obtained by dividing the low frequency power by the total power.

RRV_HFn : The normalized high frequency, obtained by dividing the low frequency power by total power.

RRV_HFn : The normalized high frequency, obtained by dividing the low frequency power by total power.

RRV_SD1 : SD1 is a measure of the spread of breath-to-breath intervals on the Poincaré plot perpendicular to the line of identity. It is an index of short-term variability.

RRV_SD1 : SD1 is a measure of the spread of breath-to-breath intervals on the Poincaré plot perpendicular to the line of identity. It is an index of short-term variability.

RRV_SD2 : SD2 is a measure of the spread of breath-to-breath intervals on the Poincaré plot along the line of identity. It is an index of long-term variability.

RRV_SD2 : SD2 is a measure of the spread of breath-to-breath intervals on the Poincaré plot along the line of identity. It is an index of long-term variability.

RRV_SD2SD1 : The ratio between short and long term fluctuations of the breath-to-breath intervals (SD2 divided by SD1).

RRV_SD2SD1 : The ratio between short and long term fluctuations of the breath-to-breath intervals (SD2 divided by SD1).

RRV_DFA_alpha1 : The “short-term” fluctuation value generated from Detrended Fluctuation Analysis i.e. the root mean square deviation from the fitted trend of the breath-to-breath intervals. Will only be computed if mora than 160 breath cycles in the signal.

RRV_DFA_alpha1 : The “short-term” fluctuation value generated from Detrended Fluctuation Analysis i.e. the root mean square deviation from the fitted trend of the breath-to-breath intervals. Will only be computed if mora than 160 breath cycles in the signal.

RRV_DFA_alpha2 : The long-term fluctuation value. Will only be computed if mora than 640 breath cycles in the signal.

RRV_DFA_alpha2 : The long-term fluctuation value. Will only be computed if mora than 640 breath cycles in the signal.

RRV_ApEn : The approximate entropy of RRV, calculated by :func:`.entropy_approximate`.

RRV_ApEn : The approximate entropy of RRV, calculated by :func:`.entropy_approximate`.

RRV_SampEn : The sample entropy of RRV, calculated by :func:`.entropy_sample`.

RRV_SampEn : The sample entropy of RRV, calculated by :func:`.entropy_sample`.

MFDFA indices : Indices related to the multifractal spectrum .

MFDFA indices : Indices related to the multifractal spectrum .

signal_rate , rsp_peaks , signal_power , entropy_sample , entropy_approximate

Soni, R., & Muniyandi, M. (2019). Breath rate variability: a novel measure to study the
meditation effects. International Journal of Yoga, 12(1), 45.

Soni, R., & Muniyandi, M. (2019). Breath rate variability: a novel measure to study the
meditation effects. International Journal of Yoga, 12(1), 45.

Computes Respiratory Volume per Time (RVT). RVT is the product of respiratory volume and
breathing rate. RVT can be used to identify the global fMRI confounds of breathing, which is
often considered noise.

rsp_signal ( array ) – Array containing the respiratory rate, produced by signal_rate() .

rsp_signal ( array ) – Array containing the respiratory rate, produced by signal_rate() .

sampling_rate ( int, optional ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

sampling_rate ( int, optional ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

method ( str, optional ) – The rvt method to apply. Can be one of "power2020" (default), "harrison2021" or "birn2006" .

method ( str, optional ) – The rvt method to apply. Can be one of "power2020" (default), "harrison2021" or "birn2006" .

boundaries ( list, optional ) – Only applies if method is "harrison" . Lower and upper limit of (humanly possible)
breath frequency in Hertz.

boundaries ( list, optional ) – Only applies if method is "harrison" . Lower and upper limit of (humanly possible)
breath frequency in Hertz.

iterations ( int, optional ) – Only applies if method is "harrison" . Amount of phase refinement estimates
to remove high frequencies. Synthetic samples often take less than 3.

iterations ( int, optional ) – Only applies if method is "harrison" . Amount of phase refinement estimates
to remove high frequencies. Synthetic samples often take less than 3.

show ( bool, optional ) – If True , will return a simple plot of the RVT (with the re-scaled original RSP signal).

show ( bool, optional ) – If True , will return a simple plot of the RVT (with the re-scaled original RSP signal).

silent ( bool, optional ) – If True , warnings will not be printed.

silent ( bool, optional ) – If True , warnings will not be printed.

**kwargs – Arguments to be passed to the underlying peak detection algorithm.

**kwargs – Arguments to be passed to the underlying peak detection algorithm.

array – Array containing the current RVT at every timestep.

signal_rate , rsp_peaks , rsp_process , rsp_clean

Birn, R. M., Diamond, J. B., Smith, M. A., & Bandettini, P. A. (2006). Separating
respiratory-variation-related fluctuations from neuronal-activity-related fluctuations in
fMRI. Neuroimage, 31(4), 1536-1548.

Birn, R. M., Diamond, J. B., Smith, M. A., & Bandettini, P. A. (2006). Separating
respiratory-variation-related fluctuations from neuronal-activity-related fluctuations in
fMRI. Neuroimage, 31(4), 1536-1548.

Power, J. D., Lynch, C. J., Dubin, M. J., Silver, B. M., Martin, A., & Jones, R. M. (2020).
Characteristics of respiratory measures in young adults scanned at rest, including systematic
changes and “missed” deep breaths. Neuroimage, 204, 116234.

Power, J. D., Lynch, C. J., Dubin, M. J., Silver, B. M., Martin, A., & Jones, R. M. (2020).
Characteristics of respiratory measures in young adults scanned at rest, including systematic
changes and “missed” deep breaths. Neuroimage, 204, 116234.

Harrison, S. J., Bianchi, S., Heinzle, J., Stephan, K. E., Iglesias, S., & Kasper, L. (2021).
A Hilbert-based method for processing respiratory timeseries. Neuroimage, 230, 117787.

Harrison, S. J., Bianchi, S., Heinzle, J., Stephan, K. E., Iglesias, S., & Kasper, L. (2021).
A Hilbert-based method for processing respiratory timeseries. Neuroimage, 230, 117787.

Performs event-related RSP analysis on epochs

epochs ( Union[dict, pd.DataFrame] ) – A dict containing one DataFrame per event/trial, usually obtained via epochs_create() , or a DataFrame containing all epochs, usually obtained
via epochs_to_df() .

epochs ( Union[dict, pd.DataFrame] ) – A dict containing one DataFrame per event/trial, usually obtained via epochs_create() , or a DataFrame containing all epochs, usually obtained
via epochs_to_df() .

silent ( bool ) – If True , silence possible warnings.

silent ( bool ) – If True , silence possible warnings.

DataFrame – A dataframe containing the analyzed RSP features for each epoch, with each epoch indicated
by the Label column (if not present, by the Index column). The analyzed features
consist of the following: RSP_Rate_Max : The maximum respiratory rate after stimulus onset. RSP_Rate_Min : The minimum respiratory rate after stimulus onset. RSP_Rate_Mean : The mean respiratory rate after stimulus onset. RSP_Rate_SD : The standard deviation of the respiratory rate after stimulus onset. RSP_Rate_Max_Time : The time at which maximum respiratory rate occurs. RSP_Rate_Min_Time : The time at which minimum respiratory rate occurs. RSP_Amplitude_Baseline : The respiratory amplitude at stimulus onset. RSP_Amplitude_Max : The change in maximum respiratory amplitude from before stimulus onset. RSP_Amplitude_Min : The change in minimum respiratory amplitude from before stimulus onset. RSP_Amplitude_Mean : The change in mean respiratory amplitude from before stimulus onset. RSP_Amplitude_SD : The standard deviation of the respiratory amplitude after stimulus onset. RSP_Phase : Indication of whether the onset of the event concurs with respiratory inspiration (1) or expiration (0). RSP_PhaseCompletion : Indication of the stage of the current respiration phase (0 to 1) at the onset of the event.

DataFrame – A dataframe containing the analyzed RSP features for each epoch, with each epoch indicated
by the Label column (if not present, by the Index column). The analyzed features
consist of the following:

RSP_Rate_Max : The maximum respiratory rate after stimulus onset.

RSP_Rate_Max : The maximum respiratory rate after stimulus onset.

RSP_Rate_Min : The minimum respiratory rate after stimulus onset.

RSP_Rate_Min : The minimum respiratory rate after stimulus onset.

RSP_Rate_Mean : The mean respiratory rate after stimulus onset.

RSP_Rate_Mean : The mean respiratory rate after stimulus onset.

RSP_Rate_SD : The standard deviation of the respiratory rate after stimulus onset.

RSP_Rate_SD : The standard deviation of the respiratory rate after stimulus onset.

RSP_Rate_Max_Time : The time at which maximum respiratory rate occurs.

RSP_Rate_Max_Time : The time at which maximum respiratory rate occurs.

RSP_Rate_Min_Time : The time at which minimum respiratory rate occurs.

RSP_Rate_Min_Time : The time at which minimum respiratory rate occurs.

RSP_Amplitude_Baseline : The respiratory amplitude at stimulus onset.

RSP_Amplitude_Baseline : The respiratory amplitude at stimulus onset.

RSP_Amplitude_Max : The change in maximum respiratory amplitude from before stimulus onset.

RSP_Amplitude_Max : The change in maximum respiratory amplitude from before stimulus onset.

RSP_Amplitude_Min : The change in minimum respiratory amplitude from before stimulus onset.

RSP_Amplitude_Min : The change in minimum respiratory amplitude from before stimulus onset.

RSP_Amplitude_Mean : The change in mean respiratory amplitude from before stimulus onset.

RSP_Amplitude_Mean : The change in mean respiratory amplitude from before stimulus onset.

RSP_Amplitude_SD : The standard deviation of the respiratory amplitude after stimulus onset.

RSP_Amplitude_SD : The standard deviation of the respiratory amplitude after stimulus onset.

RSP_Phase : Indication of whether the onset of the event concurs with respiratory inspiration (1) or expiration (0).

RSP_Phase : Indication of whether the onset of the event concurs with respiratory inspiration (1) or expiration (0).

RSP_PhaseCompletion : Indication of the stage of the current respiration phase (0 to 1) at the onset of the event.

RSP_PhaseCompletion : Indication of the stage of the current respiration phase (0 to 1) at the onset of the event.

events_find , epochs_create , bio_process

Performs RSP analysis on longer periods of data (typically > 10 seconds), such as resting-state
data. It returns a dataframe containing features and characteristics of respiration in that
interval.

data ( DataFrame or dict ) – A DataFrame containing the different processed signal(s) as different columns, typically
generated by rsp_process() or bio_process() . Can also take a dict containing
sets of separately processed DataFrames.

data ( DataFrame or dict ) – A DataFrame containing the different processed signal(s) as different columns, typically
generated by rsp_process() or bio_process() . Can also take a dict containing
sets of separately processed DataFrames.

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

DataFrame – A dataframe containing the analyzed RSP features.
The analyzed features consist of the following: RSP_Rate_Mean : The mean respiratory rate. RSP_Amplitude_Mean : The mean respiratory amplitude. RSP_Phase_Duration_Inspiration : The average inspiration duration. RSP_Phase_Duration_Expiration : The average expiration duration. RSP_Phase_Duration_Ratio : The inspiration-to-expiratory time ratio (I/E). "RSP_RRV" : the different respiratory rate variability metrices.
See rsp_rrv() docstrings for details.

DataFrame – A dataframe containing the analyzed RSP features.
The analyzed features consist of the following:

RSP_Rate_Mean : The mean respiratory rate.

RSP_Rate_Mean : The mean respiratory rate.

RSP_Amplitude_Mean : The mean respiratory amplitude.

RSP_Amplitude_Mean : The mean respiratory amplitude.

RSP_Phase_Duration_Inspiration : The average inspiration duration.

RSP_Phase_Duration_Inspiration : The average inspiration duration.

RSP_Phase_Duration_Expiration : The average expiration duration.

RSP_Phase_Duration_Expiration : The average expiration duration.

RSP_Phase_Duration_Ratio : The inspiration-to-expiratory time ratio (I/E).

RSP_Phase_Duration_Ratio : The inspiration-to-expiratory time ratio (I/E).

"RSP_RRV" : the different respiratory rate variability metrices.
See rsp_rrv() docstrings for details.

"RSP_RRV" : the different respiratory rate variability metrices.
See rsp_rrv() docstrings for details.

bio_process , rsp_eventrelated , rsp_rrv , rsp_rav

Any function appearing below this point is not explicitly part of the documentation and should be added. Please open an issue if there is one.

This function analyzes and specifies the methods used in the preprocessing, and create a
textual description of the methods used. It is used by rsp_process() to dispatch the
correct methods to each subroutine of the pipeline and rsp_report() to create a
preprocessing report.

sampling_rate ( int ) – The sampling frequency of the raw RSP signal (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of the raw RSP signal (in Hz, i.e., samples/second).

method ( str ) – The method used for cleaning and peak finding if "method_cleaning" and "method_peaks" are set to "default" . Can be one of "Khodadad" , "BioSPPy" .
Defaults to "Khodadad" .

method ( str ) – The method used for cleaning and peak finding if "method_cleaning" and "method_peaks" are set to "default" . Can be one of "Khodadad" , "BioSPPy" .
Defaults to "Khodadad" .

method_cleaning ( str ) – The method used to clean the raw RSP signal. If "default" ,
will be set to the value of "method" . Defaults to "default" .
For more information, see the "method" argument
of rsp_clean() .

method_cleaning ( str ) – The method used to clean the raw RSP signal. If "default" ,
will be set to the value of "method" . Defaults to "default" .
For more information, see the "method" argument
of rsp_clean() .

method_peaks ( str ) – The method used to find peaks. If "default" ,
will be set to the value of "method" . Defaults to "default" .
For more information, see the "method" argument
of rsp_peaks() .

method_peaks ( str ) – The method used to find peaks. If "default" ,
will be set to the value of "method" . Defaults to "default" .
For more information, see the "method" argument
of rsp_peaks() .

method_rvt ( str ) – The method used to compute respiratory volume per time. Defaults to "harrison" .
For more information, see the "method" argument
of rsp_rvt() .

method_rvt ( str ) – The method used to compute respiratory volume per time. Defaults to "harrison" .
For more information, see the "method" argument
of rsp_rvt() .

**kwargs – Other arguments to be passed to rsp_clean() , rsp_peaks() , and rsp_rvt() .

**kwargs – Other arguments to be passed to rsp_clean() , rsp_peaks() , and rsp_rvt() .

report_info ( dict ) – A dictionary containing the keyword arguments passed to the cleaning
and peak finding functions, text describing the methods, and the corresponding
references.

Assess the quality of the RSP Signal. using template matching:

The "templatematch" method (loosely based on Charlton et al., 2021) computes a continuous
index of quality of the RSP signal, by calculating the correlation coefficient between each
individual breath and an average (template) breath shape. This index is therefore
relative: 1 corresponds to breaths that are closest to the average breath shape (i.e.
correlate exactly with it) and 0 corresponds to there being no correlation with the average
breath shape. Note that for pre-processing, Charlton et al. cleaned the signal with a low-pass filter
below 1 Hz (the “charlton2021” method in rsp_clean), and used the “bettermann1996” breath detection
algorithm (the “bettermann1996” method in rsp_peaks).

The "templatematch" method (loosely based on Charlton et al., 2021) computes a continuous
index of quality of the RSP signal, by calculating the correlation coefficient between each
individual breath and an average (template) breath shape. This index is therefore
relative: 1 corresponds to breaths that are closest to the average breath shape (i.e.
correlate exactly with it) and 0 corresponds to there being no correlation with the average
breath shape. Note that for pre-processing, Charlton et al. cleaned the signal with a low-pass filter
below 1 Hz (the “charlton2021” method in rsp_clean), and used the “bettermann1996” breath detection
algorithm (the “bettermann1996” method in rsp_peaks).

The "dissimilarity" method (borrowed from Sabeti et al., 2019, who proposed it for the PPG signal)
computes a continuous index of quality of the RSP signal, by calculating the level of dissimilarity between
each individual breath and an average (template) breath shape (after they are normalised). A value of
zero indicates no dissimilarity (i.e. equivalent breath shapes), whereas values above or below
indicate increasing dissimilarity.

The "dissimilarity" method (borrowed from Sabeti et al., 2019, who proposed it for the PPG signal)
computes a continuous index of quality of the RSP signal, by calculating the level of dissimilarity between
each individual breath and an average (template) breath shape (after they are normalised). A value of
zero indicates no dissimilarity (i.e. equivalent breath shapes), whereas values above or below
indicate increasing dissimilarity.

rsp_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned RSP signal in the form of a vector of values.

rsp_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned RSP signal in the form of a vector of values.

peaks ( tuple or list ) – The list of RSP peak samples returned by rsp_peaks() . If None, peaks is computed from
the signal input.

peaks ( tuple or list ) – The list of RSP peak samples returned by rsp_peaks() . If None, peaks is computed from
the signal input.

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

method ( str ) – The method for computing RSP signal quality. The only option is "templatematch" (default).

method ( str ) – The method for computing RSP signal quality. The only option is "templatematch" (default).

quality ( array ) – Vector containing the quality index ranging from 0 to 1.

Charlton, P.H, et al. (2021). An impedance pneumography signal quality index: Design, assessment
and application to respiratory rate monitoring. Biomedical Signal Processing and Control, 65, 102339.

Charlton, P.H, et al. (2021). An impedance pneumography signal quality index: Design, assessment
and application to respiratory rate monitoring. Biomedical Signal Processing and Control, 65, 102339.

Sabeti E. et al. (2019). Signal quality measure for pulsatile physiological signals using morphological features:
Applications in reliability measure for pulse oximetry. Informatics in Medicine Unlocked, 16, 100222.

Sabeti E. et al. (2019). Signal quality measure for pulsatile physiological signals using morphological features:
Applications in reliability measure for pulse oximetry. Informatics in Medicine Unlocked, 16, 100222.

Computes indices of amplitude variability, such as the mean and SD of the amplitude, and the
RMSSD of the successive differences.

This is an exploratory feature. If you manage to find studies and literature on RAV, please
let us know by opening an issue on GitHub. Adding more indices (similar to HRV) would be
trivial, but having some evidence as for its usefulness would be prerequisite.

amplitude ( Union[list, np.array, pd.Series] ) – The amplitude signal as returned by rsp_amplitude() .

amplitude ( Union[list, np.array, pd.Series] ) – The amplitude signal as returned by rsp_amplitude() .

peaks ( list or array or DataFrame or Series or dict ) – The samples at which the inhalation peaks occur. If a dict or a DataFrame is passed, it is
assumed that these containers were obtained with rsp_findpeaks() .

peaks ( list or array or DataFrame or Series or dict ) – The samples at which the inhalation peaks occur. If a dict or a DataFrame is passed, it is
assumed that these containers were obtained with rsp_findpeaks() .

troughs ( list or array or DataFrame or Series or dict ) – The samples at which the inhalation troughs occur. If a dict or a DataFrame is passed, it is
assumed that these containers were obtained with rsp_findpeaks() . This argument can
be inferred from the peaks argument if the information.

troughs ( list or array or DataFrame or Series or dict ) – The samples at which the inhalation troughs occur. If a dict or a DataFrame is passed, it is
assumed that these containers were obtained with rsp_findpeaks() . This argument can
be inferred from the peaks argument if the information.

pd.DataFrame – A DataFrame of containing the following columns with RAV indices.

Segment a respiratory signal into individual breaths

Segment a respiratory signal into individual breaths. Convenient for visualizing all the breaths.

rsp_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned respiratory channel as returned by rsp_clean() .

rsp_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned respiratory channel as returned by rsp_clean() .

peaks ( dict ) – The samples at which the peaks (exhalation onsets) occur. Dict returned by rsp_peaks() . Defaults to None .

peaks ( dict ) – The samples at which the peaks (exhalation onsets) occur. Dict returned by rsp_peaks() . Defaults to None .

sampling_rate ( int ) – The sampling frequency of rsp_cleaned (in Hz, i.e., samples/second). Defaults to 1000.

sampling_rate ( int ) – The sampling frequency of rsp_cleaned (in Hz, i.e., samples/second). Defaults to 1000.

show ( bool ) – If True , will return a plot of breaths. Defaults to False .

show ( bool ) – If True , will return a plot of breaths. Defaults to False .

dict – A dict containing DataFrames for all segmented breaths.
