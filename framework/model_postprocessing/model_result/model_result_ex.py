from framework.model_postprocessing.model_result.interface import *
import pandas as pd
class ModelResultEx():

    def __init__(self, data, X, Y, Y_pred, *args, **kwargs):
        df = pd.DataFrame()
        last_size = len(Y_pred[-1])
        data_size = data.shape[0]
        size = last_size + data_size

        if kwargs['orig_column_name'] is not None:
            column_name = kwargs['orig_column_name']
        else:
            column_name = "original_data"

        if kwargs['y_pred_column_name'] is not None:
            y_pred_column_name = kwargs['y_pred_column_name']
        else:
            y_pred_column_name = "prediction"

        if kwargs['date_column_name'] is not None:
            date_column_name = kwargs['date_column_name']
        else:
            date_column_name = "date"

        # строки кирпича Y идут последовательно без пересечений и разрывов
        if X.shape[1] + Y.shape[0]*Y.shape[1] == data.shape[0]:

            #Обработка Дат
            new_index = pd.date_range(data.index[-1], periods=last_size + 1, freq='H')
            indices = data.index.union(new_index)
            df[date_column_name] = indices

            # Обработка Y
            arr = np.full(size, None, dtype=object)

            if kwargs['orig_column_name'] is not None:
                arr[0:data_size] = data[column_name]
            else:
                arr[0:data_size] = data.iloc[:, 0]
            df[column_name] = arr

            # Обработка Y_pred
            Y_pred = Y_pred.flatten()
            Y_pred_size = len(Y_pred)
            arr = np.full(size, None, dtype=object)
            arr[-Y_pred_size:] = Y_pred
            df[y_pred_column_name] = arr

        else:
            Y = Y.flatten()
            Y_size = len(Y)

            Y_pred = Y_pred.flatten()
            Y_pred_size = len(Y_pred)

            # Обработка Дат
            arr = np.full(Y_pred_size, None, dtype=object)
            new_index = pd.date_range(data.index[-1], periods=last_size + 1, freq='H')
            arr[-last_size:] = new_index[1:]
            df[date_column_name] = arr

            # Обработка Y
            arr = np.full(Y_pred_size, None, dtype=object)
            arr[0:Y_size] = Y
            df[column_name] = arr

            # Обработка Y_pred
            arr = np.full(Y_pred_size, None, dtype=object)
            arr = Y_pred
            df[y_pred_column_name] = arr

        self.df = df

    def __repr__(self):
        csv_data = self.df.to_csv(index=False)
        return csv_data
