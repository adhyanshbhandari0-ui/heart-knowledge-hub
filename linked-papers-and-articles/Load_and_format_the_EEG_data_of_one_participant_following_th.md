# 
    "Load and format the EEG data of one participant following this [MNE example

**Source:** https://mne.tools/dev/auto_tutorials/evoked/30_eeg_erp.html

---

Go to the end to download the full example code or to run this example in your browser via JupyterLite.

EEG analysis - Event-Related Potentials (ERPs) #

This tutorial shows how to perform standard ERP analyses in MNE-Python. Most of
the material here is covered in other tutorials too, but for convenience the
functions and methods most useful for ERP analyses are collected here, with
links to other tutorials where more detailed information is given.

As usual we’ll start by importing the modules we need and loading some example
data. Instead of parsing the events from the raw data’s stim channel (like we do in this tutorial ), we’ll load
the events from an external events file. Finally, to speed up computations
we’ll crop the raw data from ~4.5 minutes down to 90 seconds.

The file that we loaded has already been partially processed: 3D sensor
locations have been saved as part of the .fif file, the data have been
low-pass filtered at 40 Hz, and a common average reference is set for the
EEG channels, stored as a projector (see Creating the average reference as a projector in the Setting the EEG reference tutorial for more info about when you may want to do
this). We’ll discuss how to do each of these below.

Since this is a combined EEG/MEG dataset, let’s start by restricting the data
to just the EEG and EOG channels. This will cause the other projectors saved
in the file (which apply only to magnetometer channels) to be removed. By
looking at the measurement info we can see that we now have 59 EEG channels
and 1 EOG channel.

In practice it is quite common to have some channels labeled as EEG that are
actually EOG channels. Raw objects have a set_channel_types() method that can be used to change a
channel that is mislabeled as eeg to eog .

You can also rename channels using rename_channels() .
Detailed examples of both of these methods can be found in the tutorial The Raw data structure: continuous data .

In our data set, all channel types are already correct. Therefore, we’ll only
remove a space and a leading zero in the channel names and convert to
lowercase:

The assignment to a temporary name _ (the _ = part) is included
here to suppress automatic printing of the raw object. You do not
have to do this in your interactive analysis.

The tutorial Working with sensor locations describes how sensor locations are
handled in great detail. To briefly summarize: MNE-Python distinguishes montages (which contain 3D sensor locations x , y ,
and z , in meters) from layouts (which define 2D sensor
arrangements for plotting schematic sensor location diagrams). Additionally,
montages may specify idealized sensor locations (based on, e.g., an
idealized spherical head model), or they may contain realistic sensor
locations obtained by digitizing the 3D locations of the sensors when placed
on a real person’s head.

This dataset has realistic digitized 3D sensor locations saved as part of the .fif file, so we can view the sensor locations in 2D or 3D using the plot_sensors() method:

If you’re working with a standard montage like the 10–20 system, you can add sensor locations to the data with raw.set_montage('spherical_1020') (see Working with sensor locations for
information on other standard montages included with MNE-Python).

If you have digitized realistic sensor locations, there are dedicated
functions for loading those digitization files into MNE-Python (see Reading sensor digitization files for discussion and Supported formats for digitized 3D locations for a list
of supported formats). Once loaded, the digitized sensor locations can be
added to the data by passing the loaded montage object to set_montage() .

As mentioned, this data already has an EEG common average reference
added as a projector . We can view the effect of this projector on the
raw data by plotting it with and without the projector applied:

The referencing scheme can be changed with the function mne.set_eeg_reference() (which by default operates on a copy of the
data) or the raw.set_eeg_reference() method (which always modifies the data in-place ). The tutorial Setting the EEG reference shows several examples.

MNE-Python has extensive support for different ways of filtering data. For a
general discussion of filter characteristics and MNE-Python defaults, see Background information on filtering . For practical examples of how to apply filters to your
data, see Filtering and resampling data . Here, we’ll apply a simple high-pass
filter for illustration:

Evoked responses: epoching and averaging #

The general process for extracting evoked responses from continuous data is
to use the Epochs constructor, and then average the resulting
epochs to create an Evoked object. In MNE-Python, events are
represented as a NumPy array containing event
latencies (in samples) and integer event codes. The event codes are stored in
the last column of the events array:

The Working with events tutorial discusses event arrays in more detail.
Integer event codes are mapped to more descriptive text using a Python dictionary usually called event_id . This mapping is
determined by your experiment (i.e., it reflects which event codes you chose
to represent different experimental events or conditions). The Sample data uses the following mapping:

