# documentation for Research

**Source:** https://analysiscenter.github.io/batchflow/intro/research.html

---

Research class allows you to easily:
* describe complex domains of parameters
* create flexible experiment plan as a sequence of callables, generators and BatchFlow pipelines
* parallelize experiments by CPUs and GPUs
* save and load results of experiments in a unified form

Let’s consider the simplest experiment: call function power and save its output:

Generally speaking, run will iterate over all possible configurations of parameters from the domain (here it is empty,
so there is only one empty configuration). Then for each configuration it will run several iterations of the experiment
(there is only one by default) and save the result. By default, Research create folder and store its results there but
we specify dump_results=False to store results in RAM.

The results can be seen in a special table even during the research execution. They are stored in research.results which
can be transformed to pandas.DataFrame by calling research.results.df property.

The number of units (callables and generators added into Research are called executable units) is not limited. The order
in which they are added determines the order in which they are executed at each iteration.

Flexible way to define parameters domain 

The first profit is Domain class which is intended to define tricky domains of experiment parameters. In the described
experiment we have two parameters: a and b . Let’s say we want to run an experiment for all possible combinations of
parameters a and b which are defined by lists [2, 3] and [2, 3, 4] , correspondingly.

EC (abbreviation for experiment config) is a named expression to refer to items of config which will be assigned to
experiment. In general, named expression is a way to refer to objects that doesn’t exist at the moment of the
definition. Thus, EC(‘key’) is for experiment config item, EC() without args stands for the entire experiment config.

More detailes you can find in tutorials and docstrings.
