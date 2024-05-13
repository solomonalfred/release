from framework.model_postprocessing.model_statistics.array_statistics import *



class Statistics:
    def __init__(self, x_origin, y_origin, y_predicted, time_line=None):

        self.x_origin = x_origin
        self.y_origin = np.array(y_origin)
        self.y_estimated = np.array(y_predicted)
        self.time_line = time_line

        self.difference = self.y_estimated - self.y_origin
        self.difference_percent = self.difference / self.y_origin * 100

        self.abs_difference = np.abs(self.difference)
        self.abs_difference_percent = self.abs_difference / self.y_origin * 100

        mask = (self.difference >= 0)
        self.plus_difference = self.difference[mask]
        self.plus_difference_percent = self.difference_percent[mask]

        mask = (self.difference < 0)
        self.minus_difference = self.difference[mask]
        self.minus_difference_percent = self.difference_percent[mask]


        self.difference_statistics = ArrayStatistics(self.difference)
        self.difference_percent_statistics = ArrayStatistics(self.difference_percent)
        self.abs_difference_statistics = ArrayStatistics(self.abs_difference)
        self.abs_difference_percent_statistics = ArrayStatistics(self.abs_difference_percent)
        self.plus_difference_statistics = ArrayStatistics(self.plus_difference_percent)
        self.minus_difference_statistics = ArrayStatistics(self.minus_difference_percent)

        self.mse = np.mean(np.square(self.difference))
        self.mae = np.mean(np.abs(self.difference))

    def __repr__(self):
        num = 25
        sumbol = "-"
        result = "\nStatistics:\n"
        result += f"\tMSE: {self.mse}\n"
        result += f"\tMAE: {self.mae}\n"
        result += f"\t% average: {self.abs_difference_percent_statistics.mean}\n"
        result += f"\t% plus: {self.plus_difference_statistics.mean}\n"
        result += f"\t% minus {self.minus_difference_statistics.mean}\n"
        result += f"\t{sumbol*num}\n"
        result += f"\tРазница между значением и предсказанием: \n"
        result += str(ArrayStatistics(self.difference))
        result += f"\t{sumbol*num}\n"
        result += f"\tРазница (в процентах) между значением и предсказанием: \n"
        result += str(ArrayStatistics(self.difference_percent))
        result += f"\t{sumbol*num}\n"
        result += f"\tАбсолютная разница между значением и предсказанием: \n"
        result += str(ArrayStatistics(self.abs_difference))
        result += f"\t{sumbol*num}\n"
        result += f"\tАбсолютная разница (в процентах) между значением и предсказанием: \n"
        result += str(ArrayStatistics(self.abs_difference_percent))
        result += f"\t{sumbol*num}\n"
        result += f"\tОшибки завышения(в процентах) между значением и предсказанием: \n"
        result += str(ArrayStatistics(self.plus_difference_percent))
        result += f"\t{sumbol*num}\n"
        result += f"\tОшибки занижения (в процентах) между значением и предсказанием: \n"
        result += str(ArrayStatistics(self.minus_difference_percent))
        result += f"\t{sumbol*num}\n"
        return result





'''

        self.n = self.abs_difference.size


    def difference(self):
        return self.difference

    def difference_percent(self):
        return self.difference_percent

    def difference_percent_min(self):
        return self.difference_percent.min()

    def difference_percent_max(self):
        return self.difference_percent.min()

    def difference_percent_mean(self):
        return self.difference_percent.mean()

    def difference_percent_median(self):
        return self.difference_percent.mean()




    def abs_difference(self):
        return self.abs_difference

    def abs_difference_percent(self):
        return self.abs_difference_percent


    def abs_difference_percent_min(self):
        return self.abs_difference_percent.min()

    def abs_difference_percent_max(self):
        return self.abs_difference_percent.min()

    def abs_difference_percent_mean(self):
        return self.abs_difference_percent_mean()


    def abs_difference_percent_median(self):
        return self.difference_percent.mean()



    def max_deviation(self):  #несколько одинаковых
        pos = self.abs_difference.argmax()
        value = np.max(self.abs_difference)
        return (pos, value)

    def min_deviation(self):  #несколько одинаковых
        pos = self.abs_difference.argmin()
        value = np.min(self.abs_difference)
        return (pos, value)

    def arithmetic_mean(self):
        return self.abs_difference.mean()

    def sum_of_errors(self):
        return np.sum(self.abs_difference)

    def sum_of_squares(self):
        return np.sum(np.square(self.abs_difference))

    def root_mean_square(self):
        res = np.sum(np.square(self.abs_difference)) / self.n
        return np.sqrt(res)

    def standard_deviation(self):
        return np.std(self.abs_difference)

    def harmonic_mean(self):
        return self.n / np.sum(1.0 / self.abs_difference)

    def mean_median(self):
        res = np.absolute(self.abs_difference - np.median(self.abs_difference))
        return np.sum(res)/self.n

'''







