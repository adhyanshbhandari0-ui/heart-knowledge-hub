# ``core``

**Source:** https://analysiscenter.github.io/cardio/modules/core.html

---

CardIO’s core classes are EcgBatch and EcgDataset . They are responsible for
storing of ECGs, batch generation and applying actions to batches.

EcgBatch is a class that defines how to store ECG data and contains actions
that can be applied to ECG in preprocessing stage.

signal , stores ECG signals in numpy array

annotation , array of dicts with different types of annotations, e.g. array of R-peaks

meta , array of dicts with metadata about ECG records, e.g. signal frequency

target , array of labels assigned to ECG records

unique_labels , array of all possible target labels in dataset

load ECG records from wfdb, DICOM, EDF, wav or blosc format

To learn more about actions refer to the tutorial .

EcgDataset helps to conveniently create a list of ECG indices and generate batches
(small subsets of data) of default type EcgBatch .

CardIO generates batches trought a Dataset library. To initialize this process we need to create a sequence of data item ids, e.g. using names of files in specific folder:

Then we specify type of batches we want to generate, e.g. EcgBatch :

EcgDataset helps to get the same result in a shorter way:

Now we can call EcgDataset.next_batch with specified batch_size argument to generate batches and process them using actions of EcgBatch .
