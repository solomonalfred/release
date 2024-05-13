from abc import ABC, abstractmethod
import numpy as np
class ABCModelResult(ABC):



    @abstractmethod
    def prepare(self, date, X, Y, Y_pred, *args, **kwargs):
        pass

