# 
    "These features include the RMSSD (square root of the mean of the sum of successive differences between adjacent RR intervals), MeanNN (mean of RR intervals) so on and so forth. You can also visualize the distribution of R-R intervals by specifying `show=True` in [hrv_time()

**Source:** https://neuropsychology.github.io/NeuroKit/functions/hrv.html

---

This function computes all HRV indices available in NeuroKit. It is essentially a convenience
function that aggregates results from the time domain , frequency domain , and non-linear domain .

We strongly recommend checking our open-access paper Pham et al. (2021) on HRV indices as well as Frasch (2022) for more information.

peaks ( dict ) – Samples at which R-peaks occur. Can be a list of indices or the output(s) of other
functions such as ecg_peaks() , ppg_peaks() , ecg_process() or bio_process() . Can also be a dict containing the keys RRI and RRI_Time to directly pass the R-R intervals and their timestamps, respectively.

peaks ( dict ) – Samples at which R-peaks occur. Can be a list of indices or the output(s) of other
functions such as ecg_peaks() , ppg_peaks() , ecg_process() or bio_process() . Can also be a dict containing the keys RRI and RRI_Time to directly pass the R-R intervals and their timestamps, respectively.

sampling_rate ( int, optional ) – Sampling rate (Hz) of the continuous cardiac signal in which the peaks occur. Should be at
least twice as high as the highest frequency in vhf. By default 1000.

sampling_rate ( int, optional ) – Sampling rate (Hz) of the continuous cardiac signal in which the peaks occur. Should be at
least twice as high as the highest frequency in vhf. By default 1000.

show ( bool, optional ) – If True , returns the plots that are generated for each of the domains.

show ( bool, optional ) – If True , returns the plots that are generated for each of the domains.

DataFrame – Contains HRV indices in a DataFrame. If RSP data was provided (e.g., output of bio_process() ), RSA indices will also be included.

hrv_time , hrv_frequency , hrv_nonlinear , hrv_rsa , ecg_peaks , ppg_peaks

Example 1 : Only using a list of R-peaks locations

Example 2 : Compute HRV directly from processed data

Pham, T., Lau, Z. J., Chen, S. H. A., & Makowski, D. (2021). Heart Rate Variability in
Psychology: A Review of HRV Indices and an Analysis Tutorial. Sensors, 21(12), 3998. https://doi.org/10.3390/s21123998

Pham, T., Lau, Z. J., Chen, S. H. A., & Makowski, D. (2021). Heart Rate Variability in
Psychology: A Review of HRV Indices and an Analysis Tutorial. Sensors, 21(12), 3998. https://doi.org/10.3390/s21123998

Frasch, M. G. (2022). Comprehensive HRV estimation pipeline in Python using Neurokit2:
Application to sleep physiology. MethodsX, 9, 101782.

Frasch, M. G. (2022). Comprehensive HRV estimation pipeline in Python using Neurokit2:
Application to sleep physiology. MethodsX, 9, 101782.

Stein, P. K. (2002). Assessing heart rate variability from real-world Holter reports. Cardiac
electrophysiology review, 6(3), 239-244.

Stein, P. K. (2002). Assessing heart rate variability from real-world Holter reports. Cardiac
electrophysiology review, 6(3), 239-244.

Shaffer, F., & Ginsberg, J. P. (2017). An overview of heart rate variability metrics and
norms. Frontiers in public health, 5, 258.

Shaffer, F., & Ginsberg, J. P. (2017). An overview of heart rate variability metrics and
norms. Frontiers in public health, 5, 258.

Computes time-domain indices of Heart Rate Variability (HRV)

Time-domain measures reflect the total variability of HR and are relatively indiscriminate when
it comes to precisely quantifying the respective contributions of different underlying
regulatory mechanisms. However, this “general” sensitivity can be seen as a positive feature
(e.g., in exploratory studies or when specific underlying neurophysiological mechanisms are not
the focus). Moreover, as they are easy to compute and interpret, time-domain measures are still
among the most commonly reported HRV indices.

The time-domain indices can be categorized into deviation-based and difference-based indices
where the former are calculated directly from the normal beat-to-beat intervals (normal RR
intervals or NN intervals), and the latter are derived from the difference between successive NN
intervals.

We strongly recommend checking our open-access paper Pham et al. (2021) on HRV indices for more information.

peaks ( dict ) – Samples at which cardiac extrema (i.e., R-peaks, systolic peaks) occur.
Can be a list of indices or the output(s) of other functions such as ecg_peaks() , ppg_peaks() , ecg_process() or bio_process() .
Can also be a dict containing the keys RRI and RRI_Time to directly pass the R-R intervals and their timestamps, respectively.

peaks ( dict ) – Samples at which cardiac extrema (i.e., R-peaks, systolic peaks) occur.
Can be a list of indices or the output(s) of other functions such as ecg_peaks() , ppg_peaks() , ecg_process() or bio_process() .
Can also be a dict containing the keys RRI and RRI_Time to directly pass the R-R intervals and their timestamps, respectively.

sampling_rate ( int, optional ) – Sampling rate (Hz) of the continuous cardiac signal in which the peaks occur. Should be at
least twice as high as the highest frequency in vhf. By default 1000.

sampling_rate ( int, optional ) – Sampling rate (Hz) of the continuous cardiac signal in which the peaks occur. Should be at
least twice as high as the highest frequency in vhf. By default 1000.

show ( bool ) – If True , will plot the distribution of R-R intervals.

show ( bool ) – If True , will plot the distribution of R-R intervals.

DataFrame – Contains time domain HRV metrics: MeanNN : The mean of the RR intervals. SDNN : The standard deviation of the RR intervals. SDANN1 , SDANN2 , SDANN5 : The standard deviation of average RR intervals
extracted from n-minute segments of time series data (1, 2 and 5 by default). Note that
these indices require a minimal duration of signal to be computed (3, 6 and 15 minutes
respectively) and will be silently skipped if the data provided is too short. SDNNI1 , SDNNI2 , SDNNI5 : The mean of the standard deviations of RR intervals
extracted from n-minute segments of time series data (1, 2 and 5 by default). Note that
these indices require a minimal duration of signal to be computed (3, 6 and 15 minutes
respectively) and will be silently skipped if the data provided is too short. RMSSD : The square root of the mean of the squared successive differences between
adjacent RR intervals. It is equivalent (although on another scale) to SD1, and
therefore it is redundant to report correlations with both (Ciccone, 2017). SDSD : The standard deviation of the successive differences between RR intervals. CVNN : The standard deviation of the RR intervals ( SDNN ) divided by the mean of
the RR intervals ( MeanNN ). CVSD : The root mean square of successive differences ( RMSSD ) divided by
the mean of the RR intervals ( MeanNN ). MedianNN : The median of the RR intervals. MadNN : The median absolute deviation of the RR intervals. MCVNN : The median absolute deviation of the RR intervals ( MadNN ) divided by the
median of the RR intervals ( MedianNN ). IQRNN : The interquartile range ( IQR ) of the RR intervals. SDRMSSD : SDNN / RMSSD, a time-domain equivalent for the low Frequency-to-High
Frequency (LF/HF) Ratio (Sollers et al., 2007). Prc20NN : The 20th percentile of the RR intervals (Han, 2017; Hovsepian, 2015). Prc80NN : The 80th percentile of the RR intervals (Han, 2017; Hovsepian, 2015). pNN50 : The percentage of absolute differences in successive RR intervals greater than
50 ms (Bigger et al., 1988; Mietus et al., 2002). pNN20 : The percentage of absolute differences in successive RR intervals greater than
20 ms (Mietus et al., 2002). MinNN : The minimum of the RR intervals (Parent, 2019; Subramaniam, 2022). MaxNN : The maximum of the RR intervals (Parent, 2019; Subramaniam, 2022). TINN : A geometrical parameter of the HRV, or more specifically, the baseline width of
the RR intervals distribution obtained by triangular interpolation, where the error of
least squares determines the triangle. It is an approximation of the RR interval
distribution. HTI : The HRV triangular index, measuring the total number of RR intervals divided by
the height of the RR intervals histogram.

DataFrame – Contains time domain HRV metrics:

SDNN : The standard deviation of the RR intervals.

SDNN : The standard deviation of the RR intervals.

SDANN1 , SDANN2 , SDANN5 : The standard deviation of average RR intervals
extracted from n-minute segments of time series data (1, 2 and 5 by default). Note that
these indices require a minimal duration of signal to be computed (3, 6 and 15 minutes
respectively) and will be silently skipped if the data provided is too short.

SDANN1 , SDANN2 , SDANN5 : The standard deviation of average RR intervals
extracted from n-minute segments of time series data (1, 2 and 5 by default). Note that
these indices require a minimal duration of signal to be computed (3, 6 and 15 minutes
respectively) and will be silently skipped if the data provided is too short.

SDNNI1 , SDNNI2 , SDNNI5 : The mean of the standard deviations of RR intervals
extracted from n-minute segments of time series data (1, 2 and 5 by default). Note that
these indices require a minimal duration of signal to be computed (3, 6 and 15 minutes
respectively) and will be silently skipped if the data provided is too short.

SDNNI1 , SDNNI2 , SDNNI5 : The mean of the standard deviations of RR intervals
extracted from n-minute segments of time series data (1, 2 and 5 by default). Note that
these indices require a minimal duration of signal to be computed (3, 6 and 15 minutes
respectively) and will be silently skipped if the data provided is too short.

RMSSD : The square root of the mean of the squared successive differences between
adjacent RR intervals. It is equivalent (although on another scale) to SD1, and
therefore it is redundant to report correlations with both (Ciccone, 2017).

RMSSD : The square root of the mean of the squared successive differences between
adjacent RR intervals. It is equivalent (although on another scale) to SD1, and
therefore it is redundant to report correlations with both (Ciccone, 2017).

SDSD : The standard deviation of the successive differences between RR intervals.

SDSD : The standard deviation of the successive differences between RR intervals.

CVNN : The standard deviation of the RR intervals ( SDNN ) divided by the mean of
the RR intervals ( MeanNN ).

