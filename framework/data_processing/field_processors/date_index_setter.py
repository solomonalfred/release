
import pandas as pd


class DateIndexSetter:

    def __init__(self, date_column, is_drop_date=True):
        self.date_column = date_column
        self.is_drop_date = is_drop_date

    def transform(self, data_frame) -> pd.DataFrame:
        if self.date_column is None:
            return data_frame
        else:
            if isinstance(self.date_column, int):
                position = data_frame.columns[self.date_column]
                return data_frame.set_index(position, drop=self.is_drop_date)
            elif isinstance(self.date_column, str):
                return data_frame.set_index(self.date_column, drop=self.is_drop_date)
            else:
                raise Exception("Wrong type of date column.")

'''
            try:
                return data_frame.set_index(self.date_column, drop=self.is_drop_date)
            except:
                return data_frame.set_index(, drop=self.is_drop_date)
            
            if isinstance(item, str):
                    position = data_frame.columns.get_loc(item)
                    positions.append(position)
                elif isinstance(item, int):
                    positions.append(item)
                    
'''