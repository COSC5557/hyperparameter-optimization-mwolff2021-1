# -*- coding: utf-8 -*-
"""PML_HPO

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ap_WaQslMUdIaGSfZBgipQYrTvq3d_cI
"""

import pandas as pd
import numpy as np
import sklearn

#suppress warnings about class imbalances
import warnings
warnings.filterwarnings("ignore")

#import models, packages
from sklearn import linear_model, ensemble
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
import numpy

import skopt
from skopt.space import Real, Categorical, Integer
from skopt import BayesSearchCV

#import grid search and cross_validate
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate

#print python version for report
import sys; print(sys.version)

#read and display data
data = pd.read_csv("winequality-red.csv", sep = ";")

#display information about dataset for report
data.columns
print(data.groupby(['quality']).count())

#split into features/target
x = data.drop(columns = ['quality'])
#attemptd normalization at one point but this step yielded lower performance
#x_norm = sklearn.preprocessing.normalize(x, axis=0)
y = data['quality']

ridge_opt = BayesSearchCV(linear_model.RidgeClassifier(),
    {
    "alpha": Real(1.0, 5.0, prior='log-uniform'),
    "tol": Real(0.0001, 0.1, prior='log-uniform'),
    "solver": Categorical(["svd", "cholesky", "lsqr", "sparse_cg"]),
    "max_iter": Integer(100, 100000, prior='log-uniform'),
    },
     n_iter=32,
     random_state=0,
     scoring = "balanced_accuracy"

)

bagging_opt = BayesSearchCV(ensemble.BaggingClassifier(),
                {"n_estimators" : Integer(100, 10000, prior = 'log-uniform'),
               "max_samples" : Real(0.01, 1.0, prior='log-uniform'),
                "max_features" : Real(0.01, 1.0, prior='log-uniform'),
                },
        n_iter=32,
        random_state=0,
        scoring = "balanced_accuracy"

)

rf_opt = BayesSearchCV(ensemble.RandomForestClassifier(),
        {
    "n_estimators" : Integer(100, 10000, prior = 'log-uniform'),
    "criterion" : Categorical(["gini", "entropy", "log_loss"]),
    "max_depth" : Real(2, 10, prior='log-uniform')
        },
        n_iter=32,
        random_state=0,
        scoring = "balanced_accuracy"
)

def nested_resampling_bayesian(optimizer, x, y):
     for i in range(0, 3): #3-fold outer cross-validation
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2, random_state=42)
        #10_fold inner resampling -- performs 10-fold cross-validation on each hyperparameter configuration and stores results
        cv_results = cross_validate(
           optimizer, x_train, y_train, cv=10, return_estimator=True, scoring = "balanced_accuracy"
        )
        cv_results = pd.DataFrame(cv_results)
        print(cv_results)
        cv_test_scores = cv_results["test_score"]
        #display results
        print(
            "Generalization score with hyperparameters tuning:\n"
            f"{cv_test_scores.mean():.3f} ± {cv_test_scores.std():.3f}"
        )
        
        optimizer.fit(x_train, y_train)
        print(optimizer.best_estimator_)
        print(optimizer.best_params_)
        print(optimizer.best_score_)
        print(optimizer.score(x_test, y_test))

nested_resampling_bayesian(ridge_opt, x, y)

nested_resampling_bayesian(bagging_opt, x, y)

nested_resampling_bayesian(rf_opt, x, y)