CVNN : The standard deviation of the RR intervals ( SDNN ) divided by the mean of
the RR intervals ( MeanNN ).

CVSD : The root mean square of successive differences ( RMSSD ) divided by
the mean of the RR intervals ( MeanNN ).

CVSD : The root mean square of successive differences ( RMSSD ) divided by
the mean of the RR intervals ( MeanNN ).

MedianNN : The median of the RR intervals.

MedianNN : The median of the RR intervals.

MadNN : The median absolute deviation of the RR intervals.

MadNN : The median absolute deviation of the RR intervals.

MCVNN : The median absolute deviation of the RR intervals ( MadNN ) divided by the
median of the RR intervals ( MedianNN ).

MCVNN : The median absolute deviation of the RR intervals ( MadNN ) divided by the
median of the RR intervals ( MedianNN ).

IQRNN : The interquartile range ( IQR ) of the RR intervals.

IQRNN : The interquartile range ( IQR ) of the RR intervals.

SDRMSSD : SDNN / RMSSD, a time-domain equivalent for the low Frequency-to-High
Frequency (LF/HF) Ratio (Sollers et al., 2007).

SDRMSSD : SDNN / RMSSD, a time-domain equivalent for the low Frequency-to-High
Frequency (LF/HF) Ratio (Sollers et al., 2007).

Prc20NN : The 20th percentile of the RR intervals (Han, 2017; Hovsepian, 2015).

Prc20NN : The 20th percentile of the RR intervals (Han, 2017; Hovsepian, 2015).

Prc80NN : The 80th percentile of the RR intervals (Han, 2017; Hovsepian, 2015).

Prc80NN : The 80th percentile of the RR intervals (Han, 2017; Hovsepian, 2015).

pNN50 : The percentage of absolute differences in successive RR intervals greater than
50 ms (Bigger et al., 1988; Mietus et al., 2002).

pNN50 : The percentage of absolute differences in successive RR intervals greater than
50 ms (Bigger et al., 1988; Mietus et al., 2002).

pNN20 : The percentage of absolute differences in successive RR intervals greater than
20 ms (Mietus et al., 2002).

pNN20 : The percentage of absolute differences in successive RR intervals greater than
20 ms (Mietus et al., 2002).

MinNN : The minimum of the RR intervals (Parent, 2019; Subramaniam, 2022).

MinNN : The minimum of the RR intervals (Parent, 2019; Subramaniam, 2022).

MaxNN : The maximum of the RR intervals (Parent, 2019; Subramaniam, 2022).

MaxNN : The maximum of the RR intervals (Parent, 2019; Subramaniam, 2022).

TINN : A geometrical parameter of the HRV, or more specifically, the baseline width of
the RR intervals distribution obtained by triangular interpolation, where the error of
least squares determines the triangle. It is an approximation of the RR interval
distribution.

TINN : A geometrical parameter of the HRV, or more specifically, the baseline width of
the RR intervals distribution obtained by triangular interpolation, where the error of
least squares determines the triangle. It is an approximation of the RR interval
distribution.

HTI : The HRV triangular index, measuring the total number of RR intervals divided by
the height of the RR intervals histogram.

HTI : The HRV triangular index, measuring the total number of RR intervals divided by
the height of the RR intervals histogram.

ecg_peaks , ppg_peaks , hrv_frequency , hrv_summary , hrv_nonlinear

Where applicable, the unit used for these metrics is the millisecond.

Bigger Jr, J. T., Kleiger, R. E., Fleiss, J. L., Rolnitzky, L. M., Steinman, R. C., & Miller,
J. P. (1988). Components of heart rate variability measured during healing of acute myocardial
infarction. The American journal of cardiology, 61(4), 208-215.

Bigger Jr, J. T., Kleiger, R. E., Fleiss, J. L., Rolnitzky, L. M., Steinman, R. C., & Miller,
J. P. (1988). Components of heart rate variability measured during healing of acute myocardial
infarction. The American journal of cardiology, 61(4), 208-215.

Pham, T., Lau, Z. J., Chen, S. H. A., & Makowski, D. (2021). Heart Rate Variability in
Psychology: A Review of HRV Indices and an Analysis Tutorial. Sensors, 21(12), 3998. https://doi.org/10.3390/s21123998

Pham, T., Lau, Z. J., Chen, S. H. A., & Makowski, D. (2021). Heart Rate Variability in
Psychology: A Review of HRV Indices and an Analysis Tutorial. Sensors, 21(12), 3998. https://doi.org/10.3390/s21123998

Ciccone, A. B., Siedlik, J. A., Wecht, J. M., Deckert, J. A., Nguyen, N. D., & Weir, J. P.
(2017). Reminder: RMSSD and SD1 are identical heart rate variability metrics. Muscle & nerve,
56(4), 674-678.

Ciccone, A. B., Siedlik, J. A., Wecht, J. M., Deckert, J. A., Nguyen, N. D., & Weir, J. P.
(2017). Reminder: RMSSD and SD1 are identical heart rate variability metrics. Muscle & nerve,
56(4), 674-678.

Han, L., Zhang, Q., Chen, X., Zhan, Q., Yang, T., & Zhao, Z. (2017). Detecting work-related
stress with a wearable device. Computers in Industry, 90, 42-49.

Han, L., Zhang, Q., Chen, X., Zhan, Q., Yang, T., & Zhao, Z. (2017). Detecting work-related
stress with a wearable device. Computers in Industry, 90, 42-49.

Hovsepian, K., Al’Absi, M., Ertin, E., Kamarck, T., Nakajima, M., & Kumar, S. (2015). cStress:
towards a gold standard for continuous stress assessment in the mobile environment. In
Proceedings of the 2015 ACM international joint conference on pervasive and ubiquitous
computing (pp. 493-504).

Hovsepian, K., Al’Absi, M., Ertin, E., Kamarck, T., Nakajima, M., & Kumar, S. (2015). cStress:
towards a gold standard for continuous stress assessment in the mobile environment. In
Proceedings of the 2015 ACM international joint conference on pervasive and ubiquitous
computing (pp. 493-504).

Mietus, J. E., Peng, C. K., Henry, I., Goldsmith, R. L., & Goldberger, A. L. (2002). The pNNx
files: re-examining a widely used heart rate variability measure. Heart, 88(4), 378-380.

Mietus, J. E., Peng, C. K., Henry, I., Goldsmith, R. L., & Goldberger, A. L. (2002). The pNNx
files: re-examining a widely used heart rate variability measure. Heart, 88(4), 378-380.

Parent, M., Tiwari, A., Albuquerque, I., Gagnon, J. F., Lafond, D., Tremblay, S., & Falk, T.
H. (2019). A multimodal approach to improve the robustness of physiological stress prediction
during physical activity. In 2019 IEEE International Conference on Systems, Man and
Cybernetics (SMC) (pp. 4131-4136). IEEE.

Parent, M., Tiwari, A., Albuquerque, I., Gagnon, J. F., Lafond, D., Tremblay, S., & Falk, T.
H. (2019). A multimodal approach to improve the robustness of physiological stress prediction
during physical activity. In 2019 IEEE International Conference on Systems, Man and
Cybernetics (SMC) (pp. 4131-4136). IEEE.

Stein, P. K. (2002). Assessing heart rate variability from real-world Holter reports. Cardiac
electrophysiology review, 6(3), 239-244.

Stein, P. K. (2002). Assessing heart rate variability from real-world Holter reports. Cardiac
electrophysiology review, 6(3), 239-244.

Shaffer, F., & Ginsberg, J. P. (2017). An overview of heart rate variability metrics and
norms. Frontiers in public health, 5, 258.

Shaffer, F., & Ginsberg, J. P. (2017). An overview of heart rate variability metrics and
norms. Frontiers in public health, 5, 258.

Subramaniam, S. D., & Dass, B. (2022). An Efficient Convolutional Neural Network for Acute
Pain Recognition Using HRV Features. In Proceedings of the International e-Conference on
Intelligent Systems and Signal Processing (pp. 119-132). Springer, Singapore.

Subramaniam, S. D., & Dass, B. (2022). An Efficient Convolutional Neural Network for Acute
Pain Recognition Using HRV Features. In Proceedings of the International e-Conference on
Intelligent Systems and Signal Processing (pp. 119-132). Springer, Singapore.

Sollers, J. J., Buchanan, T. W., Mowrer, S. M., Hill, L. K., & Thayer, J. F. (2007).
Comparison of the ratio of the standard deviation of the RR interval and the root mean
squared successive differences (SD/rMSSD) to the low frequency-to-high frequency (LF/HF)
ratio in a patient population and normal healthy controls. Biomed Sci Instrum, 43, 158-163.

Sollers, J. J., Buchanan, T. W., Mowrer, S. M., Hill, L. K., & Thayer, J. F. (2007).
Comparison of the ratio of the standard deviation of the RR interval and the root mean
squared successive differences (SD/rMSSD) to the low frequency-to-high frequency (LF/HF)
ratio in a patient population and normal healthy controls. Biomed Sci Instrum, 43, 158-163.

Computes frequency-domain indices of Heart Rate Variability (HRV)

Computes frequency domain HRV metrics, such as the power in different frequency bands.

ULF : The spectral power of ultra low frequencies (by default, .0 to
.0033 Hz). Very long signals are required for this to index to be
extracted, otherwise, will return NaN.

ULF : The spectral power of ultra low frequencies (by default, .0 to
.0033 Hz). Very long signals are required for this to index to be
extracted, otherwise, will return NaN.

VLF : The spectral power of very low frequencies (by default, .0033 to .04 Hz).

VLF : The spectral power of very low frequencies (by default, .0033 to .04 Hz).

LF : The spectral power of low frequencies (by default, .04 to .15 Hz).

LF : The spectral power of low frequencies (by default, .04 to .15 Hz).

HF : The spectral power of high frequencies (by default, .15 to .4 Hz).

HF : The spectral power of high frequencies (by default, .15 to .4 Hz).

VHF : The spectral power of very high frequencies (by default, .4 to .5 Hz).

VHF : The spectral power of very high frequencies (by default, .4 to .5 Hz).

LFHF : The ratio obtained by dividing the low frequency power by the high frequency power.

