import numpy as np
import pandas as pd
from string import punctuation
import re

class Vocabulary:
    def __init__(self, fileName):
        self.file = pd.read_csv(fileName, delimiter=',')
        self.words = self.file['words']

    def countWords (self, data):
        featureMatrix = {}
        translator = str.maketrans('', '', punctuation)
        for index, row in data.iterrows():
            featureMatrix[index] = {}
            article = str(row['text'])
            for word in self.words:
                (featureMatrix[index])[word] = article.translate(translator).lower().split().count(word)
        return pd.DataFrame.from_dict(featureMatrix)

    def countWordsTotal (self, data): 
        featureMatrix = {}
        translator = str.maketrans('', '', punctuation)
        for index, row in data.iterrows():
            article = str(row['text'])
            cleanedArticle = article.translate(translator).lower().split()
            for word in self.words:
                if word in featureMatrix:
                    featureMatrix[word] += cleanedArticle.count(word)
                else:
                    featureMatrix[word] = cleanedArticle.count(word)
            print(featureMatrix)    
        return pd.DataFrame.from_dict(featureMatrix)




