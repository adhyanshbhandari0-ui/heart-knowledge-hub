# ecg_heartbeats.html

**Source:** https://neuropsychology.github.io/NeuroKit/examples/ecg_heartbeats/ecg_heartbeats.html

---

Extract and Visualize Individual Heartbeats

Extract and Visualize Individual Heartbeats #

This example can be referenced by citing the package .

This example shows how to use NeuroKit to extract and visualize the QRS complexes (individual heartbeats) from an electrocardiogram (ECG).

In this example, we will use a simulated ECG signal. However, you can use any of your signal (for instance, extracted from the dataframe using the read_acqknowledge() .

Once you have a raw ECG signal in the shape of a vector (i.e., a one-dimensional array), or a list, you can use ecg_process() to process it.

Note: It is critical that you specify the correct sampling rate of your signal throughout many processing functions, as this allows NeuroKit to have a time reference.

This function outputs two elements, a dataframe containing the different signals (raw, cleaned, etc.) and a dictionary containing various additional information (peaks location, …).

The processing function does two important things for our purpose: 1) it cleans the signal and 2) it detects the location of the R-peaks. Let’s extract these from the output.

Great. We can visualize the R-peaks location in the signal to make sure it got detected correctly by marking their location in the signal.

Once that we know where the R-peaks are located, we can create windows of signal around them (of a length of for instance 1 second, ranging from 400 ms before the R-peak), which we can refer to as epochs .

Segment the signal around the heart beats #

You can now epoch all these individual heart beats, synchronized by their R peaks with the ecg_segment() function.

This create a dictionary of dataframes for each ‘epoch’ (in this case, each heart beat).

This section is written for a more advanced purpose of plotting and visualizing all the heartbeats segments. The code below uses packages other than NeuroKit2 to manually set the colour gradient of the signals and to create a more interactive experience for the user - by hovering your cursor over each signal, an annotation of the signal corresponding to the heart beat index is shown.

Here, we define a function to create the epochs. It takes in cleaned as the cleaned signal dataframe, and peaks as the array of R-peaks locations.

We then pivot the dataframe so that each column corresponds to the signal values of one channel, or Label .

This section of the code incorporates the aesthetics and interactivity of the plot produced. Unfortunately, the interactivity is not active in this example but it should work in your console! As you hover your cursor over each signal, annotation of the channel that produced it is shown. You will need to uncomment the code below.

Note: you need to install the mplcursors package for the interactive part ( pip install mplcursors )