Now we can proceed to epoch the continuous data. An interactive plot allows
us to click on epochs to mark them as “bad” and drop them from the
analysis (it is not interactive on this documentation website, but will be
when you run epochs.plot() in a Python console).

It is also possible to automatically drop epochs (either when first creating
them or later on) by providing maximum peak-to-peak signal value thresholds
(passed to Epochs as the reject parameter; see Rejecting Epochs based on peak-to-peak channel amplitude for details).  You can also do this after
the epochs are already created using drop_bad() :

Next, we generate a barplot of which channels contributed most to epochs
getting rejected. If one channel is responsible for many epoch rejections,
it may be worthwhile to mark that channel as “bad” in the Raw object and then re-run epoching (fewer channels with
more good epochs may be preferable to keeping all channels but losing many
epochs). See Handling bad channels for more information.

Epochs can also be dropped automatically if the event around which the epoch
is created is too close to the start or end of the Raw object (e.g., if the epoch would extend past the end of the recording; this
is the cause for the “TOO_SHORT” entry in the plot_drop_log() plot).

Epochs may also be dropped automatically if the Raw object
contains annotations that begin with either bad or edge (“edge” annotations are automatically inserted when concatenating two or more Raw objects). See Rejecting bad data spans and breaks for more
information on annotation-based epoch rejection.

Now that we’ve dropped all bad epochs, let’s look at our evoked responses for
some conditions we care about. Here, the average() method
will create an Evoked object, which we can then plot. Notice
that we select which condition we want to average using square-bracket
indexing (like for a dictionary ). This returns a subset with
only the desired epochs, which we then average:

These Evoked objects have their own interactive plotting method
(though again, it won’t be interactive on the documentation website).
Clicking and dragging a span of time will generate a topography of scalp
potentials for the selected time segment. Here, we also demonstrate built-in
color-coding the channel traces by location:

Scalp topographies can also be obtained non-interactively with the plot_topomap() method. Here, we display topomaps of the
average evoked potential in 50 ms time windows centered at -200 ms, 100 ms,
and 400 ms.

Considerable customization of these plots is possible, see the docstring of plot_topomap() for details.

There is also a built-in method for combining butterfly plots of the signals
with scalp topographies called plot_joint() . Like in plot_topomap() , you can specify times for the scalp
topographies or you can let the method choose times automatically as shown
here:

Global field power [ 1 ] [ 2 ] [ 3 ] is,
generally speaking, a measure of agreement of the signals picked up by all
sensors across the entire scalp: if all sensors have the same value at a
given time point, the GFP will be zero at that time point. If the signals
differ, the GFP will be non-zero at that time point. GFP
peaks may reflect “interesting” brain activity, warranting further
investigation. Mathematically, the GFP is the population standard
deviation across all sensors, calculated separately for every time point.

You can plot the GFP using evoked.plot(gfp=True) . The GFP
trace will be black if spatial_colors=True and green otherwise. The EEG
reference does not affect the GFP:

To plot the GFP by itself, you can pass gfp='only' (this makes it easier to
read off the GFP data values, because the scale is aligned):

The GFP is the population standard deviation of the signal
across channels. To compute it manually, we can leverage the fact that evoked.data is a NumPy array ,
and verify by plotting it using plain Matplotlib commands:

Averaging across channels with regions of interest #

Since our sample data contains responses to left and right auditory and
visual stimuli, we may want to compare left versus right regions of interest
(ROIs). To average across channels in a given ROI, we first find the relevant
channel indices. Revisiting the 2D sensor plot above, we might choose the
following channels for left and right ROIs, respectively:

Now we can create a new Evoked object with two virtual channels (one for each
ROI):

If we wanted to contrast auditory to visual stimuli, a useful function is mne.viz.plot_compare_evokeds() . By default, this function will combine
all channels in each evoked object using GFP (or RMS for MEG channels); here
instead we specify to combine by averaging, and restrict it to a subset of
channels by passing picks :

We can also generate confidence intervals by treating each epoch as a
separate observation using iter_evoked() . A confidence
interval across subjects could also be obtained by passing a list of Evoked objects (one per subject) to the plot_compare_evokeds() function.

We can also compare conditions by subtracting one Evoked object
from another using the mne.combine_evoked() function (this function
also supports pooling of epochs without subtraction).

