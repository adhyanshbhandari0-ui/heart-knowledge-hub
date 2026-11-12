# WFDB Software Package

**Source:** https://www.physionet.org/content/wfdb

---

George Moody , Tom Pollard , Benjamin Moody

Moody, G., Pollard, T., & Moody, B. (2022). WFDB Software Package (version 10.7.0). PhysioNet . RRID:SCR_007345. https://doi.org/10.13026/gjvw-1m31

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

Effective processing and analysis of physiological data requires specialized software. We have developed a large collection of such software over the past thirty years, and much of it is contained within the WFDB (Waveform Database) Software Package. The WFDB Software Package comprises over 70 applications for signal processing and automated analysis. A comprehensive collection of documentation, including tutorials and reference manuals, is also included in the package. The package is written in highly portable C and can be used on all popular platforms, including GNU/Linux, MacOS, MS-Windows, and all versions of Unix. The package has also been ported to other popular languages, including Matlab and Python.

Physiological waveforms - such as electrocardiograms ( ECG ), electroencephalograms ( EEG ), and electromyograms ( EMG ) - are frequently measured during the course of routine patient care. These signals contain information that can be used to understand underlying conditions of health. For example, ECGs aid diagnosis of abnormal heart conditions, EEGs aid detection of disorders such as epilepsy, and EMGs aid diagnosis of neuromuscular diseases. Despite the potential utility of waveforms, their complexity and granularity present challenges for retrospective analysis. Effective storage, processing and analysis of physiological signals requires specialized software.

Established in 1999, PhysioNet has provided researchers, clinicians, educators, and students with free access to large collections of physiological signals for research and education. Many of the signals are accompanied by detailed annotations that mark the locations of individual events, such as heart beats and alarms. One of the first of such signal collections was the MIT-BIH Arrhythmia Database, a publicly available set of standard test material for evaluation of arrhythmia detectors [1,2]. Other examples of high cadence physiological signals on PhysioNet include the Non-Invasive Fetal ECG Arrhythmia Database and PTB-XL, a large publicly available electrocardiography database [3,4].

The WFDB (Waveform Database) Software Package has been developed over the past thirty years, providing a large collection of software for processing and analyzing physiological waveforms. The package is written in highly portable C and can be used on all popular platforms, including GNU/Linux, MacOS X, MS-Windows, and all versions of Unix.

The foundation of the WFDB Software Package is the WFDB library, consisting of a set of functions for reading and writing digitized signals and annotations. These functions can be used by programs written in C, C++, or Fortran, running under any operating system for which an ANSI/ISO C compiler is available, including all versions of Unix, MS-DOS, MS-Windows, the Macintosh OS, and VMS.

The WFDB library makes use of two other libraries (optional, but strongly recommended):

The libFLAC library [5] is used for reading and writing compressed signal files.

The libcurl library [6] is used for reading input files directly from a web server, such as PhysioNet, without downloading and storing the entire record locally.

The WFDB library is documented by the WFDB Programmer’s Guide [7]. Texinfo sources for the WFDB Programmer’s Guide are included in the doc/wpg-src directory of the WFDB Software Package.

A large collection of interoperable command-line tools for signal processing and automated analysis is included in the app , convert , and psd directories of the WFDB Software Package. These applications are described in the WFDB Applications Guide [8]. The troff (Unix man page) sources for the WFDB Applications Guide are included in the doc/wag-src directory.

Two American National Standards, ANSI / AAMI EC38:1998 (Ambulatory Electrocardiographs) and ANSI / AAMI EC57:1998 (Testing and Reporting Performance Results of Cardiac Rhythm and ST Segment Measurement Algorithms) require the use of several of the WFDB applications for evaluation of certain devices and algorithms. For details, see Evaluating ECG Analyzers in the WFDB Applications Guide [8].

There are a few important concepts that should be well understood before using the WFDB software. These concepts include records ; signals , samples , and time ; and annotations .

