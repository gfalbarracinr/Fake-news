import pandas as pd

class helperClass:

    def writeToFile(self, data, fileName):
        data.to_csv(fileName)