The code above yields an equal-weighted difference . If you have
different numbers of epochs per condition, you might want to equalize the
number of events per condition first by using epochs.equalize_event_counts() before averaging.

To compute grand averages across conditions (or subjects), you can pass a
list of Evoked objects to mne.grand_average() . The result
is another Evoked object.

For combining conditions it is also possible to make use of HED tags in the condition names when selecting which epochs to average. For
example, we have the condition names:

We can select the auditory conditions (left and right together) by passing:

See Subselecting epochs for more details on that.

The tutorials The Epochs data structure: discontinuous data and The Evoked data structure: evoked/averaged data have many
more details about working with the Epochs and Evoked classes.

It is common in ERP research to extract measures of amplitude or latency to
compare across different conditions. There are many measures that can be
extracted from ERPs, and many of these are detailed (including the respective
strengths and weaknesses) in chapter 9 of Luck [ 4 ] (also see
the Measurement Tool in the ERPLAB Toolbox [ 5 ] ).

This part of the tutorial will demonstrate how to extract three common
measures:

The most common measures of amplitude and latency are peak measures.
Peak measures are basically the maximum amplitude of the signal in a
specified time window and the time point (or latency) at which the peak
amplitude occurred.

Peak measures can be obtained using the get_peak() method.
There are two important things to point out about get_peak() . First, it finds the strongest peak
looking across all channels of the selected type that are available in
the Evoked object. As a consequence, if you want to restrict
the search to a group of channels or a single channel, you
should first use the pick() or pick_channels() methods. Second, the get_peak() method can find different types of peaks using
the mode argument. There are three options:

mode='pos' : finds the peak with a positive voltage (ignores
negative voltages)

mode='pos' : finds the peak with a positive voltage (ignores
negative voltages)

mode='neg' : finds the peak with a negative voltage (ignores
positive voltages)

mode='neg' : finds the peak with a negative voltage (ignores
positive voltages)

mode='abs' : finds the peak with the largest absolute voltage
regardless of sign (positive or negative)

mode='abs' : finds the peak with the largest absolute voltage
regardless of sign (positive or negative)

The following example demonstrates how to find the first positive peak in the
ERP (i.e., the P100) for the left visual condition (i.e., the l_vis Evoked object). The time window used to search for
the peak ranges from 0.08 to 0.12 s. This time window was selected because it
is when P100 typically occurs. Note that all 'eeg' channels are submitted
to the get_peak() method.

The output shows that channel eeg55 had the maximum positive peak in
the chosen time window from all of the 'eeg' channels searched.
In practice, one might want to pull out the peak for
an a priori region of interest or a single channel depending on the study.
This can be done by combining the pick() or pick_channels() methods with the get_peak() method.

Here, let’s assume we believe the effects of interest will occur
at eeg59 .

While the peak latencies are the same in channels eeg55 and eeg59 ,
the peak amplitudes differ. This approach can also be applied to virtual
channels created with the combine_channels() function and
difference waves created with the mne.combine_evoked() function (see aud_minus_vis in section Comparing conditions above).

Peak measures are very susceptible to high frequency noise in the
signal (for discussion, see [ 4 ] ). Specifically, high
frequency noise positively biases peak amplitude measures. This bias can
confound comparisons across conditions where ERPs differ in the level of high
frequency noise, such as when the conditions differ in the number of trials
contributing to the ERP. One way to avoid this is to apply a non-causal
low-pass filter to the ERP. Low-pass filters reduce the contribution of high
frequency noise by smoothing out fast (i.e., high frequency) fluctuations in
the signal (see Background information on filtering ). While this can reduce the positive
bias in peak amplitude measures caused by high frequency noise, low-pass
filtering the ERP can introduce challenges in interpreting peak latency
measures for effects of interest [ 6 ] [ 7 ] .

If using peak measures, it is critical to visually inspect the data to
make sure the selected time window actually contains a peak. The get_peak() method detects the maximum or minimum voltage in
the specified time range and returns the latency and amplitude of this peak.
There is no guarantee that this method will return an actual peak. Instead,
it may return a value on the rising or falling edge of a peak we are trying
to find.

The following example demonstrates why visual inspection is crucial. Below,
we use a known bad time window (0.095 to 0.135 s) to search for a peak in
channel eeg59 .

