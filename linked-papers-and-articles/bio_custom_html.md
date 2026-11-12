# bio_custom.html

**Source:** https://neuropsychology.github.io/NeuroKit/examples/bio_custom/bio_custom.html

---

This example can be referenced by citing the package .

While NeuroKit is designed to be beginner-friendly, experts who desire to have more control over their own processing pipeline are also offered the possibility to tune functions to their specific usage. This example shows how to use NeuroKit to customize your own processing pipeline for advanced users taking ECG processing as an example.

The Default NeuroKit processing pipeline #

NeuroKit provides a very useful set of functions, *_process() (e.g. ecg_process() , eda_process() , emg_process() , …), which are all-in-one functions that cleans, preprocesses and processes the signals. It includes good and sensible defaults that should be suited for most of users and typical use-cases. That being said, in some cases, you might want to have more control over the processing pipeline.

This is how ecg_process() is typically used:

Now, if you look at the code of ecg_process() (see here for how to explore the code), you can see that it is in fact very simple.

It uses what can be referred to as “mid-level functions”, such as ecg_clean() , ecg_peaks() , ecg_rate() etc.

This means that you can basically re-create the ecg_process() function very easily by calling these mid-level functions:

You can now use this function as you would do with ecg_process() .

Now, you might want to ask, why would you re-create the processing function? Well, it allows you to change the parameters of the inside as you please. Let’s say you want to use a specific cleaning method.

First, let’s look at the documentation for ecg_clean() , you can see that they are several different methods for cleaning which can be specified. The default is the NeuroKit method, however depending on the quality of your signal (and several other factors), other methods may be more appropriate. It is up to you to make this decision.

You can now change the methods as you please for each function in your custom processing function that you have written above:

Similarly, you can select a different method for the peak detection.

It is possible that none of these methods suit your needs, or that you want to test a new method. Rejoice yourself, as NeuroKit allows you to do that by providing what can be referred to as “low-level” functions.

For instance, you can rewrite the cleaning procedure by using the signal processing tools offered by NeuroKit :

You can use this function inside your custom processing written above:

Congrats, you have created your own processing pipeline! Let’s see how it performs:

This doesn’t look bad :) Can you do better?
