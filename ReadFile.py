import pandas as pd
from langdetect import detect
from DataSetCleaner import DataSetCleaner
from vocabulary import Vocabulary

data = pd.read_csv('test.csv', delimiter=',')
dataSetCleaner = DataSetCleaner

#data = dataSetCleaner.removeLanguage(DataSetCleaner, data, 'en')
#data = dataSetCleaner.removeHTML(DataSetCleaner, data)
#dataSetCleaner.writeToFile(DataSetCleaner, data, 'test.csv')
vocabulary = Vocabulary('fn.csv')
totalWords = vocabulary.countWordsTotal(data)
dataSetCleaner.writeToFile(dataSetCleaner, totalWords, 'words.csv')
print(totalWords)