LFHF : The ratio obtained by dividing the low frequency power by the high frequency power.

LFn : The normalized low frequency, obtained by dividing the low frequency power by
the total power.

LFn : The normalized low frequency, obtained by dividing the low frequency power by
the total power.

HFn : The normalized high frequency, obtained by dividing the low frequency power by
the total power.

HFn : The normalized high frequency, obtained by dividing the low frequency power by
the total power.

Note that a minimum duration of the signal containing the peaks is recommended for some HRV
indices to be meaningful. For instance, 1, 2 and 5 minutes of high quality signal are the
recommended minima for HF, LF and LF/HF, respectively.

We strongly recommend checking our open-access paper Pham et al. (2021) on HRV indices for more information.

peaks ( dict ) – Samples at which cardiac extrema (i.e., R-peaks, systolic peaks) occur.
Can be a list of indices or the output(s) of other functions such as ecg_peaks() , ppg_peaks() , ecg_process() or bio_process() .
Can also be a dict containing the keys RRI and RRI_Time to directly pass the R-R intervals and their timestamps, respectively.

peaks ( dict ) – Samples at which cardiac extrema (i.e., R-peaks, systolic peaks) occur.
Can be a list of indices or the output(s) of other functions such as ecg_peaks() , ppg_peaks() , ecg_process() or bio_process() .
Can also be a dict containing the keys RRI and RRI_Time to directly pass the R-R intervals and their timestamps, respectively.

sampling_rate ( int, optional ) – Sampling rate (Hz) of the continuous cardiac signal in which the peaks occur.

sampling_rate ( int, optional ) – Sampling rate (Hz) of the continuous cardiac signal in which the peaks occur.

ulf ( tuple, optional ) – Upper and lower limit of the ultra-low frequency band. By default (0, 0.0033).

ulf ( tuple, optional ) – Upper and lower limit of the ultra-low frequency band. By default (0, 0.0033).

vlf ( tuple, optional ) – Upper and lower limit of the very-low frequency band. By default (0.0033, 0.04).

vlf ( tuple, optional ) – Upper and lower limit of the very-low frequency band. By default (0.0033, 0.04).

lf ( tuple, optional ) – Upper and lower limit of the low frequency band. By default (0.04, 0.15).

lf ( tuple, optional ) – Upper and lower limit of the low frequency band. By default (0.04, 0.15).

hf ( tuple, optional ) – Upper and lower limit of the high frequency band. By default (0.15, 0.4).

hf ( tuple, optional ) – Upper and lower limit of the high frequency band. By default (0.15, 0.4).

vhf ( tuple, optional ) – Upper and lower limit of the very-high frequency band. By default (0.4, 0.5).

vhf ( tuple, optional ) – Upper and lower limit of the very-high frequency band. By default (0.4, 0.5).

psd_method ( str ) – Method used for spectral density estimation. For details see signal_power() .
By default "welch" .

psd_method ( str ) – Method used for spectral density estimation. For details see signal_power() .
By default "welch" .

silent ( bool ) – If False , warnings will be printed. Default to True .

silent ( bool ) – If False , warnings will be printed. Default to True .

show ( bool ) – If True , will plot the power in the different frequency bands.

show ( bool ) – If True , will plot the power in the different frequency bands.

normalize ( bool ) – Normalization of power by maximum PSD value. Default to True .
Normalization allows comparison between different PSD methods.

normalize ( bool ) – Normalization of power by maximum PSD value. Default to True .
Normalization allows comparison between different PSD methods.

order_criteria ( str ) – The criteria to automatically select order in parametric PSD (only used for autoregressive
(AR) methods such as "burg" ). Defaults to None .

order_criteria ( str ) – The criteria to automatically select order in parametric PSD (only used for autoregressive
(AR) methods such as "burg" ). Defaults to None .

interpolation_rate ( int, optional ) – Sampling rate (Hz) of the interpolated interbeat intervals. Should be at least twice as
high as the highest frequency in vhf. By default 100. To replicate Kubios defaults, set to 4.
To not interpolate, set interpolation_rate to None (in case the interbeat intervals are already
interpolated or when using the "lombscargle" psd_method for which interpolation is not required).

interpolation_rate ( int, optional ) – Sampling rate (Hz) of the interpolated interbeat intervals. Should be at least twice as
high as the highest frequency in vhf. By default 100. To replicate Kubios defaults, set to 4.
To not interpolate, set interpolation_rate to None (in case the interbeat intervals are already
interpolated or when using the "lombscargle" psd_method for which interpolation is not required).

DataFrame – DataFrame consisting of the computed HRV frequency metrics, which includes: HRV_ULF : The spectral power of ultra low frequencies (by default, .0 to .0033 Hz). Very long signals are required for this to index to be extracted, otherwise, will return NaN. HRV_VLF : The spectral power of very low frequencies (by default, .0033 to .04 Hz). HRV_LF : The spectral power of low frequencies (by default, .04 to .15 Hz). HRV_HF : The spectral power of high frequencies (by default, .15 to .4 Hz). HRV_VHF : The spectral power of very high frequencies (by default, .4 to .5 Hz). HRV_TP : The total spectral power. HRV_LFHF : The ratio obtained by dividing the low frequency power by the high frequency power. HRV_LFn : The normalized low frequency, obtained by dividing the low frequency power by the total power. HRV_HFn : The normalized high frequency, obtained by dividing the low frequency power by the total power. HRV_LnHF : The log transformed HF.

DataFrame – DataFrame consisting of the computed HRV frequency metrics, which includes:

HRV_ULF : The spectral power of ultra low frequencies (by default, .0 to .0033 Hz). Very long signals are required for this to index to be extracted, otherwise, will return NaN.

HRV_ULF : The spectral power of ultra low frequencies (by default, .0 to .0033 Hz). Very long signals are required for this to index to be extracted, otherwise, will return NaN.

HRV_VLF : The spectral power of very low frequencies (by default, .0033 to .04 Hz).

HRV_VLF : The spectral power of very low frequencies (by default, .0033 to .04 Hz).

HRV_LF : The spectral power of low frequencies (by default, .04 to .15 Hz).

HRV_LF : The spectral power of low frequencies (by default, .04 to .15 Hz).

HRV_HF : The spectral power of high frequencies (by default, .15 to .4 Hz).

HRV_HF : The spectral power of high frequencies (by default, .15 to .4 Hz).

HRV_VHF : The spectral power of very high frequencies (by default, .4 to .5 Hz).

HRV_VHF : The spectral power of very high frequencies (by default, .4 to .5 Hz).

HRV_LFHF : The ratio obtained by dividing the low frequency power by the high frequency power.

HRV_LFHF : The ratio obtained by dividing the low frequency power by the high frequency power.

HRV_LFn : The normalized low frequency, obtained by dividing the low frequency power by the total power.

HRV_LFn : The normalized low frequency, obtained by dividing the low frequency power by the total power.

HRV_HFn : The normalized high frequency, obtained by dividing the low frequency power by the total power.

HRV_HFn : The normalized high frequency, obtained by dividing the low frequency power by the total power.

ecg_peaks , ppg_peaks , hrv_summary , hrv_time , hrv_nonlinear

Pham, T., Lau, Z. J., Chen, S. H. A., & Makowski, D. (2021). Heart Rate Variability in
Psychology: A Review of HRV Indices and an Analysis Tutorial. Sensors, 21(12), 3998.

Pham, T., Lau, Z. J., Chen, S. H. A., & Makowski, D. (2021). Heart Rate Variability in
Psychology: A Review of HRV Indices and an Analysis Tutorial. Sensors, 21(12), 3998.

Stein, P. K. (2002). Assessing heart rate variability from real-world Holter reports. Cardiac
electrophysiology review, 6(3), 239-244.

Stein, P. K. (2002). Assessing heart rate variability from real-world Holter reports. Cardiac
electrophysiology review, 6(3), 239-244.

Shaffer, F., & Ginsberg, J. P. (2017). An overview of heart rate variability metrics and
norms. Frontiers in public health, 5, 258.

Shaffer, F., & Ginsberg, J. P. (2017). An overview of heart rate variability metrics and
norms. Frontiers in public health, 5, 258.

Boardman, A., Schlindwein, F. S., & Rocha, A. P. (2002). A study on the optimum order of
autoregressive models for heart rate variability. Physiological measurement, 23(2), 325.

Boardman, A., Schlindwein, F. S., & Rocha, A. P. (2002). A study on the optimum order of
autoregressive models for heart rate variability. Physiological measurement, 23(2), 325.

Bachler, M. (2017). Spectral Analysis of Unevenly Spaced Data: Models and Application in Heart
Rate Variability. Simul. Notes Eur., 27(4), 183-190.

Bachler, M. (2017). Spectral Analysis of Unevenly Spaced Data: Models and Application in Heart
Rate Variability. Simul. Notes Eur., 27(4), 183-190.

Nonlinear indices of Heart Rate Variability (HRV)

This function computes non-linear indices, which include features derived from the Poincaré
plot , as well as other complexity() indices corresponding to entropy or fractal
dimension.

There exist many more complexity indices available in NeuroKit2, that could be applied to
HRV. The hrv_nonlinear() function only includes the most commonly used indices.
Please see the documentation page for all the func: .complexity features.

The Poincaré plot is a graphical representation of each NN interval plotted against its
preceding NN interval. The ellipse that emerges is a visual quantification of the correlation
between successive NN intervals.

Basic indices derived from the Poincaré plot analysis include:

SD1 : Standard deviation perpendicular to the line of identity. It is an index of
short-term RR interval fluctuations, i.e., beat-to-beat variability. It is equivalent
(although on another scale) to RMSSD, and therefore it is redundant to report correlation
with both.

SD1 : Standard deviation perpendicular to the line of identity. It is an index of
short-term RR interval fluctuations, i.e., beat-to-beat variability. It is equivalent
(although on another scale) to RMSSD, and therefore it is redundant to report correlation
with both.

SD2 : Standard deviation along the identity line. Index of long-term HRV changes.

SD2 : Standard deviation along the identity line. Index of long-term HRV changes.

