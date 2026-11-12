# A multimodal dental dataset facilitating machine learning research and clinic services

**Source:** https://physionet.org/content/multimodal-dental-dataset/1.0.0

---

A multimodal dental dataset facilitating machine learning research and clinic services

liu, w., Huang, Y., & Tang, S. (2023). A multimodal dental dataset facilitating machine learning research and clinic services (version 1.0.0). PhysioNet . RRID:SCR_007345. https://doi.org/10.13026/s5z3-2766

Pollard, T., Moody, B. E., Lehman, L., Gow, B., Fernandes, C., Xie, C., Johnson, A., Mark, R. G., & Heldt, T. (2026). PhysioNet as a global platform for biomedical research. Nature Health. https://doi.org/10.1038/s44360-026-00096-z . Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC13641116/

Oral diseases affect nearly 3.5 billion people, with the majority residing in low- and middle-income countries. Due to limited healthcare resources, many individuals are unable to access proper oral healthcare services. Image-based machine learning technology is one of the most promising approaches to improving oral healthcare services and reducing patient costs. Openly accessible datasets play a crucial role in facilitating the development of machine learning techniques. However, existing dental datasets have limitations such as a scarcity of Cone Beam Computed Tomography (CBCT) data, lack of matched multi-modal data, and insufficient complexity and diversity of the data. This project addresses these challenges by providing a dataset that includes 574 CBCT images from 389 patients, multi-modal data with matching modalities, and images representing various oral health conditions.

According to the "Global Oral Health Status Report" released by the World Health Organization in 2022, nearly half of the world's population (45% or 3.5 billion people) suffers from oral diseases, and three-quarters of them live in low- and middle-income countries [1]. The number of oral disease cases worldwide has increased by 1 billion over the past 30 years, suggesting that many people do not have access to oral disease prevention and treatment services [1]. Due to the large number of patients and the shortage of medical resources, accurate, cheap and easy-to-use disease diagnosis and treatment methods are very important for three purposes: (1) improve dental care services; (2) reduce patient costs; (3) reach more patients , especially those in remote areas. As one of the most promising technologies for improving medical services and reducing health burden, imaging-based machine learning techniques have been widely introduced into the field of dentistry for reconstruction of oral 3D structures, image translation, dental implant detection, etc[2-11]. The development of machine learning cannot be separated from the drive of data， and currently, there is a scarcity of publicly available dental datasets. Even among the existing datasets, there is a lack of sufficient CBCT data, as well as a shortage of multimodal data. In contrast, this dataset provides three of the most commonly used dental imaging data types, including 574 CBCT files.

The research project has been approved by the Ethics Committee of Guilin Medical University. This project is a retrospective study and does not involve recruitment or additional physical risks to the patients. Furthermore, patient identifiers and protected health information have been removed from the data. The research was not affect the daily workflow of the clinic, therefore, the patient informed consent was waived . The dataset consists of data from 389 patients, including 574 CBCT files, 13 panoramic radiographs, and 333 periapical files . The creation process of the dataset involved three steps: (1) data collection, (2) data processing, and (3) technical validation .

This project collected dental image data from adult patients taken at a dental clinic between January 2021 and January 2022. After removing data with poor image quality, we ended up with 574 CBCT files and 13 panoramic radiographs, involving 389 patients. These image files are all stored in the Digital Imaging and Communications in Medicine (DICOM) format [12]. To obtain periapical radiographs of each tooth, multiple X-ray exposures are typically required, which may expose patients to additional radiation. However, in CBCT images, all the necessary information for generating periapical radiographs is already present. Therefore, we extracted the required information from CBCT images and generated corresponding periapical radiographs. In the end, we obtained 333 folder s from 240 patients and generated 29,199 periapical radiographs. The periapical radiographs are stored in TIFF format.

To ensure the protection of patient privacy, we have implemented de-identification measures. Patient demographic information, including gender and age, has been retained, while other sensitive information has been removed or given new values. Patient names and IDs have been replaced with randomly generated new IDs. Other IDs in the files, such as StudyInstanceUID, have also been regenerated. The date of birth has been removed, and other dates, such as study dates, have been replaced with randomly generated dates . For patients' age information, no patients aged over 89 years old appear in the dataset.

