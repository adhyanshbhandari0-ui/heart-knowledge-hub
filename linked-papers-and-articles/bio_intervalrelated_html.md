# bio_intervalrelated.html

**Source:** https://neuropsychology.github.io/NeuroKit/examples/bio_intervalrelated/bio_intervalrelated.html

---

This example can be referenced by citing the package .

This example shows how to use NeuroKit to analyze longer periods of data (i.e., greater than 10 seconds) such as resting state data . If you are looking to perform event-related analysis on epochs, you can refer to this NeuroKit example here.

First, download the dataset located on the GitHub repository.

It contains 5 minutes of physiological signals recorded at a frequency of 100Hz (5 x 60 x 100 = 30000 data points).

It contains the following signals : ECG, PPG, RSP

This is the resting state data from 1 participant who was asked to close his/her eyes for 8 minutes, trying not to think of anything as well as not to fall asleep.

In this analysis here, we will focus on extracting ECG and RSP features. To process the respective physiological signals, you can use ecg_process() and rsp_process() . You can then then visualize these signals using ecg_plot() and rsp_plot() . For the purposes of these example, we will select just 3000 datapoints (or 30s) to visualize.

Note: Do remember to specify the correct sampling_rate (in this case, to 100Hz) in which the signals were generated, in all the relevant functions.

Now that we have the processed signals, we can now perform the analysis using ecg_intervalrelated() and rsp_intervalrelated() . Simply provide the processed dataframe and these functions will return a dataframe of the features pertaining to the specific signal.

These features will be quite different from event-related features (See Event-related analysis example ) as these signals were generated over a longer period of time. Hence, apart from the mean signal rate, variability metrices pertaining to heart rate variability (HRV) and respiratory rate variability (RRV) are also extracted here.

If you want to segment your data for analysis, such as analyzing two separate portions of your resting state data, you can simply do so by splitting the ecg_signals dataframe into epochs using epochs_create() . Using this example dataset, let’s say you want to analyze the first half and the second half of the ECG data. This means that each halved data would last for 60 x 2.5s = 150s .

In this function, we would also specify the onset of events to be at the 0th (for the first half of the data) and the 15000th datapoint (for the second half of the data), since there are 30000 data points in total.

This returns a dictionary of 2 processed ECG dataframes, which you can then enter into ecg_intervalrelated() .

This then returns a dataframe of the analyzed features, with the rows representing the respective segmented signals. Try doing this with your own signals!
