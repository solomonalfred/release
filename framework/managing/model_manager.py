

class ModelManager:

    def __init__(self,
                 data_source,
                 data_processor,
                 data_cooker,
                 model):
        self.data_source = data_source
        self.data_processor = data_processor
        self.data_cooker = data_cooker
        self.model = model

    def load_raw_data(self, data_source=None):
        if data_source is not None:
            self.data_source = data_source
        data = self.data_source.load()
        return data

    def process_data(self, data, data_processor=None):
        if data_processor is not None:
            self.data_processor = data_processor
        self.data_processor.fit(data)
        return self.data_processor.transform(data)

    def extract_features(self, data, data_cooker=None):
        if data_cooker is not None:
            self.data_cooker = data_cooker
        self.data_cooker.fit(data)
        return self.data_cooker.transform(data)

    def inverse_extractor(self, data):
        return self.data_cooker.inverse_transform(data)

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model


    def model_fit(self, X, Y, model=None):
        if model is not None:
            self.model = model
        self.model.fit(X, Y)

    def model_predict(self, X):
        result = self.model.predict(X)
        return self.data_cooker.inverse_transform(result)


    '''

    #path_to_dir - путь до директории + сохранение по имени
    #path_to_file - путь до непосредственного файла
    def model_save(self, path_to_file=None):
        self.model.save(path_to_file=path_to_file)

    def model_load(self, file_path):
        return self.model.load(file_path)



    def report_result(self, result):
        #file_name = f'{self.result_dir}{self.model.full_name()}.csv'
        self.result_reporter.output(result)

    def report_statistics(self, result):
        #file_name = f'{self.result_dir}{self.model.full_name()}.csv'
        self.result_reporter.output(result)
    '''



