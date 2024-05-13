import pandas as pd
from abc import ABC, abstractmethod
from typing import Any


import json


class ABCReporter(ABC):


    @abstractmethod
    def output(self, data):
        ...

