from typing import Sequence
from framework.data_processing.interface import *


class RowCleaner(ABCDataProcessor):

    def __init__(self, row_indexes=None):
        if isinstance(row_indexes, int):
            self.row_indexes = (row_indexes, )
        elif isinstance(row_indexes,str):
            self.row_indexes = (row_indexes,)
        elif isinstance(self.row_indexes,Sequence):
            self.row_indexes = row_indexes
        else:
            raise TypeError("Wrong type of row indexes.")

    def fit(self, data_frame: pd.DataFrame):
        pass

    def transform(self, data_frame: pd.DataFrame):
        if self.row_indexes is None:
            return data_frame
        try:
            return data_frame.drop(index=self.row_indexes)
        except:
            positions = [data_frame.index[item] for item in self.row_indexes]
            return data_frame.drop(index=positions)





