# 
    "In the next step we configure the model. Let's see into ```model_config```. It states that:\n",
    "* inputs for the model are signals and labels\n",
    "* shape of signals will be computed directly from batch\n",
    "* labels will be transformed from original classes 'A' and 'NO' using one-hot-encoding ('ohe')\n",
    "* ```signals``` will be considered as feature vector\n",
    "* we have total 2 classes\n",
    "* loss is crossentropy\n",
    "* we use Adam optimizer\n",
    "* output will be transformed to probabilities (default are logits).\n",
    "\n",
    "Note how we set ```shape``` parameter. Since batches will appear only when pipeline will be run, a specific substitution rule is required to obtain batch shape. This rule is given by named expression ```F```, which accepts ```batch``` and returns shape of batch items. Read more about named expressions in [documentation

**Source:** https://analysiscenter.github.io/batchflow/intro/named_expr.html

---

As pipelines are declarative you might need a way to address data which exists only when the pipeline is executed.
For instance, model training takes batch data, but you don’t have any batches when you declare a pipeline.
Batches appear only when the pipeline is run. This is where named expressions come into play.

A named expression specifies a substitution rule. When the pipeline is being executed,
a named expression is replaced with the value calculated according to that rule.

There are several types of named expressions:

B(‘name’) - a batch class attribute or component name

B(‘name’) - a batch class attribute or component name

P(…) - a wrapper for parallel actions that calculates its expression as a batch-sized vector

P(…) - a wrapper for parallel actions that calculates its expression as a batch-sized vector

PP(…) - a wrapper for parallel actions that calculate its expression batch-size times in a cycle

PP(…) - a wrapper for parallel actions that calculate its expression batch-size times in a cycle

Named expressions can be defined in two ways:

through instance creation, e.g. B(‘attr’), V(‘name’), C(‘option’)

through instance creation, e.g. B(‘attr’), V(‘name’), C(‘option’)

through attribution, e.g. B.attr, V.name, C.option.

through attribution, e.g. B.attr, V.name, C.option.

The only difference is that the former allows for assignment mode, V(‘name’, mode=’append’),
while the latter requires fewer letters to type (so the default mode is implied).

Named expressions can be used in pipelines as variables to get data from and to store data into them.

Each named expression is calculated on each iteration and then its current value will be passed into action.
Therefore, actions get usual parameter values, not named expressions.

You may also use named expressions in your custom methods.

There are two main methods: get() and set() .

Named expressions support basic arithmetic operations like + , - , etc.

To convert a named expression value to a string use str() method:

At each iteration B('features') and B('labels') will be replaced with current_batch.features and current_batch.labels , i.e. batch components or attributes.

B() (i.e. without a component name) returns the batch itself.
To avoid unexpected changes of the batch, the copy can be created with B(copy=True) .

At each iteration V('model_name') will be replaced with the current value of pipeline.get_variable('model_name') .

Thus, you can even change the model trained (or any other pipeline parameter) during pipeline execution.

At each iteration C('model') will be replaced with the current value of pipeline.config['model'] .

If there is no model key in the pipeline config, a default value will be used.
If default is not set, KeyError is raised.

This is an example of a model independent pipeline which allows to change models, for instance,
to assess performance of various models.

At each iteration D('data_path') will be replaced with the current value of pipeline.dataset.data_path .

D() (i.e. without an attribute name) returns the dataset itself.

I(‘ratio’) returns the ratio current / max and thus allows to control the iteration progress.
For instance, at each iteration dataset items can be rotated at a random angle which increases with time:

As static models are initialized before a pipeline is run (i.e. before any batch is created),
all F -functions specified in static init_model cannot get batch :

It can also be an arbitrary function with arbitrary arguments:

A sample from a random distribution. All numpy distributions are supported:

To pass a named expression to an action without evaluating it within a pipeline you can wrap it:

As a result some_action will get not a current value of a pipeline variable, but a V -expression itself.

It comes in handy for parallel actions so that @inbatch_parallel could determine that
different values should be passed to parallel invocations of the action.

For instance, each item in the batch will be rotated at its own angle:

Without P all images in the batch will be rotated at the same angle,
since an angle randomized across batches only:

Every image in the batch gets a noise of the same intensity (7%), but of a different color:

P can be used not only with R -expressions:

However, more often P is applied to R -expressions.

PP(expr) is essentially P([expr for _ in batch.indices]) .

It comes in handy for shape-specific operations (e.g. @ - matrix multiplication) or external functions which return single values.

As far as R is concerned, P(R(...)) is more efficient as it evaluates only once (as R(..., size=batch.size) ).
Whereas PP(R(...)) will evaluate R multiple times (once for each batch item).
