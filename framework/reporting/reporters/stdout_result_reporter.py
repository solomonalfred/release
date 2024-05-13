from framework.reporting.reporters.interface import *
import pandas as pd
import numpy as np

import json


class STDOUTResultReporter(ABCReporter):

    def __init__(self):
        pass


    def output(self, data : str):
        print(data)