SD1/SD2 : ratio of SD1 to SD2 . Describes the ratio of short term to long term
variations in HRV.

SD1/SD2 : ratio of SD1 to SD2 . Describes the ratio of short term to long term
variations in HRV.

S : Area of ellipse described by SD1 and SD2 ( pi * SD1 * SD2 ). It is
proportional to SD1SD2 .

S : Area of ellipse described by SD1 and SD2 ( pi * SD1 * SD2 ). It is
proportional to SD1SD2 .

CSI : The Cardiac Sympathetic Index (Toichi, 1997) is a measure of cardiac sympathetic
function independent of vagal activity, calculated by dividing the longitudinal variability of
the Poincaré plot ( 4*SD2 ) by its transverse variability ( 4*SD1 ).

CSI : The Cardiac Sympathetic Index (Toichi, 1997) is a measure of cardiac sympathetic
function independent of vagal activity, calculated by dividing the longitudinal variability of
the Poincaré plot ( 4*SD2 ) by its transverse variability ( 4*SD1 ).

CVI : The Cardiac Vagal Index (Toichi, 1997) is an index of cardiac parasympathetic
function (vagal activity unaffected by sympathetic activity), and is equal equal to the
logarithm of the product of longitudinal ( 4*SD2 ) and transverse variability ( 4*SD1 ).

CVI : The Cardiac Vagal Index (Toichi, 1997) is an index of cardiac parasympathetic
function (vagal activity unaffected by sympathetic activity), and is equal equal to the
logarithm of the product of longitudinal ( 4*SD2 ) and transverse variability ( 4*SD1 ).

CSI_Modified : The modified CSI (Jeppesen, 2014) obtained by dividing the square of the
longitudinal variability by its transverse variability.

CSI_Modified : The modified CSI (Jeppesen, 2014) obtained by dividing the square of the
longitudinal variability by its transverse variability.

Indices of Heart Rate Asymmetry (HRA), i.e., asymmetry of the Poincaré plot (Yan, 2017),
include:

GI : Guzik’s Index, defined as the distance of points above line of identity (LI) to LI
divided by the distance of all points in Poincaré plot to LI except those that are located on
LI.

GI : Guzik’s Index, defined as the distance of points above line of identity (LI) to LI
divided by the distance of all points in Poincaré plot to LI except those that are located on
LI.

SI : Slope Index, defined as the phase angle of points above LI divided by the phase angle
of all points in Poincaré plot except those that are located on LI.

SI : Slope Index, defined as the phase angle of points above LI divided by the phase angle
of all points in Poincaré plot except those that are located on LI.

AI : Area Index, defined as the cumulative area of the sectors corresponding to the points
that are located above LI divided by the cumulative area of sectors corresponding to all
points in the Poincaré plot except those that are located on LI.

AI : Area Index, defined as the cumulative area of the sectors corresponding to the points
that are located above LI divided by the cumulative area of sectors corresponding to all
points in the Poincaré plot except those that are located on LI.

PI : Porta’s Index, defined as the number of points below LI divided by the total number
of points in Poincaré plot except those that are located on LI.

PI : Porta’s Index, defined as the number of points below LI divided by the total number
of points in Poincaré plot except those that are located on LI.

SD1d and SD1a : short-term variance of contributions of decelerations (prolongations
of RR intervals) and accelerations (shortenings of RR intervals), respectively (Piskorski,
2011)

SD1d and SD1a : short-term variance of contributions of decelerations (prolongations
of RR intervals) and accelerations (shortenings of RR intervals), respectively (Piskorski,
2011)

C1d and C1a : the contributions of heart rate decelerations and accelerations to
short-term HRV, respectively (Piskorski,  2011).

C1d and C1a : the contributions of heart rate decelerations and accelerations to
short-term HRV, respectively (Piskorski,  2011).

SD2d and SD2a : long-term variance of contributions of decelerations (prolongations of
RR intervals) and accelerations (shortenings of RR intervals), respectively (Piskorski, 2011).

SD2d and SD2a : long-term variance of contributions of decelerations (prolongations of
RR intervals) and accelerations (shortenings of RR intervals), respectively (Piskorski, 2011).

C2d and C2a : the contributions of heart rate decelerations and accelerations to
long-term HRV, respectively (Piskorski,  2011).

C2d and C2a : the contributions of heart rate decelerations and accelerations to
long-term HRV, respectively (Piskorski,  2011).

SDNNd and SDNNa : total variance of contributions of decelerations (prolongations of
RR intervals) and accelerations (shortenings of RR intervals), respectively (Piskorski, 2011).

SDNNd and SDNNa : total variance of contributions of decelerations (prolongations of
RR intervals) and accelerations (shortenings of RR intervals), respectively (Piskorski, 2011).

Cd and Ca : the total contributions of heart rate decelerations and accelerations to
HRV.

Cd and Ca : the total contributions of heart rate decelerations and accelerations to
HRV.

Indices of Heart Rate Fragmentation (Costa, 2017) include:

PIP : Percentage of inflection points of the RR intervals series.

PIP : Percentage of inflection points of the RR intervals series.

IALS : Inverse of the average length of the acceleration/deceleration segments.

IALS : Inverse of the average length of the acceleration/deceleration segments.

PSS : Fraction of successive RR differences in short acceleration/deceleration segments
(fewer than three differences).

PSS : Fraction of successive RR differences in short acceleration/deceleration segments
(fewer than three differences).

PAS : Percentage of NN intervals in alternation segments.

PAS : Percentage of NN intervals in alternation segments.

Indices of Complexity and Fractal Physiology include:

HFD : See fractal_higuchi() (with kmax set to "default" ).

HFD : See fractal_higuchi() (with kmax set to "default" ).

DFA_alpha1 : The monofractal detrended fluctuation analysis of the HR signal,
corresponding to short-term correlations. See fractal_dfa() .

DFA_alpha1 : The monofractal detrended fluctuation analysis of the HR signal,
corresponding to short-term correlations. See fractal_dfa() .

DFA_alpha2 : The monofractal detrended fluctuation analysis of the HR signal,
corresponding to long-term correlations. See fractal_dfa() .

DFA_alpha2 : The monofractal detrended fluctuation analysis of the HR signal,
corresponding to long-term correlations. See fractal_dfa() .

MFDFA indices : Indices related to the multifractal spectrum .

MFDFA indices : Indices related to the multifractal spectrum .

Other non-linear indices include those based on Recurrence Quantification Analysis (RQA), which
can be computed with hrv_rqa() .

We strongly recommend checking our open-access paper Pham et al. (2021) on HRV indices, as well as Lau et al. (2021) on complexity, for more information.

peaks ( dict ) – Samples at which cardiac extrema (i.e., R-peaks, systolic peaks) occur.
Can be a list of indices or the output(s) of other functions such as ecg_peaks() , ppg_peaks() , ecg_process() or bio_process() .
Can also be a dict containing the keys RRI and RRI_Time to directly pass the R-R intervals and their timestamps, respectively.

peaks ( dict ) – Samples at which cardiac extrema (i.e., R-peaks, systolic peaks) occur.
Can be a list of indices or the output(s) of other functions such as ecg_peaks() , ppg_peaks() , ecg_process() or bio_process() .
Can also be a dict containing the keys RRI and RRI_Time to directly pass the R-R intervals and their timestamps, respectively.

sampling_rate ( int, optional ) – Sampling rate (Hz) of the continuous cardiac signal in which the peaks occur. Should be at
least twice as high as the highest frequency in vhf. By default 1000.

sampling_rate ( int, optional ) – Sampling rate (Hz) of the continuous cardiac signal in which the peaks occur. Should be at
least twice as high as the highest frequency in vhf. By default 1000.

show ( bool, optional ) – If True , will return a Poincaré plot, a scattergram, which plots each RR interval
against the next successive one. The ellipse centers around the average RR interval. By
default False .

show ( bool, optional ) – If True , will return a Poincaré plot, a scattergram, which plots each RR interval
against the next successive one. The ellipse centers around the average RR interval. By
default False .

**kwargs – Other arguments to be passed into fractal_dfa() and fractal_correlation() .

**kwargs – Other arguments to be passed into fractal_dfa() and fractal_correlation() .

DataFrame – DataFrame consisting of the computed non-linear HRV metrics, which includes: HRV_SD1 : Standard deviation perpendicular to the line of identity. It is an index of short-term RR interval fluctuations, i.e., beat-to-beat variability. It is equivalent (although on another scale) to RMSSD, and therefore it is redundant to report correlation with both. HRV_SD2 : Standard deviation along the identity line. Index of long-term HRV changes. HRV_SD1SD2 : Ratio of SD1 to SD2. Describes the ratio of short term to long term variations in HRV. HRV_S : Area of ellipse described by *SD1* and *SD2* (``pi * SD1 * SD2``). It is proportional to *SD1SD2*. HRV_CSI : The Cardiac Sympathetic Index (Toichi, 1997) is a measure of cardiac sympathetic function independent of vagal activity, calculated by dividing the longitudinal variability of the Poincaré plot (``4*SD2``) by its transverse variability (``4*SD1``). HRV_CVI : The Cardiac Vagal Index (Toichi, 1997) is an index of cardiac parasympathetic function (vagal activity unaffected by sympathetic activity), and is equal equal to the logarithm of the product of longitudinal (``4*SD2``) and transverse variability (``4*SD1``). HRV_CSI_Modified : The modified CSI (Jeppesen, 2014) obtained by dividing the square of the longitudinal variability by its transverse variability. HRV_GI : Guzik’s Index, defined as the distance of points above line of identity (LI) to LI divided by the distance of all points in Poincaré plot to LI except those that are located on LI. HRV_SI : Slope Index, defined as the phase angle of points above LI divided by the phase angle of all points in Poincaré plot except those that are located on LI. HRV_AI : Area Index, defined as the cumulative area of the sectors corresponding to the points that are located above LI divided by the cumulative area of sectors corresponding to all points in the Poincaré plot except those that are located on LI. HRV_PI : Porta’s Index, defined as the number of points below LI divided by the total number of points in Poincaré plot except those that are located on LI. HRV_SD1a : Short-term variance of contributions of decelerations (prolongations of RR intervals), (Piskorski, 2011). HRV_SD1d : Short-term variance of contributions of accelerations (shortenings of RR intervals), (Piskorski, 2011). HRV_C1a : The contributions of heart rate accelerations to short-term HRV, (Piskorski, 2011). HRV_C1d : The contributions of heart rate decelerations to short-term HRV, (Piskorski, 2011). HRV_SD2a : Long-term variance of contributions of accelerations (shortenings of RR intervals), (Piskorski, 2011). HRV_SD2d : Long-term variance of contributions of decelerations (prolongations of RR intervals), (Piskorski, 2011). HRV_C2a : The contributions of heart rate accelerations to long-term HRV, (Piskorski, 2011). HRV_C2d : The contributions of heart rate decelerations to long-term HRV, (Piskorski, 2011). HRV_SDNNa : Total variance of contributions of accelerations (shortenings of RR intervals), (Piskorski, 2011). HRV_SDNNd : Total variance of contributions of decelerations (prolongations of RR intervals), (Piskorski, 2011). HRV_Ca : The total contributions of heart rate accelerations to HRV. HRV_Cd : The total contributions of heart rate decelerations to HRV. HRV_PIP : Percentage of inflection points of the RR intervals series. HRV_IALS : Inverse of the average length of the acceleration/deceleration segments. HRV_PSS : Fraction of RR differences in short acceleration/deceleration segments. HRV_PAS : Percentage of NN intervals in alternation segments.

