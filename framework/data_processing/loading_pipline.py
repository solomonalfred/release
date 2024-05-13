from typing import Iterable, Any

class DataLoadingPipline:

    def __init__(self, *processors, fit_before_transform=True):
        self.processors = processors
        self.fit_before_transform = fit_before_transform

    def fit(self, data):
        pass
    def transform(self, data):
        for processor in self.processors:
            if self.fit_before_transform and hasattr(processor, 'fit'):
                processor.fit(data)
            if hasattr(processor, 'transform'):
                data = processor.transform(data)
            elif hasattr(processor, 'load'):
                data = processor.load_raw_data()
        return data