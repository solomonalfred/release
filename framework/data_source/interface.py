import pandas as pd
from abc import ABC, abstractmethod
from typing import Any

class ABCRawDataLoader(ABC):


    @abstractmethod
    def load(self):
        ...

