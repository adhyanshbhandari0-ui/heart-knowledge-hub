# signal.html#signal-decompose

**Source:** https://neuropsychology.github.io/NeuroKit/functions/signal.html

---

duration ( float ) – Desired length of duration (s).

duration ( float ) – Desired length of duration (s).

sampling_rate ( int ) – The desired sampling rate (in Hz, i.e., samples/second).

sampling_rate ( int ) – The desired sampling rate (in Hz, i.e., samples/second).

frequency ( float or list ) – Oscillatory frequency of the signal (in Hz, i.e., oscillations per second).

frequency ( float or list ) – Oscillatory frequency of the signal (in Hz, i.e., oscillations per second).

amplitude ( float or list ) – Amplitude of the oscillations.

amplitude ( float or list ) – Amplitude of the oscillations.

noise ( float ) – Noise level (amplitude of the laplace noise).

noise ( float ) – Noise level (amplitude of the laplace noise).

silent ( bool ) – If False (default), might print warnings if impossible frequencies are queried.

silent ( bool ) – If False (default), might print warnings if impossible frequencies are queried.

random_state ( None, int, numpy.random.RandomState or numpy.random.Generator ) – Seed for the random number generator. See for misc.check_random_state for further information.

random_state ( None, int, numpy.random.RandomState or numpy.random.Generator ) – Seed for the random number generator. See for misc.check_random_state for further information.

Filter a signal using different methods such as “butterworth”, “fir”, “savgol” or “powerline”
filters.

Apply a lowpass (if “highcut” frequency is provided), highpass (if “lowcut” frequency is
provided) or bandpass (if both are provided) filter to the signal.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

lowcut ( float ) – Lower cutoff frequency in Hz. The default is None .

lowcut ( float ) – Lower cutoff frequency in Hz. The default is None .

highcut ( float ) – Upper cutoff frequency in Hz. The default is None .

highcut ( float ) – Upper cutoff frequency in Hz. The default is None .

method ( str ) – Can be one of "butterworth" , "fir" , "bessel" , "chebyshevii" or "savgol" . Note that for
Butterworth and Chebyshev, the function uses the SOS method from scipy.signal.sosfiltfilt() ,
recommended for general purpose filtering. One can also specify "butterworth_ba" for a
more traditional and legacy method (often implemented in other software).

method ( str ) – Can be one of "butterworth" , "fir" , "bessel" , "chebyshevii" or "savgol" . Note that for
Butterworth and Chebyshev, the function uses the SOS method from scipy.signal.sosfiltfilt() ,
recommended for general purpose filtering. One can also specify "butterworth_ba" for a
more traditional and legacy method (often implemented in other software).

order ( int ) – Only used if method is "butterworth" , "chebyshevii" or "savgol" . Order of the filter (default
is 2).

order ( int ) – Only used if method is "butterworth" , "chebyshevii" or "savgol" . Order of the filter (default
is 2).

window_size ( int ) – Only used if method is "savgol" . The length of the filter window (i.e. the number of
coefficients). Must be an odd integer. If default, will be set to the sampling rate
divided by 10 (101 if the sampling rate is 1000 Hz).

window_size ( int ) – Only used if method is "savgol" . The length of the filter window (i.e. the number of
coefficients). Must be an odd integer. If default, will be set to the sampling rate
divided by 10 (101 if the sampling rate is 1000 Hz).

powerline ( int ) – Only used if method is "powerline" .
The powerline frequency (normally 50 Hz or 60Hz).

powerline ( int ) – Only used if method is "powerline" .
The powerline frequency (normally 50 Hz or 60Hz).

show ( bool ) – If True , plot the filtered signal as an overlay of the original.

show ( bool ) – If True , plot the filtered signal as an overlay of the original.

array – Vector containing the filtered signal.

signal ( Series ) – The indexed input signal ( pandas Dataframe.set_index() )

Resample a continuous signal to a different length or sampling rate

Up- or down-sample a signal. The user can specify either a desired length for the vector, or
input the original sampling rate and the desired sampling rate.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

desired_length ( int ) – The desired length of the signal.

desired_length ( int ) – The desired length of the signal.

sampling_rate ( int ) – The original sampling frequency (in Hz, i.e., samples/second).

sampling_rate ( int ) – The original sampling frequency (in Hz, i.e., samples/second).

desired_sampling_rate ( int ) – The desired (output) sampling frequency (in Hz, i.e., samples/second).

desired_sampling_rate ( int ) – The desired (output) sampling frequency (in Hz, i.e., samples/second).

method ( str ) – Can be "interpolation" (see scipy.ndimage.zoom() ), "numpy" for numpy’s
interpolation (see np.interp() ),``”pandas”`` for Pandas’ time series resampling, "poly" (see scipy.signal.resample_poly() ) or "FFT" (see scipy.signal.resample() ) for the Fourier method. "FFT" is the most accurate
(if the signal is periodic), but becomes exponentially slower as the signal length
increases. In contrast, "interpolation" is the fastest, followed by "numpy" , "poly" and "pandas" .

method ( str ) – Can be "interpolation" (see scipy.ndimage.zoom() ), "numpy" for numpy’s
interpolation (see np.interp() ),``”pandas”`` for Pandas’ time series resampling, "poly" (see scipy.signal.resample_poly() ) or "FFT" (see scipy.signal.resample() ) for the Fourier method. "FFT" is the most accurate
(if the signal is periodic), but becomes exponentially slower as the signal length
increases. In contrast, "interpolation" is the fastest, followed by "numpy" , "poly" and "pandas" .

array – Vector containing resampled signal values.

Fill missing values in a signal using specific methods.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

method ( str ) – The method to use to fill missing values. Can be one of "forward" , "backward" ,
or "both" . The default is "both" .

method ( str ) – The method to use to fill missing values. Can be one of "forward" , "backward" ,
or "both" . The default is "both" .

Convert a continuous signal into zeros and ones depending on a given threshold.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

method ( str ) – The algorithm used to discriminate between the two states. Can be one of "mixture" (default) or "threshold" . If "mixture" , will use a Gaussian Mixture Model to
categorize between the two states. If "threshold" , will consider as activated all
points which value is superior to the threshold.

method ( str ) – The algorithm used to discriminate between the two states. Can be one of "mixture" (default) or "threshold" . If "mixture" , will use a Gaussian Mixture Model to
categorize between the two states. If "threshold" , will consider as activated all
points which value is superior to the threshold.

threshold ( float ) – If method is "mixture" , then it corresponds to the minimum probability required to
be considered as activated (if "auto" , then 0.5). If method is "threshold" ,
then it corresponds to the minimum amplitude to detect as onset. If "auto" , takes the
value between the max and the min.

threshold ( float ) – If method is "mixture" , then it corresponds to the minimum probability required to
be considered as activated (if "auto" , then 0.5). If method is "threshold" ,
then it corresponds to the minimum amplitude to detect as onset. If "auto" , takes the
value between the max and the min.

list – A list or array depending on the type passed.

Signal decomposition into different sources using different methods, such as Empirical Mode
Decomposition (EMD) or Singular spectrum analysis (SSA)-based signal separation method.

The extracted components can then be recombined into meaningful sources using signal_recompose() .

signal ( Union[list, np.array, pd.Series] ) – Vector of values.

signal ( Union[list, np.array, pd.Series] ) – Vector of values.

method ( str ) – The decomposition method. Can be one of "emd" or "ssa" .

method ( str ) – The decomposition method. Can be one of "emd" or "ssa" .

n_components ( int ) – Number of components to extract. Only used for "ssa" method. If None , will default
to 50.

n_components ( int ) – Number of components to extract. Only used for "ssa" method. If None , will default
to 50.

**kwargs – Other arguments passed to other functions.

**kwargs – Other arguments passed to other functions.

Array – Components of the decomposed signal.

Combine signal sources after decomposition

Combine and reconstruct meaningful signal sources after signal decomposition.

components ( array ) – Array of components obtained via signal_decompose() .

components ( array ) – Array of components obtained via signal_decompose() .

method ( str ) – The decomposition method. Can be one of "wcorr" .

method ( str ) – The decomposition method. Can be one of "wcorr" .

threshold ( float ) – The threshold used to group components together.

threshold ( float ) – The threshold used to group components together.

keep_sd ( float ) – If a float is specified, will only keep the reconstructed components that are superior
or equal to that percentage of the max standard deviaiton (SD) of the components. For
instance, keep_sd=0.01 will remove all components with SD lower than 1% of the
max SD. This can be used to filter out noise.

keep_sd ( float ) – If a float is specified, will only keep the reconstructed components that are superior
or equal to that percentage of the max standard deviaiton (SD) of the components. For
instance, keep_sd=0.01 will remove all components with SD lower than 1% of the
max SD. This can be used to filter out noise.

**kwargs – Other arguments used to override, for instance metric="chebyshev" .

**kwargs – Other arguments used to override, for instance metric="chebyshev" .

Array – Components of the recomposed components.

Apply a baseline (order = 0), linear (order = 1), or polynomial (order > 1) detrending to the
signal (i.e., removing a general trend). One can also use other methods, such as smoothness
priors approach described by Tarvainen (2002) or LOESS regression, but these scale badly for
long signals.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

method ( str ) – Can be one of "polynomial" (default; traditional detrending of a given order) or "tarvainen2002" to use the smoothness priors approach described by Tarvainen (2002)
(mostly used in HRV analyses as a lowpass filter to remove complex trends), "loess" for
LOESS smoothing trend removal or "locreg" for local linear regression (the ‘runline’ algorithm from chronux).

