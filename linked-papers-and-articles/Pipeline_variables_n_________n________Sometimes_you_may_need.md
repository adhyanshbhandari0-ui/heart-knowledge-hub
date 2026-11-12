# 
    "## Pipeline variables\n",
    "\n",
    "Sometimes you may need to remember intermediate results within workflows. [Pipeline variable

**Source:** https://analysiscenter.github.io/batchflow/intro/pipeline.html

---

Quite often you can’t just use the data itself, as it needs some specific preprocessing beforehand. And not too rarely
you end up with several processing workflows which you have to use simultaneously.
That is the situation when pipelines might come in handy.

Firstly, you create a batch class with all necessary actions:

Secondly, you create a dataset ( client_index is an instance of DatasetIndex ):

And now you can define a workflow pipeline:

And nothing happens! Because all the actions are lazy.
Let’s run them.:

Now the dataset is split into batches and then all the actions are executed for each batch independently.

In the very same way you can define an augmentation workflow:

And again, no action is executed until its result is needed.:

Pipeline actions might come from 3 sources:

Pipeline API contains operations with variables and models.

Batch class comprises data loading operations, preprocessing methods and augmentations.
A batch class method marked with action decorator might be used in a pipeline workflow.

Besides, pipeline actions chains might include arbitrary functions from given namespaces.

Just add a namespace (e.g. a class, a module) which contains the functions needed within a pipeline.

The result of these actions can be stored with save_to parameter:

Normally, named expressions <named_expr> are used in save_to . However, lists or numpy arrays also work out.
Note that save_to argument is never passed to a function, since it is fully processed within the pipeline.

For convenience the main module and the dataset class are automatically added to namespaces available.
So you can use dataset methods or functions defined right in the main module in the pipeline chain.

More complicated pipelines include setup and tear down actions. That’s exactly what before and after pipelines are supposed to do.

before and after pipelines are executed automatically when the main pipeline is executed (specifically, before and after it).

Note that the main module and the dataset class are automatically added to namespaces available.
And result of these actions can be retrieved and stored with save_to parameter.

However, take into account that when you iterate over the pipeline with gen_batch(…) or next_batch(…) , after -pipeline
will be executed automatically only when the iteration is fully finished.
If you break the iteration process (e.g. when early stopping is occurred or when exception is caught),
you should explicitly call pipeline.after.run() .

See API for methods available in before and after pipelines.

The whole pipeline can be chained in a single instruction:

An action chain is a concise and convenient way to write pipelines. But sometimes it’s not enough, for instance, when you want to manipulate with many pipelines adding them or multiplying as if they were numbers or matrices. And that’s what we call a pipeline algebra .

There are 5 operations available: + , * , @ , << , >> .

Add two pipelines by concatenating them, so the actions from the first pipeline will be executed before actions from the second one. p.resize(shape=(256, 256)) + p.rotate(angle=45)

Repeat the pipeline several times. p.random_rotate(angle=(-30, 30)) * 3

Execute the pipeline with the given probability. p.random_rotate(angle=(-30, 30)) @ 0.5

Link a pipeline to a dataset. dataset >> pipeline or pipeline << dataset

Or update pipeline’s config. config >> pipeline or pipeline << config

Pipelines can be created from scratch or from a dataset.

The code below creates a pipeline from scratch.

Or one can use a context manager with pipeline algebra:

However, you cannot execute this pipeline as it doesn’t linked to any dataset.
On the other hand, such pipelines might be applied to different datasets:

Every call to dataset.pipeline() or dataset.p creates a new pipeline.

batch will be the batch returned from the very last action of the pipeline.

BATCH_SIZE is a size of the batch taken from the dataset. Actions might change the size of the batch and thus the batch you will get from the pipeline might have a different size.

Pipeline execution might take a long time so showing a progress bar might be helpful. Just add bar=True to gen_batch parameters.

To start from scratch, reset parameter can be used:

You might reset pipeline variables, the batch iterator and models. See reset() for details.

To execute the pipeline right now for all iterations at once call run() :

Some people prefer a slightly longer, but a bit more certain name run_now() .

Usually run is used to execute the pipeline without resetting all the variables and models
(thus continuing the execution which started earlier and keeping the values and trained models).
However, you might want to start from scratch re-initialzing the variables and/or the models:

my_pipeline.run_now(BATCH_SIZE, n_iters=1000, reset=’all’)

In this case the pipeline variables will be reinitialized and the modes will be reset to initial untrained state.

You can add run with lazy=True or just run_later() as the last action in the pipeline and
then call run() or next_batch() without arguments at all:

If you need to start from scratch, you might call reset() beforehand:

A pipeline might be run for one given batch only with execute_for() :

Sometimes batches can be processed in a “do and forget” manner: when you take a batch, make some data transformations and then switch to another batch.
However, not infrequently you might need to remember some parameters or intermediate results (e.g. a value of loss function or accuracy on every batch
to draw a graph later). This is why you might need pipeline variables.

To initialize a variable just add to a pipeline init_variable(…) with a variable name and a default value.
Variables might be initialized once in a lifetime (e.g. some global state or a configuration parameter) or before each run
(like counters or history stores).

