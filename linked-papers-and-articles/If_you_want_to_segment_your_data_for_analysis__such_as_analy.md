# 
    "If you want to segment your data for analysis, such as analyzing two separate portions of your resting state data, you can simply do so by splitting the `ecg_signals` dataframe into **epochs** using [epochs_create()

**Source:** https://neuropsychology.github.io/NeuroKit/functions/epochs.html

---

Create epochs of a signal or a dataframe.

data ( DataFrame ) – A DataFrame containing the different signal(s) as different columns.
If a vector of values is passed, it will be transformed in a DataFrame
with a single ‘Signal’ column.

data ( DataFrame ) – A DataFrame containing the different signal(s) as different columns.
If a vector of values is passed, it will be transformed in a DataFrame
with a single ‘Signal’ column.

events ( list or ndarray or dict ) – Events onset location. If a dict is passed (e.g., from events_find() ),
will select only the ‘onset’ list. If an integer is passed,
will use this number to create an evenly spaced list of events. If None,
will chunk the signal into successive complete blocks of the set duration,
starting at the first sample and including a final full-length block.

events ( list or ndarray or dict ) – Events onset location. If a dict is passed (e.g., from events_find() ),
will select only the ‘onset’ list. If an integer is passed,
will use this number to create an evenly spaced list of events. If None,
will chunk the signal into successive complete blocks of the set duration,
starting at the first sample and including a final full-length block.

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

sampling_rate ( int ) – The sampling frequency of the signal (in Hz, i.e., samples/second).

epochs_start ( int, list ) – Epochs start relative to events_onsets (in seconds). The start can be negative to start
epochs before a given event (to have a baseline for instance). An integer can be specified
to have the same start for all epochs. A list of equal length to the events can be
specified to have a different start for each epoch.

epochs_start ( int, list ) – Epochs start relative to events_onsets (in seconds). The start can be negative to start
epochs before a given event (to have a baseline for instance). An integer can be specified
to have the same start for all epochs. A list of equal length to the events can be
specified to have a different start for each epoch.

epochs_end ( int, list ) – Epochs end relative to events_onsets (in seconds). An integer can be specified to have the
same end for all epochs. A list of equal length to the events can be specified to have a
different end for each epoch. If "from_events" , events must be a dict (from events_find() ). Duration from events will be used as epochs_end .

epochs_end ( int, list ) – Epochs end relative to events_onsets (in seconds). An integer can be specified to have the
same end for all epochs. A list of equal length to the events can be specified to have a
different end for each epoch. If "from_events" , events must be a dict (from events_find() ). Duration from events will be used as epochs_end .

event_labels ( list ) – A list containing unique event identifiers. If None , will use the event index number.

event_labels ( list ) – A list containing unique event identifiers. If None , will use the event index number.

event_conditions ( list ) – An optional list containing, for each event, for example the trial category, group or
experimental conditions.

event_conditions ( list ) – An optional list containing, for each event, for example the trial category, group or
experimental conditions.

baseline_correction ( bool ) – Whether to subtract a baseline computed separately for each epoch. The baseline
extends from the epoch start to time zero. If the epoch starts after zero,
its first sample is used instead. Defaults to False.

baseline_correction ( bool ) – Whether to subtract a baseline computed separately for each epoch. The baseline
extends from the epoch start to time zero. If the epoch starts after zero,
its first sample is used instead. Defaults to False.

dict – A dict containing DataFrames for all epochs.

events_find , events_plot , epochs_to_df , epochs_plot

Example 5 : Epochs with list of starting points

Example 5 : Epochs with list of starting points

epochs ( dict ) – A dict containing one DataFrame per event/trial. Usually obtained via epochs_create() .

epochs ( dict ) – A dict containing one DataFrame per event/trial. Usually obtained via epochs_create() .

legend ( bool ) – Display the legend (the key of each epoch).

legend ( bool ) – Display the legend (the key of each epoch).

columns ( str or list ) – Which columns to plot. If ‘all’, plot all columns. If a list, plot only the columns in the list.

columns ( str or list ) – Which columns to plot. If ‘all’, plot all columns. If a list, plot only the columns in the list.

**kwargs – Other arguments to pass (not used for now).

**kwargs – Other arguments to pass (not used for now).

events_find , events_plot , epochs_create , epochs_to_df

Average epochs and returns the grand average, as well as the SD and the confidence interval.

epochs ( dict ) – A dict containing one DataFrame per event/trial. Usually obtained via epochs_create() .

epochs ( dict ) – A dict containing one DataFrame per event/trial. Usually obtained via epochs_create() .

which ( str or list ) – The name of the column(s) to compute the average from.

which ( str or list ) – The name of the column(s) to compute the average from.

**kwargs – Other arguments to pass (not used for now).

**kwargs – Other arguments to pass (not used for now).

events_find , events_plot , epochs_create , epochs_to_df

TODO: We would like to make it work with uneven epochs (not the same length).

epochs ( dict ) – A dict containing one DataFrame per event/trial. Usually obtained via epochs_create() .

events_find , events_plot , epochs_create , epochs_plot

epochs ( dict ) – A dict containing one DataFrame per event/trial. Usually obtained via epochs_create() .

DataFrame – A DataFrame containing all epochs identifiable by the ‘Label’ column, which time axis
is stored in the ‘Time’ column.

events_find , events_plot , epochs_create , epochs_plot