method ( str ) – Can be one of "polynomial" (default; traditional detrending of a given order) or "tarvainen2002" to use the smoothness priors approach described by Tarvainen (2002)
(mostly used in HRV analyses as a lowpass filter to remove complex trends), "loess" for
LOESS smoothing trend removal or "locreg" for local linear regression (the ‘runline’ algorithm from chronux).

order ( int ) – Only used if method is "polynomial" . The order of the polynomial. 0, 1 or > 1 for a
baseline (‘constant detrend’, i.e., remove only the mean), linear (remove the linear trend)
or polynomial detrending, respectively. Can also be "auto" , in which case it will
attempt to find the optimal order to minimize the RMSE.

order ( int ) – Only used if method is "polynomial" . The order of the polynomial. 0, 1 or > 1 for a
baseline (‘constant detrend’, i.e., remove only the mean), linear (remove the linear trend)
or polynomial detrending, respectively. Can also be "auto" , in which case it will
attempt to find the optimal order to minimize the RMSE.

regularization ( int ) – Only used if method="tarvainen2002" . The regularization parameter (default to 500).

regularization ( int ) – Only used if method="tarvainen2002" . The regularization parameter (default to 500).

alpha ( float ) – Only used if method is “loess”. The parameter which controls the degree of smoothing.

alpha ( float ) – Only used if method is “loess”. The parameter which controls the degree of smoothing.

window ( float ) – Only used if method is “locreg”. The detrending window should correspond to the
1 divided by the desired low-frequency band to remove
( window = 1 / detrend_frequency )
For instance, to remove frequencies below 0.67Hz the window should be 1.5 ( 1 / 0.67 = 1.5 ).

window ( float ) – Only used if method is “locreg”. The detrending window should correspond to the
1 divided by the desired low-frequency band to remove
( window = 1 / detrend_frequency )
For instance, to remove frequencies below 0.67Hz the window should be 1.5 ( 1 / 0.67 = 1.5 ).

stepsize ( float ) – Only used if method is "locreg" .

stepsize ( float ) – Only used if method is "locreg" .

components ( list ) – Only used if method is "EMD" . What Intrinsic Mode Functions (IMFs) from EMD to
remove. By default, the last one.

components ( list ) – Only used if method is "EMD" . What Intrinsic Mode Functions (IMFs) from EMD to
remove. By default, the last one.

sampling_rate ( int, optional ) – Only used if method is “locreg”. Sampling rate (Hz) of the signal.
If not None, the stepsize and window arguments will be multiplied
by the sampling rate. By default 1000.

sampling_rate ( int, optional ) – Only used if method is “locreg”. Sampling rate (Hz) of the signal.
If not None, the stepsize and window arguments will be multiplied
by the sampling rate. By default 1000.

array – Vector containing the detrended signal.

signal_filter , fit_loess , signal_decompose

Tarvainen, M. P., Ranta-Aho, P. O., & Karjalainen, P. A. (2002). An advanced detrending
method with application to HRV analysis. IEEE Transactions on Biomedical Engineering, 49(2),
172-175

Tarvainen, M. P., Ranta-Aho, P. O., & Karjalainen, P. A. (2002). An advanced detrending
method with application to HRV analysis. IEEE Transactions on Biomedical Engineering, 49(2),
172-175

Add noise of a given frequency, amplitude and shape to a signal.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

noise_shape ( str ) – The shape of the noise. Can be one of "laplace" (default) or "gaussian" .

noise_shape ( str ) – The shape of the noise. Can be one of "laplace" (default) or "gaussian" .

noise_amplitude ( float ) – The amplitude of the noise (the scale of the random function, relative
to the standard deviation of the signal).

noise_amplitude ( float ) – The amplitude of the noise (the scale of the random function, relative
to the standard deviation of the signal).

noise_frequency ( float ) – The frequency of the noise (in Hz, i.e., samples/second).

noise_frequency ( float ) – The frequency of the noise (in Hz, i.e., samples/second).

powerline_amplitude ( float ) – The amplitude of the powerline noise (relative to the standard
deviation of the signal).

powerline_amplitude ( float ) – The amplitude of the powerline noise (relative to the standard
deviation of the signal).

powerline_frequency ( float ) – The frequency of the powerline noise (in Hz, i.e., samples/second).

powerline_frequency ( float ) – The frequency of the powerline noise (in Hz, i.e., samples/second).

artifacts_amplitude ( float ) – The amplitude of the artifacts (relative to the standard deviation of
the signal).

artifacts_amplitude ( float ) – The amplitude of the artifacts (relative to the standard deviation of
the signal).

artifacts_frequency ( int ) – The frequency of the artifacts (in Hz, i.e., samples/second).

artifacts_frequency ( int ) – The frequency of the artifacts (in Hz, i.e., samples/second).

artifacts_number ( int ) – The number of artifact bursts. The bursts have a random duration
between 1 and 10% of the signal duration.

artifacts_number ( int ) – The number of artifact bursts. The bursts have a random duration
between 1 and 10% of the signal duration.

linear_drift ( bool ) – Whether or not to add linear drift to the signal.

linear_drift ( bool ) – Whether or not to add linear drift to the signal.

random_state ( None, int, numpy.random.RandomState or numpy.random.Generator ) – Seed for the random number generator. See for misc.check_random_state for further information.

random_state ( None, int, numpy.random.RandomState or numpy.random.Generator ) – Seed for the random number generator. See for misc.check_random_state for further information.

silent ( bool ) – Whether or not to display warning messages.

silent ( bool ) – Whether or not to display warning messages.

array – Vector containing the distorted signal.

Return the Flatline Percentage of the Signal

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

threshold ( float, optional ) – Flatline threshold relative to the biggest change in the signal.
This is the percentage of the maximum value of absolute consecutive
differences.

threshold ( float, optional ) – Flatline threshold relative to the biggest change in the signal.
This is the percentage of the maximum value of absolute consecutive
differences.

float – Percentage of signal where the absolute value of the derivative is lower then the threshold.

Interpolate a signal using different methods.

x_values ( Union[list, np.array, pd.Series] ) – The samples corresponding to the values to be interpolated.

x_values ( Union[list, np.array, pd.Series] ) – The samples corresponding to the values to be interpolated.

y_values ( Union[list, np.array, pd.Series] ) – The values to be interpolated. If not provided, any NaNs in the x_values
will be interpolated with _signal_interpolate_nan() ,
considering the x_values as equally spaced.

y_values ( Union[list, np.array, pd.Series] ) – The values to be interpolated. If not provided, any NaNs in the x_values
will be interpolated with _signal_interpolate_nan() ,
considering the x_values as equally spaced.

x_new ( Union[list, np.array, pd.Series] or int ) – The samples at which to interpolate the y_values. Samples before the first value in x_values
or after the last value in x_values will be extrapolated. If an integer is passed, nex_x
will be considered as the desired length of the interpolated signal between the first and
the last values of x_values. No extrapolation will be done for values before or after the
first and the last values of x_values.

x_new ( Union[list, np.array, pd.Series] or int ) – The samples at which to interpolate the y_values. Samples before the first value in x_values
or after the last value in x_values will be extrapolated. If an integer is passed, nex_x
will be considered as the desired length of the interpolated signal between the first and
the last values of x_values. No extrapolation will be done for values before or after the
first and the last values of x_values.

method ( str ) – Method of interpolation. Can be "linear" , "nearest" , "zero" , "slinear" , "quadratic" , "cubic" , "previous" , "next" , "monotone_cubic" , or "akima" .
The methods "zero" , "slinear" , "quadratic" and "cubic" refer to a spline
interpolation of zeroth, first, second or third order; whereas "previous" and "next" simply return the previous or next value of the point. An integer specifying the
order of the spline interpolator to use.
See monotone cubic method for details on the "monotone_cubic" method.
See akima method for details on the "akima" method.

method ( str ) – Method of interpolation. Can be "linear" , "nearest" , "zero" , "slinear" , "quadratic" , "cubic" , "previous" , "next" , "monotone_cubic" , or "akima" .
The methods "zero" , "slinear" , "quadratic" and "cubic" refer to a spline
interpolation of zeroth, first, second or third order; whereas "previous" and "next" simply return the previous or next value of the point. An integer specifying the
order of the spline interpolator to use.
See monotone cubic method for details on the "monotone_cubic" method.
See akima method for details on the "akima" method.

fill_value ( float or tuple or str ) – If a ndarray (or float), this value will be used to fill in for
requested points outside of the data range.
If a two-element tuple, then the first element is used as a fill value
for x_new < x[0] and the second element is used for x_new > x[-1].
If “extrapolate”, then points outside the data range will be extrapolated.
If not provided, then the default is ([y_values[0]], [y_values[-1]]).

fill_value ( float or tuple or str ) – If a ndarray (or float), this value will be used to fill in for
requested points outside of the data range.
If a two-element tuple, then the first element is used as a fill value
for x_new < x[0] and the second element is used for x_new > x[-1].
If “extrapolate”, then points outside the data range will be extrapolated.
If not provided, then the default is ([y_values[0]], [y_values[-1]]).

Arbitrary addition of two signals with different time ranges

signal1 ( Union[list, np.array, pd.Series] ) – The first signal (i.e., a time series)s in the form of a vector of values.

