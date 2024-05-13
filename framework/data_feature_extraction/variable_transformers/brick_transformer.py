import pandas as pd
from framework.data_feature_extraction.interface import *


class BrickTransformer(ABCCooker):
    def __init__(self, period, step, shift, align_right, delta):
        self.period = period
        self.step = step
        self.shift = shift
        self.align_right = align_right
        self.delta = delta

    def fit(self, data):
        pass

    def transform(self, series): #ToDo переход на numpy в выходе
        result = []
        if self.align_right:
            first = self.shift + self.delta
            last = len(series) - self.period + 1
        else:
            first = self.shift
            last = len(series) - self.period - self.delta + 1

        for i in range(first, last, self.step):
            result.append(series.iloc[i: i + self.period].reset_index(drop=True))

        result = pd.concat(result, axis=1).transpose().reset_index(drop=True)
        return result

    def inverse_transform(self, data):
        return data
'''
from unittest import result

import pandas as pd
from framework.data_feature_extraction.interface import *

class BrickTransformer(ABCCooker):
    def __init__(self, period, shift, step=1):
        self.period = period
        self.shift = shift
        self.step = step

    def fit(self, data):
        pass


    def transform(self, series): #ToDo переход на numpy в выходе
        result = []
        length = len(series) - self.period
        delta = length % self.step
        for i in range(self.shift + delta, len(series) - self.period + 1, self.step):
             result.append(series.iloc[i: i + self.period].reset_index(drop=True))
        result = pd.concat(result, axis=1).transpose().reset_index(drop=True)
        return result


    def inverse_transform(self, data):
        return data
'''