import json

import numpy as np



class ArrayStatistics:

    def __init__(self, array):
        self.length = len(array)
        self.min = float(np.min(array))
        self.max = float(np.max(array))
        self.mean = float(np.mean(array))
        self.median = float(np.median(array))

    def __repr__(self):
        result = f"\t\tМинимальное значение: \t{self.min:.2f} \n"
        result += f"\t\tМаксимальное значение: \t{self.max:.2f} \n"
        result += f"\t\tСреднее значение: \t{self.mean:.2f} \n"
        result += f"\t\tМедианное значение: \t{self.median:.2f} \n"
        return result


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)