signal1 ( Union[list, np.array, pd.Series] ) – The first signal (i.e., a time series)s in the form of a vector of values.

signal2 ( Union[list, np.array, pd.Series] ) – The second signal (i.e., a time series)s in the form of a vector of values.

signal2 ( Union[list, np.array, pd.Series] ) – The second signal (i.e., a time series)s in the form of a vector of values.

time1 ( list ) – Lists containing two numeric values corresponding to the beginning and end of signal1 .

time1 ( list ) – Lists containing two numeric values corresponding to the beginning and end of signal1 .

time2 ( list ) – Same as above, but for signal2 .

time2 ( list ) – Same as above, but for signal2 .

array – Vector containing the sum of the two signals.

This function generates pure Gaussian (1/f)**beta noise. The power-spectrum of the generated
noise is proportional to S(f) = (1 / f)**beta . The following categories of noise have been
described:

duration ( float ) – Desired length of duration (s).

duration ( float ) – Desired length of duration (s).

sampling_rate ( int ) – The desired sampling rate (in Hz, i.e., samples/second).

sampling_rate ( int ) – The desired sampling rate (in Hz, i.e., samples/second).

random_state ( None, int, numpy.random.RandomState or numpy.random.Generator ) – Seed for the random number generator. See for misc.check_random_state for further information.

random_state ( None, int, numpy.random.RandomState or numpy.random.Generator ) – Seed for the random number generator. See for misc.check_random_state for further information.

noise ( array ) – The signal of pure noise.

Timmer, J., & Koenig, M. (1995). On generating power law noise. Astronomy and Astrophysics,
300, 707.

Timmer, J., & Koenig, M. (1995). On generating power law noise. Astronomy and Astrophysics,
300, 707.

https://en.wikipedia.org/wiki/Colors_of_noise

https://en.wikipedia.org/wiki/Colors_of_noise

Generate a surrogate version of a signal. Different methods are available, such as:

random : Performs a random permutation of the signal value. This way, the signal
distribution is unaffected and the serial correlations are cancelled, yielding a whitened
signal with an distribution identical to that of the original.

random : Performs a random permutation of the signal value. This way, the signal
distribution is unaffected and the serial correlations are cancelled, yielding a whitened
signal with an distribution identical to that of the original.

IAAFT : Returns an Iterative Amplitude Adjusted Fourier Transform (IAAFT) surrogate.
It is a phase randomized, amplitude adjusted surrogates that have the same power spectrum
(to a very high accuracy) and distribution as the original data, using an iterative scheme.

IAAFT : Returns an Iterative Amplitude Adjusted Fourier Transform (IAAFT) surrogate.
It is a phase randomized, amplitude adjusted surrogates that have the same power spectrum
(to a very high accuracy) and distribution as the original data, using an iterative scheme.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

method ( str ) – Can be "random" or "IAAFT" .

method ( str ) – Can be "random" or "IAAFT" .

random_state ( None, int, numpy.random.RandomState or numpy.random.Generator ) – Seed for the random number generator. See for misc.check_random_state for further information.

random_state ( None, int, numpy.random.RandomState or numpy.random.Generator ) – Seed for the random number generator. See for misc.check_random_state for further information.

**kwargs – Other keywords arguments, such as max_iter (by default 1000).

**kwargs – Other keywords arguments, such as max_iter (by default 1000).

Create surrogates using different methods.

As we can see, the signal pattern is destroyed by random surrogates, but not in the IAAFT one.
And their distributions are identical:

However, the power spectrum of the IAAFT surrogate is preserved.

Schreiber, T., & Schmitz, A. (1996). Improved surrogate data for nonlinearity tests. Physical
review letters, 77(4), 635.

Schreiber, T., & Schmitz, A. (1996). Improved surrogate data for nonlinearity tests. Physical
review letters, 77(4), 635.

Locate peaks (local maxima) in a signal and their related characteristics, such as height
(prominence), width and distance with other peaks.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

height_min ( float ) – The minimum height (i.e., amplitude in terms of absolute values). For example, height_min=20 will remove all peaks which height is smaller or equal to 20 (in the
provided signal’s values).

height_min ( float ) – The minimum height (i.e., amplitude in terms of absolute values). For example, height_min=20 will remove all peaks which height is smaller or equal to 20 (in the
provided signal’s values).

height_max ( float ) – The maximum height (i.e., amplitude in terms of absolute values).

height_max ( float ) – The maximum height (i.e., amplitude in terms of absolute values).

relative_height_min ( float ) – The minimum height (i.e., amplitude) relative to the sample (see below). For example, relative_height_min=-2.96 will remove all peaks which height lies below 2.96 standard
deviations from the mean of the heights.

relative_height_min ( float ) – The minimum height (i.e., amplitude) relative to the sample (see below). For example, relative_height_min=-2.96 will remove all peaks which height lies below 2.96 standard
deviations from the mean of the heights.

relative_height_max ( float ) – The maximum height (i.e., amplitude) relative to the sample (see below).

relative_height_max ( float ) – The maximum height (i.e., amplitude) relative to the sample (see below).

relative_mean ( bool ) – If a relative threshold is specified, how should it be computed (i.e., relative to what?). relative_mean=True will use Z-scores.

relative_mean ( bool ) – If a relative threshold is specified, how should it be computed (i.e., relative to what?). relative_mean=True will use Z-scores.

relative_median ( bool ) – If a relative threshold is specified, how should it be computed (i.e., relative to what?).
Relative to median uses a more robust form of standardization (see standardize() ).

relative_median ( bool ) – If a relative threshold is specified, how should it be computed (i.e., relative to what?).
Relative to median uses a more robust form of standardization (see standardize() ).

relative_max ( bool ) – If a relative threshold is specified, how should it be computed (i.e., relative to what?).
Relative to max will consider the maximum height as the reference.

relative_max ( bool ) – If a relative threshold is specified, how should it be computed (i.e., relative to what?).
Relative to max will consider the maximum height as the reference.

dict – Returns a dict itself containing 5 arrays: "Peaks" : contains the peaks indices (as relative to the given signal). For instance,
the value 3 means that the third data point of the signal is a peak. "Distance" : contains, for each peak, the closest distance with another peak. Note
that these values will be recomputed after filtering to match the selected peaks. "Height" : contains the prominence of each peak.
See scipy.signal.peak_prominences() . "Width" : contains the width of each peak. See scipy.signal.peak_widths() . "Onset" : contains the onset, start (or left trough), of each peak. "Offset" : contains the offset, end (or right trough), of each peak.

Returns a dict itself containing 5 arrays:

"Peaks" : contains the peaks indices (as relative to the given signal). For instance,
the value 3 means that the third data point of the signal is a peak.

"Peaks" : contains the peaks indices (as relative to the given signal). For instance,
the value 3 means that the third data point of the signal is a peak.

"Distance" : contains, for each peak, the closest distance with another peak. Note
that these values will be recomputed after filtering to match the selected peaks.

"Distance" : contains, for each peak, the closest distance with another peak. Note
that these values will be recomputed after filtering to match the selected peaks.

"Height" : contains the prominence of each peak.
See scipy.signal.peak_prominences() .

"Height" : contains the prominence of each peak.
See scipy.signal.peak_prominences() .

"Width" : contains the width of each peak. See scipy.signal.peak_widths() .

"Width" : contains the width of each peak. See scipy.signal.peak_widths() .

"Onset" : contains the onset, start (or left trough), of each peak.

"Onset" : contains the onset, start (or left trough), of each peak.

"Offset" : contains the offset, end (or right trough), of each peak.

"Offset" : contains the offset, end (or right trough), of each peak.

Identify and correct erroneous peak placements based on outliers in peak-to-peak differences
(period).

peaks ( list or array or DataFrame or Series or dict ) – The samples at which the peaks occur. If an array is passed in, it is assumed that it was
obtained with signal_findpeaks() . If a DataFrame is passed in, it is assumed to be
obtained with ecg_findpeaks() or ppg_findpeaks() and to be of the same length
as the input signal.

peaks ( list or array or DataFrame or Series or dict ) – The samples at which the peaks occur. If an array is passed in, it is assumed that it was
obtained with signal_findpeaks() . If a DataFrame is passed in, it is assumed to be
obtained with ecg_findpeaks() or ppg_findpeaks() and to be of the same length
as the input signal.

