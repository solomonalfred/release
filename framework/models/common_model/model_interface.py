import pandas as pd
from abc import ABC, abstractmethod
from typing import Sequence




class ABCModel(ABC):

    @abstractmethod
    def fit(self, X, Y):
        ...

    @abstractmethod
    def predict(self, X):
        ...

    @abstractmethod
    def save(self, path_to_file):
        ...

    @abstractmethod
    def load(self, path_to_file):
        ...