DataFrame – DataFrame consisting of the computed non-linear HRV metrics, which includes:

HRV_SD1 : Standard deviation perpendicular to the line of identity. It is an index of short-term RR interval fluctuations, i.e., beat-to-beat variability. It is equivalent (although on another scale) to RMSSD, and therefore it is redundant to report correlation with both.

HRV_SD1 : Standard deviation perpendicular to the line of identity. It is an index of short-term RR interval fluctuations, i.e., beat-to-beat variability. It is equivalent (although on another scale) to RMSSD, and therefore it is redundant to report correlation with both.

HRV_SD2 : Standard deviation along the identity line. Index of long-term HRV changes.

HRV_SD2 : Standard deviation along the identity line. Index of long-term HRV changes.

HRV_SD1SD2 : Ratio of SD1 to SD2. Describes the ratio of short term to long term variations in HRV.

HRV_SD1SD2 : Ratio of SD1 to SD2. Describes the ratio of short term to long term variations in HRV.

HRV_S : Area of ellipse described by *SD1* and *SD2* (``pi * SD1 * SD2``). It is proportional to *SD1SD2*.

HRV_S : Area of ellipse described by *SD1* and *SD2* (``pi * SD1 * SD2``). It is proportional to *SD1SD2*.

HRV_CSI : The Cardiac Sympathetic Index (Toichi, 1997) is a measure of cardiac sympathetic function independent of vagal activity, calculated by dividing the longitudinal variability of the Poincaré plot (``4*SD2``) by its transverse variability (``4*SD1``).

HRV_CSI : The Cardiac Sympathetic Index (Toichi, 1997) is a measure of cardiac sympathetic function independent of vagal activity, calculated by dividing the longitudinal variability of the Poincaré plot (``4*SD2``) by its transverse variability (``4*SD1``).

HRV_CVI : The Cardiac Vagal Index (Toichi, 1997) is an index of cardiac parasympathetic function (vagal activity unaffected by sympathetic activity), and is equal equal to the logarithm of the product of longitudinal (``4*SD2``) and transverse variability (``4*SD1``).

HRV_CVI : The Cardiac Vagal Index (Toichi, 1997) is an index of cardiac parasympathetic function (vagal activity unaffected by sympathetic activity), and is equal equal to the logarithm of the product of longitudinal (``4*SD2``) and transverse variability (``4*SD1``).

HRV_CSI_Modified : The modified CSI (Jeppesen, 2014) obtained by dividing the square of the longitudinal variability by its transverse variability.

HRV_CSI_Modified : The modified CSI (Jeppesen, 2014) obtained by dividing the square of the longitudinal variability by its transverse variability.

HRV_GI : Guzik’s Index, defined as the distance of points above line of identity (LI) to LI divided by the distance of all points in Poincaré plot to LI except those that are located on LI.

HRV_GI : Guzik’s Index, defined as the distance of points above line of identity (LI) to LI divided by the distance of all points in Poincaré plot to LI except those that are located on LI.

HRV_SI : Slope Index, defined as the phase angle of points above LI divided by the phase angle of all points in Poincaré plot except those that are located on LI.

HRV_SI : Slope Index, defined as the phase angle of points above LI divided by the phase angle of all points in Poincaré plot except those that are located on LI.

HRV_AI : Area Index, defined as the cumulative area of the sectors corresponding to the points that are located above LI divided by the cumulative area of sectors corresponding to all points in the Poincaré plot except those that are located on LI.

HRV_AI : Area Index, defined as the cumulative area of the sectors corresponding to the points that are located above LI divided by the cumulative area of sectors corresponding to all points in the Poincaré plot except those that are located on LI.

HRV_PI : Porta’s Index, defined as the number of points below LI divided by the total number of points in Poincaré plot except those that are located on LI.

HRV_PI : Porta’s Index, defined as the number of points below LI divided by the total number of points in Poincaré plot except those that are located on LI.

HRV_SD1a : Short-term variance of contributions of decelerations (prolongations of RR intervals), (Piskorski, 2011).

HRV_SD1a : Short-term variance of contributions of decelerations (prolongations of RR intervals), (Piskorski, 2011).

HRV_SD1d : Short-term variance of contributions of accelerations (shortenings of RR intervals), (Piskorski, 2011).

HRV_SD1d : Short-term variance of contributions of accelerations (shortenings of RR intervals), (Piskorski, 2011).

HRV_C1a : The contributions of heart rate accelerations to short-term HRV, (Piskorski, 2011).

HRV_C1a : The contributions of heart rate accelerations to short-term HRV, (Piskorski, 2011).

HRV_C1d : The contributions of heart rate decelerations to short-term HRV, (Piskorski, 2011).

HRV_C1d : The contributions of heart rate decelerations to short-term HRV, (Piskorski, 2011).

HRV_SD2a : Long-term variance of contributions of accelerations (shortenings of RR intervals), (Piskorski, 2011).

HRV_SD2a : Long-term variance of contributions of accelerations (shortenings of RR intervals), (Piskorski, 2011).

HRV_SD2d : Long-term variance of contributions of decelerations (prolongations of RR intervals), (Piskorski, 2011).

HRV_SD2d : Long-term variance of contributions of decelerations (prolongations of RR intervals), (Piskorski, 2011).

HRV_C2a : The contributions of heart rate accelerations to long-term HRV, (Piskorski, 2011).

HRV_C2a : The contributions of heart rate accelerations to long-term HRV, (Piskorski, 2011).

HRV_C2d : The contributions of heart rate decelerations to long-term HRV, (Piskorski, 2011).

HRV_C2d : The contributions of heart rate decelerations to long-term HRV, (Piskorski, 2011).

HRV_SDNNa : Total variance of contributions of accelerations (shortenings of RR intervals), (Piskorski, 2011).

HRV_SDNNa : Total variance of contributions of accelerations (shortenings of RR intervals), (Piskorski, 2011).

HRV_SDNNd : Total variance of contributions of decelerations (prolongations of RR intervals), (Piskorski, 2011).

HRV_SDNNd : Total variance of contributions of decelerations (prolongations of RR intervals), (Piskorski, 2011).

HRV_Ca : The total contributions of heart rate accelerations to HRV.

HRV_Ca : The total contributions of heart rate accelerations to HRV.

HRV_Cd : The total contributions of heart rate decelerations to HRV.

HRV_Cd : The total contributions of heart rate decelerations to HRV.

HRV_PIP : Percentage of inflection points of the RR intervals series.

HRV_PIP : Percentage of inflection points of the RR intervals series.

HRV_IALS : Inverse of the average length of the acceleration/deceleration segments.

HRV_IALS : Inverse of the average length of the acceleration/deceleration segments.

HRV_PSS : Fraction of RR differences in short acceleration/deceleration segments.

HRV_PSS : Fraction of RR differences in short acceleration/deceleration segments.

HRV_PAS : Percentage of NN intervals in alternation segments.

HRV_PAS : Percentage of NN intervals in alternation segments.

ecg_peaks , ppg_peaks , hrv_frequency , hrv_time , hrv_summary , hrv_symbolic , hrv_rqa

Pham, T., Lau, Z. J., Chen, S. H., & Makowski, D. (2021). Heart Rate Variability in
Psychology: A Review of HRV Indices and an Analysis Tutorial. Sensors, 21(12), 3998. https://doi.org/10.3390/s21123998

Pham, T., Lau, Z. J., Chen, S. H., & Makowski, D. (2021). Heart Rate Variability in
Psychology: A Review of HRV Indices and an Analysis Tutorial. Sensors, 21(12), 3998. https://doi.org/10.3390/s21123998

Yan, C., Li, P., Ji, L., Yao, L., Karmakar, C., & Liu, C. (2017). Area asymmetry of heart
rate variability signal. Biomedical engineering online, 16(1), 112.

Yan, C., Li, P., Ji, L., Yao, L., Karmakar, C., & Liu, C. (2017). Area asymmetry of heart
rate variability signal. Biomedical engineering online, 16(1), 112.

Ciccone, A. B., Siedlik, J. A., Wecht, J. M., Deckert, J. A., Nguyen, N. D., & Weir, J. P.      (2017). Reminder: RMSSD and SD1 are identical heart rate variability metrics. Muscle & nerve,
56 (4), 674-678.

Ciccone, A. B., Siedlik, J. A., Wecht, J. M., Deckert, J. A., Nguyen, N. D., & Weir, J. P.      (2017). Reminder: RMSSD and SD1 are identical heart rate variability metrics. Muscle & nerve,
56 (4), 674-678.

Shaffer, F., & Ginsberg, J. P. (2017). An overview of heart rate variability metrics and
norms. Frontiers in public health, 5, 258.