sampling_rate ( int ) – The sampling frequency of the signal that contains the peaks (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of the signal that contains the peaks (in Hz, i.e., samples/second).

iterative ( bool ) – Whether or not to apply the artifact correction repeatedly (results in superior artifact
correction).

iterative ( bool ) – Whether or not to apply the artifact correction repeatedly (results in superior artifact
correction).

show ( bool ) – Whether or not to visualize artifacts and artifact thresholds.

show ( bool ) – Whether or not to visualize artifacts and artifact thresholds.

interval_min ( float ) – Only when method = "neurokit" . The minimum interval between the peaks (in seconds).

interval_min ( float ) – Only when method = "neurokit" . The minimum interval between the peaks (in seconds).

interval_max ( float ) – Only when method = "neurokit" . The maximum interval between the peaks (in seconds).

interval_max ( float ) – Only when method = "neurokit" . The maximum interval between the peaks (in seconds).

relative_interval_min ( float ) – Only when method = "neurokit" . The minimum interval between the peaks as relative to
the sample (expressed in standard deviation from the mean).

relative_interval_min ( float ) – Only when method = "neurokit" . The minimum interval between the peaks as relative to
the sample (expressed in standard deviation from the mean).

relative_interval_max ( float ) – Only when method = "neurokit" . The maximum interval between the peaks as relative to
the sample (expressed in standard deviation from the mean).

relative_interval_max ( float ) – Only when method = "neurokit" . The maximum interval between the peaks as relative to
the sample (expressed in standard deviation from the mean).

robust ( bool ) – Only when method = "neurokit" . Use a robust method of standardization (see standardize() ) for the relative thresholds.

robust ( bool ) – Only when method = "neurokit" . Use a robust method of standardization (see standardize() ) for the relative thresholds.

method ( str ) – Either "Kubios" or "neurokit" . "Kubios" uses the artifact detection and
correction described in Lipponen, J. A., & Tarvainen, M. P. (2019). Note that "Kubios" is only meant for peaks in ECG or PPG. "neurokit" can be used with peaks in ECG, PPG,
or respiratory data.

method ( str ) – Either "Kubios" or "neurokit" . "Kubios" uses the artifact detection and
correction described in Lipponen, J. A., & Tarvainen, M. P. (2019). Note that "Kubios" is only meant for peaks in ECG or PPG. "neurokit" can be used with peaks in ECG, PPG,
or respiratory data.

peaks_clean ( array ) – The corrected peak locations. artifacts ( dict ) – Only if method="Kubios" . A dictionary containing the indices of artifacts, accessible
with the keys "ectopic" , "missed" , "extra" , and "longshort" .

peaks_clean ( array ) – The corrected peak locations.

peaks_clean ( array ) – The corrected peak locations.

artifacts ( dict ) – Only if method="Kubios" . A dictionary containing the indices of artifacts, accessible
with the keys "ectopic" , "missed" , "extra" , and "longshort" .

artifacts ( dict ) – Only if method="Kubios" . A dictionary containing the indices of artifacts, accessible
with the keys "ectopic" , "missed" , "extra" , and "longshort" .

signal_findpeaks , ecg_findpeaks , ecg_peaks , ppg_findpeaks , ppg_peaks

Lipponen, J. A., & Tarvainen, M. P. (2019). A robust algorithm for heart rate variability time
series artefact correction using novel beat classification. Journal of medical engineering &
technology, 43(3), 173-181. 10.1080/03091902.2019.1640306

Lipponen, J. A., & Tarvainen, M. P. (2019). A robust algorithm for heart rate variability time
series artefact correction using novel beat classification. Journal of medical engineering &
technology, 43(3), 173-181. 10.1080/03091902.2019.1640306

signal ( Union[list, np.array, pd.Series] ) – Vector of values.

signal ( Union[list, np.array, pd.Series] ) – Vector of values.

lag ( int ) – Time lag. If specified, one value of autocorrelation between signal with its lag self will
be returned.

lag ( int ) – Time lag. If specified, one value of autocorrelation between signal with its lag self will
be returned.

demean ( bool ) – If True , the mean of the signal will be subtracted from the signal before ACF
computation.

demean ( bool ) – If True , the mean of the signal will be subtracted from the signal before ACF
computation.

method ( str ) – Using "auto" runs scipy.signal.correlate to determine the faster algorithm. Other
methods are kept for legacy reasons, but are not recommended. Other methods include "correlation" (using np.correlate() ) or "fft" (Fast Fourier Transform).

method ( str ) – Using "auto" runs scipy.signal.correlate to determine the faster algorithm. Other
methods are kept for legacy reasons, but are not recommended. Other methods include "correlation" (using np.correlate() ) or "fft" (Fast Fourier Transform).

show ( bool ) – If True , plot the autocorrelation at all values of lag.

show ( bool ) – If True , plot the autocorrelation at all values of lag.

r ( float ) – The cross-correlation of the signal with itself at different time lags. Minimum time lag is
0, maximum time lag is the length of the signal. Or a correlation value at a specific lag
if lag is not None . info ( dict ) – A dictionary containing additional information, such as the confidence interval.

r ( float ) – The cross-correlation of the signal with itself at different time lags. Minimum time lag is
0, maximum time lag is the length of the signal. Or a correlation value at a specific lag
if lag is not None .

r ( float ) – The cross-correlation of the signal with itself at different time lags. Minimum time lag is
0, maximum time lag is the length of the signal. Or a correlation value at a specific lag
if lag is not None .

info ( dict ) – A dictionary containing additional information, such as the confidence interval.

info ( dict ) – A dictionary containing additional information, such as the confidence interval.

Only the PELT method is implemented for now.

signal ( Union[list, np.array, pd.Series] ) – Vector of values.

signal ( Union[list, np.array, pd.Series] ) – Vector of values.

change ( str ) – Can be one of "meanvar" (default), "mean" or "var" .

change ( str ) – Can be one of "meanvar" (default), "mean" or "var" .

penalty ( float ) – The algorithm penalty. Defaults to np.log(len(signal)) .

penalty ( float ) – The algorithm penalty. Defaults to np.log(len(signal)) .

Array – Values indicating the samples at which the changepoints occur. Fig – Figure of plot of signal with markers of changepoints.

Array – Values indicating the samples at which the changepoints occur.

Array – Values indicating the samples at which the changepoints occur.

Fig – Figure of plot of signal with markers of changepoints.

Fig – Figure of plot of signal with markers of changepoints.

Killick, R., Fearnhead, P., & Eckley, I. A. (2012). Optimal detection of changepoints with a
linear computational cost. Journal of the American Statistical Association, 107(500), 1590-1598.

Killick, R., Fearnhead, P., & Eckley, I. A. (2012). Optimal detection of changepoints with a
linear computational cost. Journal of the American Statistical Association, 107(500), 1590-1598.

Calculate signal period from a series of peaks

Calculate the period of a signal from a series of peaks. The period is defined as the time
in seconds between two consecutive peaks.

peaks ( Union[list, np.array, pd.DataFrame, pd.Series, dict] ) – The samples at which the peaks occur. If an array is passed in, it is assumed that it was
obtained with signal_findpeaks() . If a DataFrame is passed in, it is assumed it is
of the same length as the input signal in which occurrences of R-peaks are marked as “1”,
with such containers obtained with e.g., ecg_findpeaks() or rsp_findpeaks() .

peaks ( Union[list, np.array, pd.DataFrame, pd.Series, dict] ) – The samples at which the peaks occur. If an array is passed in, it is assumed that it was
obtained with signal_findpeaks() . If a DataFrame is passed in, it is assumed it is
of the same length as the input signal in which occurrences of R-peaks are marked as “1”,
with such containers obtained with e.g., ecg_findpeaks() or rsp_findpeaks() .

sampling_rate ( int ) – The sampling frequency of the signal that contains peaks (in Hz, i.e., samples/second).
Defaults to 1000.

sampling_rate ( int ) – The sampling frequency of the signal that contains peaks (in Hz, i.e., samples/second).
Defaults to 1000.

desired_length ( int ) – If left at the default None , the returned period will have the same number of elements
as peaks . If set to a value larger than the sample at which the last peak occurs in the
signal (i.e., peaks[-1] ), the returned period will be interpolated between peaks over desired_length samples. To interpolate the period over the entire duration of the
signal, set desired_length to the number of samples in the signal. Cannot be smaller
than or equal to the sample at which the last peak occurs in the signal.
Defaults to None .

desired_length ( int ) – If left at the default None , the returned period will have the same number of elements
as peaks . If set to a value larger than the sample at which the last peak occurs in the
signal (i.e., peaks[-1] ), the returned period will be interpolated between peaks over desired_length samples. To interpolate the period over the entire duration of the
signal, set desired_length to the number of samples in the signal. Cannot be smaller
than or equal to the sample at which the last peak occurs in the signal.
Defaults to None .

interpolation_method ( str ) – Method used to interpolate the rate between peaks. See signal_interpolate() . "monotone_cubic" is chosen as the default interpolation method since it ensures monotone
interpolation between data points (i.e., it prevents physiologically implausible
“overshoots” or “undershoots” in the y-direction). In contrast, the widely used cubic
spline interpolation does not ensure monotonicity.

interpolation_method ( str ) – Method used to interpolate the rate between peaks. See signal_interpolate() . "monotone_cubic" is chosen as the default interpolation method since it ensures monotone
interpolation between data points (i.e., it prevents physiologically implausible
“overshoots” or “undershoots” in the y-direction). In contrast, the widely used cubic
spline interpolation does not ensure monotonicity.

signal_findpeaks , signal_fixpeaks , signal_plot

The real phase has the property to rotate uniformly, leading to a uniform distribution density.
The prophase typically doesn’t fulfill this property. The following functions applies a
nonlinear transformation to the phase signal that makes its distribution exactly uniform. If a
binary vector is provided (containing 2 unique values), the function will compute the phase of
completion of each phase as denoted by each value.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

method ( str ) – The values in which the phase is expressed. Can be "radians" (default), "degrees" (for values between 0 and 360) or "percents" (for values between 0 and 1).

method ( str ) – The values in which the phase is expressed. Can be "radians" (default), "degrees" (for values between 0 and 360) or "percents" (for values between 0 and 1).

signal_filter , signal_zerocrossings , signal_findpeaks

array – A vector containing the phase of the signal, between 0 and 2*pi.

rsp = nk.rsp_simulate(duration=30)
phase = nk.signal_phase(rsp, method=”degrees”)
@savefig p_signal_phase2.png scale=100%
nk.signal_plot([rsp, phase])
@suppress
plt.close()

Plot signal with events as vertical lines

signal ( array or DataFrame ) – Signal array (can be a dataframe with many signals).

signal ( array or DataFrame ) – Signal array (can be a dataframe with many signals).

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second). Needs to be supplied if
the data should be plotted over time in seconds. Otherwise the data is plotted over samples.
Defaults to None .

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second). Needs to be supplied if
the data should be plotted over time in seconds. Otherwise the data is plotted over samples.
Defaults to None .

