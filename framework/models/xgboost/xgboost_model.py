import xgboost as xgb
from framework.models.common_model.model_main import *

# ToDo инкрементное обучение
XGBOOST_MODEL_NAME = "XGBOOST"

#ToDo убрать контроль имен из модели
class XGBoostModel(ModelMain):

    def __init__(self, history_period, predict_period, n_estimators=1000, max_depth=5, learning_rate=0.1):
        super().__init__()
        self.history_period = history_period
        self.predict_period = predict_period
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.learning_rate = learning_rate

        count = int(1)
        if os.cpu_count() > 2:
            count = os.cpu_count() // 2

        self.model = xgb.XGBRegressor(n_estimators=self.n_estimators, max_depth=self.max_depth,
                                      learning_rate=self.learning_rate, n_jobs=count)

    def fit(self, X, Y):
        if (X.shape[1] != self.history_period):
            raise ValueError('Wrong X data size')
        if (Y.shape[1] != self.predict_period):
            raise ValueError('Wrong Y data size')
        self.model.fit(X, Y.ravel())

    def predict(self, x):
        result = self.model.predict(x)
        if result.ndim == 1:
            result = result.reshape(-1, 1)
        return result

    @property
    def parameters(self):
        return [self.n_estimators, self.max_depth, self.learning_rate]

    @parameters.setter
    def parameters(self, value):
        self.n_estimators = value[0]
        self.max_depth = value[1]
        self.learning_rate = value[2]

        count = int(1)
        if os.cpu_count() > 2:
            count = os.cpu_count() // 2

        self.model = xgb.XGBRegressor(n_estimators=self.n_estimators, max_depth=self.max_depth,
                                      learning_rate=self.learning_rate, n_jobs=count)


