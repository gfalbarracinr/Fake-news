import pandas as pd
from langdetect import detect
from DataSetCleaner import DataSetCleaner
# data = pd.read_csv('test.csv', delimiter=',')
# #df = pd.DataFrame('train.csv')
# print(data.shape)

# for index, row in data.iterrows():
#     try:
#         if detect(row['text']) != "en":
#             data = data.drop(index)
#     except:
#         pass
# data.to_csv("testEnglish.csv")
# print(data.shape)


# data = pd.read_csv('testEnglish.csv')


data = pd.read_csv('trainEnglish.csv', delimiter=',')

dataSetCleaner = DataSetCleaner

#dataSetCleaner.removeLanguage(data, 'en')
dataSetCleaner.removeHTML(DataSetCleaner, data)
dataSetCleaner.writeToFile(DataSetCleaner, data, 'trainEnglish.csv')