subplots ( bool ) – If True , each signal is plotted in a subplot.

subplots ( bool ) – If True , each signal is plotted in a subplot.

standardize ( bool ) – If True , all signals will have the same scale (useful for visualisation).

standardize ( bool ) – If True , all signals will have the same scale (useful for visualisation).

labels ( str or list ) – Defaults to None .

labels ( str or list ) – Defaults to None .

**kwargs ( optional ) – Arguments passed to matplotlib plotting.

**kwargs ( optional ) – Arguments passed to matplotlib plotting.

ecg_plot , rsp_plot , ppg_plot , emg_plot , eog_plot

Though the function returns nothing, the figure can be retrieved and saved as follows .. code-block:: console – # To be run after signal_plot()
fig = plt.gcf()
fig.savefig(“myfig.png”)

Though the function returns nothing, the figure can be retrieved and saved as follows

Though the function returns nothing, the figure can be retrieved and saved as follows

.. code-block:: console – # To be run after signal_plot()
fig = plt.gcf()
fig.savefig(“myfig.png”)

.. code-block:: console – # To be run after signal_plot()
fig = plt.gcf()
fig.savefig(“myfig.png”)

Compute the power of a signal in a given frequency band

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

frequency_band ( tuple or list ) – Tuple or list of tuples indicating the range of frequencies to compute the power in.

frequency_band ( tuple or list ) – Tuple or list of tuples indicating the range of frequencies to compute the power in.

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

continuous ( bool ) – Compute instant frequency, or continuous power.

continuous ( bool ) – Compute instant frequency, or continuous power.

show ( bool ) – If True , will return a Poincaré plot. Defaults to False .

show ( bool ) – If True , will return a Poincaré plot. Defaults to False .

normalize ( bool ) – Normalization of power by maximum PSD value. Default to True .
Normalization allows comparison between different PSD methods.

normalize ( bool ) – Normalization of power by maximum PSD value. Default to True .
Normalization allows comparison between different PSD methods.

**kwargs – Keyword arguments to be passed to signal_psd() .

**kwargs – Keyword arguments to be passed to signal_psd() .

pd.DataFrame – A DataFrame containing the Power Spectrum values and a plot if show is True .

# Continuous (simulated signal)
signal = np.concatenate((nk.ecg_simulate(duration=30, heart_rate=75), nk.ecg_simulate(duration=30, heart_rate=85)))
power = nk.signal_power(signal, frequency_band=[(72/60, 78/60), (82/60, 88/60)], continuous=True)
processed, _ = nk.ecg_process(signal)
power[“ECG_Rate”] = processed[“ECG_Rate”]

@savefig p_signal_power2.png scale=100%
nk.signal_plot(power, standardize=True)
@suppress
plt.close()

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

method ( str ) – Either "welch" (default), "fft" , "multitapers" (requires the ‘mne’ package), "lombscargle" (requires the ‘astropy’ package) or "burg" .

method ( str ) – Either "welch" (default), "fft" , "multitapers" (requires the ‘mne’ package), "lombscargle" (requires the ‘astropy’ package) or "burg" .

show ( bool ) – If True , will return a plot. If False , will return the density values that can be
plotted externally.

show ( bool ) – If True , will return a plot. If False , will return the density values that can be
plotted externally.

normalize ( bool ) – Normalization of power by maximum PSD value. Default to True .
Normalization allows comparison between different PSD methods.

normalize ( bool ) – Normalization of power by maximum PSD value. Default to True .
Normalization allows comparison between different PSD methods.

min_frequency ( str, float ) – The minimum frequency. If default, min_frequency is chosen based on the sampling rate and
length of signal to optimize the frequency resolution.

min_frequency ( str, float ) – The minimum frequency. If default, min_frequency is chosen based on the sampling rate and
length of signal to optimize the frequency resolution.

max_frequency ( float ) – The maximum frequency.

max_frequency ( float ) – The maximum frequency.

window ( int ) – Length of each window in seconds (for “Welch” method). If None (default), window will be
automatically calculated to capture at least 2 cycles of min_frequency. If the length of
recording does not allow the formal, window will be default to half of the length of
recording.

window ( int ) – Length of each window in seconds (for “Welch” method). If None (default), window will be
automatically calculated to capture at least 2 cycles of min_frequency. If the length of
recording does not allow the formal, window will be default to half of the length of
recording.

window_type ( str ) – Desired window to use. Defaults to "hann" . See scipy.signal.get_window() for list
of windows.

window_type ( str ) – Desired window to use. Defaults to "hann" . See scipy.signal.get_window() for list
of windows.

order ( int ) – The order of autoregression (only used for autoregressive (AR) methods such as "burg" ).

order ( int ) – The order of autoregression (only used for autoregressive (AR) methods such as "burg" ).

order_criteria ( str ) – The criteria to automatically select order in parametric PSD (only used for autoregressive
(AR) methods such as "burg" ).

order_criteria ( str ) – The criteria to automatically select order in parametric PSD (only used for autoregressive
(AR) methods such as "burg" ).

order_corrected ( bool ) – Should the order criteria (AIC or KIC) be corrected? If unsure which method to use to choose
the order, rely on the default (i.e., the corrected KIC).

order_corrected ( bool ) – Should the order criteria (AIC or KIC) be corrected? If unsure which method to use to choose
the order, rely on the default (i.e., the corrected KIC).

silent ( bool ) – If False , warnings will be printed. Default to True .

silent ( bool ) – If False , warnings will be printed. Default to True .

t ( array ) – The timestamps corresponding to each sample in the signal, in seconds
(for "lombscargle" method). Defaults to None.

t ( array ) – The timestamps corresponding to each sample in the signal, in seconds
(for "lombscargle" method). Defaults to None.

**kwargs ( optional ) – Keyword arguments to be passed to scipy.signal.welch() or np.fft.rfft() (when
method is ‘fft’, such as n , which determines the number of windows).

**kwargs ( optional ) – Keyword arguments to be passed to scipy.signal.welch() or np.fft.rfft() (when
method is ‘fft’, such as n , which determines the number of windows).

signal_filter , mne.time_frequency.psd_array_multitaper , scipy.signal.welch

data ( pd.DataFrame ) – A DataFrame containing the Power Spectrum values and a plot if show is True .

Calculate signal rate (per minute) from a series of peaks. It is a general function that works
for any series of peaks (i.e., not specific to a particular type of signal). It is computed as 60 / period , where the period is the time between the peaks (see func: .signal_period ).

This function is implemented under signal_rate() , but it also re-exported under
different names, such as ecg_rate() , or rsp_rate() . The
aliases are provided for consistency.

peaks ( Union[list, np.array, pd.DataFrame, pd.Series, dict] ) – The samples at which the peaks occur. If an array is passed in, it is assumed that it was
obtained with signal_findpeaks() . If a DataFrame is passed in, it is assumed it is
of the same length as the input signal in which occurrences of R-peaks are marked as “1”,
with such containers obtained with e.g., :func:.`ecg_findpeaks` or rsp_findpeaks() .

peaks ( Union[list, np.array, pd.DataFrame, pd.Series, dict] ) – The samples at which the peaks occur. If an array is passed in, it is assumed that it was
obtained with signal_findpeaks() . If a DataFrame is passed in, it is assumed it is
of the same length as the input signal in which occurrences of R-peaks are marked as “1”,
with such containers obtained with e.g., :func:.`ecg_findpeaks` or rsp_findpeaks() .

sampling_rate ( int ) – The sampling frequency of the signal that contains peaks (in Hz, i.e., samples/second).
Defaults to 1000.

sampling_rate ( int ) – The sampling frequency of the signal that contains peaks (in Hz, i.e., samples/second).
Defaults to 1000.

desired_length ( int ) – If left at the default None, the returned rated will have the same number of elements as peaks . If set to a value larger than the sample at which the last peak occurs in the
signal (i.e., peaks[-1] ), the returned rate will be interpolated between peaks over desired_length samples. To interpolate the rate over the entire duration of the signal,
set desired_length to the number of samples in the signal. Cannot be smaller than or
equal to the sample at which the last peak occurs in the signal. Defaults to None .

desired_length ( int ) – If left at the default None, the returned rated will have the same number of elements as peaks . If set to a value larger than the sample at which the last peak occurs in the
signal (i.e., peaks[-1] ), the returned rate will be interpolated between peaks over desired_length samples. To interpolate the rate over the entire duration of the signal,
set desired_length to the number of samples in the signal. Cannot be smaller than or
equal to the sample at which the last peak occurs in the signal. Defaults to None .

interpolation_method ( str ) –    Method used to interpolate the rate between peaks. See signal_interpolate() . "monotone_cubic" is chosen as the default interpolation method since it ensures monotone
interpolation between data points (i.e., it prevents physiologically implausible
“overshoots” or “undershoots” in the y-direction). In contrast, the widely used cubic
spline interpolation does not ensure monotonicity. show bool If True , shows a plot. Defaults to False .

