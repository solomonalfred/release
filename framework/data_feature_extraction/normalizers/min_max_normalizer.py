from framework.data_feature_extraction.interface import *


class MinMaxNormalizer(ABCCooker):

    def __init__(self, axis:int=None):
        if isinstance(axis, float):
            raise Exception("Axis must be integer or NoneType")
        self.max = None
        self.min = None
        self.axis = axis

    def fit(self, data):
        if isinstance(data, tuple):
            if self.axis is None:
                self.min = float(data[0].min())
                self.max = float(data[0].max())
            elif self.axis == 0:
                self.min = data[0].min(axis=self.axis)[np.newaxis, :]
                self.max = data[0].max(axis=self.axis)[np.newaxis, :]
            elif self.axis == 1:
                self.min = data[0].min(axis=self.axis)[:, np.newaxis]
                self.max = data[0].max(axis=self.axis)[:, np.newaxis]
            else:
                raise Exception("Wrong axis (0 <= axis < 2)")

        else:
            if self.axis is None:
                self.min = float(data.min())
                self.max = float(data.max())
            elif self.axis == 0:
                self.min = data.min(axis=self.axis)[np.newaxis, :]
                self.max = data.max(axis=self.axis)[np.newaxis, :]
            elif self.axis == 1:
                self.min = data.min(axis=self.axis)[:, np.newaxis]
                self.max = data.max(axis=self.axis)[:, np.newaxis]
            else:
                raise Exception("Wrong axis (0 <= axis < 2)")


    def transform(self, data):
        if isinstance(data, tuple):
            return ((item - self.min) / (self.max - self.min) for item in data)
        else:
            return (data - self.min) / (self.max - self.min)


    def inverse_transform(self, data):
        if isinstance(data, tuple):
            return (item * (self.max - self.min) + self.min for item in data)
        else:
            return data * (self.max - self.min) + self.min
