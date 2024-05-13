import numpy as np
from abc import ABC, abstractmethod


class ABCCooker(ABC):

    @abstractmethod
    def fit(self, data):
       ...

    @abstractmethod
    def transform(self, data):
        ...


    @abstractmethod
    def inverse_transform(self, data):
        ...
