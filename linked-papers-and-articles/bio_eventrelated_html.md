# bio_eventrelated.html

**Source:** https://neuropsychology.github.io/NeuroKit/examples/bio_eventrelated/bio_eventrelated.html

---

This example can be referenced by citing the package .

This example shows how to use NeuroKit to extract epochs from data based on events localisation and its corresponding physiological signals. That way, you can compare experimental conditions with one another.

Use the nk.data() function to load the dataset located on NeuroKit data folder.

It contains 2.5 minutes of biosignals recorded at a frequency of 100Hz (2.5 x 60 x 100 = 15000 data points).

Biosignals : ECG, RSP, EDA + Photosensor (event signal)

This is the data from one participant that saw 4 emotional and neutral images from the IAPS ), which we will refer to as events .

Importantly, the images were marked in the recording system (the “triggers”) by a small black rectangle on the screen, which led to the photosensor signal to go down (and then up again after the image). This is what will allow us to retrieve the location of these events.

They were 2 types of images (the condition ) that were shown to the participant: “Negative” vs. “Neutral” (in terms of emotion). Each picture was presented for 3 seconds. The following list is the condition order.

These events can be localized and extracted using events_find() .

Note that you should also specify whether to select events that are higher or below the threshold using the threshold_keep argument.

As we can see, events_find() returns a dict containing onsets and durations for each corresponding event, based on the label for event identifiers and each event condition. Each event here lasts for 300 data points (equivalent to 3 seconds sampled at 100Hz).

The output of events_plot() shows the corresponding events in the signal, with the blue dashed line representing a Negative event and red dashed line representing a Neutral event.

Now that we have the events location, we can go ahead and process the data.

Biosignals processing can be done quite easily using NeuroKit with the bio_process() function. Simply provide the appropriate biosignal channels and additional channels that you want to keep (for example, the photosensor), and bio_process() will take care of the rest. It will return a dataframe containing processed signals and a dictionary containing useful information.

We now have to transform this dataframe into epochs , i.e. segments (chunks) of data around the events using epochs_create() . We want it to start 1 second before the event onset and end 6 seconds after. These values are passed into the epochs_start and epochs_end arguments, respectively.

Our epochs will then cover the region from -1 s to +6 s (i.e., 700 data points since the signal is sampled at 100Hz).

Let’s plot some of the signals of the first epoch (and transform them to the same scale for visualization purposes).

Manually Extract Event Related Features #

With these segments, we are able to compare how the physiological signals vary across the different events. We do this by:

Storing the mean value of $X$ feature of each condition in a new dictionary

Storing the mean value of $X$ feature of each condition in a new dictionary

We will call these 3 objects epochs-dictionary , the mean-dictionary and our results-dataframe .

You can save this dataframe ( df.to_csv("results.csv") ) and proceed to do some actual statistics on it.

While manual feature creation allows you to compute and extract exactly what you need, using our automated pipeline is a lot easier.

You can now plot and compare how these features differ according to the event of interest.

Interpretation : As we can see, there seems to be a difference between the negative and the neutral pictures. Negative stimuli, as compared to neutral stimuli, were related to a stronger cardiac deceleration (i.e., higher heart rate variability), an accelerated breathing rate, and higher SCR magnitude.

Of course, because of data size limits on Github, we had to downsample the signals and have only one participant with a few events. That said, the same workflow can apply for more events, and more participants (you just need to additionally loop through all participants).