The databases for which the WFDB library was designed consist of a number of records. Each record contains a continuous recording from a single subject, which might be only a few seconds or might be multiple days in length. A typical application program accesses only a single record, and in most cases, it reads the record in order from beginning to end. Each record is identified by a name consisting of letters, digits, and/or underscores. For example, record names in the MIT-BIH Arrhythmia Database are three-digit numbers [1,2].

Case is significant in record names that contain letters, even in environments such as MS-Windows for which case translation is normally performed by the operating system on file names; thus ‘e0104’ is the name of a record found in the European ST-T Database, whereas ‘E0104’ is not [9]. A record is made up of several files, which contain signals, annotations, and specifications of signal attributes; each file belonging to a given record normally includes the record name as the first part of its name. A record is an extensible collection of files, which need not all be located in the same directory, or even on the same physical device.

Signals are commonly understood to be functions of time obtained by observation of physical variables. In our case, a signal is defined more restrictively as a finite sequence of integer samples, usually obtained by digitizing a continuous observed function of time at a fixed sampling frequency expressed in Hz (samples per second). The time interval between any pair of adjacent samples in a given signal is a sample interval; all sample intervals for a given signal are equal. The integer value of each sample is usually interpreted as a voltage, and the units are called analog-to-digital converter units, or adu. The gain defined for each signal specifies how many adus correspond to one physical unit (usually one millivolt, the nominal amplitude of a normal QRS complex on a body-surface ECG lead roughly parallel to the mean cardiac electrical axis). All signals in a given record are usually sampled at the same frequency, but not necessarily at the same gain. Records in the MIT-BIH Arrhythmia Database are sampled at 360 Hz; other database records may be sampled at 250 Hz or even 500 Hz.

The sample number is an attribute of a sample, defined as the number of samples of the same signal that precede it; thus the sample number of the first sample in each signal is zero. The units of time are sample intervals; hence the “time” of a sample is synonymous with its sample number.

Samples having the same sample number in different signals of the same record are treated as simultaneous. In truth, they are usually not precisely simultaneous, since most multi-channel digitizers sample signals in “round-robin” fashion. If this subtlety makes a difference to you, you should be prepared to compensate for inter-signal sampling skew in your programs.

Annotation files provide additional information about a record, for example providing beat labels or highlighting when an alarm was triggered. The “time” of an annotation is simply the sample number of the sample with which the annotation is associated. Annotations may be associated with a single signal, if desired. No more than one annotation in a given annotation file may be associated with any given sample of any given signal. There may be many annotation files associated with the same record, however; they are distinguished by annotator names. The annotator name ‘atr’ is reserved to identify reference annotation files supplied by the developers of the databases to document correct beat labels. You may use other annotator names (which may contain letters, digits and underscores, as for record names) to identify annotation files that you create. You may wish to adopt the convention that the annotator name is the name of the file’s creator (a program or a person).

Annotations are visible to the WFDB library user as C structures, the fields of which specify time, beat type, and several user-definable variables. The WFDB library performs efficient conversions between these structures and a compact bit-packed representation used for storage of annotations in annotation files.

The process for installing the package is the same on all platforms, and is outlined in brief below. For more detailed installation instructions, see the INSTALL file.

Install any prerequisites needed for your platform . These include the following, which are free (open-source) software and available for all popular platforms: A C compiler such as gcc (the GNU Compiler Collection) The standard Unix make tool The libFLAC library [5] The libcurl library [6]

A C compiler such as gcc (the GNU Compiler Collection)

Download and unpack the WFDB Software Package . Versions for all platforms are built from a single package of portable sources, which is available as a gzip-compressed tar archive ( GPG signature ).

Configure the package for your system . The configure script creates a customized building procedure for your system. Run the commands: tar xfz wfdb-10.7.0.tar.gz
cd wfdb-10.7.0
./configure For more choices, such as where to install the package, you can run ./configure --interactive .

Make and verify a test build . The package includes a set of test scripts that are run to verify basic operations of the WFDB library and many of the applications, permitting them to be tested before installation: make

