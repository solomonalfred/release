from framework.data_feature_extraction.interface import *


class FeatureExtractionPipline(ABCCooker):

    def __init__(self, *cookers):
        self.cookers = cookers


    def fit(self, data):
       pass

    def transform(self, data):
        for cooker in self.cookers:
            cooker.fit(data)
            data = cooker.transform(data)
        return data


    def inverse_transform(self, data):
        for cooker in self.cookers[::-1]:
            data = cooker.inverse_transform(data)
        return data