"monotone_cubic" is chosen as the default interpolation method since it ensures monotone
interpolation between data points (i.e., it prevents physiologically implausible
“overshoots” or “undershoots” in the y-direction). In contrast, the widely used cubic
spline interpolation does not ensure monotonicity.

If True , shows a plot. Defaults to False .

array – A vector containing the rate (peaks per minute).

signal_period , signal_findpeaks , signal_fixpeaks , signal_plot

Signal smoothing can be achieved using either the convolution of a filter kernel with the input
signal to compute the smoothed signal (Smith, 1997) or a LOESS regression.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

method ( str ) – Can be one of "convolution" (default) or "loess" .

method ( str ) – Can be one of "convolution" (default) or "loess" .

kernel ( Union[str, np.array] ) – Only used if method is "convolution" . Type of kernel to use; if array, use directly
as the kernel. Can be one of "median" , "boxzen" , "boxcar" , "triang" , "blackman" , "hamming" , "hann" , "bartlett" , "flattop" , "parzen" , "bohman" , "blackmanharris" , "nuttall" , "barthann" , "kaiser" (needs beta), "gaussian" (needs std), "general_gaussian" (needs power
width), "slepian" (needs width) or "chebwin" (needs attenuation).

kernel ( Union[str, np.array] ) – Only used if method is "convolution" . Type of kernel to use; if array, use directly
as the kernel. Can be one of "median" , "boxzen" , "boxcar" , "triang" , "blackman" , "hamming" , "hann" , "bartlett" , "flattop" , "parzen" , "bohman" , "blackmanharris" , "nuttall" , "barthann" , "kaiser" (needs beta), "gaussian" (needs std), "general_gaussian" (needs power
width), "slepian" (needs width) or "chebwin" (needs attenuation).

size ( int ) – Only used if method is "convolution" . Size of the kernel; ignored if kernel is an
array.

size ( int ) – Only used if method is "convolution" . Size of the kernel; ignored if kernel is an
array.

alpha ( float ) – Only used if method is "loess" . The parameter which controls the degree of
smoothing.

alpha ( float ) – Only used if method is "loess" . The parameter which controls the degree of
smoothing.

Smith, S. W. (1997). The scientist and engineer’s guide to digital signal processing.

Smith, S. W. (1997). The scientist and engineer’s guide to digital signal processing.

Signal coherence refers to the strength of the mutual relationship (i.e., the amount of shared
information) between two signals. Synchrony is coherence “in phase” (two waveforms are “in
phase” when the peaks and troughs occur at the same time). Synchrony will always be coherent,
but coherence need not always be synchronous.

This function computes a continuous index of coupling between two signals either using the "hilbert" method to get the instantaneous phase synchrony, or using a rolling window
correlation.

The instantaneous phase synchrony measures the phase similarities between signals at each
timepoint. The phase refers to the angle of the signal, calculated through the hilbert
transform, when it is resonating between -pi to pi degrees. When two signals line up in phase
their angular difference becomes zero.

For less clean signals, windowed correlations are widely used because of their simplicity, and
can be a good a robust approximation of synchrony between two signals. The limitation is the
need to select a window size.

signal1 ( Union[list, np.array, pd.Series] ) – Time series in the form of a vector of values.

signal1 ( Union[list, np.array, pd.Series] ) – Time series in the form of a vector of values.

signal2 ( Union[list, np.array, pd.Series] ) – Time series in the form of a vector of values.

signal2 ( Union[list, np.array, pd.Series] ) – Time series in the form of a vector of values.

method ( str ) – The method to use. Can be one of "hilbert" or "correlation" .

method ( str ) – The method to use. Can be one of "hilbert" or "correlation" .

window_size ( int ) – Only used if method='correlation' . The number of samples to use for rolling correlation.

window_size ( int ) – Only used if method='correlation' . The number of samples to use for rolling correlation.

scipy.signal.hilbert , mutual_information

array – A vector containing the phase of the signal, between 0 and 2*pi.

http://jinhyuncheong.com/jekyll/update/2017/12/10/Timeseries_synchrony_tutorial_and_simulations.html

http://jinhyuncheong.com/jekyll/update/2017/12/10/Timeseries_synchrony_tutorial_and_simulations.html

Quantify changes of a nonstationary signal’s frequency over time The objective of time-frequency analysis is to offer a more informative description of the
signal which reveals the temporal variation of its frequency contents.

There are many different Time-Frequency Representations (TFRs) available:

Linear TFRs: efficient but create tradeoff between time and frequency resolution Short Time Fourier Transform (STFT): the time-domain signal is windowed into short
segments and FT is applied to each segment, mapping the signal into the TF plane. This
method assumes that the signal is quasi-stationary (stationary over the duration of the
window). The width of the window is the trade-off between good time (requires short
duration window) versus good frequency resolution (requires long duration windows) Wavelet Transform (WT): similar to STFT but instead of a fixed duration window function,
a varying window length by scaling the axis of the window is used. At low frequency, WT
proves high spectral resolution but poor temporal resolution. On the other hand, for high
frequencies, the WT provides high temporal resolution but poor spectral resolution. The
PyWavelet wavelet transform is used in NeuroKit and follows their naming convention of
wavelets. To adjust the wavelet type, add an underscore and the wavelet name to the
‘cwt’ method input. I.e., ‘cwt_cgau1’.

Linear TFRs: efficient but create tradeoff between time and frequency resolution

Short Time Fourier Transform (STFT): the time-domain signal is windowed into short
segments and FT is applied to each segment, mapping the signal into the TF plane. This
method assumes that the signal is quasi-stationary (stationary over the duration of the
window). The width of the window is the trade-off between good time (requires short
duration window) versus good frequency resolution (requires long duration windows)

Short Time Fourier Transform (STFT): the time-domain signal is windowed into short
segments and FT is applied to each segment, mapping the signal into the TF plane. This
method assumes that the signal is quasi-stationary (stationary over the duration of the
window). The width of the window is the trade-off between good time (requires short
duration window) versus good frequency resolution (requires long duration windows)

Wavelet Transform (WT): similar to STFT but instead of a fixed duration window function,
a varying window length by scaling the axis of the window is used. At low frequency, WT
proves high spectral resolution but poor temporal resolution. On the other hand, for high
frequencies, the WT provides high temporal resolution but poor spectral resolution. The
PyWavelet wavelet transform is used in NeuroKit and follows their naming convention of
wavelets. To adjust the wavelet type, add an underscore and the wavelet name to the
‘cwt’ method input. I.e., ‘cwt_cgau1’.

Wavelet Transform (WT): similar to STFT but instead of a fixed duration window function,
a varying window length by scaling the axis of the window is used. At low frequency, WT
proves high spectral resolution but poor temporal resolution. On the other hand, for high
frequencies, the WT provides high temporal resolution but poor spectral resolution. The
PyWavelet wavelet transform is used in NeuroKit and follows their naming convention of
wavelets. To adjust the wavelet type, add an underscore and the wavelet name to the
‘cwt’ method input. I.e., ‘cwt_cgau1’.

Quadratic TFRs: better resolution but computationally expensive and suffers from having
cross terms between multiple signal components Wigner Ville Distribution (WVD): while providing very good resolution in time and
frequency of the underlying signal structure, because of its bilinear nature, existence
of negative values, the WVD has misleading TF results in the case of multi-component
signals such as EEG due to the presence of cross terms and inference terms. Cross WVD
terms can be reduced by using smoothing kernel functions as well as analyzing the
analytic signal (instead of the original signal) Smoothed Pseudo Wigner Ville Distribution (SPWVD): to address the problem of cross-terms
suppression, SPWVD allows two independent analysis windows, one in time and the other in
frequency domains.

Quadratic TFRs: better resolution but computationally expensive and suffers from having
cross terms between multiple signal components

Wigner Ville Distribution (WVD): while providing very good resolution in time and
frequency of the underlying signal structure, because of its bilinear nature, existence
of negative values, the WVD has misleading TF results in the case of multi-component
signals such as EEG due to the presence of cross terms and inference terms. Cross WVD
terms can be reduced by using smoothing kernel functions as well as analyzing the
analytic signal (instead of the original signal)

Wigner Ville Distribution (WVD): while providing very good resolution in time and
frequency of the underlying signal structure, because of its bilinear nature, existence
of negative values, the WVD has misleading TF results in the case of multi-component
signals such as EEG due to the presence of cross terms and inference terms. Cross WVD
terms can be reduced by using smoothing kernel functions as well as analyzing the
analytic signal (instead of the original signal)

Smoothed Pseudo Wigner Ville Distribution (SPWVD): to address the problem of cross-terms
suppression, SPWVD allows two independent analysis windows, one in time and the other in
frequency domains.

Smoothed Pseudo Wigner Ville Distribution (SPWVD): to address the problem of cross-terms
suppression, SPWVD allows two independent analysis windows, one in time and the other in
frequency domains.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

method ( str ) – Time-Frequency decomposition method.

method ( str ) – Time-Frequency decomposition method.

min_frequency ( float ) – The minimum frequency.

min_frequency ( float ) – The minimum frequency.

max_frequency ( float ) – The maximum frequency.

max_frequency ( float ) – The maximum frequency.