Make, install, and test a final build : sudo make install
make check

Detailed documentation for the WFDB software is available online [7,8]. For convenience, PDF versions of the documentation are included in this project.

The WFDB Applications Guide (wag.pdf) consists of UNIX-style man pages that describe the applications included in the WFDB Software Package.

The WFDB Programmer’s Guide (wpg.pdf) describes how to write C-language programs that use the WFDB library to read and write signals and annotations.

Every version of the WFDB Software Package is compatible with previous versions, so applications that were written using an older version of WFDB will continue to work with the current version. New features (such as support for new file formats) are added periodically, and in most cases, applications will not require any changes to take advantage of these features.

Major changes in the WFDB 10.7 series include the following:

WFDB 10.7.0 introduces support for signal files that are compressed using the FLAC format. You will need to have the libFLAC library installed in order to read and write compressed signal files. Compressed signal files are denoted by a format code of 508, 516, or 524. The WFDB library and applications can handle very long-duration records (more than 2 31 sample intervals in length), even on systems where a long integer is 32 bits. If your program needs to handle long-duration records, you should add #define WFDB_LARGETIME to the top of your program source file. This release also introduces macros that can be used for parsing and displaying numeric values, such as WFDB_Pd_SAMP and WFDB_Si_TIME .

WFDB 10.7.0 introduces support for signal files that are compressed using the FLAC format. You will need to have the libFLAC library installed in order to read and write compressed signal files. Compressed signal files are denoted by a format code of 508, 516, or 524.

The WFDB library and applications can handle very long-duration records (more than 2 31 sample intervals in length), even on systems where a long integer is 32 bits. If your program needs to handle long-duration records, you should add #define WFDB_LARGETIME to the top of your program source file.

This release also introduces macros that can be used for parsing and displaying numeric values, such as WFDB_Pd_SAMP and WFDB_Si_TIME .

For a more complete list of changes since version 10.0.0, see the NEWS file.

Sources for the WFDB Software Package, including past versions, are available on GitHub [10]. If you are a user of the software and encounter issues, then we suggest searching to see if the issue is already tracked on the GitHub repository. If not, then please raise a new issue, clearly describing the problem that you have encountered and what steps you have taken to try to address it. We welcome and encourage community contributions (including new features, bug fixes, and documentation improvements) via GitHub pull requests.

This package contains small examples of physiological signal data that were collected from human subjects and previously published, in de-identified form, as part of the MIT-BIH Arrhythmia Database [1] and the MIMIC Database [11]. These examples do not contain any personally identifiable information.

The algorithms included in this package were designed and optimized based on these and other open-access, de-identified databases published on PhysioNet. These algorithms do not contain personally identifiable information of any individual.

Many people have contributed to the development of the WFDB library. Thanks to Paul Albrecht, Ted Baker, Phil Devlin, Scott Greenwald, Thomas Heldt, Isaac Henry, David Israel, Roger Mark, Joe Mietus, Warren Muldrow, Ikaro Silva, Wei Zong, and especially to Paul Schluter, whose elegant 8080 assembly language functions inspired these (long live getann !). Pat Hamilton and Bob Farrell contributed ports, to classic Mac OS and the MS 32-bit Windows environments, respectively. Jose Garcia Moros and Salvador Olmos contributed Matlab/Octave reimplementations of a useful subset of the WFDB library. Jonas Carlson wrote, documented, and contributed a set of Matlab wrappers for the WFDB library, and Michael Craig created and contributed the original WFDB Toolbox for Matlab. Isaac Henry contributed SWIG wrappers that provide interfaces for a variety of scripting languages, as well as a set of translations of the C example programs in this guide into the languages supported by the SWIG wrappers. Mike Dakin provided the first implementation of NETFILES (HTTP client support in the WFDB library) based on the W3C’s libwww .

