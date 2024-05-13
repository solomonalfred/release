from framework.utils.class_save_load import *


class ModelFileLoader:
    def __init__(self, model_file_path):
        self.model_path = model_file_path

    def load(self, model_path=None):
        if model_path is None:
            model_path = self.model_path
        return load_object_from_pickle(model_path)
