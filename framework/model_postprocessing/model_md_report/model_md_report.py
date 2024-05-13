from collections import OrderedDict


class ModelMdReport:
    def __init__(self, data, X, Y, Y_pred, statistics, *args, **kwargs):
        self.data = data
        self.X = X
        self.Y = Y
        self.Y_pred = Y_pred
        self.stat = statistics
        try:
            self.model_name = kwargs['model_name'] # Модель
            self.input_file = kwargs['input_file'] #Сегмент (источник)
            self.main_column = kwargs['main_column'] #Метрика сегмента
            self.date_from = kwargs['date_from'] #Начальная дата выборки
            self.date_to = kwargs['date_to'] # Конечная дата выборки
            self.history_period = kwargs['history_period'] # Глубина ретроспективы
            self.predict_period = kwargs['predict_period'] # Глубина прогноза
            self.output_file = kwargs['output_file'] #Файл с результатами
            #self. = kwargs[''] #
        except:
            raise ValueError("Недостаточено параметров для формирования статистики report.md")

    def __make_row(self, name, value):
        return f"|{name}| {value}\n"


    def __make_table(self, header, name, value, rows):
        res = (f"## {header}\n"
               f"| {name}| {value}\n"
               f"| :--- | :---\n")
        for row in rows:
            res += row
        return res

    def __repr__(self):
        out = OrderedDict([
            ("Глубина прогноза", self.predict_period),
            ("Глубина ретроспективы", self.history_period),
            ("Сегмент (источник)", self.input_file),
            ("Метрика сегмента", self.main_column),
            ("Начальная дата выборки", self.date_from),
            ("Конечная дата выборки", self.date_to),
            ("Глубина ретроспективы", self.history_period),
            ("Глубина прогноза", self.predict_period),
            ("Файл с результатами", self.output_file), #ToDo Прописать правтльные пути
        ])
        rows = [self.__make_row(name, value) for name, value in out.items()]
        table_1 = self.__make_table('Параметры теста', 'Модель', self.model_name,  rows)

        out = OrderedDict([
            ("Средняя ошибка", f"{self.stat.abs_difference_percent_statistics.mean:.2f} %"),
            ("Средняя ошибка сверху", f"{self.stat.plus_difference_statistics.mean:.2f} %"),
            ("Средняя ошибка снизу", f"{self.stat.minus_difference_statistics.mean:.2f} %"),
            ("Среднеквадратическая ошибка (MSE)", f"{self.stat.mse:.2f}"),
            ("Cредняя абсолютная ошибка(MAE)", f"{self.stat.mae:.2f}"),
            ("Минимальная абсолютная ошибка ", f"{self.stat.abs_difference_percent_statistics.min:.2f} %"),
            ("Максимальная абсолютная ошибка ", f"{self.stat.abs_difference_percent_statistics.max:.2f} %"),
            ("Cредняя абсолютная ошибка", f"{self.stat.abs_difference_percent_statistics.mean:.2f} %"),
            ("Медианная абсолютная ошибка ", f"{self.stat.abs_difference_percent_statistics.median:.2f} %"),
        ]) #f"{self.stat.:.2f} %"
        rows = [self.__make_row(name, value) for name, value in out.items()]
        table_2 = self.__make_table('Статистика', 'Метрика', 'Значение', rows)

        return f"# Тест  \n{table_1}\n{table_2}"