All the CBCT images in the data set come from a CBCT machine, which uses a two-dimensional flat panel detector to collect object cone beam ray projection data, scans with a large diameter cone X-ray beam, and performs 180° - 360° synchronous rotation on the plane . The patient's head is used to acquire volumetric image data of the entire scanned area [13]. Then enter the 3D reconstruction through software, and finally generate a 3D image.

A panoramic radiograph also uses a cone-shaped X-ray beam to capture the data of the oral cavity and creates a single flat 2D image of the curved structure of the entire mouth. Compared to traditional CBCT, the panoramic radiograph only generates approximately 1/40 radiation but lacks spatial structure information.

Prior to generating periapical radiographs, we enlisted the help of 13 researchers to label the CBCT files, marking the position of each tooth in each file. The process of generating periapical radiographs can be divided into four steps. Firstly, based on the annotations, the teeth are cropped from the CBCT files, resulting in cubes of size 6 0 mm x 5 0 mm x 50 mm . Secondly, the Siddon-Jacobs ray-tracing algorithm is applied to the cube with rotations to ensure consistent orientation, with the outer side of the face oriented towards the positive y-axis and the teeth oriented towards the positive z-axis. Thridl y, the Insight Segmentation and Registration Toolkit (ITK) imaging package is employed with the Siddon-Jacobs ray-tracing algorithm to simulate the X-ray process by propagating incoming X-ray photons (from the radiation source) through the cube ,adjusting the angle at which the light source strikes, and generating three Images from different angles (20-25 degrees to the left and 5-10 degrees to the left, and 20-25 degrees to the right). Finally, since the typical size of periapical radiographs is often 4 0 mm x 3 0mm , the images are cropped to a size of 4 0 mm x 3 0mm. After checking, 333 files containing 29,199 pictures finally met the requirements.

For CBCT and panoramic radiographs, we utilized the 3D Slicer software tool to open the files and manually inspect the image quality. We had 13 researchers involved in the label process for the CBCT files. They were divided into groups of two, with one person working individually. After completing the labels, the members within each group checked the quality of each other's labels . Finally, one person conducted an overall quality check. After generating the periapical radiographs, a manual quality check was performed, and only the images that met the required standards were retained.

The dataset includes three folders to store image data: CBCT, PaX-ray, and PeX-ray. The corresponding CSV files for these three folders are CBCT_info.csv, PaX_info.csv, and PeX_info.csv. Additionally, there are two additional CSV files named patient_statistics_info.csv and implant_marking.csv.

CBCT: There are a total of 574 CBCT files in the dataset, belonging to 389 different patients. For each patient, there might be multiple files if they had multiple visits. This CBCT files are named using the patient ID and are sorted based on the visitation date with a suffix. For example, "0021_0" indicates the data from the first visit of the patient with ID 21, while "0021_1" represents the data from their second visit. Each CBCT file consists of multiple dcm files (typically 420 files). The path for each dcm file is CBCT/<PatientID_ < suffix number> >/Slice_ <serial number>.dcm .

PaX-ray : Contains 13 panoramic radiographs. Similarly, the files are named using patient IDs, which correspond to the patient IDs in the CBCT dataset. For example, the file "0059_1" in the PaX dataset and the file "0059_0" in the CBCT dataset belong to the same patient. Since the visitation date in the CBCT file is earlier than the visitation date in the PaX file, the suffix for the CBCT file is "0," and the suffix for the PaX file is "1". The same convention applies to data from other patients.  There is a dcm file under each file.  Each file in the PaX dataset has a corresponding dcm file. The path to each dcm file is PaX-ray/<PatientID_< suffix number>>/Slice_0000.dcm.

