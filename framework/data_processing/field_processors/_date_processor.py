from framework.data_processing.interface import *


class DateProcessor(ABCDataProcessor):

    def __init__(self, date_column):
        self.date_column = date_column

    def __get_index(self, data_frame, index_value):
        if isinstance(index_value, int):
            index = index_value
            name = data_frame.columns[index]
        else:
            index = data_frame.columns.get_loc(index_value)
            name = index_value
        return index, name




    def fit(self, data_frame):
        pass

    def transform(self, data_frame):
        index, name = self.__get_index(data_frame, self.date_column)


        try:
            data_frame.iloc[:, index] = pd.to_datetime(data_frame.iloc[:, index])
        except:
            tmp = data_frame.iloc[:, index].str.split(' - ', expand=True)
            data_frame.iloc[:, index] = pd.to_datetime(tmp[0])
        #data_frame = data_frame.set_index(data_frame.columns[index])
        return data_frame

