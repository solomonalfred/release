from framework.data_feature_extraction.interface import *
from framework.data_feature_extraction.variable_transformers.brick_transformer import *


class BrickXYTransformer(ABCCooker):
    def __init__(self, x_period, y_period, start=None, end=None, step=24, shift=0,
                 is_future=True, align_right=True):

        self.x_period = x_period
        self.y_period = y_period

        self.start = start
        self.end = end

        self.step = step
        self.shift = shift

        self.is_future = is_future
        self.align_right = align_right


    def fit(self, data):
        pass

    def transform(self, data_frame):
        # для тестов:
        #data_frame = pd.DataFrame(range(1, len(data_frame)+1), index=data_frame.index, columns=data_frame.columns)
        #data_frame.reset_index(drop=True, inplace=True)

        data_frame = data_frame.reset_index(drop=True)

        if self.end is not None:
            data_frame.drop(index=range(self.end,data_frame.shape[0]), inplace=True)
        if self.start is not None:
            data_frame.drop(index=range(self.start), inplace=True)


        # print("period", self.x_period)
        # print("len data", len(data_frame))
        length = len(data_frame) - self.x_period
        # print(length)
        delta = length % self.step
        # print("delta", delta)

        x_transformer = BrickTransformer(self.x_period, self.step, 0, self.align_right, delta)
        y_transformer = BrickTransformer(self.y_period, self.step, self.shift + self.x_period, self.align_right, delta)

        X = x_transformer.transform(data_frame)
        Y = y_transformer.transform(data_frame)
        size = min(X.shape[0], Y.shape[0])

        if self.is_future:
            return X[:size+1].to_numpy(), Y[:size].to_numpy()
        return X[:size].to_numpy(), Y[:size].to_numpy()

    def inverse_transform(self, data):
        return data