window ( int ) – Length of each segment in seconds. If None (default), window will be automatically
calculated. For "STFT" method .

window ( int ) – Length of each segment in seconds. If None (default), window will be automatically
calculated. For "STFT" method .

window_type ( str ) – Type of window to create, defaults to "hann" . See scipy.signal.get_window() to
see full options of windows. For "STFT" method .

window_type ( str ) – Type of window to create, defaults to "hann" . See scipy.signal.get_window() to
see full options of windows. For "STFT" method .

mode ( str ) – Type of return values for "STFT" method . Can be "psd" , "complex" (default,
equivalent to output of "STFT" with no padding or boundary extension), "magnitude" , "angle" , "phase" . Defaults to "psd" .

mode ( str ) – Type of return values for "STFT" method . Can be "psd" , "complex" (default,
equivalent to output of "STFT" with no padding or boundary extension), "magnitude" , "angle" , "phase" . Defaults to "psd" .

nfreqbin ( int, float ) – Number of frequency bins. If None (default), nfreqbin will be set to 0.5*sampling_rate .

nfreqbin ( int, float ) – Number of frequency bins. If None (default), nfreqbin will be set to 0.5*sampling_rate .

overlap ( int ) – Number of points to overlap between segments. If None , noverlap = nperseg // 8 .
Defaults to None .

overlap ( int ) – Number of points to overlap between segments. If None , noverlap = nperseg // 8 .
Defaults to None .

analytical_signal ( bool ) – If True , analytical signal instead of actual signal is used in Wigner Ville
Distribution methods.

analytical_signal ( bool ) – If True , analytical signal instead of actual signal is used in Wigner Ville
Distribution methods.

show ( bool ) – If True , will return two PSD plots.

show ( bool ) – If True , will return two PSD plots.

frequency ( np.array ) – Frequency. time ( np.array ) – Time array. stft ( np.array ) – Short Term Fourier Transform. Time increases across its columns and frequency increases
down the rows.

stft ( np.array ) – Short Term Fourier Transform. Time increases across its columns and frequency increases
down the rows.

stft ( np.array ) – Short Term Fourier Transform. Time increases across its columns and frequency increases
down the rows.

Locate the indices where the signal crosses zero

Note that when the signal crosses zero between two points, the first index is returned.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) in the form of a vector of values.

direction ( str ) – Direction in which the signal crosses zero, can be "positive" , "negative" or "both" (default).

direction ( str ) – Direction in which the signal crosses zero, can be "positive" , "negative" or "both" (default).

array – Vector containing the indices of zero crossings.

Any function appearing below this point is not explicitly part of the documentation and should be added. Please open an issue if there is one.

Segment a signal (e.g. ECG, PPG, respiratory) into individual cycles (e.g. heartbeats, pulse waves, breaths).

signal_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned signal channel, such as that returned by ppg_clean() or ecg_clean() .

signal_cleaned ( Union[list, np.array, pd.Series] ) – The cleaned signal channel, such as that returned by ppg_clean() or ecg_clean() .

cycle_indices ( dict ) – The samples indicating individual cycles (such as PPG peaks or ECG R-peaks), such as a dict
returned by ppg_peaks() .

cycle_indices ( dict ) – The samples indicating individual cycles (such as PPG peaks or ECG R-peaks), such as a dict
returned by ppg_peaks() .

ratio_pre ( float ) – The proportion of the cycle window which takes place before the cycle index (e.g. the proportion of the
interbeat interval which takes place before the PPG pulse peak or ECG R peak).

ratio_pre ( float ) – The proportion of the cycle window which takes place before the cycle index (e.g. the proportion of the
interbeat interval which takes place before the PPG pulse peak or ECG R peak).

sampling_rate ( int ) – The sampling frequency of signal_cleaned (in Hz, i.e., samples/second). Defaults to 1000.

sampling_rate ( int ) – The sampling frequency of signal_cleaned (in Hz, i.e., samples/second). Defaults to 1000.

show ( bool ) – If True , will return a plot of cycles. Defaults to False . If “return”, returns
the axis of the plot.

show ( bool ) – If True , will return a plot of cycles. Defaults to False . If “return”, returns
the axis of the plot.

signal_name ( str ) – The name of the signal (only used for plotting).

signal_name ( str ) – The name of the signal (only used for plotting).

dict – A dict containing DataFrames for all segmented cycles. average_cycle_rate ( float ) – The average cycle rate (e.g. heart rate, respiratory rate) (in Hz, i.e., samples/second)

dict – A dict containing DataFrames for all segmented cycles.

dict – A dict containing DataFrames for all segmented cycles.

average_cycle_rate ( float ) – The average cycle rate (e.g. heart rate, respiratory rate) (in Hz, i.e., samples/second)

average_cycle_rate ( float ) – The average cycle rate (e.g. heart rate, respiratory rate) (in Hz, i.e., samples/second)

ppg_clean , ecg_clean , ppg_peaks , ecg_peaks , ppg_quality , ecg_quality

Transforms a peak-info dict to a signal of given length

Assess quality of signal using various metrics

Assess the quality of a quasi-periodic signal (e.g. PPG, ECG or RSP) using the specified method. You can pass an
unfiltered signal as an input, but typically a filtered signal (e.g. cleaned using ppg_clean() , ecg_clean() or rsp_clean() ) will result in more reliable results. The following methods are available:

The "templatematch" method (loosely based on Orphanidou et al., 2015) computes a continuous
index of quality of the PPG or ECG signal, by calculating the correlation coefficient between each
individual cycle’s (i.e. beat’s) morphology and an average (template) cycle morphology. This index is therefore
relative: 1 corresponds to a signal where each individual cycle’s morphology is closest to the average cycle morphology
(i.e. correlate exactly with it) and 0 corresponds to there being no correlation with the average cycle morphology.

The "templatematch" method (loosely based on Orphanidou et al., 2015) computes a continuous
index of quality of the PPG or ECG signal, by calculating the correlation coefficient between each
individual cycle’s (i.e. beat’s) morphology and an average (template) cycle morphology. This index is therefore
relative: 1 corresponds to a signal where each individual cycle’s morphology is closest to the average cycle morphology
(i.e. correlate exactly with it) and 0 corresponds to there being no correlation with the average cycle morphology.

The "dissimilarity" method (loosely based on Sabeti et al., 2019) computes a continuous index
of quality of the PPG or ECG signal, by calculating the level of dissimilarity between each individual
cycle’s (i.e. beat’s) morphology and an average (template) cycle morphology (after they are normalised). A value of
zero indicates no dissimilarity (i.e. equivalent cycle morphologies), whereas values above or below
indicate increasing dissimilarity. The original method used dynamic time-warping to align the pulse
waves prior to calculating the level of dsimilarity, whereas this implementation does not currently
include this step.

The "dissimilarity" method (loosely based on Sabeti et al., 2019) computes a continuous index
of quality of the PPG or ECG signal, by calculating the level of dissimilarity between each individual
cycle’s (i.e. beat’s) morphology and an average (template) cycle morphology (after they are normalised). A value of
zero indicates no dissimilarity (i.e. equivalent cycle morphologies), whereas values above or below
indicate increasing dissimilarity. The original method used dynamic time-warping to align the pulse
waves prior to calculating the level of dsimilarity, whereas this implementation does not currently
include this step.

The "ici" method (based on Ho et al., 2025) assesses signal quality on a cycle-by-cycle (e.g. beat-by-beat)
basis by predicting whether each intercycle-interval (ICI) (e.g. interbeat-intervals, IBIs) is accurate.
To do so, cycles (e.g. beats) are detected using a primary detector, and each ICI is predicted to be accurate
only if a secondary detector detects cycles in the same positions (within a tolerance). In this implementation,
all signal samples within an ICI are rated as high quality (1) if that ICI is predicted to be accurate, or low
quality (0) if that ICI is predicted to be inaccurate. This approach was derived from the previously
proposed bSQI approach. The resulting quality signal is 1-padded, with all samples before the first cycle
and after the last cycle set to 1.

The "ici" method (based on Ho et al., 2025) assesses signal quality on a cycle-by-cycle (e.g. beat-by-beat)
basis by predicting whether each intercycle-interval (ICI) (e.g. interbeat-intervals, IBIs) is accurate.
To do so, cycles (e.g. beats) are detected using a primary detector, and each ICI is predicted to be accurate
only if a secondary detector detects cycles in the same positions (within a tolerance). In this implementation,
all signal samples within an ICI are rated as high quality (1) if that ICI is predicted to be accurate, or low
quality (0) if that ICI is predicted to be inaccurate. This approach was derived from the previously
proposed bSQI approach. The resulting quality signal is 1-padded, with all samples before the first cycle
and after the last cycle set to 1.

The "skewness" method (based on Selveraj, 2011 and Elgendi, 2016) computes the skewness of the signal in moving
windows. The skewness is a measure of the asymmetry of the probability distribution of the signal’s amplitude values.
For the PPG, higher quality signals were generally found to have higher skewness values (Elgendi, 2016).
The window length and overlap can be adjusted using the window_sec and overlap_sec parameters.

The "skewness" method (based on Selveraj, 2011 and Elgendi, 2016) computes the skewness of the signal in moving
windows. The skewness is a measure of the asymmetry of the probability distribution of the signal’s amplitude values.
For the PPG, higher quality signals were generally found to have higher skewness values (Elgendi, 2016).
The window length and overlap can be adjusted using the window_sec and overlap_sec parameters.

