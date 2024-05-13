from framework.utils.class_save_load import *
class ModelFileSaver:
    def __init__(self, model_file_path):
        self.model_path = model_file_path

    def save(self, model, model_path=None):
        if model_path is None:
            model_path = self.model_path
        save_object_to_pickle(model, model_path)
