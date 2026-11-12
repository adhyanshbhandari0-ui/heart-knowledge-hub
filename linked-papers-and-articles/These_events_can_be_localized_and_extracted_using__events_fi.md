# 
    "These events can be localized and extracted using [events_find()

**Source:** https://neuropsychology.github.io/NeuroKit/functions/events.html

---

Create events dictionnary from list of onsets

event_onsets ( array or list ) – A list of events onset.

event_onsets ( array or list ) – A list of events onset.

event_durations ( array or list ) – A list of durations. If none is passed, will take the duration
between each onset (i.e., will assume that events are consecutive).

event_durations ( array or list ) – A list of durations. If none is passed, will take the duration
between each onset (i.e., will assume that events are consecutive).

event_labels ( list ) – A list containing unique event identifiers. If None , will use the event index number.

event_labels ( list ) – A list containing unique event identifiers. If None , will use the event index number.

event_conditions ( list ) – An optional list containing, for each event, for example the trial category, group or
experimental conditions.

event_conditions ( list ) – An optional list containing, for each event, for example the trial category, group or
experimental conditions.

dict – Dict containing 3 or 4 arrays, "onset" for event onsets, "duration" for event
durations, "label" for the event identifiers and the optional "conditions" passed
to event_conditions .

events_plot , events_to_mne , events_find

Find and select events in a continuous signal (e.g., from a photosensor).

event_channel ( array or list or DataFrame ) – The channel containing the events. If multiple channels are entered, the channels are
handled as reflecting different events new channel is created based on them.

event_channel ( array or list or DataFrame ) – The channel containing the events. If multiple channels are entered, the channels are
handled as reflecting different events new channel is created based on them.

threshold ( str or float ) – The threshold value by which to select the events. If "auto" , takes the value between
the max and the min. If "auto" is used with multi-channel inputs, the default value
of 0.9 is used to capture all events.

threshold ( str or float ) – The threshold value by which to select the events. If "auto" , takes the value between
the max and the min. If "auto" is used with multi-channel inputs, the default value
of 0.9 is used to capture all events.

threshold_keep ( str ) – "above" or "below" , define the events as above or under the threshold. For
photosensors, a white screen corresponds usually to higher values. Therefore, if your
events are signaled by a black colour, events values are the lower ones (i.e., the signal
“drops” when the events onset), and you should set the cut to "below" .

threshold_keep ( str ) – "above" or "below" , define the events as above or under the threshold. For
photosensors, a white screen corresponds usually to higher values. Therefore, if your
events are signaled by a black colour, events values are the lower ones (i.e., the signal
“drops” when the events onset), and you should set the cut to "below" .

start_at ( int ) – Keep events which onset is after a particular time point.

start_at ( int ) – Keep events which onset is after a particular time point.

end_at ( int ) – Keep events which onset is before a particular time point.

end_at ( int ) – Keep events which onset is before a particular time point.

duration_min ( int ) – The minimum duration of an event to be considered as such (in time points).

duration_min ( int ) – The minimum duration of an event to be considered as such (in time points).

duration_max ( int ) – The maximum duration of an event to be considered as such (in time points).

duration_max ( int ) – The maximum duration of an event to be considered as such (in time points).

inter_min ( int ) – The minimum duration after an event for the subsequent event to be considered as such (in
time points). Useful when spurious consecutive events are created due to very high sampling
rate.

inter_min ( int ) – The minimum duration after an event for the subsequent event to be considered as such (in
time points). Useful when spurious consecutive events are created due to very high sampling
rate.

discard_first ( int ) – Discard first or last n events. Useful if the experiment starts with some spurious events.
If discard_first=0 , no first event is removed.

discard_first ( int ) – Discard first or last n events. Useful if the experiment starts with some spurious events.
If discard_first=0 , no first event is removed.

discard_last ( int ) – Discard first or last n events. Useful if the experiment ends with some spurious events.
If discard_last=0 , no last event is removed.

discard_last ( int ) – Discard first or last n events. Useful if the experiment ends with some spurious events.
If discard_last=0 , no last event is removed.

event_labels ( list ) – A list containing unique event identifiers. If None , will use the event index number.

event_labels ( list ) – A list containing unique event identifiers. If None , will use the event index number.

event_conditions ( list ) – An optional list containing, for each event, for example the trial category, group or
experimental conditions. This option is ignored when multiple channels are supplied, as
the function generates these automatically.

event_conditions ( list ) – An optional list containing, for each event, for example the trial category, group or
experimental conditions. This option is ignored when multiple channels are supplied, as
the function generates these automatically.

dict – Dict containing 3 to 5 arrays, "onset" for event onsets, "duration" for event
durations, "label" for the event identifiers, the optional "condition" passed
to event_conditions and the events_channel if multiple channels were supplied
to the function.

events_plot , events_to_mne , events_create

Simulate a trigger signal (e.g., from photosensor)

The second event is an artifact (too short), we can skip it

Combine multiple digital signals into a single channel and its compute its events
The higher the channel, the higher the bit representation on the channel.

Convert the event condition results its human readable representation

events ( list or ndarray or dict ) – Events onset location. Can also be a list of lists, in which case it will mark them with
different colors. If a dict is passed (e.g., from events_find() ), it will only plot
the onsets.

events ( list or ndarray or dict ) – Events onset location. Can also be a list of lists, in which case it will mark them with
different colors. If a dict is passed (e.g., from events_find() ), it will only plot
the onsets.

signal ( array or DataFrame ) – Signal array (can be a dataframe with many signals).

signal ( array or DataFrame ) – Signal array (can be a dataframe with many signals).

color ( str ) – Argument passed to matplotlib plotting.

color ( str ) – Argument passed to matplotlib plotting.

linestyle ( str ) – Argument passed to matplotlib plotting.

linestyle ( str ) – Argument passed to matplotlib plotting.

fig – Figure representing a plot of the signal and the event markers.

Example 4 : Different colors for all events

Example 4 : Different colors for all events

Create MNE compatible events for integration with
M/EEG.

events ( list or ndarray or dict ) – Events onset location. Can also be a dict obtained through events_find() .

events ( list or ndarray or dict ) – Events onset location. Can also be a dict obtained through events_find() .

event_conditions ( list ) – An optional list containing, for each event, for example the trial category, group or
experimental conditions. Defaults to None .

event_conditions ( list ) – An optional list containing, for each event, for example the trial category, group or
experimental conditions. Defaults to None .

tuple – MNE-formatted events and the event id, that can be added
via raw.add_events(events) , and a dictionary with event’s names.
