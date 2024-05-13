from framework.utils.class_save_load import *
class MdReport:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def output(self, data, path_to_file=None):
        if path_to_file is None:
            path_to_file = self.path_to_file
        data = str(data)
        with open(path_to_file, 'w') as file:
            file.write(data)