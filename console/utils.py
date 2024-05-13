from framework.data_processing.field_processors._date_processor import *
from framework.data_processing.cleaners.column_cleaner import *
from framework.data_processing.cleaners.row_cleaner import *
from framework.data_processing.sorters.row_date_sorter import *
from framework.data_processing.data_filler.missing_date_filler import *
from framework.data_processing.loading_pipline import *
from framework.data_source.csv_file_source import CSVFileSource
from framework.managing.model_manager import ModelManager
from framework.data_feature_extraction.normalizers.min_max_normalizer import *
from framework.data_feature_extraction.xy_transformers.brick_xy_transformer import *
from framework.data_feature_extraction.feature_extraction_pipline import *
from framework.reporting.reporters.stdout_result_reporter import *
from framework.model_postprocessing.model_statistics.model_statistics import *
from framework.model_postprocessing.model_result.model_result_ex import *
from framework.data_processing.field_processors.date_index_setter import *
from framework.data_processing.data_filter.date_filter import *
from framework.data_source.csv_http_source import *
from framework.utils.class_save_load import *


import sys

from framework.models.xgboost.xgboost_model import *

from console.console_parser import *


def build_full_model_name(model_name, fit_data_name, date_from, date_to, history_period, predict_period, main_column,
                          parameters):
    params = '_'.join(parameters)
    model_name = f'{model_name}_{fit_data_name}_{date_from}_{date_to}_{main_column}_{history_period}_{predict_period}_{params}'
    return model_name

def build_manager(data_source, date_filter, model, input_date_column,
                  input_main_column, history_period, predict_period, missing_frequency, cut_future):

    # data processors
    date_processor = DateProcessor(input_date_column)
    date_index_setter = DateIndexSetter(input_date_column)
    cleaner = ColumnCleaner((input_main_column, ))
    row_cleaner = RowCleaner(0)
    row_date_sorter = RowDateSorter()
    missing_date_filler = MissingDateFiller(frequency=missing_frequency)
    #date_filter
    data_processor = DataLoadingPipline(row_cleaner,
                                        date_processor,
                                        date_index_setter,
                                        cleaner,
                                        missing_date_filler,
                                        row_date_sorter,
                                        date_filter)



    # normalizer
    normalizer = MinMaxNormalizer()

    # xy tranformer
    #xy_transformer = BrickXYTransformer(history_period, predict_period, cut_future=cut_future)
    xy_transformer = BrickXYTransformer(history_period, predict_period, start=None, end=None, step=predict_period,
                                        shift=0, is_future=not cut_future, align_right=True)

    # cooker
    feature_extractor = FeatureExtractionPipline(xy_transformer, normalizer)  # , ...

    # manager
    model_manager = ModelManager(data_source, data_processor, feature_extractor, model)
    return model_manager



def fit(model_manager):
    data = model_manager.load_raw_data()
    proc_data = model_manager.process_data(data)
    if proc_data.shape[0] == 0:
        raise ValueError("Нет данных для обработки")
    X, Y = model_manager.extract_features(proc_data)
    model_manager.model_fit(X, Y)




def predict(model_manager):
    data = model_manager.load_raw_data()
    proc_data = model_manager.process_data(data)
    if proc_data.shape[0] == 0:
        raise ValueError("Нет данных для обработки")
    X, Y = model_manager.extract_features(proc_data)
    Y_pred = model_manager.model_predict(X)
    Y = model_manager.inverse_extractor(Y)
    return proc_data, X, Y, Y_pred



'''
# source для загрузки тестовых данных
data_source = CSVSource(input_path)
#data_source = CSVSource(input_path, date_column='Час визита')

# xy tranformer
xy_transformer = BrickXYTransformer(history_period, predict_period, predict_period, cut_future=False)

# cooker
cooker = CookerPipline(xy_transformer, normalizer)  # , ...

# test date processor
date_filter = DateFilter(date_from='2024-01-01', date_to='2025-01-01')
data_processor = DataLoadingPipline(row_cleaner,
                                   date_processor,
                                   date_index_setter,
                                   cleaner,
                                   missing_date_filler,
                                   row_date_sorter,
                                   date_filter)

# manager
model_manager = ModelManager(data_source, data_processor, cooker, model, result_reporter, result_dir=output_path)

# load
data = model_manager.load_raw_data()
tmp = model_manager.process_data(data)
X, Y = model_manager.cook_data(tmp)
model_manager.model_load(model_path) #загружаем вместо обучения
Y = model_manager.inverse_cooker(Y)
Y_pred = model_manager.model_predict(X)


result = ModelResultEx(tmp, X, Y, Y_pred, orig_column_date=date_column, orig_column_name=column,
                            y_column_name=column, y_pred_column_name=y_pred_column_name, date_column_name=date_column_name)


model_manager.report_result(result)


if stat_output == 1:
    statistics = Statistics(X[:-1], Y, Y_pred[:-1])
    model_manager.report_statistics(statistics)
'''