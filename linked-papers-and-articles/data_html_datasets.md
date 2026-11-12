# data.html#datasets

**Source:** https://neuropsychology.github.io/NeuroKit/functions/data.html

---

NeuroKit includes datasets that can be used for testing. These datasets are not downloaded
automatically with the package (to avoid increasing its weight), but can be downloaded via the nk.data() function (note that an internet connection is necessary). See the examples below.

Signals : The following signals (that will return an array) are available:

ecg_1000hz : Returns a vector containing ECG signal ( sampling_rate=1000 ).

ecg_1000hz : Returns a vector containing ECG signal ( sampling_rate=1000 ).

ecg_3000hz : Returns a vector containing ECG signal ( sampling_rate=3000 ).

ecg_3000hz : Returns a vector containing ECG signal ( sampling_rate=3000 ).

rsp_1000hz : Returns a vector containing RSP signal ( sampling_rate=1000 ).

rsp_1000hz : Returns a vector containing RSP signal ( sampling_rate=1000 ).

eeg_150hz : Returns a vector containing EEG signal ( sampling_rate=150 ).

eeg_150hz : Returns a vector containing EEG signal ( sampling_rate=150 ).

eog_100hz : Returns a vector containing vEOG signal ( sampling_rate=100 ).

eog_100hz : Returns a vector containing vEOG signal ( sampling_rate=100 ).

DataFrames : The following datasets (that will return a pd.DataFrame ) are available:

iris : Convenient access to the Iris dataset in a DataFrame, exactly how it is in R.

iris : Convenient access to the Iris dataset in a DataFrame, exactly how it is in R.

eogs_200hz : Returns a DataFrame with hEOG , vEOG . Single subject Visual and horizontal electrooculagraphy sampling_rate=200

eogs_200hz : Returns a DataFrame with hEOG , vEOG .

bio_resting_5min_100hz : Returns a DataFrame with ECG , PPG , RSP . Single subject Resting-state of 5 min (pre-cropped, with some ECG noise towards the end) sampling_rate=100

bio_resting_5min_100hz : Returns a DataFrame with ECG , PPG , RSP .

Resting-state of 5 min (pre-cropped, with some ECG noise towards the end)

Resting-state of 5 min (pre-cropped, with some ECG noise towards the end)

bio_resting_8min_100hz : Returns a DataFrame with ECG , RSP , EDA , PhotoSensor . Single subject Resting-state of 8 min when the photosensor is low (need to crop the data) sampling_rate=100

bio_resting_8min_100hz : Returns a DataFrame with ECG , RSP , EDA , PhotoSensor .

Resting-state of 8 min when the photosensor is low (need to crop the data)

Resting-state of 8 min when the photosensor is low (need to crop the data)

bio_resting_8min_200hz : Returns a dictionary with four subjects ( S01 , S02 , S03 , S04 ). Resting-state recordings 8 min ( sampling_rate=200 ) Each subject is DataFrame  with ECG , RSP`, ``PhotoSensor , Participant

bio_resting_8min_200hz : Returns a dictionary with four subjects ( S01 , S02 , S03 , S04 ).

Each subject is DataFrame  with ECG , RSP`, ``PhotoSensor , Participant

