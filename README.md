[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11789043&assignment_repo_type=AssignmentRepo)
# Hyperparameter Optimization

For this exercise, we will have a look at Hyperparameter Optimization --
instead of just choosing the best type of machine learning model, we also want
to choose the best hyperparameter setting for a task. The end result (i.e. the
predictive performance) is again not important; how you get there is.

Your deliverable will be a report, written in a style that it
would be suitable for inclusion in an academic paper as the "Experimental
Setup" section or similar. If unsure, check an academic paper of your choice,
for example [this one](https://www.eecs.uwyo.edu/~larsko/papers/pulatov_opening_2022-1.pdf). The
level of detail should be higher than in a typical academic paper though. Your
report should be at most five pages, including references and figures but
excluding appendices. It should have the following structure:
- Introduction: What problem are you solving, how are you going to solve it.
- Dataset Description: Describe the data you're using, e.g. how many features and observations, what are you predicting, any missing values, etc.
- Experimental Setup: What specifically are you doing to solve the problem, i.e.\ what programming languages and libraries, how are you processing the data, what machine learning algorithms are you considering and what hyperparameters and value ranges, what measures you are using to evaluate them, what hyperparameter optimization method you chose, etc.
- Results: Description of what you observed, including plots.
- Code: Add the code you've used as a separate file.

There is no required format for the report. You could, for example, use an
iPython notebook.

## Data

We will have a look at the [Wine Quality
dataset](https://archive-beta.ics.uci.edu/dataset/186/wine+quality). Choose the
one that corresponds to your preference in wine. You may also use a dataset of
your choice, for example one that's relevant to your research.

Choose a small number of different machine learning algorithms and
hyperparameters, along with value ranges, for each. You can use implementations
of AutoML systems (e.g. auto-sklearn), scientific papers, or the documentation
of the library you are using to determine the hyperparameters to tune and the
value ranges. Note that there is not only a single way to do this, but define a
reasonable space (e.g. don't include whether to turn on debug output or random
forests with 1,000,000 trees).

Determine the best machine learning algorithm and hyperparameter setting for
your dataset. Make sure to optimize both the type of machine learning algorithm
and the hyperparameters at the same time (do not first choose the best ML
algorithm and then optimize its hyperparameters). Choose a suitable
hyperparameter optimizer; you could also use several and e.g. compare the
results achieved by random search and Bayesian optimization. Make sure that the
way you evaluate model performance avoids bias and overfitting. You could use
statistical tests to make this determination.

## Submission

Add your report and code to this repository. Bonus points if you can set up a
Github action to automatically run the code and generate the report!

## References
https://blog.finxter.com/how-to-check-python-version-in-colab/
https://thuijskens.github.io/2016/12/29/bayesian-optimisation/
https://scikit-learn.org/stable/modules/grid_search.html
https://towardsdatascience.com/bayesian-optimization-with-python-85c66df711ec
https://pypi.org/project/scikit-optimize/
https://www.overleaf.com/learn/latex/Bibliography_management_with_bibtex

https://en.wikipedia.org/wiki/Pandas_(software)
https://stackoverflow.com/questions/62837550/count-rows-with-same-values-in-specific-column-using-pandas
https://scikit-optimize.github.io/stable/auto_examples/sklearn-gridsearchcv-replacement.html#sphx-glr-auto-examples-sklearn-gridsearchcv-replacement-py
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier
https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier
https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html
https://scikit-learn.org/stable/modules/generated/sklearn.utils.resample.html
https://scikit-learn.org/stable/modules/grid_search.html
https://wires.onlinelibrary.wiley.com/doi/full/10.1002/widm.1484
https://towardsdatascience.com/nested-cross-validation-hyperparameter-optimization-and-model-selection-5885d84acda
https://pyimagesearch.com/2021/05/31/hyperparameter-tuning-for-deep-learning-with-scikit-learn-keras-and-tensorflow/https://pyimagesearch.com/2021/05/17/introduction-to-hyperparameter-tuning-with-scikit-learn-and-python/
https://machinelearningmastery.com/scikit-optimize-for-hyperparameter-tuning-in-machine-learning/
https://towardsdatascience.com/hyperparameter-optimization-with-scikit-learn-scikit-opt-and-keras-f13367f3e796
https://inria.github.io/scikit-learn-mooc/python_scripts/parameter_tuning_nested.html
https://scikit-learn.org/stable/modules/grid_search.html
https://inria.github.io/scikit-learn-mooc/python_scripts/parameter_tuning_nested.html
https://learn.ki-campus.org/courses/automl-luh2021/items/6THUjybtGN0rAnzQS7vUSehttps://www.overleaf.com/learn/latex/Code_listing
https://stackoverflow.com/questions/944700/how-to-check-for-nan-values