The "kurtosis" method (based on Selveraj, 2011 and Elgendi, 2016) computes the kurtosis of the signal in moving
windows. The kurtosis is a measure of the “tailedness” of the probability distribution of the signal’s amplitude values.
For the PPG, higher quality signals are generally found to have higher kurtosis values (Elgendi, 2016).
The window length and overlap can be adjusted using the window_sec and overlap_sec parameters.

The "kurtosis" method (based on Selveraj, 2011 and Elgendi, 2016) computes the kurtosis of the signal in moving
windows. The kurtosis is a measure of the “tailedness” of the probability distribution of the signal’s amplitude values.
For the PPG, higher quality signals are generally found to have higher kurtosis values (Elgendi, 2016).
The window length and overlap can be adjusted using the window_sec and overlap_sec parameters.

The "entropy" method (based on Selvaraj et al., 2011, and inspired by Elgendi, 2016) computes the entropy of the
signal in moving windows. The entropy is a measure of the randomness in the signal’s amplitude values.

The "entropy" method (based on Selvaraj et al., 2011, and inspired by Elgendi, 2016) computes the entropy of the
signal in moving windows. The entropy is a measure of the randomness in the signal’s amplitude values.

signal ( Union[list, np.array, pd.Series] ) – The cleaned signal, such as that returned by ppg_clean() or ecg_clean() .

signal ( Union[list, np.array, pd.Series] ) – The cleaned signal, such as that returned by ppg_clean() or ecg_clean() .

sampling_rate ( int ) – The sampling frequency of signal (in Hz, i.e., samples/second). Defaults to 1000.

sampling_rate ( int ) – The sampling frequency of signal (in Hz, i.e., samples/second). Defaults to 1000.

cycle_inds ( tuple or list ) – The list of cycle samples (e.g. beat or breath samples, such as PPG or ECG peaks returned by ppg_peaks() or ecg_peaks() , or RSP peaks returned by rsp_peaks() ).

cycle_inds ( tuple or list ) – The list of cycle samples (e.g. beat or breath samples, such as PPG or ECG peaks returned by ppg_peaks() or ecg_peaks() , or RSP peaks returned by rsp_peaks() ).

signal_type ( str ) – The signal type (e.g. ‘ppg’, ‘ecg’, or ‘rsp’).

signal_type ( str ) – The signal type (e.g. ‘ppg’, ‘ecg’, or ‘rsp’).

method ( str ) – The processing pipeline to apply. Can be one of "templatematch" , "dissimilarity" , "ici" , "skewness" , "kurtosis" , or "entropy" . The default is "templatematch" .

method ( str ) – The processing pipeline to apply. Can be one of "templatematch" , "dissimilarity" , "ici" , "skewness" , "kurtosis" , or "entropy" . The default is "templatematch" .

primary_detector ( str ) – The name of the primary cycle (i.e. beat or breath) detector (e.g. the defaults are "unsw" for the ECG, and "charlton" for the PPG).

primary_detector ( str ) – The name of the primary cycle (i.e. beat or breath) detector (e.g. the defaults are "unsw" for the ECG, and "charlton" for the PPG).

secondary_detector ( str ) – The name of the secondary cycle detector (e.g. the defaults are "neurokit" for the ECG, and "elgendi" for the PPG).

secondary_detector ( str ) – The name of the secondary cycle detector (e.g. the defaults are "neurokit" for the ECG, and "elgendi" for the PPG).

tolerance_window_ms ( int ) – The tolerance window size (in milliseconds) for use with the “ici” method when assessing agreement between
primary and secondary cycle detectors.

tolerance_window_ms ( int ) – The tolerance window size (in milliseconds) for use with the “ici” method when assessing agreement between
primary and secondary cycle detectors.

window_sec ( float, optional ) – Window length in seconds for windowed metrics (default: 3). Used for the "skewness" and "kurtosis" methods.

window_sec ( float, optional ) – Window length in seconds for windowed metrics (default: 3). Used for the "skewness" and "kurtosis" methods.

overlap_sec ( float, optional ) – Overlap between windows in seconds for windowed metrics (default: 2). Used for the "skewness" and "kurtosis" methods.

overlap_sec ( float, optional ) – Overlap between windows in seconds for windowed metrics (default: 2). Used for the "skewness" and "kurtosis" methods.

no_bins ( int ) – Number of bins for "entropy" calculation (default: 16).

no_bins ( int ) – Number of bins for "entropy" calculation (default: 16).

**kwargs – Additional keyword arguments, usually specific for each method.

**kwargs – Additional keyword arguments, usually specific for each method.

quality ( array ) – Vector containing the quality index ranging from 0 to 1 for "templatematch" method,
or an unbounded value (where 0 indicates high quality) for "dissimilarity" method,
or zeros and ones (where 1 indicates high quality) for "ici" method,
or an unbounded value for "skewness" , "kurtosis" , or "entropy" methods.

Orphanidou, C. et al. (2015). “Signal-quality indices for the electrocardiogram and photoplethysmogram:
derivation and applications to wireless monitoring”. IEEE Journal of Biomedical and Health Informatics, 19(3), 832-8.

Orphanidou, C. et al. (2015). “Signal-quality indices for the electrocardiogram and photoplethysmogram:
derivation and applications to wireless monitoring”. IEEE Journal of Biomedical and Health Informatics, 19(3), 832-8.

Sabeti E. et al. (2019). Signal quality measure for pulsatile physiological signals using morphological features:
Applications in reliability measure for pulse oximetry. Informatics in Medicine Unlocked, 16, 100222.

Sabeti E. et al. (2019). Signal quality measure for pulsatile physiological signals using morphological features:
Applications in reliability measure for pulse oximetry. Informatics in Medicine Unlocked, 16, 100222.

Ho, S.Y.S et al. (2025). “Accurate RR-interval extraction from single-lead, telehealth electrocardiogram signals.
medRxiv, 2025.03.10.25323655. https://doi.org/10.1101/2025.03.10.25323655

Ho, S.Y.S et al. (2025). “Accurate RR-interval extraction from single-lead, telehealth electrocardiogram signals.
medRxiv, 2025.03.10.25323655. https://doi.org/10.1101/2025.03.10.25323655

Elgendi, M. et al. (2016). “Optimal signal quality index for photoplethysmogram signals”.
Bioengineering, 3(4), 1–15. doi: https://doi.org/10.3390/bioengineering3040021

Elgendi, M. et al. (2016). “Optimal signal quality index for photoplethysmogram signals”.
Bioengineering, 3(4), 1–15. doi: https://doi.org/10.3390/bioengineering3040021

Selvaraj, N. et al. (2011). “Statistical approach for the detection of motion/noise artifacts in Photoplethysmogram”.
Proc IEEE EMBC; pp. 4972–4975.

Selvaraj, N. et al. (2011). “Statistical approach for the detection of motion/noise artifacts in Photoplethysmogram”.
Proc IEEE EMBC; pp. 4972–4975.

Example 1: Using ICI method to assess PPG signal quality

Example 1: Using ICI method to assess PPG signal quality

Example 2: Using template-matching method to assess ECG signal quality

Example 2: Using template-matching method to assess ECG signal quality

Example 3: Using template-matching method to assess RSP signal quality

Example 3: Using template-matching method to assess RSP signal quality

Example 4: Using skewness method to assess PPG signal quality

Example 4: Using skewness method to assess PPG signal quality

Tidy up PPG peaks and onsets to make them conform to the following rules:
(i) No two points at the same time
(ii) At least one local minimum between consecutive peaks
(iii) At least one local maximum between consecutive onsets
(iv) Alternates between onsets and peaks
(v) Starts with onset, and ends with peak
(vi) Same number of peaks and onsets

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) that contains the peaks and onsets, in the form of a vector of values.

signal ( Union[list, np.array, pd.Series] ) – The signal (i.e., a time series) that contains the peaks and onsets, in the form of a vector of values.

peaks ( list or array or DataFrame or Series or dict ) – The samples at which the peaks occur.

peaks ( list or array or DataFrame or Series or dict ) – The samples at which the peaks occur.

onsets ( list or array or DataFrame or Series or dict ) – The samples at which the onsets occur.

onsets ( list or array or DataFrame or Series or dict ) – The samples at which the onsets occur.

method ( str ) – "Charlton2022" uses the approach used in the ppg-beats toolbox, Zenodo, https://doi.org/10.5281/zenodo.6037646 This approach was designed for PPG signals.

method ( str ) – "Charlton2022" uses the approach used in the ppg-beats toolbox, Zenodo, https://doi.org/10.5281/zenodo.6037646 This approach was designed for PPG signals.

peaks_clean ( array ) – The corrected peak locations. onsets_clean ( array ) – The corrected onset locations.

peaks_clean ( array ) – The corrected peak locations.

peaks_clean ( array ) – The corrected peak locations.

onsets_clean ( array ) – The corrected onset locations.

onsets_clean ( array ) – The corrected onset locations.

Charlton, P. H. et al. (2022). Detecting beats in the photoplethysmogram: benchmarking open-source algorithms.
Physiological Measurement, 46, 035002, doi:10.1088/1361-6579/adb89e

Charlton, P. H. et al. (2022). Detecting beats in the photoplethysmogram: benchmarking open-source algorithms.
Physiological Measurement, 46, 035002, doi:10.1088/1361-6579/adb89e
