
class DateFilter:

    def __init__(self, date_column = None, date_from = None, date_to = None):
        self.date_from = date_from
        self.date_to = date_to
        self.date_column = date_column

    def transform(self, data_frame):

        if (self.date_from is not None):
            if self.date_column is None:
                index = data_frame.index
            else:
                index = data_frame[self.date_column]
            data_frame = data_frame[index >= self.date_from]


        if (self.date_to is not None):
            if self.date_column is None:
                index = data_frame.index
            else:
                index = data_frame[self.date_column]
            data_frame = data_frame[index < self.date_to]

        return data_frame