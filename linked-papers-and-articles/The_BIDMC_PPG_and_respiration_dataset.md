# The BIDMC PPG and respiration dataset

**Source:** https://physionet.org/content/bidmc/1.0.0

---

Marco Pimentel , Alistair Johnson , Peter Charlton , David Clifton

New Database Added: BIDMC (June 20, 2018, midnight) This dataset contains signals and numerics extracted from the much larger MIMIC-II matched waveform Database, along with manual breath annotations made from two annotators, using the impedance respiratory signal.

This dataset contains signals and numerics extracted from the much larger MIMIC-II matched waveform Database, along with manual breath annotations made from two annotators, using the impedance respiratory signal.

Pimentel, M.A.F. et al. Towards a Robust Estimation of Respiratory Rate from Pulse Oximeters. IEEE Transactions on Biomedical Engineering, 64(8), pp.1914-1923, 2016. [DOI: 10.1109/TBME.2016.2613124](http://doi.org/10.1109/TBME.2016.2613124) . https://ieeexplore.ieee.org/document/7748483/

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

This dataset contains signals and numerics extracted from the much larger MIMIC II matched waveform Database , along with manual breath annotations made from two annotators, using the impedance respiratory signal.

The original data was acquired from critically-ill patients during hospital care at the Beth Israel Deaconess Medical Centre (Boston, MA, USA). Two annotators manually annotated individual breaths in each recording using the impedance respiratory signal. The 53 recordings within the dataset, each of 8-minute duration, each contain:

Physiological signals, such as the PPG, impedance respiratory signal, and electrocardiogram (ECG). These are sampled at 125 Hz.

Physiological parameters, such as the heart rate (HR), respiratory rate (RR), and blood oxygen saturation level (SpO2). These are sampled at 1 Hz.

This dataset was first reported in the referenced publication, in which the data was used to evaluate the performance of different algorithms for estimating respiratory rate from the pulse oximetry, or photoplethysmogram (PPG) signal.

The dataset is distributed in three formats:

WFDB (WaveForm DataBase) format, which is the standard format used by PhysioNet.

Matlab (r) format, in a manner which is a compatible with the RRest Toolbox of respiratory rate algorithms

Five files are provided for each recording (where ## is the subject number):

bidmc##.breath: Manual breath annotations

Further details on the contents of each file are provided here

Separate CSV files are provided for each recording (where ## is the subject number), containing:

bidmc_##_Breaths.csv: Manual breath annotations

bidmc_##_Signals.csv: Physiological signals

bidmc_##_Numerics.csv: Physiological parameters

The *bidmc_data.mat* file contains the following subset of the dataset in a single Matlab (r) variable named *data*. The following are provided for each of the 53 recordings:

ekg: Lead II ECG signal. Each signal is provided in a structure, where the *v* field denotes the signal values, and *fs* is the sampling frequency.

ref.resp_sig.imp: Impedance respiratory signal

ref.breaths: Manual annotations of breaths provided by two independent annotators. A vector of sample numbers is provided, which correspond to the signal sample numbers.

ref.params: Physiological parameters: rr (respiratory rate, derived by the monitor from the impedance signal, breaths per minute), hr (heart rate, derived from the ECG, beats per minute), pr (pulse rate, derived from the PPG, beats per minute), spo2 (blood oxygen saturation level, %).

fix: A structure of fixed variables, including: id (the MIMIC II matched waveform database subject ID and recording identifier), loc (the ward location), and source (the URLs from which the original data were downloaded).

12 publications cite this project.
    The most recent are listed below.

IoT-Enabled Healthcare Management: Enhancing Patient Monitoring and Service Delivery Smart Healthcare Management Through Internet of Things Technologies Siddhartha Saini, Dr. Ajay Rana, Arun Kumar Rana. Computer and decision making. ,
        2026.

Context-Augmented, Session-Calibrated Blood Pressure Tracking from Photoplethysmography Farouk Ganiyu Adewumi, Timothy Oladunni. arXiv (Cornell University) ,
        2026.

Detecting Neurovascular Instability from Multimodal Physiological Signals Using Wearable-Compatible Edge AI: A Responsible Computational Framework Truong Quynh Hoa, Hoàng Đình Cường, Truong Xuan Khanh. arXiv (Cornell University) ,
        2026.

High-Altitude Pilot Physiological Monitoring Dataset: Respiratory Performance and SpO₂ Analysis Chunyang Jia, Meng Yang, Chuangang Zhao. Scientific Data ,
        2026.

An Intelligent IoT and AI Framework for Real-Time Remote Patient Monitoring and Healthcare Management Sri Lekha Bandla, Binitkumar M Vaghani. International Journal of Artificial Intelligence and Machine Learning ,
        2026.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.

Download
              the ZIP file (207.8 MB)

Download with the PhysioNet Python package : physionet download bidmc --version 1.0.0

Download the files using your terminal: wget -r -N -c -np https://physionet.org/files/bidmc/1.0.0/

To download the files using AWS command line tools, first configure your AWS credentials .