If all we had were the above values, it would be unclear if they are truly
identifying a peak in the ERP. In fact, the 0.095 to 0.135 s time window
actually does not contain the true peak, which is shown in the top panel
below. The bad time window (highlighted in orange) does not contain the true
peak (the pink star). In contrast, the time window defined initially (0.08 to
0.12 s; highlighted in blue) returns an actual peak instead of a just a
maximum or minimum in the searched time window. Visual inspection will always
help you to convince yourself that the returned values are actual peaks.

Another common practice in ERP studies is to define a component (or effect)
as the mean amplitude within a specified time window. One advantage of this
approach is that it is less sensitive to high frequency noise (compared to
peak amplitude measures), because averaging over a time window acts as a
low-pass filter (see discussion in the previous section Peak latency and amplitude ).

When using mean amplitude measures, selecting the time window based on
the effect of interest (e.g., the difference between two conditions) can
inflate the likelihood of finding false positives in your
results [ 8 ] . There are other, and
better, ways to identify a time window to use for extracting mean amplitude
measures. First, you can use an a priori time window based on prior
research.
A second option is to define a time window from an independent condition or
set of trials not used in the analysis (e.g., a “localizer”). A third
approach is
to define a time window using the across-condition grand average. This latter
approach is not circular because the across-condition mean and condition
difference are independent of one another. The issues discussed above also
apply to selecting channels used for analysis.

The following example demonstrates how to pull out the mean amplitude
from the left visual condition (i.e., the l_vis Evoked object) from selected channels and time windows. Stimulating the
left visual field increases neural activity of visual cortex in the
contralateral (i.e., right) hemisphere. We can test this by examining the
amplitude of the ERP for left visual field stimulation over right
(contralateral) and left (ipsilateral) channels. The channels used for this
analysis are eeg54 and eeg57 (left hemisphere), and eeg59 and eeg55 (right hemisphere). The time window used is 0.08 ( good_tmin )
to 0.12 s ( good_tmax ) as it corresponds to when the P100 typically
occurs.
The P100 is sensitive to left and right visual field stimulation. The mean
amplitude is extracted from the above four channels and stored in a pandas.DataFrame .

As demonstrated in this example, the mean amplitude was higher and
positive in right compared to left hemisphere channels. It should be
reiterated that both spatial and temporal windows used in the analysis should
be determined in an independent manner (e.g., defined a priori from prior
research, a “localizer” or another independent condition) and not based
on the data you will use to test your hypotheses.

The example can be modified to extract the mean amplitude
from all channels and store the resulting output in a pandas.DataFrame . This can be useful for statistical analyses
conducted in other programming languages.

Dietrich Lehmann and Wolfgang Skrandies. Reference-free identification of components of checkerboard-evoked multichannel potential fields. Electroencephalography and Clinical Neurophysiology , 48(6):609–621, 1980. doi:10.1016/0013-4694(80)90419-8 .

Dietrich Lehmann and Wolfgang Skrandies. Spatial analysis of evoked potentials in man—a review. Progress in Neurobiology , 23(3):227–250, 1984. doi:10.1016/0301-0082(84)90003-0 .

Micah M. Murray, Denis Brunet, and Christoph M. Michel. Topographic ERP analyses: A step-by-step tutorial review. Brain Topography , 20(4):249–264, 2008. doi:10.1007/s10548-008-0054-5 .

Steven J Luck. An Introduction to the Event-Related Potential Technique . The MIT Press, Cambridge, MA, 2nd edition, 2014. ISBN 978-0-262-52585-5. URL: https://mitpress.mit.edu/9780262525855/an-introduction-to-the-event-related-potential-technique .

Javier Lopez-Calderon and Steven J. Luck. Erplab: an open-source toolbox for the analysis of event-related potentials. Frontiers in Human Neuroscience , 2014. doi:10.3389/fnhum.2014.00213 .

Guillaume A. Rousselet. Does filtering preclude us from studying ERP time-courses? Frontiers in Psychology , 2012. doi:10.3389/fpsyg.2012.00131 .

Rufin VanRullen. Four common conceptual fallacies in mapping the time course of recognition. Frontiers in Psychology , 2011. doi:10.3389/fpsyg.2011.00365 .

Steven J. Luck and Nicholas Gaspelin. How to get statistically significant effects in any ERP experiment (and why you shouldn’t). Psychophysiology , 54(1):146–157, 2017. doi:10.1111/psyp.12639 .

Total running time of the script: (0 minutes 6.648 seconds)

Download Jupyter notebook: 30_eeg_erp.ipynb

Download Python source code: 30_eeg_erp.py
