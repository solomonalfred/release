from typing import Sequence
from framework.data_processing.interface import *


class ColumnCleaner(ABCDataProcessor):

    def __init__(self, column_names):
        self.column_names = column_names

    def fit(self, data_frame: pd.DataFrame):
        pass

    def transform(self, data_frame: pd.DataFrame):
        if isinstance(self.column_names, int):
            result = pd.DataFrame()
            result[data_frame.columns[self.column_names]] = data_frame.iloc[:, self.column_names]
            return result
        elif isinstance(self.column_names, str):
            result = pd.DataFrame()
            result[self.column_names] = data_frame.loc[:, self.column_names]
            return result
        elif isinstance(self.column_names, Sequence):
            try:
                positions = []
                for item in self.column_names:
                    if isinstance(item, str):
                        position = data_frame.columns.get_loc(item)
                        positions.append(position)
                    elif isinstance(item, int):
                        positions.append(item)
                    else:
                        raise TypeError("Wrong index type for column")
                return data_frame.iloc[:, positions]
            except:
                raise Exception("Wrong column index")
        else:
            raise Exception("Wrong column index")





