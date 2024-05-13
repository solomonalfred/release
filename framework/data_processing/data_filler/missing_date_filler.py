
import pandas as pd


class MissingDateFiller:

    def __init__(self, column_name=None, frequency='H'):
        self.column_name = column_name
        self.frequency = frequency

    def transform(self, data_frame) -> pd.DataFrame:
        if self.column_name is None:
            result = data_frame.fillna(0)
        else:
            result = data_frame[self.column_name].fillna(0)
        result = result.asfreq(self.frequency, fill_value=0)
        return result
