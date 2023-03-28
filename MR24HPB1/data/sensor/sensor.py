class Sensor:
    def __init__(self, dataFrame):
        self._dataFrame = dataFrame

    def parse(self, data):
        return self._dataFrame.parse(data)
