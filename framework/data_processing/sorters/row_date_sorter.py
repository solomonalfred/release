from framework.data_processing.interface import *


class RowDateSorter(ABCDataProcessor):

    def __init__(self, column=None):
        self.column = column

    def fit(self, data_frame: pd.DataFrame):
        pass

    def transform(self, data_frame: pd.DataFrame):
        if self.column is None:
            return data_frame.sort_index()
        else:
            return data_frame.sort_values(by=self.column)





