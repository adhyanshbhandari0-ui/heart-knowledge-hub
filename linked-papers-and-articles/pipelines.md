# ``pipelines``

**Source:** https://analysiscenter.github.io/cardio/modules/pipelines.html

---

Module pipelines contains functions that build pipelines that we used to train models and make predictions. You can use them as-is to train similar models or adjust them in order to get better perfomance.

Pre-defined pipelines were designed to make it easier to use our models and make code simpler and more readable.

In both cases you obtain pipeline , ready for training DirichletModel . The first example is short but only allows to vary some hyperparameters of the model, while the second example is more flexible in data preprocessing.

Working with pipelines consists of 3 simple steps. First, we import desired pipeline, e.g. dirichlet_train_pipeline :

Second, we specify its parameters, e.g. path to a file with labels:

Third, we pass dataset to the pipeline and run caclulation:

Result is typically a trained model or some values stored in pipeline variable (e.g. model predicitons).

At this moment the module contains following pipelines:

To learn more about using these pipelines and building new ones see the tutorial .

Pipelines About pipelines How to use Available pipelines API