Shaffer, F., & Ginsberg, J. P. (2017). An overview of heart rate variability metrics and
norms. Frontiers in public health, 5, 258.

Costa, M. D., Davis, R. B., & Goldberger, A. L. (2017). Heart rate fragmentation: a new
approach to the analysis of cardiac interbeat interval dynamics. Front. Physiol. 8, 255.

Costa, M. D., Davis, R. B., & Goldberger, A. L. (2017). Heart rate fragmentation: a new
approach to the analysis of cardiac interbeat interval dynamics. Front. Physiol. 8, 255.

Jeppesen, J., Beniczky, S., Johansen, P., Sidenius, P., & Fuglsang-Frederiksen, A. (2014).
Using Lorenz plot and Cardiac Sympathetic Index of heart rate variability for detecting
seizures for patients with epilepsy. In 2014 36th Annual International Conference of the IEE
Engineering in Medicine and Biology Society (pp. 4563-4566). IEEE.

Jeppesen, J., Beniczky, S., Johansen, P., Sidenius, P., & Fuglsang-Frederiksen, A. (2014).
Using Lorenz plot and Cardiac Sympathetic Index of heart rate variability for detecting
seizures for patients with epilepsy. In 2014 36th Annual International Conference of the IEE
Engineering in Medicine and Biology Society (pp. 4563-4566). IEEE.

Piskorski, J., & Guzik, P. (2011). Asymmetric properties of long-term and total heart rate
variability. Medical & biological engineering & computing, 49(11), 1289-1297.

Piskorski, J., & Guzik, P. (2011). Asymmetric properties of long-term and total heart rate
variability. Medical & biological engineering & computing, 49(11), 1289-1297.

Stein, P. K. (2002). Assessing heart rate variability from real-world Holter reports. Cardiac
electrophysiology review, 6(3), 239-244.

Stein, P. K. (2002). Assessing heart rate variability from real-world Holter reports. Cardiac
electrophysiology review, 6(3), 239-244.

Brennan, M. et al. (2001). Do Existing Measures of Poincaré Plot Geometry Reflect Nonlinear
Features of Heart Rate Variability?. IEEE Transactions on Biomedical Engineering, 48(11),
1342-1347.

Brennan, M. et al. (2001). Do Existing Measures of Poincaré Plot Geometry Reflect Nonlinear
Features of Heart Rate Variability?. IEEE Transactions on Biomedical Engineering, 48(11),
1342-1347.

Toichi, M., Sugiura, T., Murai, T., & Sengoku, A. (1997). A new method of assessing cardiac
autonomic function and its comparison with spectral analysis and coefficient of variation of
R-R interval. Journal of the autonomic nervous system, 62(1-2), 79-84.

Toichi, M., Sugiura, T., Murai, T., & Sengoku, A. (1997). A new method of assessing cardiac
autonomic function and its comparison with spectral analysis and coefficient of variation of
R-R interval. Journal of the autonomic nervous system, 62(1-2), 79-84.

Acharya, R. U., Lim, C. M., & Joseph, P. (2002). Heart rate variability analysis using
correlation dimension and detrended fluctuation analysis. Itbm-Rbm, 23(6), 333-339.

Acharya, R. U., Lim, C. M., & Joseph, P. (2002). Heart rate variability analysis using
correlation dimension and detrended fluctuation analysis. Itbm-Rbm, 23(6), 333-339.

Cysarz, D., Porta, A., Montano, N., van Leeuwen, P., Kurths, J., & Wessel, N. (2013).
Quantifying heart rate dynamics using different approaches of symbolic dynamics. Eur. Phys.
J. Spec. Top. 222, 487–500. doi: 10.1140/epjst/e2013-01854-7

Cysarz, D., Porta, A., Montano, N., van Leeuwen, P., Kurths, J., & Wessel, N. (2013).
Quantifying heart rate dynamics using different approaches of symbolic dynamics. Eur. Phys.
J. Spec. Top. 222, 487–500. doi: 10.1140/epjst/e2013-01854-7

Porta, A., Tobaldini, E., Guzzetti, S., Furlan, R., Montano, N., & Gnecchi-Ruscone, T.
(2007). Assessment of cardiac autonomic modulation during graded head-up tilt by symbolic
analysis of heart rate variability. Am. J. Physiol. Heart Circ. Physiol. 293, H702–H708.
doi: 10.1152/ajpheart.00006.2007

Porta, A., Tobaldini, E., Guzzetti, S., Furlan, R., Montano, N., & Gnecchi-Ruscone, T.
(2007). Assessment of cardiac autonomic modulation during graded head-up tilt by symbolic
analysis of heart rate variability. Am. J. Physiol. Heart Circ. Physiol. 293, H702–H708.
doi: 10.1152/ajpheart.00006.2007

Respiratory sinus arrhythmia (RSA), also referred to as ‘cardiac coherence’ or ‘physiological
coherence’ (though these terms are often encompassing a wider meaning), is the naturally
occurring variation in heart rate during the breathing cycle. Metrics to quantify it are often
used as a measure of parasympathetic nervous system activity. Neurophysiology informs us that
the functional output of the myelinated vagus originating from the nucleus ambiguous has a
respiratory rhythm. Thus, there would a temporal relation between the respiratory rhythm being
expressed in the firing of these efferent pathways and the functional effect on the heart rate
rhythm manifested as RSA. Several methods exist to quantify RSA:

The Peak-to-trough (P2T) algorithm measures the statistical range in milliseconds of the
heart period oscillation associated with synchronous respiration. Operationally, subtracting
the shortest heart period during inspiration from the longest heart period during a breath
cycle produces an estimate of RSA during each breath. The peak-to-trough method makes no
statistical assumption or correction (e.g., adaptive filtering) regarding other sources of
variance in the heart period time series that may confound, distort, or interact with the
metric such as slower periodicities and baseline trend. Although it has been proposed that
the P2T method “acts as a time-domain filter dynamically centered at the exact ongoing
respiratory frequency” (Grossman, 1992), the method does not transform the time series in any
way, as a filtering process would. Instead the method uses knowledge of the ongoing
respiratory cycle to associate segments of the heart period time series with either
inhalation or exhalation (Lewis, 2012).

The Peak-to-trough (P2T) algorithm measures the statistical range in milliseconds of the
heart period oscillation associated with synchronous respiration. Operationally, subtracting
the shortest heart period during inspiration from the longest heart period during a breath
cycle produces an estimate of RSA during each breath. The peak-to-trough method makes no
statistical assumption or correction (e.g., adaptive filtering) regarding other sources of
variance in the heart period time series that may confound, distort, or interact with the
metric such as slower periodicities and baseline trend. Although it has been proposed that
the P2T method “acts as a time-domain filter dynamically centered at the exact ongoing
respiratory frequency” (Grossman, 1992), the method does not transform the time series in any
way, as a filtering process would. Instead the method uses knowledge of the ongoing
respiratory cycle to associate segments of the heart period time series with either
inhalation or exhalation (Lewis, 2012).

The Porges-Bohrer (PB) algorithm assumes that heart period time series reflect the sum of
several component time series. Each of these component time series may be mediated by
different neural mechanisms and may have different statistical features. The Porges-Bohrer
method applies an algorithm that selectively extracts RSA, even when the periodic process
representing RSA is superimposed on a complex baseline that may include aperiodic and slow
periodic processes. Since the method is designed to remove sources of variance in the heart
period time series other than the variance within the  frequency band of spontaneous
breathing, the method is capable of accurately quantifying RSA when the signal to noise ratio
is low.

The Porges-Bohrer (PB) algorithm assumes that heart period time series reflect the sum of
several component time series. Each of these component time series may be mediated by
different neural mechanisms and may have different statistical features. The Porges-Bohrer
method applies an algorithm that selectively extracts RSA, even when the periodic process
representing RSA is superimposed on a complex baseline that may include aperiodic and slow
periodic processes. Since the method is designed to remove sources of variance in the heart
period time series other than the variance within the  frequency band of spontaneous
breathing, the method is capable of accurately quantifying RSA when the signal to noise ratio
is low.

ecg_signals ( DataFrame ) – DataFrame obtained from ecg_process() . Should contain columns ECG_Rate and ECG_R_Peaks . Can also take a DataFrame comprising of both ECG and RSP signals,
generated by bio_process() .

ecg_signals ( DataFrame ) – DataFrame obtained from ecg_process() . Should contain columns ECG_Rate and ECG_R_Peaks . Can also take a DataFrame comprising of both ECG and RSP signals,
generated by bio_process() .

rsp_signals ( DataFrame ) – DataFrame obtained from rsp_process() . Should contain columns RSP_Phase and RSP_PhaseCompletion . No impact when a DataFrame comprising of both the ECG and RSP
signals are passed as ecg_signals . Defaults to None .

rsp_signals ( DataFrame ) – DataFrame obtained from rsp_process() . Should contain columns RSP_Phase and RSP_PhaseCompletion . No impact when a DataFrame comprising of both the ECG and RSP
signals are passed as ecg_signals . Defaults to None .

rpeaks ( dict ) – The samples at which the R-peaks of the ECG signal occur. Dict returned by ecg_peaks() , ecg_process() , or bio_process() . Defaults to None .

rpeaks ( dict ) – The samples at which the R-peaks of the ECG signal occur. Dict returned by ecg_peaks() , ecg_process() , or bio_process() . Defaults to None .

