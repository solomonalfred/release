import pandas as pd
from abc import ABC, abstractmethod



class ABCDataProcessor(ABC):

    @abstractmethod
    def fit(self, data_frame: pd.DataFrame):
        ...

    @abstractmethod
    def transform(self, data_frame: pd.DataFrame):
        ...