PeX-ray : Contains 333 files.  Each of the folders contains three subfolders: left, middle, and right, representing three different angles of light exposure. The "left" folder corresponds to a left deviation of 20-25 degrees, the "middle" folder corresponds to a left deviation of 5-10 degrees, and the "right" folder corresponds to a right deviation of 20-25 degrees. Within each of these folders, the periapical radiographs of each tooth are stored in TIFF format. The naming format of the TIFF files is as follows: <number>_<number>. The first digit indicates whether it is an upper or lower jaw image, with 0 representing the lower jaw and 1 representing the upper jaw. The second digit represents the specific tooth number.  For example, 0_0.tif represents the periapical radiograph of the first tooth in the lower jaw. For the convenience of uploading and downloading, each file is compressed into a zip. Notes: To maintain consistency with the lower jaw, the images of the upper jaw have been flipped vertically.

CBCT_info.csv : Each row represents a CBCT file, providing the gender and age of the patient and data associated with the image. The attributes in each row are: PatientID: Patient ID uniquely identifies each patient. PatientSex: Patient gender. PatientAge: Patient age. Modality: The modality of the image. The modality for CBCT is "CT," and the modality for panoramic radiographs is "PX". SliceThickness: Nominal slice thickness, in mm. KVP: Peak kilo voltage output of the x-ray generator used. XRayTubeCurrent: X-ray Tube Current in mA. Rows: Number of rows in the image. Columns: Number of columns in the image. PixelSpacing: Physical distance in the patient between the center of each pixel, specified by a numeric pair - adjacent row spacing (delimiter) adjacent column spacing in mm. BitsAllocated: Number of bits allocated for each pixel sample. BitsStored:  Number of bits stored for each pixel sample. HighBit: Most significant bit for pixel sample data. WindowCenter: Window Center for display. WindowWidth: Window Width for display. FileName: CBCT file name.

PatientID: Patient ID uniquely identifies each patient.

Modality: The modality of the image. The modality for CBCT is "CT," and the modality for panoramic radiographs is "PX".

SliceThickness: Nominal slice thickness, in mm.

KVP: Peak kilo voltage output of the x-ray generator used.

XRayTubeCurrent: X-ray Tube Current in mA.

PixelSpacing: Physical distance in the patient between the center of each pixel, specified by a numeric pair - adjacent row spacing (delimiter) adjacent column spacing in mm.

BitsAllocated: Number of bits allocated for each pixel sample.

BitsStored:  Number of bits stored for each pixel sample.

HighBit: Most significant bit for pixel sample data.

PeX_info.csv : Each row represents data for one oral cavity. The same attributes as those in the CBCT_info file will not be described in detail, and the other attributes are respectively： LeftNum: Number of images owned under the "left" file. MiddleNum: Number of images owned under the "middle" file. RightNum:  Number of images owned under the "right" file. TotalNum: Total number of images under the three folders.

LeftNum: Number of images owned under the "left" file.

MiddleNum: Number of images owned under the "middle" file.

RightNum:  Number of images owned under the "right" file.

TotalNum: Total number of images under the three folders.

patient_statistics_info.csv : From the patient's perspective, each row represents data for one patient. The attributes, excluding those mentioned in the previous files, are as follows: CBCTFileNames:  The filenames of the CBCT image owned by the patient. PaXFileNames: The filenames of the panoramic radiographs owned by the patient. PeXFileNames:  The filenames of the periapical radiographs owned by the patient.

CBCTFileNames:  The filenames of the CBCT image owned by the patient.

PaXFileNames: The filenames of the panoramic radiographs owned by the patient.

PeXFileNames:  The filenames of the periapical radiographs owned by the patient.

implant_marking.csv : Each row represents one CBCT file, and each row has three attribute values: PatientID：Patient ID uniquely identifies each patient. FileName:  CBCT file name. Label: The indication of whether the CBCT image contains dental implants is represented by a value of 0 or 1. A value of 0 signifies that there are no dental implants present in the CBCT image, while a value of 1 indicates the presence of dental implants.

PatientID：Patient ID uniquely identifies each patient.

Label: The indication of whether the CBCT image contains dental implants is represented by a value of 0 or 1. A value of 0 signifies that there are no dental implants present in the CBCT image, while a value of 1 indicates the presence of dental implants.

The folder structure of the dataset is as follows:

Machine learning is one of the most promising technologies for enhancing dental healthcare services, and its development in the field of dentistry relies on the availability of datasets. Currently, there is a scarcity of publicly available dental datasets, particularly in terms of Cone Beam Computed Tomography (CBCT) data, and the lack of multimodal data. This dataset addresses these limitations by providing a large volume of CBCT data and including three of the most common types of dental imaging data. It can be utilized for tasks such as reconstructing 3D oral structures, image translation, dental implant detection, and other related research endeavors[2-11] .

The limitations of the dataset include two aspects. First, there is a scarcity of data for panoramic dental radiographs. Second, the image quality of periapical radiographs is not high.

The authors declare no ethics concerns. This research has been approved by the Ethics Committee of Guilin Medical University. The IRB number is GLMC20230502.

The authors(s) have no conflicts of interest to declare.

https://www.who.int/zh/news/item/18-11-2022-who-highlights-oral-health-neglect-affecting-nearly-half-of-the-world-s-population

Cui Z, Li C, Wang W. ToothNet: automatic tooth instance segmentation and identification from cone beam CT images[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2019: 6368-6377.

Lee D W, Kim S Y, Jeong S N, et al. Artificial intelligence in fractured dental implant detection and classification: evaluation using dataset from two dental hospitals[J]. Diagnostics, 2021, 11(2): 233.

Zhang X, Liang Y, Li W, et al. Development and evaluation of deep learning for screening dental caries from oral photographs[J]. Oral diseases, 2022, 28(1): 173-181.

Hwang J J, Jung Y H, Cho B H, et al. An overview of deep learning in the field of dentistry[J]. Imaging science in dentistry, 2019, 49(1): 1-7.

Nguyen T T, Larrivée N, Lee A, et al. Use of artificial intelligence in dentistry. Current clinical trends and research advances[J]. J Can Dent Assoc, 2021, 87(l7): 1488-2159.

Khanagar S B, Al-Ehaideb A, Maganur P C, et al. Developments, application, and performance of artificial intelligence in dentistry–A systematic review[J]. Journal of dental sciences, 2021, 16(1): 508-522.

Carrillo‐Perez F, Pecho O E, Morales J C, et al. Applications of artificial intelligence in dentistry: A comprehensive review[J]. Journal of Esthetic and Restorative Dentistry, 2022, 34(1): 259-280.

Song W, Liang Y, Yang J, et al. Oral-3d: Reconstructing the 3d structure of oral cavity from panoramic x-ray[C]//Proceedings of the AAAI conference on artificial intelligence. 2021, 35(1): 566-573.

Paavilainen P, Akram S U, Kannala J. Bridging the gap between paired and unpaired medical image translation[C]//Deep Generative Models, and Data Augmentation, Labelling, and Imperfections: First Workshop, DGM4MICCAI 2021, and First Workshop, DALI 2021, Held in Conjunction with MICCAI 2021, Strasbourg, France, October 1, 2021, Proceedings. Cham: Springer International Publishing, 2021: 35-44.

Jang W S, Kim S, Yun P S, et al. Accurate detection for dental implant and peri-implant tissue by transfer learning of faster R-CNN: a diagnostic accuracy study[J]. BMC Oral Health, 2022, 22(1): 1-7.

Afshar P, Heidarian S, Enshaei N, et al. COVID-CT-MD, COVID-19 computed tomography scan dataset applicable in machine learning and deep learning[J]. Scientific Data, 2021, 8(1): 121.

Scarfe W C, Farman A G, Sukovic P. Clinical applications of cone-beam computed tomography in dental practice[J]. Journal-Canadian Dental Association, 2006, 72(1): 75.

2 publications cite this project.
    The most recent are listed below.

MMDental - A multimodal dataset of tooth CBCT images with expert medical records Chengkai Wang, Yifan Zhang, Chengyu Wu et al. Scientific Data ,
        2025.

A multimodal dental dataset facilitating machine learning research and clinic services Yunyou Huang, Wenjing Liu, Caiqin Yao et al. Scientific Data ,
        2024.

Citation data from OpenAlex . Papers that use the project without citing it may be missing.
