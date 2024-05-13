from framework.data_source.interface import *


class CSVFileSource(ABCRawDataLoader):

    def __init__(self, path: Any = None):
        self.path = path

    def load(self):
        try:
            df = pd.read_csv(self.path, index_col=False)
            return df
        except:
            raise Exception("Can't load data from CSV file.")

