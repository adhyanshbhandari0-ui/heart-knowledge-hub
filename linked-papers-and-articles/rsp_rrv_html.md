# rsp_rrv.html

**Source:** https://neuropsychology.github.io/NeuroKit/examples/rsp_rrv/rsp_rrv.html

---

This example can be referenced by citing the package .

Respiratory Rate Variability (RRV), or variations in respiratory rhythm, are crucial indices of general health and respiratory complications. This example shows how to use NeuroKit to perform RRV analysis.

Download Data and Extract Relevant Signals #

In this example, we will download a dataset that contains electrocardiogram, respiratory, and electrodermal activity signals, and extract only the respiratory (RSP) signal.

You now have the raw RSP signal in the shape of a vector (i.e., a one-dimensional array). You can then clean it using rsp_clean() and extract the inhalation peaks of the signal using rsp_peaks() . This will output 1) a dataframe indicating the occurrences of inhalation peaks and exhalation troughs (“1” marked in a list of zeros), and 2) a dictionary showing the samples of peaks and troughs.

Note: As the dataset has a frequency of 100Hz, make sure the sampling_rate is also set to 100Hz. It is critical that you specify the correct sampling rate of your signal throughout all the processing functions.

Now that we have extracted the respiratory rate signal and the peaks dictionary, you can then input these into rsp_rrv() . This outputs a variety of RRV indices including time domain, frequency domain, and nonlinear features. Examples of time domain features include RMSSD (root-mean-squared standard deviation) or SDBB (standard deviation of the breath-to-breath intervals). Power spectral analyses (e.g., LF, HF, LFHF) and entropy measures (e.g., sample entropy, SampEn where smaller values indicate that respiratory rate is regular and predictable) are also examples of frequency domain and nonlinear features respectively.

A Poincaré plot is also shown when setting show=True , plotting each breath-to-breath interval against the next successive one. It shows the distribution of successive respiratory rates.

This is a simple visualization tool for short-term (SD1) and long-term variability (SD2) in respiratory rhythm.