Sometimes it is more convenient to initialize variables indirectly through a function. For instance, loss_history cannot be initialized with [] as it would make a global variable which won’t be cleared on every run. What you actually need is to call list() on each run.

Init functions are also a good place for some complex logic or randomization.

Each batch instance have a pointer to the pipeline it was created in (or None if the batch was created manually).

So getting an access to a variable is easy:

If a variable does not exist, it might be created and initialized, if create parameter is set to True .
For a flexible initialization default , init and init_on_each_run might also be passed to get_variable() .

An explicit variable initialization in a pipeline is a preferred way to create variables.

If create is False (which is by default), then get_variable will raise a KeyError if a variable does not exist.

v() is a shorter alias for get_variable() :

To change a variable value just call set_variable within an action:

The first parameter specifies a named expression where the value will be stored.
The second parameter is an updating value and it can be a value of any type or a named expression .

Note that a named expression might have a mode (e.g. V(‘name’, mode=’a’) ) which could be one of:

‘w’ or ‘write’ to rewrite a variable with a new value. This is a default mode.

‘w’ or ‘write’ to rewrite a variable with a new value. This is a default mode.

‘a’ or ‘append’ to append a value to a variable (e.g. if a variable is a list).

‘a’ or ‘append’ to append a value to a variable (e.g. if a variable is a list).

‘e’ or ‘extend’ to extend a variable with a new value (e.g. if a variable is a list and a value is a list too).

‘e’ or ‘extend’ to extend a variable with a new value (e.g. if a variable is a list and a value is a list too).

‘u’ or ‘update’ to update a variable with a new value (e.g. if a variable is a dict).

‘u’ or ‘update’ to update a variable with a new value (e.g. if a variable is a dict).

For sets and dicts ‘u’ and ‘a’ do the same.

Just call pipeline.delete_variable(“variable_name”) or pipeline.del_variable(“variable_name”) .

As simple as pipeline.delete_all_variables() .

A pipeline might need custom calculations which can be implemented with save_to() update() :

The first parameter is a named expression where the result will be stored, while the second parameter is an expression
which value will be re-calculated at each iteration.

Some other useful examples might include:

collecting loss history: pipeline . init_variable ( 'loss_history' , list ) ... . save_to ( V ( 'list' , mode = 'a' ), V ( 'current_loss' ))

collecting predictions: pipeline . init_variable ( 'all_predictions' , list ) ... . update ( V ( 'all_predictions' , mode = 'e' ), V ( 'predictions' ))

assessing performance: pipeline . update ( B ( 'time' ), L ( time . time )) ... . save_to ( B ( 'time' ), L ( time . time ) - B ( 'time' )) . update ( V ( 'throughput' ), B ( 'images' ) . nbytes / B ( 'time' )) ...

The methods are synonyms and might be used interchangably to fit your pipeline narrative.

If you use multi-threading prefetching or in-batch parallelism ,
than you might require synchronization when accessing some shared resource:

Locks are stored as variables with the very same names. So you can access a lock easiliy as pipeline.v('lock_name') and use it within actions or even custom functions.

init_lock is not required as the first acquire will create the lock if needed.
However, init_lock allow for cleaner and tidier pipelines.

If you have a pipeline images and a pipeline labels , you might join them for a more convenient processing:

When this pipeline is run, the following will happen for each batch of images :

the actions load , resize and random_rotate will be executed

the actions load , resize and random_rotate will be executed

a batch of labels with the same index will be created

a batch of labels with the same index will be created

the labels batch will be passed into some_action as a first argument (after self , of course).

the labels batch will be passed into some_action as a first argument (after self , of course).

So, images batch class should look as follows:

Thus, the tuple of batches from labels and masks will be passed into some_action as the first arguments (as always, after self ).

You can also merge data from two pipelines (this is not the same as concatenating pipelines ).:

images_with_augmentation will generate batches of size 16

images_with_augmentation will generate batches of size 16

all_images before merge will generate batches of size 16

all_images before merge will generate batches of size 16

merge will combine both batches in some way.

merge will combine both batches in some way.

Pipeline’s merge calls batch_class.merge([batche_from_pipe1, batch_from_pipe2]) .

The default Batch.merge just concatenate data from both batches, thus making a batch of double size.

Take into account that the default merge also changes index to numpy.arange(new_size) .

When actions change the batch size (for instance, dropping some bad or skipping incomplete data),
you might end up in a situation when you don’t know the batch size and, what is sometimes much worse,
batch size differs. To solve this problem, just call rebatch :

Under the hood rebatch calls merge , so you must ensure that merge works properly for your specific data and write your own merge if needed.

Sometimes you might want to stop processing a batch within a pipeline (e.g. if it does not meet a certain criteria or contains erroneous data, etc).
Just throw SkipBatchException in an action method and the pipeline will skip this batch and switch to a new one.

When you call several run (or gen_batch , or next_batch ) one after another without resetting a batch iterator (see reset() ),
you might bump into a situation when the batch iterator is exhausted. Whenever this happens, EmptyBatchSequence warning is emitted,
which can ba caught if needed:

To debug a pipeline you might pass debug parameter when executing the pipeline, e.g.:

Execution parameters are gathered into pipeline.debug_info data frame, which contains
batch id, action name, start time and execution time.

This might help you to analyze pipeline exection, find bottlenecks and so on.
