import argparse

class ConsoleParser:

    def __init__(self):
        self.args = {}

    def parse_args(self, params):
        parser = argparse.ArgumentParser(description='Консольная утилита для предсказания диапозонов')
        parser.add_argument('-mode', type=str, action='store', dest='mode', help='Режим работы утилиты (predict/fit)')

        #fit
        parser.add_argument('-input_file', type=str, action='store', dest='input_file', help='Путь до csv файла, который необходимо обработать')
        parser.add_argument('-input_http_file', type=str, action='store', dest='input_http_file', help='Путь до удаленного csv файла, который необходимо обработать')
        parser.add_argument('-output_file', type=str, action='store', dest='output_file', help='Путь до csv файла, который необходимо сохранить')
        parser.add_argument('-output_http_file', type=str, action='store', dest='output_http_file', help='Путь до удаленного csv файла, который необходимо сохранить')
        parser.add_argument('-report_file', type=str, action='store', dest='report_file', help='Путь до отчета (md - файла)')
        parser.add_argument('-history_period', type=int, action='store', dest='history_period', help='Глубина истории')
        parser.add_argument('-predict_period', type=int, action='store', dest='predict_period', help='Глубина предсказания')
        parser.add_argument('-main_column', type=str, action='store', dest='main_column', help='Колонка с данными временного ряда во входном файле')
        parser.add_argument('-date_column', type=str, action='store', dest='date_column', help='Колонка с датами во входном файле')
        parser.add_argument('-predict_column', type=str, action='store', dest='predict_column', help='Колонка с предсказаниями в выходном файле')
        parser.add_argument('-statistics', type=int, action='store', dest='statistics', help='Выводить ли статистику 0 \ 1')
        parser.add_argument('-model', type=str, action='store', dest='model', help='Название модели')
        parser.add_argument('-model_params', nargs='+', type=str, action='store', dest='model_params', help='Параметры модели')
        parser.add_argument('-model_path', type=str, action='store', dest='model_path', help='Путь до модели')
        parser.add_argument('-date_from', type=str, action='store', dest='date_from', help='Дата начала')
        parser.add_argument('-date_to', type=str, action='store', dest='date_to', help='Дата конца')




        parser.add_argument('-i', type=str, action='store', dest='input', help='Путь до csv файла, который необходимо обработать')
        parser.add_argument('-o', type=str, action='store', dest='output', help='Путь до папки, где будут сохранятся результаты')
        parser.add_argument('-ic', type=str, action='store', dest='input_column', help='Колонка с данными во входном файле')
        parser.add_argument('-id', type=str, action='store', dest='input_date', help='Колонка с датами во входном файле ')
        parser.add_argument('-md', type=str, action='store', dest='model_dir', help='Путь до папки, где будут находится модели')
        parser.add_argument('-f', type=str, action='store', dest='fit_path', help='Путь до тренировочного файла')
        #parser.add_argument('-f', type=str, action='store', dest='o', help='[опцион] Путь до файла, который будет использоваться в обучении')

        parser.add_argument('-oy', type=str, action='store', dest='y_column_name', help='Название колонки Y(основные значения) в выходном файле')
        parser.add_argument('-od', type=str, action='store', dest='date_column_name', help='Название колонки Date(дата\время) в выходном файле')
        parser.add_argument('-oyp', type=str, action='store', dest='y_pred_column_name', help='Назваеие колонки Y_pred(предсказанные значения) в выходном файле')

        parser.add_argument('-hp', type=int, action='store', dest='history', help='Глубина истории')
        parser.add_argument('-pp', type=int, action='store', dest='predict', help='Глубина предсказания')
        #parser.add_argument('-models', nargs = '+', type=str, action='store', dest='models', help='Выбор модели')
        #parser.add_argument('-weights', nargs = '+', type=float, action='store', dest='weights', help='model names')

        parser.add_argument('-v', type=int, action='store', dest='stat_output', help='Вывод статистики')


        self.args = parser.parse_args()

    def get_mode(self):
        return self.args.mode


    def get_input_file(self):
        return self.args.input_file

    def get_input_http_file(self):
        return self.args.input_http_file

    def get_output_file(self):
        return self.args.output_file

    def get_output_http_file(self):
        return self.args.output_http_file

    def get_report_file(self):
        return self.args.report_file

    def get_history_period(self):
        return self.args.history_period

    def get_predict_period(self):
        return self.args.predict_period

    def get_main_column(self):
        return self.args.main_column

    def get_date_column(self):
        return self.args.date_column

    def get_predict_column(self):
        return self.args.predict_column


    def get_statistics(self):
        return self.args.statistics

    def get_model(self):
        return self.args.model

    def get_model_params(self):
        return self.args.model_params

    def get_model_path(self):
        return self.args.model_path

    def get_date_from(self):
        return self.args.date_from

    def get_date_to(self):
        return self.args.date_to






    def get_model_dir(self):
        return self.args.model_dir

    def get_fit_path(self):
        return self.args.fit_path


    def get_y_column_name(self):
        return self.args.y_column_name

    def get_y_pred_column_name(self):
        return self.args.y_pred_column_name

    def get_date_column_name(self):
        return self.args.date_column_name

    def get_stat_output(self):
        return self.args.stat_output




'''


    def get_models(self):
        return self.args.models

    def get_weights(self):
        return self.args.weights
'''