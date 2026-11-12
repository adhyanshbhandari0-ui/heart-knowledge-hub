# publication

**Source:** https://physionet.org/content/wfdb-python

---

Waveform Database Software Package (WFDB) for Python

Chen Xie , Lucas McCullum , Alistair Johnson , Tom Pollard , Brian Gow , Benjamin Moody

Xie, C., McCullum, L., Johnson, A., Pollard, T., Gow, B., & Moody, B. (2023). Waveform Database Software Package (WFDB) for Python (version 4.1.0). PhysioNet . RRID:SCR_007345. https://doi.org/10.13026/9njx-6322

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

Physiological waveforms - such as electrocardiograms (ECG), electroencephalograms (EEG), electromyograms (EMG) - are generated during the course of routine care. These signals contain information that can be used to understand underlying conditions of health. Effective processing and analysis of physiological data requires specialized software. The waveform-database (WFDB) package for Python is a library of tools for reading, writing, and processing physiological signals and annotations, written in the Python programming language. Core components of the Python package are loosely based on the specifications of the original C-language WFDB software. We aim to implement as many of the core WFDB features as possible, with user-friendly APIs. Additional features are added over time.

Physiological waveforms - such as electrocardiograms (ECG), electroencephalograms (EEG), electromyograms (EMG) - are generated during the course of routine care. These signals contain information that can be used to understand underlying conditions of health. For example, ECGs aid diagnosis of abnormal heart conditions, EEGs aid detection of disorders such as epilepsy, and EMGs aid diagnosis of neuromuscular diseases. Despite the potential utility of waveforms, their complexity and granularity present challenges for retrospective analysis. Effective storage, processing and analysis of physiological signals requires specialized software.

The original Waveform Database (WFDB) Software Package, written in C, provides a large collection of software for processing and analyzing physiological waveforms [1]. Python is an increasingly popular language for data processing and analysis, particularly for tasks such as machine learning [2].

This project describes Waveform Database Software Package (WFDB) for Python, a version of the WFDB Software implemented in Python. Core components of the Python package are loosely based on the specifications of the original C-language WFDB software, but there are significant differences between the two implementations. While there are many benefits to working with the original C-language library, most noticeably in terms of speed, Python may be a more familiar language to some researchers. At its core, the package allows users to import functions that can be used to read physiological signal files and associated annotations, to plot the signals and annotations, and to extract features of interest.

The development version of the WFDB Software for Python is hosted on GitHub [4]. The code follows standard conventions found in the PEP8 Style Guidelines [5]. Unit tests are written to help ensure integrity of code during development. Core packages used in the implementation include:

SciPy, for general scientific support [9]

MatPlotLib, for visual display of signals [10]

There are a few important concepts that should be well understood before using the WFDB software. These concepts include " records" ; " signals , samples , and time" ; and " annotations" . We suggest reviewing the original WFDB documentation for more details on these concepts [1].

The distribution is hosted on PyPI, the package manager for Python [3]. The software can be installed directly from PyPI using the following command:

The development version of the WFDB Software for Python is hosted on GitHub [4]. This repository also contains demo scripts and example data. To install the development version, clone or download the repository, navigate to the base directory, and run:

Once installed, the following example will load a record named "a1031" and plot the waveform to screen. For more examples, please refer to the online documentation [11]:

The source code for the WFDB Software is publicly available on GitHub [4]. If you are a user of the software and encounter issues, then we suggest searching to see if the issue is already tracked on the GitHub repository. If not, then please raise a new issue, clearly describing the problem that you have encountered and what steps you have taken to try to address it. We have limited resources to support the software, and so we encourage community contributions via pull requests.

We also highly recommend reviewing documentation on the original C language implementation of the software [1]. This documentation provides detailed background on various aspects of the WFDB library, including file structures, terminology, and general user guidance.

Development of this Python package has been largely independent of the development of the original WFDB package. As a result, there are significant differences between the two implementations. In future, we hope to more closely align the development processes (for example, making efforts to ensure that behavior is consistent across implementations).

Changes from version 4.0.0 to version 4.1.0:

Converting a record into a Pandas DataFrame ( #380 )

Locating signals in a multi-segment record ( #403 )

Writing custom annotation symbols ( #404 )

Performance improvements when writing annotations ( #406 )

Correct rounding when converting floating-point signal data ( #419 )

Writing signals in compressed format ( #420 )

Decoding non-ASCII text in EDF files ( #429 )

Bug fixes when writing signal metadata ( #424 )

Documentation updates ( #401 , #407 , #433 , #437 )

The distribution is hosted on PyPI, the package manager for Python [3]. For the latest stable version of the software, we highly recommend referring to PyPI. For the latest development versions, please refer to GitHub [4].

This project contains example data from numerous databases that were previously published on PhysioNet and elsewhere.  Many of these example files were originally collected from clinical studies and were de-identified at the time they were published.  We do not believe these example files contain personally identifying information of any individual.

Development of this software was supported by the National Institute of Biomedical Imaging and Bioengineering (NIBIB) under NIH grant number R01EB030362.

The authors have no conflicts of interest to declare.

Documentation for WFDB Python. https://wfdb.readthedocs.io/en/latest/ [Accessed: 1 March 2021]

Scikit-learn: Machine Learning in Python, Pedregosa et al. (2011) Journal of Machine Learning Research (JMLR). Volume 12, pp. 2825-2830.

Moody, G., Pollard, T., & Moody, B. (2021). WFDB Software Package (version 10.6.2). PhysioNet. https://doi.org/10.13026/zzpx-h016.

Van Rossum, G., & Drake, F. L. (2009). Python 3 Reference Manual. Scotts Valley, CA: CreateSpace.

WFDB on PyPI. https://pypi.python.org/pypi/wfdb/ [Accessed: 1 March 2021]

WFDB Python on GitHub. https://github.com/MIT-LCP/wfdb-python [Accessed: 1 March 2021]

Style Guide for Python (PEP8). https://www.python.org/dev/peps/pep-0020/ [Accessed: 1 March 2021]

Harris, C.R., Millman, K.J., van der Walt, S.J. et al. Array programming with NumPy. Nature 585, 357–362 (2020). https://doi.org/0.1038/s41586-020-2649-2

McKinney, Proceedings of the 9th Python in Science Conference, Volume 445, 2010. https://doi.org/10.25080/Majora-92bf1922-00a

Virtanen P, Gommers R, Oliphant T, ... and SciPy 1.0 Contributors. (2020) SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. Nature Methods, 17(3), 261-272. https://doi.org/10.1038/s41592-019-0686-2

John D. Hunter (2007) Matplotlib: A 2D Graphics Environment, Computing in Science & Engineering, 9, 90-95. https://doi.org/10.1109/MCSE.2007.55

39 publications cite this project.
    The most recent are listed below.

BLiSS: A Beat-Local, Signal-Quality-Informed Kalman Smoother for ECG Denoising under Non-Stationary Muscle Artifact, with Ectopic-Beat Reconstruction Assessment Khanh Duy Tran. Research Square ,
        2026.

Physiology-augmented deep representations improve cross-database electrocardiogram beat classification under unseen-domain shift Mujahid Shahid¹, Oliver Konyo. Research Square ,
        2026.

Multiscale Statistical Process Control of RR Interval Dynamics for Explainable Pre-Onset Characterization of Paroxysmal Atrial Fibrillation Michel Alexander Castañeda Alarcón, Javier Díaz-Carmona, Horacio Rostro‐González et al. World Congress on Medical Physics and Biomedical Engineering, September 7 - 12, 2009, Munich, Germany ,
        2026.

Vitabel: A Python Framework for Visualizing and Labelling High-Resolution Physiological Data for Critical Care Machine Learning Simon Orlob, Wolfgang J. Kern, Benjamin Hackl et al. Journal of Medical Systems ,
        2026.

Croissant Baker: Metadata Generation for Discoverable, Governable, and Reusable ML Datasets Rafi Al Attrach, Rajna Fani, Sebastian Lobentanzer et al. arXiv (Cornell University) ,
        2026.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

Download
              the ZIP file (99.4 MB)

Download with the PhysioNet Python package : physionet download wfdb-python --version 4.1.0

Download the files using your terminal: wget -r -N -c -np https://physionet.org/files/wfdb-python/4.1.0/

Download the files using AWS command line tools: aws s3 sync --no-sign-request s3://physionet-open/wfdb-python/4.1.0/ DESTINATION