sampling_rate ( int ) – The sampling frequency of signals (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of signals (in Hz, i.e., samples/second).

continuous ( bool ) – If False , will return RSA properties computed from the data (one value per index).
If True , will return continuous estimations of RSA of the same length as the signal.
See below for more details.

continuous ( bool ) – If False , will return RSA properties computed from the data (one value per index).
If True , will return continuous estimations of RSA of the same length as the signal.
See below for more details.

window ( int ) – For calculating RSA second by second. Length of each segment in seconds. If None (default), window will be set at 32 seconds.

window ( int ) – For calculating RSA second by second. Length of each segment in seconds. If None (default), window will be set at 32 seconds.

window_number ( int ) – Between 2 and 8. For calculating RSA second by second. Number of windows to be
calculated in Peak Matched Multiple Window. If None (default), window_number will be
set at 8.

window_number ( int ) – Between 2 and 8. For calculating RSA second by second. Number of windows to be
calculated in Peak Matched Multiple Window. If None (default), window_number will be
set at 8.

rsa ( dict ) – A dictionary containing the RSA features, which includes: RSA_P2T_Values : The estimate of RSA during each breath cycle, produced by subtracting the shortest heart period (or RR interval) from the longest heart period in ms. RSA_P2T_Mean : The mean peak-to-trough across all cycles in ms. RSA_P2T_Mean_log : The logarithm of the mean of RSA estimates. RSA_P2T_SD : The standard deviation of all RSA estimates. RSA_P2T_NoRSA : The number of breath cycles from which RSA could not be calculated. RSA_PorgesBohrer : The Porges-Bohrer estimate of RSA, optimal when the signal to noise ratio is low, in ln(ms^2).

rsa ( dict ) – A dictionary containing the RSA features, which includes:

RSA_P2T_Values : The estimate of RSA during each breath cycle, produced by subtracting the shortest heart period (or RR interval) from the longest heart period in ms.

RSA_P2T_Values : The estimate of RSA during each breath cycle, produced by subtracting the shortest heart period (or RR interval) from the longest heart period in ms.

RSA_P2T_Mean : The mean peak-to-trough across all cycles in ms.

RSA_P2T_Mean : The mean peak-to-trough across all cycles in ms.

RSA_P2T_Mean_log : The logarithm of the mean of RSA estimates.

RSA_P2T_Mean_log : The logarithm of the mean of RSA estimates.

RSA_P2T_SD : The standard deviation of all RSA estimates.

RSA_P2T_SD : The standard deviation of all RSA estimates.

RSA_P2T_NoRSA : The number of breath cycles from which RSA could not be calculated.

RSA_P2T_NoRSA : The number of breath cycles from which RSA could not be calculated.

RSA_PorgesBohrer : The Porges-Bohrer estimate of RSA, optimal when the signal to noise ratio is low, in ln(ms^2).

RSA_PorgesBohrer : The Porges-Bohrer estimate of RSA, optimal when the signal to noise ratio is low, in ln(ms^2).

Servant, D., Logier, R., Mouster, Y., & Goudemand, M. (2009). La variabilité de la fréquence
cardiaque. Intérêts en psychiatrie. L’Encéphale, 35(5), 423-428.

Servant, D., Logier, R., Mouster, Y., & Goudemand, M. (2009). La variabilité de la fréquence
cardiaque. Intérêts en psychiatrie. L’Encéphale, 35(5), 423-428.

Lewis, G. F., Furman, S. A., McCool, M. F., & Porges, S. W. (2012). Statistical strategies to
quantify respiratory sinus arrhythmia: Are commonly used metrics equivalent?. Biological
psychology, 89(2), 349-364.

Lewis, G. F., Furman, S. A., McCool, M. F., & Porges, S. W. (2012). Statistical strategies to
quantify respiratory sinus arrhythmia: Are commonly used metrics equivalent?. Biological
psychology, 89(2), 349-364.

Zohar, A. H., Cloninger, C. R., & McCraty, R. (2013). Personality and heart rate variability:
exploring pathways from personality to cardiac coherence and health. Open Journal of Social
Sciences, 1(06), 32.

Zohar, A. H., Cloninger, C. R., & McCraty, R. (2013). Personality and heart rate variability:
exploring pathways from personality to cardiac coherence and health. Open Journal of Social
Sciences, 1(06), 32.

Recurrence Quantification Analysis (RQA) of Heart Rate Variability (HRV)

RQA is a type of complexity analysis used in non-linear dynamics (related to entropy and fractal
dimensions). See complexity_rqa() for more information.

peaks ( dict ) – Samples at which cardiac extrema (i.e., R-peaks, systolic peaks) occur.
Can be a list of indices or the output(s) of other functions such as ecg_peaks() , ppg_peaks() , ecg_process() or bio_process() .

peaks ( dict ) – Samples at which cardiac extrema (i.e., R-peaks, systolic peaks) occur.
Can be a list of indices or the output(s) of other functions such as ecg_peaks() , ppg_peaks() , ecg_process() or bio_process() .

sampling_rate ( int, optional ) – Sampling rate (Hz) of the continuous cardiac signal in which the peaks occur. Should be at
least twice as high as the highest frequency in vhf. By default 1000.

sampling_rate ( int, optional ) – Sampling rate (Hz) of the continuous cardiac signal in which the peaks occur. Should be at
least twice as high as the highest frequency in vhf. By default 1000.

delay ( int ) – See complexity_rqa() for more information.

delay ( int ) – See complexity_rqa() for more information.

dimension ( int ) – See complexity_rqa() for more information.

dimension ( int ) – See complexity_rqa() for more information.

tolerance ( float ) – See complexity_rqa() for more information. If "zimatore2021" , will be set to half
of the mean pairwise distance between points.

tolerance ( float ) – See complexity_rqa() for more information. If "zimatore2021" , will be set to half
of the mean pairwise distance between points.

show ( bool ) – See complexity_rqa() for more information.

show ( bool ) – See complexity_rqa() for more information.

**kwargs – Other arguments to be passed to complexity_rqa() .

**kwargs – Other arguments to be passed to complexity_rqa() .

Zimatore, G., Falcioni, L., Gallotta, M. C., Bonavolontà, V., Campanella, M., De Spirito, M.,
… & Baldari, C. (2021). Recurrence quantification analysis of heart rate variability to
detect both ventilatory thresholds. PloS one, 16(10), e0249504.

Zimatore, G., Falcioni, L., Gallotta, M. C., Bonavolontà, V., Campanella, M., De Spirito, M.,
… & Baldari, C. (2021). Recurrence quantification analysis of heart rate variability to
detect both ventilatory thresholds. PloS one, 16(10), e0249504.

Ding, H., Crozier, S., & Wilson, S. (2008). Optimization of Euclidean distance threshold in
the application of recurrence quantification analysis to heart rate variability studies.
Chaos, Solitons & Fractals, 38(5), 1457-1467.

Ding, H., Crozier, S., & Wilson, S. (2008). Optimization of Euclidean distance threshold in
the application of recurrence quantification analysis to heart rate variability studies.
Chaos, Solitons & Fractals, 38(5), 1457-1467.

Symbolic dynamics indices of Heart Rate Variability (HRV)

Computes symbolic dynamics HRV indices based on three quantization methods: equal-probability,
max-min, and sigma. R-R intervals are converted to symbol sequences, and consecutive 3-symbol
words are classified into four variation families:

0V : no variation — all three symbols equal.

0V : no variation — all three symbols equal.

1V : one variation — exactly one adjacent pair differs.

1V : one variation — exactly one adjacent pair differs.

2LV : two like variations — all three differ and monotone (rising or falling).

2LV : two like variations — all three differ and monotone (rising or falling).

2UV : two unlike variations — all three differ and non-monotone (peak or valley, including
patterns like [a, b, a]).

2UV : two unlike variations — all three differ and non-monotone (peak or valley, including
patterns like [a, b, a]).

Symbolic dynamics indices were developed to address limitations of both time-domain and
frequency-domain HRV methods, which assume stationarity and perform poorly on short or noisy
recordings. By coarse-graining the RR interval series into discrete symbols, the approach
captures nonlinear and non-stationary dynamics that linear methods miss, while remaining
computationally simple and interpretable. The variation families have clear physiological
correlates: 0V patterns (no variation) increase with sympathetic dominance, while 2V patterns
(high variation) increase with parasympathetic activity, a dissociation validated against
pharmacological autonomic blockade and head-up tilt protocols. Importantly, symbolic indices
track autonomic modulation even in short recordings of a few minutes where spectral LF/HF
ratios become unreliable. Proposed clinical and applied uses include monitoring autonomic
changes during postural stress, exercise, and sleep, assessing cardiac autonomic neuropathy,
and as a complement to entropy-based nonlinear indices. The three quantization methods
(equal-probability, max-min, sigma) differ in their sensitivity to distributional properties
of the RR series; equal-probability quantization has been generally recommended when comparing
across individuals or conditions, as it is invariant to the marginal distribution of RR
intervals.

The following parameterizations have been used in the literature:

quantization_level_equal_prob=(4,) is the most common choice and is recommended for
cross-subject comparisons due to its invariance to the RR interval distribution (Cysarz et
al., 2018).

quantization_level_equal_prob=(4,) is the most common choice and is recommended for
cross-subject comparisons due to its invariance to the RR interval distribution (Cysarz et
al., 2018).

quantization_level_equal_prob=(4, 6) together with quantization_level_max_min=(6,) and sigma_rate=(0.05,) allows direct comparison across all three quantization methods
at matched levels, as done in Cysarz et al. (2013).

quantization_level_equal_prob=(4, 6) together with quantization_level_max_min=(6,) and sigma_rate=(0.05,) allows direct comparison across all three quantization methods
at matched levels, as done in Cysarz et al. (2013).

The sigma method with sigma_rate=0.05 was used in the original autonomic blockade
validation work (Porta et al., 2007) and is the most physiologically interpreted variant,
with 0V linked to sympathetic and 2V to parasympathetic dominance.

The sigma method with sigma_rate=0.05 was used in the original autonomic blockade
validation work (Porta et al., 2007) and is the most physiologically interpreted variant,
with 0V linked to sympathetic and 2V to parasympathetic dominance.

quantization_level_max_min=(6,) should generally be avoided for cross-subject
comparisons as it is sensitive to outliers in the RR series.

quantization_level_max_min=(6,) should generally be avoided for cross-subject
comparisons as it is sensitive to outliers in the RR series.

peaks ( dict or list ) – Samples at which cardiac extrema (e.g., R-peaks) occur. Can be a list of indices or a
dict containing the keys RRI and RRI_Time .

peaks ( dict or list ) – Samples at which cardiac extrema (e.g., R-peaks) occur. Can be a list of indices or a
dict containing the keys RRI and RRI_Time .

sampling_rate ( int, optional ) – Sampling rate (Hz) of the continuous cardiac signal in which the peaks occur. Default 1000.

sampling_rate ( int, optional ) – Sampling rate (Hz) of the continuous cardiac signal in which the peaks occur. Default 1000.

quantization_level_equal_prob ( tuple of int, optional ) – Quantization levels for the equal-probability method. Default (4,) (the most commonly
reported variant). Pass e.g. (4, 6) to include additional levels.

quantization_level_equal_prob ( tuple of int, optional ) – Quantization levels for the equal-probability method. Default (4,) (the most commonly
reported variant). Pass e.g. (4, 6) to include additional levels.

quantization_level_max_min ( tuple of int, optional ) – Quantization levels for the max-min method. Default () (disabled). Pass e.g. (6,) to enable.

quantization_level_max_min ( tuple of int, optional ) – Quantization levels for the max-min method. Default () (disabled). Pass e.g. (6,) to enable.

sigma_rate ( tuple of float, optional ) – Sigma rates for the sigma method. Default () (disabled). Pass e.g. (0.05,) to
enable.

sigma_rate ( tuple of float, optional ) – Sigma rates for the sigma method. Default () (disabled). Pass e.g. (0.05,) to
enable.

DataFrame – Contains the HRV symbolic dynamics indices. Column names follow the pattern HRV_SymDyn_{Method}{Level}_{Family} , e.g.: HRV_Symbolic_EqualProb4_0V / _1V / _2LV / _2UV (default) HRV_Symbolic_EqualProb6_0V / _1V / _2LV / _2UV (if level 6 requested) HRV_Symbolic_MaxMin6_0V / _1V / _2LV / _2UV (if max-min enabled) HRV_Symbolic_Sigma05_0V / _1V / _2LV / _2UV (if sigma enabled; 05 = rate × 100)

DataFrame – Contains the HRV symbolic dynamics indices. Column names follow the pattern HRV_SymDyn_{Method}{Level}_{Family} , e.g.:

HRV_Symbolic_EqualProb4_0V / _1V / _2LV / _2UV (default)

HRV_Symbolic_EqualProb4_0V / _1V / _2LV / _2UV (default)

HRV_Symbolic_EqualProb6_0V / _1V / _2LV / _2UV (if level 6 requested)

HRV_Symbolic_EqualProb6_0V / _1V / _2LV / _2UV (if level 6 requested)

HRV_Symbolic_MaxMin6_0V / _1V / _2LV / _2UV (if max-min enabled)

HRV_Symbolic_MaxMin6_0V / _1V / _2LV / _2UV (if max-min enabled)

HRV_Symbolic_Sigma05_0V / _1V / _2LV / _2UV (if sigma enabled; 05 = rate × 100)

HRV_Symbolic_Sigma05_0V / _1V / _2LV / _2UV (if sigma enabled; 05 = rate × 100)

ecg_peaks , ppg_peaks , hrv_nonlinear , hrv_time , hrv_frequency , hrv_symbolic

Cysarz, D., Edelhäuser, F., Javorka, M., Montano, N., & Porta, A. (2018). On the relevance
of symbolizing heart rate variability by means of a percentile-based coarse graining approach.
Physiol. Meas. 39:105010. doi: 10.1088/1361-6579/aae302

Cysarz, D., Edelhäuser, F., Javorka, M., Montano, N., & Porta, A. (2018). On the relevance
of symbolizing heart rate variability by means of a percentile-based coarse graining approach.
Physiol. Meas. 39:105010. doi: 10.1088/1361-6579/aae302

Cysarz, D., Porta, A., Montano, N., van Leeuwen, P., Kurths, J., & Wessel, N. (2013).
Quantifying heart rate dynamics using different approaches of symbolic dynamics. Eur. Phys.
J. Spec. Top. 222, 487–500. doi: 10.1140/epjst/e2013-01854-7

Cysarz, D., Porta, A., Montano, N., van Leeuwen, P., Kurths, J., & Wessel, N. (2013).
Quantifying heart rate dynamics using different approaches of symbolic dynamics. Eur. Phys.
J. Spec. Top. 222, 487–500. doi: 10.1140/epjst/e2013-01854-7

Wessel, N., Malberg, H., Bauernschmitt, R., & Kurths, J. (2007). Nonlinear methods of
cardiovascular physics and their clinical applicability. Int. J. Bifurc. Chaos 17, 3325–3371.
doi: 10.1142/s0218127407019093

Wessel, N., Malberg, H., Bauernschmitt, R., & Kurths, J. (2007). Nonlinear methods of
cardiovascular physics and their clinical applicability. Int. J. Bifurc. Chaos 17, 3325–3371.
doi: 10.1142/s0218127407019093

Porta, A., Tobaldini, E., Guzzetti, S., Furlan, R., Montano, N., & Gnecchi-Ruscone, T.
(2007). Assessment of cardiac autonomic modulation during graded head-up tilt by symbolic
analysis of heart rate variability. Am. J. Physiol. Heart Circ. Physiol. 293, H702–H708.
doi: 10.1152/ajpheart.00006.2007

Porta, A., Tobaldini, E., Guzzetti, S., Furlan, R., Montano, N., & Gnecchi-Ruscone, T.
(2007). Assessment of cardiac autonomic modulation during graded head-up tilt by symbolic
analysis of heart rate variability. Am. J. Physiol. Heart Circ. Physiol. 293, H702–H708.
doi: 10.1152/ajpheart.00006.2007

intervals ( list or array ) – List or numpy array of intervals, in milliseconds.

intervals ( list or array ) – List or numpy array of intervals, in milliseconds.

intervals_time ( list or array, optional ) – List or numpy array of timestamps corresponding to intervals, in seconds.

intervals_time ( list or array, optional ) – List or numpy array of timestamps corresponding to intervals, in seconds.

interpolate ( bool, optional ) – Whether to interpolate the interval signal. The default is False.

interpolate ( bool, optional ) – Whether to interpolate the interval signal. The default is False.

interpolation_rate ( int, optional ) – Sampling rate (Hz) of the interpolated interbeat intervals. Should be at least twice as
high as the highest frequency in vhf. By default 100. To replicate Kubios defaults, set
to 4.

interpolation_rate ( int, optional ) – Sampling rate (Hz) of the interpolated interbeat intervals. Should be at least twice as
high as the highest frequency in vhf. By default 100. To replicate Kubios defaults, set
to 4.

detrend ( str ) – Can be one of "polynomial" (traditional detrending of a given order) or "tarvainen2002" to use the smoothness priors approach described by Tarvainen (2002)
(mostly used in HRV analyses as a lowpass filter to remove complex trends), "loess" for
LOESS smoothing trend removal or "locreg" for local linear regression (the ‘runline’ algorithm from chronux). By default None such that there is no detrending.

detrend ( str ) – Can be one of "polynomial" (traditional detrending of a given order) or "tarvainen2002" to use the smoothness priors approach described by Tarvainen (2002)
(mostly used in HRV analyses as a lowpass filter to remove complex trends), "loess" for
LOESS smoothing trend removal or "locreg" for local linear regression (the ‘runline’ algorithm from chronux). By default None such that there is no detrending.

**kwargs – Keyword arguments to be passed to signal_interpolate() .

**kwargs – Keyword arguments to be passed to signal_interpolate() .

np.ndarray – Preprocessed intervals, in milliseconds. np.ndarray – Preprocessed timestamps corresponding to intervals, in seconds. int – Sampling rate (Hz) of the interpolated interbeat intervals.

np.ndarray – Preprocessed intervals, in milliseconds.

np.ndarray – Preprocessed intervals, in milliseconds.

np.ndarray – Preprocessed timestamps corresponding to intervals, in seconds.

np.ndarray – Preprocessed timestamps corresponding to intervals, in seconds.

int – Sampling rate (Hz) of the interpolated interbeat intervals.

int – Sampling rate (Hz) of the interpolated interbeat intervals.

Example 1 : With interpolation and detrending
.. ipython:: python

import neurokit2 as nk
import matplotlib.pyplot as plt

# Download data
data = nk.data(“bio_resting_5min_100hz”)
sampling_rate = 100

# Clean signal and find peaks
ecg_cleaned = nk.ecg_clean(data[“ECG”], sampling_rate=100)
_, info = nk.ecg_peaks(ecg_cleaned, sampling_rate=100, correct_artifacts=True)
peaks = info[“ECG_R_Peaks”]

# Convert peaks to intervals
rri = np.diff(peaks) / sampling_rate * 1000
rri_time = np.array(peaks[1:]) / sampling_rate

# # Compute HRV indices
# @savefig p_intervals_process1.png scale=100%
# plt.figure()
# plt.plot(intervals_time, intervals, label=”Original intervals”)
# intervals, intervals_time = nk.intervals_process(rri,
#                                               intervals_time=rri_time,
#                                               interpolate=True,
#                                               interpolation_rate=100,
#                                               detrend=”tarvainen2002”)
# plt.plot(intervals_time, intervals, label=”Processed intervals”)
# plt.xlabel(“Time (seconds)”)
# plt.ylabel(“Interbeat intervals (milliseconds)”)
# @suppress
# plt.close()

Convenience function to convert intervals to peaks, such as from R-R intervals to R-peaks of an
ECG signal. This can be useful if you do not have raw peak indices and have only interval data
such as breath-to-breath (BBI) or rpeak-to-rpeak (RRI) intervals.

intervals ( list or array ) – List of intervals (by default in milliseconds).

intervals ( list or array ) – List of intervals (by default in milliseconds).

intervals_time ( list or array, optional ) – Optional list of timestamps corresponding to intervals, in seconds. If None (default), the
cumulative sum of the intervals is used.

intervals_time ( list or array, optional ) – Optional list of timestamps corresponding to intervals, in seconds. If None (default), the
cumulative sum of the intervals is used.

sampling_rate ( int, optional ) – Sampling rate (Hz) of the continuous signal in which the peaks occur.

sampling_rate ( int, optional ) – Sampling rate (Hz) of the continuous signal in which the peaks occur.

np.ndarray – An array of integer values indicating the peak indices,
with the first peak occurring at sample point 0.

Any function appearing below this point is not explicitly part of the documentation and should be added. Please open an issue if there is one.
