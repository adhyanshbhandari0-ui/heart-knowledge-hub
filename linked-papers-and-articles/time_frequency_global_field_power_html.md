# time_frequency_global_field_power.html

**Source:** https://mne.tools/dev/auto_examples/time_frequency/time_frequency_global_field_power.html

---

Go to the end to download the full example code or to run this example in your browser via JupyterLite.

Explore event-related dynamics for specific frequency bands #

The objective is to show you how to explore spectrally localized
effects. For this purpose we adapt the method described in [ 1 ] and use it on the somato dataset.
The idea is to track the band-limited temporal evolution
of spatial patterns by using the global field power (GFP).

We first bandpass filter the signals and then apply a Hilbert transform. To
reveal oscillatory activity the evoked response is then subtracted from every
single trial. Finally, we rectify the signals prior to averaging across trials
by taking the magnitude of the Hilbert.
Then the GFP is computed as described in [ 2 ] , using the sum of the
squares but without normalization by the rank.
Baselining is subsequently applied to make the GFP comparable
between frequencies.
The procedure is then repeated for each frequency band of interest and
all GFPs are visualized. To estimate uncertainty, non-parametric
confidence intervals are computed as described in [ 3 ] across channels.

The advantage of this method over summarizing the Space × Time × Frequency
output of a Morlet Wavelet in frequency bands is relative speed and, more
importantly, the clear-cut comparability of the spectral decomposition (the
same type of filter is used across all bands).

Riitta Hari and Riitta Salmelin. Human cortical oscillations: a neuromagnetic view through the skull. Trends in Neurosciences , 20(1):44–49, 1997. doi:10.1016/S0166-2236(96)10065-5 .

Denis A. Engemann and Alexandre Gramfort. Automated model selection in covariance estimation and spatial whitening of MEG and EEG signals. NeuroImage , 108:328–342, 2015. doi:10.1016/j.neuroimage.2014.12.040 .

Bradley Efron and Trevor Hastie. Computer Age Statistical Inference: Algorithms, Evidence, and Data Science . Number 5 in Institute of Mathematical Statistics Monographs. Cambridge University Press, New York, 2016. ISBN 978-1-107-14989-2. URL: https://hastie.su.domains/CASI/ .

We create average power time courses for each frequency band

Now we can compute the Global Field Power
We can track the emergence of spatial patterns compared to baseline
for each frequency band, with a bootstrapped confidence interval.

We see dominant responses in the Alpha and Beta bands.

Total running time of the script: (0 minutes 7.768 seconds)

Download Jupyter notebook: time_frequency_global_field_power.ipynb

Download Python source code: time_frequency_global_field_power.py

Download zipped: time_frequency_global_field_power.zip
