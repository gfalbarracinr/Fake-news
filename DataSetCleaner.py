import pandas as pd
from langdetect import detect
import re

class DataSetCleaner:


    def __init__(self):
        #data = pd.read_csv('train.csv')
        #self.removeLanguage(data, "en", "trainEnglish.csv")
        return

    def writeToFile(self, data, fileName):
        data.to_csv(fileName)

    #This function removes the article from the dataset if its not the desired language.
    def removeLanguage (self, dataToTraverse, languageToKeep):
        for index, row in dataToTraverse.iterrows():
            try:
                if detect(row['text']) != languageToKeep:
                    dataToTraverse = dataToTraverse.drop(index)
                    
            except:
                pass

    def removeHTML(self, data):
        cleaner = re.compile('<.*?>')
        for index, row in data.iterrows():
            row['text'] = re.sub(cleaner, '', str(row['text']))
        return data
                    