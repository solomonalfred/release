from console.utils import *
from framework.data_source.csv_file_source import CSVFileSource
from framework.reporting.reporters.stdout_result_reporter import *
from framework.model_postprocessing.model_statistics.model_statistics import *
from framework.model_postprocessing.model_result.model_result_ex import *
from framework.data_processing.data_filter.date_filter import *
from framework.model_utils.model_savers.model_file_saver import *
from framework.model_utils.model_loaders.model_file_loader import *
from framework.model_postprocessing.model_md_report.model_md_report import *
from framework.reporting.reporters.md_reporter import *

import sys
from console.console_parser import *


params = sys.argv
param_parser = ConsoleParser()
param_parser.parse_args(params)


mode = param_parser.get_mode()
input_file = param_parser.get_input_file()
input_http_file = param_parser.get_input_http_file()
output_file = param_parser.get_output_file()
output_http_file = param_parser.get_output_http_file()
report_file = param_parser.get_report_file()
history_period = param_parser.get_history_period()
predict_period = param_parser.get_predict_period()
main_column = param_parser.get_main_column()
date_column = param_parser.get_date_column()
predict_column = param_parser.get_predict_column()
statistics_output = param_parser.get_statistics()
model_name = param_parser.get_model()
model_params = param_parser.get_model_params()
model_path = param_parser.get_model_path()
date_from = param_parser.get_date_from()
date_to = param_parser.get_date_to()

#ToDo добавить проверку на некорректные данные когда history period больше чем размер data


data_source = CSVFileSource(input_file)
date_filter = DateFilter(date_from=date_from, date_to=date_to)

reporter = STDOUTResultReporter()

if mode == 'fit':

    #fit

    if model_name == 'xgboost':
        n_estimators = int(model_params[0])
        max_depth = int(model_params[1])
        learning_rate = float(model_params[2])
        model = XGBoostModel(history_period, predict_period, n_estimators=n_estimators, max_depth=max_depth,
                             learning_rate=learning_rate)
    else:
        raise ValueError('Model not supported')


    manager = build_manager(data_source, date_filter, model, date_column, main_column,
                            history_period, predict_period, 'H', True)

    fit(manager)

    model = manager.get_model()
    saver = ModelFileSaver(model_path)
    saver.save(model)


elif mode == 'predict':

    # predict

    loader = ModelFileLoader(model_path)
    model = loader.load()

    manager = build_manager(data_source, date_filter, model, date_column,
                            main_column,
                            history_period, predict_period, 'H', False)
    data, X, Y, Y_pred = predict(manager)

    result = ModelResultEx(data, X, Y, Y_pred, orig_column_date=date_column, orig_column_name=main_column,
                           y_column_name=main_column, y_pred_column_name=predict_column,
                           date_column_name=date_column)
    reporter.output(result)

    if statistics_output == 1:
        statistics = Statistics(X[:-1], Y, Y_pred[:-1])
        reporter.output(statistics)
        md_report = ModelMdReport(data, X, Y, Y_pred,statistics, model_name=model_name, input_file=input_file,
                                  main_column=main_column, date_from=date_from, date_to=date_to,
                                  history_period=history_period, predict_period=predict_period, output_file=output_file, )
        reporter.output(md_report)
        MdReport(report_file).output(md_report)