Each subject is DataFrame  with ECG , RSP`, ``PhotoSensor , Participant

bio_eventrelated_100hz : Returns a DataFrame with ECG , EDA , Photosensor , RSP . Single subject Event-related recording of a participant watching 4 images for 3 seconds (the condition
order was: ["Negative", "Neutral", "Neutral", "Negative"] ) sampling_rate=100

bio_eventrelated_100hz : Returns a DataFrame with ECG , EDA , Photosensor , RSP .

Event-related recording of a participant watching 4 images for 3 seconds (the condition
order was: ["Negative", "Neutral", "Neutral", "Negative"] )

Event-related recording of a participant watching 4 images for 3 seconds (the condition
order was: ["Negative", "Neutral", "Neutral", "Negative"] )

eeg_1min_200hz : Returns an MNE raw object containing 1 min of EEG
data (from the MNE-sample dataset).

eeg_1min_200hz : Returns an MNE raw object containing 1 min of EEG
data (from the MNE-sample dataset).

dataset ( str ) – The name of the dataset.

Read and format a BIOPAC’s AcqKnowledge file into a pandas’ dataframe

The function outputs both the dataframe and the sampling rate (retrieved from the
AcqKnowledge file).

filename ( str ) – Filename (with or without the extension) of a BIOPAC’s AcqKnowledge file (e.g., "data.acq" ).

filename ( str ) – Filename (with or without the extension) of a BIOPAC’s AcqKnowledge file (e.g., "data.acq" ).

sampling_rate ( int ) – Sampling rate (in Hz, i.e., samples/second). Since an AcqKnowledge file can contain
signals recorded at different rates, harmonization is necessary in order to convert it
to a DataFrame. Thus, if sampling_rate is set to max (default), will keep the maximum
recorded sampling rate and upsample the channels with lower rate if necessary (using the signal_resample() function). If the sampling rate is set to a given value, will
resample the signals to the desired value. Note that the value of the sampling rate is
outputted along with the data.

sampling_rate ( int ) – Sampling rate (in Hz, i.e., samples/second). Since an AcqKnowledge file can contain
signals recorded at different rates, harmonization is necessary in order to convert it
to a DataFrame. Thus, if sampling_rate is set to max (default), will keep the maximum
recorded sampling rate and upsample the channels with lower rate if necessary (using the signal_resample() function). If the sampling rate is set to a given value, will
resample the signals to the desired value. Note that the value of the sampling rate is
outputted along with the data.

resample_method ( str ) – Method of resampling (see signal_resample() ).

resample_method ( str ) – Method of resampling (see signal_resample() ).

impute_missing ( bool ) – Sometimes, due to connections issues, there are lapses in the recorded signal (short
periods without signal). If impute_missing is True , will automatically fill the
signal interruptions using padding.

impute_missing ( bool ) – Sometimes, due to connections issues, there are lapses in the recorded signal (short
periods without signal). If impute_missing is True , will automatically fill the
signal interruptions using padding.

df ( DataFrame ) – The AcqKnowledge file as a pandas dataframe. sampling rate ( int ) – The sampling rate at which the data is sampled.

df ( DataFrame ) – The AcqKnowledge file as a pandas dataframe.

df ( DataFrame ) – The AcqKnowledge file as a pandas dataframe.

sampling rate ( int ) – The sampling rate at which the data is sampled.

sampling rate ( int ) – The sampling rate at which the data is sampled.

Reads and loads a BITalino file into a Pandas DataFrame.
The function outputs both the dataframe and the information (such as the sampling rate)
retrieved from the OpenSignals file.

filename ( str ) – Path (with or without the extension) of an OpenSignals file (e.g., "data.txt" ).

df ( DataFrame, dict ) – The BITalino file as a pandas dataframe if one device was read, or a dictionary
of pandas dataframes (one dataframe per device) if multiple devices are read. info ( dict ) – The metadata information containing the sensors, corresponding channel names, sampling
rate, and the events annotation timings if events_annotation is True .

df ( DataFrame, dict ) – The BITalino file as a pandas dataframe if one device was read, or a dictionary
of pandas dataframes (one dataframe per device) if multiple devices are read.

df ( DataFrame, dict ) – The BITalino file as a pandas dataframe if one device was read, or a dictionary
of pandas dataframes (one dataframe per device) if multiple devices are read.

info ( dict ) – The metadata information containing the sensors, corresponding channel names, sampling
rate, and the events annotation timings if events_annotation is True .

info ( dict ) – The metadata information containing the sensors, corresponding channel names, sampling
rate, and the events annotation timings if events_annotation is True .

Reads a video file (e.g., .mp4) into a numpy array of shape. This function requires OpenCV to
be installed via the opencv-python package.

filename ( str ) – The path of a video file.

array – numpy array of shape (frame, RGB-channel, height, width). int – Sampling rate in frames per second.

array – numpy array of shape (frame, RGB-channel, height, width).

array – numpy array of shape (frame, RGB-channel, height, width).

int – Sampling rate in frames per second.

int – Sampling rate in frames per second.

Split the data into multiple CSV files. You can then re-create them as follows:

filename ( str ) – Name of the CSV file (without the extension).

filename ( str ) – Name of the CSV file (without the extension).

parts ( int ) – Number of parts to split the data into.

parts ( int ) – Number of parts to split the data into.

Download a file from the given URL and save it to the destination path.

url ( str ) – The URL of the file to download.

url ( str ) – The URL of the file to download.

destination_path ( str, Path ) – The path to which the file will be downloaded. If None, the file name will be taken
from the last part of the URL path and downloaded to the current working directory.

destination_path ( str, Path ) – The path to which the file will be downloaded. If None, the file name will be taken
from the last part of the URL path and downloaded to the current working directory.

bool – True if the file was downloaded successfully, False otherwise.

Download a ZIP file from a URL and extract it to a destination directory.

url ( str ) – The URL of the ZIP file to download.

url ( str ) – The URL of the ZIP file to download.

destination_path ( str, Path ) – The path to which the ZIP file will be extracted. If None, the folder name will be taken
from the last part of the URL path and downloaded to the current working directory.

destination_path ( str, Path ) – The path to which the ZIP file will be extracted. If None, the folder name will be taken
from the last part of the URL path and downloaded to the current working directory.

unzip ( bool ) – Whether to unzip the file or not. Defaults to True.

unzip ( bool ) – Whether to unzip the file or not. Defaults to True.

bool – True if the ZIP file was downloaded successfully, False otherwise.

Loads an XDF file, sanitizes stream data, and resamples all streams onto a
common, synchronized timebase.

This function handles complex synchronization issues including clock offsets,
jitter removal (selective or global), and differing sampling rates. It produces
a single pandas DataFrame containing all aligned data.

This function requires the pyxdf module to be installed. You can install it with pip install pyxdf .

Note that, as XDF can store streams with different sampling rates and different time stamps, the function will resample all streams to 2 times (default) the highest sampling rate (to
minimize aliasing) and then interpolate based on an evenly spaced index. While this is generally safe, it
may produce unexpected results, particularly if the original stream has large gaps in its time series.
For more discussion, see here .

filename ( str ) – Path to the .xdf file to load.

filename ( str ) – Path to the .xdf file to load.

dejitter_timestamps ( bool or list, optional ) – Controls jitter removal (processing of timestamp irregularities).
If bool , passed directly to pyxdf ( True applies to all streams, False to none).
If list , a list of stream names (str) or indices (int); dejittering is applied only to these specific streams. Note: using a list triggers a double-load of the file, increasing
memory usage and loading time. Default is True .

dejitter_timestamps ( bool or list, optional ) – Controls jitter removal (processing of timestamp irregularities).
If bool , passed directly to pyxdf ( True applies to all streams, False to none).
If list , a list of stream names (str) or indices (int); dejittering is applied only to these specific streams. Note: using a list triggers a double-load of the file, increasing
memory usage and loading time. Default is True .

synchronize_clocks ( bool, optional ) – If True, attempts to synchronize clocks using LSL clock offset data.
Passed to pyxdf.load_xdf. Default is True.

synchronize_clocks ( bool, optional ) – If True, attempts to synchronize clocks using LSL clock offset data.
Passed to pyxdf.load_xdf. Default is True.

handle_clock_resets ( bool, optional ) – If True, handles clock resets (e.g., from hardware restarts) during recording.
Passed to pyxdf.load_xdf. Default is True.

handle_clock_resets ( bool, optional ) – If True, handles clock resets (e.g., from hardware restarts) during recording.
Passed to pyxdf.load_xdf. Default is True.

upsample_factor ( float, optional ) – Determines the target sampling rate for the final DataFrame. The target rate
is calculated as: max(nominal_srate) * upsample_factor .
Higher factors reduce aliasing but increase memory usage. Default is 2.0.

upsample_factor ( float, optional ) – Determines the target sampling rate for the final DataFrame. The target rate
is calculated as: max(nominal_srate) * upsample_factor .
Higher factors reduce aliasing but increase memory usage. Default is 2.0.

fill_method ( {‘ffill’, ‘bfill’, None}, optional ) – Method used to fill NaNs arising from resampling (e.g., at the very start of the
recording before the first sample). Default is 'ffill' (forward fill).
When fill_max is set this is automatically overridden to None so
that masked gap regions are not silently forward-filled back in. Explicitly pass
a value to override this behaviour.

fill_method ( {‘ffill’, ‘bfill’, None}, optional ) – Method used to fill NaNs arising from resampling (e.g., at the very start of the
recording before the first sample). Default is 'ffill' (forward fill).
When fill_max is set this is automatically overridden to None so
that masked gap regions are not silently forward-filled back in. Explicitly pass
a value to override this behaviour.

fill_value ( float or int, optional ) – Value used to fill any NaNs that remain after fill_method is applied.
Default is np.nan .

fill_value ( float or int, optional ) – Value used to fill any NaNs that remain after fill_method is applied.
Default is np.nan .

fill_max ( float or None, optional ) – If provided, any region of the resampled output that falls inside a gap between
consecutive original samples larger than this threshold (in seconds) is set back
to NaN after interpolation. This prevents the interpolator from silently
bridging large discontinuities (e.g., paused recordings). When this is set, fill_method is coerced to None (see above). Default is None (no
masking).

fill_max ( float or None, optional ) – If provided, any region of the resampled output that falls inside a gap between
consecutive original samples larger than this threshold (in seconds) is set back
to NaN after interpolation. This prevents the interpolator from silently
bridging large discontinuities (e.g., paused recordings). When this is set, fill_method is coerced to None (see above). Default is None (no
masking).

fillmissing ( float or None, optional ) – Deprecated. Use fill_max instead.

fillmissing ( float or None, optional ) – Deprecated. Use fill_max instead.

interpolation_method ( {‘linear’, ‘previous’}, optional ) – Method used for interpolating data onto the new timebase.

interpolation_method ( {‘linear’, ‘previous’}, optional ) – Method used for interpolating data onto the new timebase.

timestamp_reset ( bool, optional ) – If True (default), shifts all timestamps so the recording starts at t=0.0,
useful for analysis relative to the start of the specific file.
If False , preserves the absolute LSL timestamps (Unix epoch), useful when
synchronizing this data with other files or external clocks.

timestamp_reset ( bool, optional ) – If True (default), shifts all timestamps so the recording starts at t=0.0,
useful for analysis relative to the start of the specific file.
If False , preserves the absolute LSL timestamps (Unix epoch), useful when
synchronizing this data with other files or external clocks.

timestamp_method ( {‘circular’, ‘anchored’}, optional ) – Algorithm used to generate the new time axis. 'circular' uses a weighted circular mean to find the optimal phase alignment
across all streams, minimizing global interpolation error. 'anchored' aligns the grid strictly to the stream with the highest effective
sampling rate. Default is 'circular' .

timestamp_method ( {‘circular’, ‘anchored’}, optional ) – Algorithm used to generate the new time axis. 'circular' uses a weighted circular mean to find the optimal phase alignment
across all streams, minimizing global interpolation error. 'anchored' aligns the grid strictly to the stream with the highest effective
sampling rate. Default is 'circular' .

mode ( {‘precise’, ‘fast’}, optional ) – 'precise' uses float64 for all data, preserving precision but using more memory. 'fast' uses float32, reducing memory usage by ~50% but may lose precision
for very large values. Default is 'precise' .

mode ( {‘precise’, ‘fast’}, optional ) – 'precise' uses float64 for all data, preserving precision but using more memory. 'fast' uses float32, reducing memory usage by ~50% but may lose precision
for very large values. Default is 'precise' .

verbose ( bool, optional ) – If True, prints progress, target sampling rates, and categorical mappings to console.
Default is True.

verbose ( bool, optional ) – If True, prints progress, target sampling rates, and categorical mappings to console.
Default is True.

show ( list of str, optional ) – A list of channel names to plot for visual quality control after resampling.
If None, no plots are generated.

show ( list of str, optional ) – A list of channel names to plot for visual quality control after resampling.
If None, no plots are generated.

show_start ( float, optional ) – The start time (in seconds) for the visual control plot window.
If None, defaults to the middle of the recording.

show_start ( float, optional ) – The start time (in seconds) for the visual control plot window.
If None, defaults to the middle of the recording.

show_duration ( float, optional ) – Duration of the visual control window in seconds. Default is 1 second.

show_duration ( float, optional ) – Duration of the visual control window in seconds. Default is 1 second.

resampled_df ( pandas.DataFrame ) – A single DataFrame containing all streams resampled to the common timebase.
The index is the timestamp (seconds).
