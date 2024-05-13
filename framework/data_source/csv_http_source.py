from framework.data_source.interface import *


class CSVHTTPSource:
    def __init__(self, path: Any = None):
        self.path = path

    def load(self):
        try:
            data_frame = pd.read_csv(self.path, index_col=False)
            return data_frame
        except:
            raise Exception("Can't load data from HTTP address.")


