# BIRL

**Source:** http://borda.github.io/BIRL

---

BIRL: Benchmark on Image Registration methods with Landmark validation

This project/framework is the key component of Automatic Non-rigid Histological Image Registration (ANHIR) challenge hosted at ISBI 2019 conference. The related discussion is hosted on forum.image.sc .

The project contains a set of sample images with related landmark annotations and experimental evaluation of state-of-the-art image registration methods.

The initial dataset of stained histological tissues is composed by image pairs of related sections (mainly, consecutive cuts).
Each image in the pair is coloured with a different stain.
The registration of those images is a challenging task due to both artefacts and deformations acquired during sample preparation and appearance differences due to staining.
For evaluation, we have manually placed landmarks in each image pair. There are at least 40 uniformly spread over the tissue.
We do not put any landmarks in the background.
For more information about annotation creation and landmarks handling, we refer to the special repository - Dataset: histology landmarks .

The dataset is defined by a CSV file containing paths to target and sensed image and their related landmarks (see ./data-images/pairs-imgs-lnds_mix.csv ) . With the change of the cover table, the benchmarks can be used for any other image dataset.

List of the main/key features of this package:

automatic execution of image registration of a sequence of image pairs

integrated evaluation of registration performances using Target Registration Error (TRE)

integrated visualization of performed registration

running several image registration experiment in parallel

resuming unfinished sequence of registration benchmark

handling around dataset and creating own experiments

using basic image pre-processing - normalizing

rerun evaluation and visualisation for finished experiments

The project contains the following folders:

benchmarks - package with benchmark & template and general useful utils utilities - useful tools and functions

bm_ANHIR - scripts related directly to ANHIR challenge

bm_dataset - package handling dataset creation and servicing

bm_experiments - package with particular benchmark experiments

configs - configs for registration methods

data-images - folder with input sample data images - sample image pairs (reference and sensed one) landmarks - related landmarks to images in previous folder lesions_ - samples of histology tissue with annotation rat-kidney_ - samples of histology tissue with annotation

images - sample image pairs (reference and sensed one)

landmarks - related landmarks to images in previous folder

lesions_ - samples of histology tissue with annotation

rat-kidney_ - samples of histology tissue with annotation

docs - sphinx documentation and references

scripts - scripts and macros (ImageJ/Python/Rscript) for registration and work around

tests - package testing and test requirements

This package can be simply install using pip running

or via setuptools running from a local folder

For installing some particular version/releases use following links https://github.com/Borda/BIRL/archive/v0.2.3.zip where the numbers match desired version
(see package releases ).

In the data-images folder we provide some sample images with landmarks for registration.
These sample registration pairs are saved in data-images/pairs-imgs-lnds_mix.csv .
You can create your own costume cover table for a given dataset (folder with images and landmarks) by hand or use script bm_dataset/create_registration_pairs.py assuming the same folder structure <dataset>/<image-set>/<scale>/<images-and-landmarks> as for the CIMA dataset .

There is a script to generate synthetic data.
Just set an initial image and their corresponding landmarks.
The script will generate a set of geometrically deformed images mimicking different stains and compute the new related landmarks.

When the synthetic datasets have been created, the cover csv file which contains the registration pairs (Reference and Moving image (landmarks)) is generated.
Two modes are created: “first2all” for registering the first image to all others and “each2all” for registering each image to all other. (note A-B is the same as B-A)

We offer a script for scaling images in to particular scales for example

We introduce an option how to randomly take only a subset (use nb_selected ) of annotated landmarks and also add some synthetic point (filling points up to nb_total ) which are across set aligned using estimate affine transformation.

Moreover we developed two additional script for converting large images, handling multiple tissue samples in single image and crop to wide background.

bm_dataset/convert_tiff2png.py converts TIFF or SVS image to PNG in a particular level

bm_dataset/split_images_two_tissues.py splits two tissue samples with clear wide bound in vertical or horizontal direction

bm_dataset/crop_tissue_images.py crops the tissue sample removing wide homogeneous background

Even though this framework is completely customizable we include several image registration methods commonly used in medical imaging.

For each registration method, different experiments can be performed independently using different values of the parameters or image pairs sets.

Sample execution of the “empty” benchmark template:

The general Image Registration benchmarks contain couple required and optional parameters which are shared among ‘all’ methods/benchmarks. The brief description is following…

-t / --path_table path to the cover table describing image/landmarks registration pairs

-d / --path_dataset path to the dataset folder with images and landmarks

-o / --path_out output path for saving results

--preprocessing offer some image pre-processing before image registration starts, the order defines order of performed operations; the options are matching-<color-space> (where <color-space> is for example rgb or hsv ) equalise source to target image and gray converting both images to gray-scale

--unique each experiment has creation stamp included in its name (prevent overwriting experiments with the same method)

--visual generate a simple visualisation of particular image registrations

Measure your computer performance using average execution time on several simple image registrations.
The registration consists of loading images, denoising, feature detection, transform estimation and image warping.

This script generate simple report exported in JSON file on given output path.

Used prepared docker image from Docker Hub

You can build it on your own, note it takes lots of time, be prepared.

For each benchmark experiment, the explanation about how to install and use a particular registration method is given in the documentation. Brief text at the top of each file.