Bug reports (and in some cases fixes) have been contributed by Omar Abdala, Winton Baker, David Brooks, Bob Farrell, Virginia Faro-Maza, Ion Gaztañaga, Fred Geheb, Mathias Gruber, Thomas Heldt, Isaac Henry, Justin Leo Chang Loong, Guido Muesch, Joonas Paalasmaa, Tony Ricke, Dave Schaffer, Dan Scott, Allavatam Venugopal, Mauro Villarroel, Andrew Walsh, Piotr Wlodarek, Chen Xie, and Yinqi Zhang.

Development of this software was supported by the National Institute of Biomedical Imaging and Bioengineering (NIBIB) under NIH grant number R01EB030362.

The authors declare that they have no conflicts of interest.

Moody, G. B. and Mark, R.G. (2005). MIT-BIH Arrhythmia Database (version 1.0.0). PhysioNet. https://doi.org/10.13026/C2F305

Moody, G. B. and Mark, R. G. (2001). The impact of the MIT-BIH Arrhythmia Database. IEEE Engineering in Medicine and Biology Magazine, 20(3), 45-50. https://doi.org/10.1109/51.932724

Behar, J. (2020). Non-Invasive Fetal ECG Arrhythmia Database (version 1.0.0). PhysioNet. https://doi.org/10.13026/C2CT0S

Wagner, P., Strodthoff, N., Bousseljot, R., Samek, W., & Schaeffter, T. (2020). PTB-XL, a large publicly available electrocardiography dataset (version 1.0.1). PhysioNet. https://doi.org/10.13026/x4td-x982.

The libFLAC library. https://xiph.org/flac/ [Accessed: 10 June 2022]

The libcurl library. https://curl.se/ [Accessed: 10 June 2022]

WFDB Programmer's Guide (HTML). https://archive.physionet.org/physiotools/wpg/wpg.htm [Accessed: 1 March 2021]

WFDB Applications Guide (HTML). https://archive.physionet.org/physiotools/wag/wag.htm [Accessed: 1 March 2021]

Taddei, A., Distante, G., Emdin, M., Pisani, P., Moody, G. B., Zeelenberg, C., Marchesi C. (2009). European ST-T Database (version 1.0.0). PhysioNet. https://doi.org/10.13026/C2D59Z

The Waveform Database Software Package on GitHub. https://github.com/bemoody/wfdb [Accessed: 1 March 2021]

Moody, G. and Mark, R.G. (2000). MIMIC Database (version 1.0.0). PhysioNet. https://doi.org/10.13026/C2JS34

18 publications cite this project.
    The most recent are listed below.

Multiscale Statistical Process Control of RR Interval Dynamics for Explainable Pre-Onset Characterization of Paroxysmal Atrial Fibrillation Michel Alexander Castañeda Alarcón, Javier Díaz-Carmona, Horacio Rostro‐González et al. World Congress on Medical Physics and Biomedical Engineering, September 7 - 12, 2009, Munich, Germany ,
        2026.

An OMOP Common Data Model pipeline for electrocardiography dataset integration by standardizing signal metadata and heart rate variability features Pierluigi Reali, Valentina Tibollo, Gaia Riboni et al. Frontiers in Bioinformatics ,
        2026.

Cross-domain transfer learning strategy enhances interpretability of deep learning model explanations Matteo Zannini, Alexander Hammer, Hagen Malberg et al. Scientific Reports ,
        2026.

Analýza a vizualizace databází se zaměřením na krevní tlak Ondřej Lakota. DSpace VŠB-TUO (VŠB-TUO) ,
        2026.

Multimodal deep learning for acute myocardial infarction detection from 12-lead electrocardiogram: a multi-centre study with cross-hospital validation Vibha Gupta, Lukas Hilgendorf, Erik Andersson et al. European Heart Journal - Digital Health ,
        2025.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

Download
              the ZIP file (3.8 MB)

Download with the PhysioNet Python package : physionet download wfdb --version 10.7.0

Download the files using your terminal: wget -r -N -c -np https://physionet.org/files/wfdb/10.7.0/

Download the files using AWS command line tools: aws s3 sync --no-sign-request s3://physionet-open/wfdb/10.7.0/ DESTINATION
