from autogoal.search import RandomSearch
from autogoal.kb import build_pipelines, CategoricalVector, List, Word, Matrix

from autogoal.contrib import find_classes
import numpy as np
import random


class AutoClassifier:
    def __init__(
        self,
        *,
        search_algorithm=RandomSearch,
        search_kwargs={},
        search_iterations=100,
        include_filter=".*",
        exclude_filter=None,
        validation_split=0.2,
        errors="warn",
    ):
        self.search_algorithm = search_algorithm
        self.search_kwargs = search_kwargs
        self.search_iterations = search_iterations
        self.include_filter = include_filter
        self.exclude_filter = exclude_filter
        self.validation_split = validation_split
        self.errors = errors

    def fit(self, X, y):
        self.pipeline_builder_ = build_pipelines(
            input=self._start_type(),
            output=CategoricalVector(),
            registry=find_classes(
                include=self.include_filter, exclude=self.exclude_filter
            ),
        )

        search = self.search_algorithm(
            self.pipeline_builder_,
            self._make_fitness_fn(X, y),
            errors=self.errors,
            **self.search_kwargs,
        )

        self.best_pipeline_, self.best_score_ = search.run(self.search_iterations)

        self.best_pipeline_.send("train")
        self.best_pipeline_.run((X, y))
        self.best_pipeline_.send("eval")

    def _start_type(self):
        return Matrix()

    def _make_fitness_fn(self, X, y):
        X = np.asarray(X)
        y = np.asarray(y)

        indices = np.arange(0, len(X))
        np.random.shuffle(indices)
        split_index = int(self.validation_split * len(indices))
        train_indices = indices[:split_index]
        test_indices = indices[split_index:]

        X_train, y_train, X_test, y_test = (
            X[train_indices],
            y[train_indices],
            X[test_indices],
            y[test_indices],
        )

        def fitness_fn(pipeline):
            pipeline.send("train")
            pipeline.run((X_train, y_train))
            pipeline.send("eval")
            _, y_pred = pipeline.run((X_test, np.zeros_like(y_test)))
            return (y_pred == y_test).astype(float).mean()

        return fitness_fn

    def predict(self, X):
        return self.best_pipeline_.run((X, [None] * len(X)))


class AutoTextClassifier(AutoClassifier):
    def _start_type(self):
        return List(Word())
