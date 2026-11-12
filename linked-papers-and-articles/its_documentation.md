# its documentation

**Source:** https://analysiscenter.github.io/batchflow

---

BatchFlow helps you conveniently work with random or sequential batches of your data
and define data processing and machine learning workflows even for datasets that do not fit into memory.

ready to use ML models and proven NN architectures

ready to use ML models and proven NN architectures

convenient layers and helper functions to build custom models

convenient layers and helper functions to build custom models

a powerful research engine with parallel model training and extended experiment logging.

a powerful research engine with parallel model training and extended experiment logging.

Classes and capabilities Index Dataset Batch class Batch class for handling images Pipeline Named expressions Within batch parallelism Inter-batch parallelism Working with models Torch models Research Model zoo

API batchflow batchflow.opensets batchflow.models batchflow.research

The trick here is that all the processing actions are lazy. They are not executed until their results are needed, e.g. when you request a preprocessed batch:

BatchFlow includes ready-to-use proven architectures like VGG, Inception, ResNet and many others.
To apply them to your data just choose a model, specify the inputs (like the number of classes or images shape)
and call train_model . Of course, you can also choose a loss function, an optimizer and many other parameters, if you want.:

BatchFlow module is in the beta stage. Your suggestions and improvements are very welcome.

In many cases it is much more convenient to install batchflow as a submodule in your project repository than as a python package:

If your python file is located in another directory, you might need to add a path to batchflow submodule location:

What is great about using a submodule is that every commit in your project can be linked to its own commit of a submodule.
This is extremely convenient in a fast paced research environment.

BatchFlow has the following strict requirments:

Some BatchFlow modules also depend on other mandatory packages:

pandas and multiprocess for batchflow.research

pandas and multiprocess for batchflow.research

Please cite BatchFlow in your publications if it helps your research.
