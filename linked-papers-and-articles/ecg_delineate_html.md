# ecg_delineate.html

**Source:** https://neuropsychology.github.io/NeuroKit/examples/ecg_delineate/ecg_delineate.html

---

This example can be referenced by citing the package .

This example shows how to use NeuroKit to delineate the ECG peaks in Python using NeuroKit. This means detecting and locating all components of the QRS complex, including P-peaks and T-peaks , as well their onsets and offsets from an ECG signal.

In this example, we will use a short segment of ECG signal with sampling rate of 3000 Hz.

The ecg_peaks() function will return a dictionary contains the samples at which R-peaks are located.

Let’s visualize the R-peaks location in the signal to make sure it got detected correctly.

Visually, the R-peaks seem to have been correctly identified. You can also explore searching for R-peaks using different methods provided by NeuroKit ecg_peaks() .

Locate other waves (P, Q, S, T) and their onset and offset #

In ecg_delineate() , NeuroKit implements different methods to segment the QRS complexes. There are the derivative method and the other methods that make use of Wavelet to delineate the complexes.

First, let’s take a look at the ‘peak’ method and its output.

Visually, the ‘peak’ method seems to have correctly identified the P-peaks, Q-peaks, S-peaks and T-peaks for this signal, at least, for the first few complexes. Well done, peak !

However, it can be quite tiring to be zooming in to each complex and inspect them one by one. To have a better overview of all complexes at once, you can make use of the show argument in ecg_delineate() as below.

The ‘peak’ method is doing a glamorous job with identifying all the ECG peaks for this piece of ECG signal.

On top of the above peaks, the peak method also identify the wave boundaries, namely the onset of P-peaks and offset of T-peaks. You can vary the argument show_type to specify the information you would like plot.

Both the onsets of P-peaks and the offsets of T-peaks appears to have been correctly identified here. This information will be used to delineate cardiac phases in ecg_phase() .

Let’s next take a look at the continuous wavelet method.

By specifying ‘all’ in the show_type argument, you can plot all delineated information output by the cwt method. However, it could be hard to evaluate the accuracy of the delineated information with everyhing plotted together. Let’s tease them apart!

Unlike the peak method, the continuous wavelet method does not idenfity the Q-peaks and S-peaks. However, it provides more information regarding the boundaries of the waves

Visually, except a few exception, CWT method is doing a great job. However, the P-waves boundaries are not very clearly identified here.

Last but not least, we will look at the third method in NeuroKit ecg_delineate() function: the discrete wavelet method.

Discrete Wavelet Method (DWT) - default method #

Visually, from the plots above, the delineated outputs of DWT appear to be more accurate than CWT, especially for the P-peaks and P-wave boundaries.

Overall, for this signal, the peak and DWT methods seem to be superior to the CWT.