bUnwarpJ is the ImageJ plugin for elastic registration (optional usage of histogram matching and integration with Feature Extraction ). python bm_experiments/bm_bUnwarpJ.py \ -t ./data-images/pairs-imgs-lnds_histol.csv \ -d ./data-images \ -o ./results \ -Fiji ~/Applications/Fiji.app/ImageJ-linux64 \ -cfg ./configs/ImageJ_bUnwarpJ_histol.yaml \ --preprocessing matching-rgb \ --visual --unique

Register Virtual Stack Slices (RVSS) is the ImageJ plugin for affine/elastic registration of a sequence of images. python bm_experiments/bm_RVSS.py \ -t ./data-images/pairs-imgs-lnds_histol.csv \ -d ./data-images \ -o ./results \ -Fiji ~/Applications/Fiji.app/ImageJ-linux64 \ -cfg ./configs/ImageJ_RVSS_histol.yaml \ --visual --unique

elastix is image registration toolkit based on ITK and it consists of a collection of algorithms that are commonly used to solve (medical) image registration problems. For more details see documentation . python bm_experiments/bm_elastix.py \ -t ./data-images/pairs-imgs-lnds_histol.csv \ -d ./data-images \ -o ./results \ -elastix ~/Applications/elastix/bin \ -cfg ./configs/elastix_affine.txt \ --visual --unique

rNiftyReg is an R-native interface to the NiftyReg image registration library which contains programs to perform rigid, affine and non-linear registration of Nifty or analyse images. NiftyReg supports max image size 2048. python bm_experiments/bm_rNiftyReg.py \ -t ./data-images/pairs-imgs-lnds_histol.csv \ -d ./data-images \ -o ./results \ -R Rscript \ -script ./scripts/Rscript/RNiftyReg_linear.r \ --visual --unique

Advanced Normalization Tools (ANTs) is a medical imaging framework containing state-of-the-art medical image registration and segmentation methods. python bm_experiments/bm_ANTs.py \ -t ./data-images/pairs-imgs-lnds_anhir.csv \ -d ./data-images \ -o ./results \ -ANTs ~/Applications/antsbin/bin \ -cfg ./configs/ANTs_SyN.txt For illustration see ANTsPy registration tutorial . python bm_experiments/bm_ANTsPy.py \ -t ./data-images/pairs-imgs-lnds_histol.csv \ -d ./data-images \ -o ./results \ -py python3 \ -script ./scripts/Python/run_ANTsPy.py \ --visual --unique

For illustration see ANTsPy registration tutorial .

DROP is image registration and motion estimation based on Markov Random Fields. python bm_experiments/bm_DROP2.py \ -t ./data-images/pairs-imgs-lnds_histol.csv \ -d ./data-images \ -o ./results \ -DROP ~/Applications/DROP2/dropreg \ -cfg ./configs/DROP2.txt \ --visual --unique

Some more image registration methods integrated in ImageJ are listed in Registration .

The only limitation of adding costume image registration methods that it has to be launched from python script or command line.
The new registration benchmark should be inherited from ImRegBenchmark as for example BmTemplate .

self._prepare() prepare the experiment, e.g. create experiment folder, copy configurations, etc.

self._load_data() the load required data - the experiment cover file

self._run() perform the sequence of experiments (optionally in parallel) and save experimental results (registration outputs and partial statistic) to common table and optionally do particular visualisation of performed experiments

self._evaluate() evaluate results of all performed experiments

self._summarise() summarize and export results from complete benchmark.

General methods that should be overwritten:

_check_required_params(...) verify that all required input parameters are given [on the beginning of benchmark]

_prepare_img_registration(...) if some extra preparation before running own image registrations are needed [before each image registration experiment]

_execute_img_registration execute/perform the image registration, time of this methods is measured as execution time. In case you call external method from command line, just rewrite _generate_regist_command(...) which prepare the registration command to be executed, also you can add generating complete registration script/macro if needed; [core of each image registration experiment]

_extract_warped_image_landmarks(...) extract the required warped landmarks or perform landmark warping in this stage if it was not already part of the image registration [after each image registration experiment]

_extract_execution_time(...) optionally extract the execution time from the external script [after each image registration experiment]

_clear_after_registration(...) removing some temporary files generated during image registration [after each image registration experiment]

The new image registration methods should be added to bm_experiments folder.

In case you need to re-compute evaluation or add visualisation to existing experiment you can use the following script.
The script require complete experiment folder with standard registration-results.scv (similar to registration pairs extended by experiment results).

The project is using the standard BSD license .

Borovec, J., Munoz-Barrutia, A., & Kybic, J. (2018). Benchmarking of image registration methods for differently stained histological slides . In IEEE International Conference on Image Processing (ICIP) (pp. 3368–3372), Athens. DOI: 10.1109/ICIP.2018.8451040

Borovec, J. (2019). BIRL: Benchmark on Image Registration methods with Landmark validation . arXiv preprint arXiv:1912.13452 .

Borovec, J., Kybic, J., et al. (2020). ANHIR: Automatic Non-rigid Histological Image Registration Challenge . In IEEE Transaction on Medical Imaging (TMI). DOI: 10.1109/TMI.2020.2986331 .

Create your own local environment, for more information see the User Guide , and install dependencies requirements.txt contains a list of packages and can be installed as

Running docString tests - documentation and samples of doc string on pymotw and python/docs
