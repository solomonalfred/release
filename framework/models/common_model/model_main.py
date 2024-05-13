import os
import pickle
from framework.models.common_model.model_interface import *


# ToDo инкрементное обучение
class ModelMain(ABCModel):

    def __init__(self):
        self.model = None

    def fit(self, X, Y):
        pass

    def predict(self, X):
        pass

    def save(self, path_to_file):
        pickle.dump(self.__dict__, open(path_to_file, "wb"))

    def load(self, path_to_file):
        tmp_dict = pickle.load(open(path_to_file, "rb"))
        self.__dict__.update(tmp_dict)

