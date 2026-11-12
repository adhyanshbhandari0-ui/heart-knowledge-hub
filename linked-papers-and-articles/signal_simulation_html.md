# signal_simulation.html

**Source:** https://neuropsychology.github.io/NeuroKit/examples/signal_simulation/signal_simulation.html

---

Simulate Artificial Physiological Signals

Simulate Artificial Physiological Signals #

This example can be referenced by citing the package .

NeuroKit’s core signal processing functions surround electrocardiogram (ECG), respiratory (RSP), electrodermal activity (EDA), and electromyography (EMG) data. Hence, this example shows how to use NeuroKit to simulate these physiological signals with customized parametric control.

With ecg_simulate() , you can generate an artificial ECG signal of a desired length (in this case here, duration=10 ), noise, and heart rate. As you can see in the plot below, ecg50 has about half the number of heart beats than ecg100 , and ecg50 also has more noise in the signal than the latter.

You can also choose to generate the default, simple simulation based on Daubechies wavelets, which roughly approximates one cardiac cycle, or a more complex one by specifiying method="ecgsyn" .

To simulate a synthetic respiratory signal, you can use rsp_simulate() and choose a specific duration and breathing rate. In this example below, you can see that rsp7 has a lower breathing rate than rsp15 . You can also decide which model you want to generate the signal. The simple rsp15 signal incorporates method = "sinusoidal" which approximates a respiratory cycle based on the trigonometric sine wave. On the other hand, the complex rsp15 signal specifies method = "breathmetrics" which uses a more advanced model by interpolating inhalation and exhalation pauses between each respiratory cycle.

Now, we come to generating an artificial EMG signal using emg_simulate() . Here, you can specify the number of bursts of muscular activity ( n_bursts ) in the signal as well as the duration of the bursts ( duration_bursts ). As you can see the active muscle periods in EMG2_Longer are greater in duration than that of EMG2 , and EMG5 contains more bursts than the former two.

Finally, eda_simulate() can be used to generate a synthetic EDA signal of a given duration, specifying the number of skin conductance responses or activity ‘peaks’ ( n_scr ) and the drift of the signal. You can also modify the noise level of the signal.
