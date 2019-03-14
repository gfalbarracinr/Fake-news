import numpy as np
import pandas as pd
from string import punctuation
import re


class Vocabulary:
    def __init__(self, fileName):
        self.file = pd.read_csv(fileName, delimiter=',')
        self.words = self.file['words']

    def countWordsPerArticle(self, data):
        featureMatrix = {}
        translator = str.maketrans('', '', punctuation)
        for index, row in data.iterrows():
            featureMatrix[index] = {}
            article = str(row['text'])
            for word in self.words:
                (featureMatrix[index])[word] = article.translate(
                    translator).lower().split().count(word)
        return featureMatrix

 

    # This function counts all the words from the vocabulary in all the articles.
    # Then return a dataframe containing the list of words and their frequency.
    def countWordsTotal(self, data):
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
        return pd.DataFrame(list(featureMatrix.items()), columns=['words', 'count'])


    def countWordsTotalFakeOrRealArticle(self, data):
        realArticleWordCounts = {}
        fakeArticleWordCounts = {}
        translator = str.maketrans('', '', punctuation)
        for index, row in data.iterrows():
            article = str(row['text'])
            cleanedArticle = article.translate(translator).lower().split()
            for word in self.words:
                label = str(row["label"])
                count = cleanedArticle.count(word)
                if label == "1":
                    if word in fakeArticleWordCounts :
                        fakeArticleWordCounts[word] += count 
                    else:
                        fakeArticleWordCounts[word] = count
                else:
                    if word in realArticleWordCounts :
                        realArticleWordCounts[word] += count
                    else:
                        realArticleWordCounts[word] = count
        
        df = pd.DataFrame(list(realArticleWordCounts.items()), columns=['words', 'realCount'])
        df["fakeCount"] = list(fakeArticleWordCounts.values())
        return df
    
    def totalNumberOfWordsInRealAndFakeArticles(self, data):
        countReal = 0
        countFake = 0
        translator = str.maketrans('', '', punctuation)

        for index, row in data.iterrows():
            article = str(row['text'])
            cleanedArticle = article.translate(translator).lower().split()
            if str(row['label']) == '0':
                countReal += len(cleanedArticle)
            else:
                countFake += len(cleanedArticle)
        return countReal, countFake
    
    #Only run once
    #Probability of a word occuring in articles
    def calculateTheProbabilityOfWordOccurancesAndAddColumns (self, data, features, articlesRealAndFake):
        featureProbabilitiesInRealArticles = []
        featureProbabilitiesInFakeArticles = []
        for index, row in features.iterrows():
            featureProbabilitiesInRealArticles.append(int(row['realCount']) / articlesRealAndFake[0]) 
            featureProbabilitiesInFakeArticles.append(int(row['fakeCount']) / articlesRealAndFake[1]) 
        features['probabilityInRealArticles'] = featureProbabilitiesInRealArticles
        features['probabilityInFakeArticles'] = featureProbabilitiesInFakeArticles
        return features

    def countWordInAnArticle(self, article, wordToCount):
        translator = str.maketrans('', '', punctuation)
        cleanedArticle = article.translate(translator).lower().split()
        return cleanedArticle.count(wordToCount)

    def probabilityOfRealAndFakeArticlesFromTheDataset(self, data):
        countReal = 0
        countFake = 0
        for index, row in data.iterrows():
            if str(row['label']) == "0":
                countReal += 1
            else:
                countFake += 1
        total = countFake + countReal
        return countReal/total, countFake/total

    def numberOfArticlesRealAndFake(self, data):
        countReal = 0
        countFake = 0
        for index, row in data.iterrows():
            if str(row['label']) == "0":
                countReal += 1
            else:
                countFake += 1
        total = countFake + countReal
        return countReal, countFake
