import pandas as pd
from langdetect import detect
import re

class DataSetCleaner:


    def __init__(self):
        return

    def writeToFile(self, data, fileName):
        data.to_csv(fileName)

    #This function removes the article from the dataset if its not the desired language.
    def removeLanguage (self, dataToTraverse, languageToKeep):
        data = dataToTraverse
        for index, row in data.iterrows():
            try:
                if detect(row['text']) != languageToKeep:
                    data = data.drop(index)
                    
            except:
                pass
        return data

    def removeHTML(self, data):
        toReturn = data
        toReturn['text'] = toReturn['text'].str.replace('<.*?>', "")
        return toReturn



                  