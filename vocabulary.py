import numpy as np
import pandas as pd
from string import punctuation
import re


def countWords (data, words):
    featureMatrix = {}
    translator = str.maketrans('', '', punctuation)
    for index, row in data.iterrows():
        featureMatrix[index] = {}
        article = str(row['text'])
        for word in words:
            (featureMatrix[index])[word] = article.translate(translator).lower().split().count(word)
    return featureMatrix

def countWordsTotal (data, words): 
    featureMatrix = {}
    translator = str.maketrans('', '', punctuation)
    for index, row in data.iterrows():
        article = str(row['text'])
        for word in words:
            if word in featureMatrix:
                featureMatrix[word] += article.translate(translator).lower().split().count(word)
            else:
                featureMatrix[word] = article.translate(translator).lower().split().count(word)
    return featureMatrix

data = pd.read_csv('testEnglish.csv', delimiter=',')
word = ['elections', "trump" ]
string = "this is random text and it's a test for the method a aa a. a' "
newMatrix = countWordsTotal(data, word)
print (newMatrix)



