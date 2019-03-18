import numpy as np
import pandas as pd
from string import punctuation
import re


class Vocabulary:
    def __init__(self, fileName):
        self.file = pd.read_csv(fileName, delimiter=',')
        self.words = self.file['words']


    #Count feature words per article
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

    #This function counts the appearence of the words from the vocabulary in all the real and fake articles
    # and then adds them to the datafram under realCount and fakeCount respectively 
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
    
    #This function counts the total amount of words there are in all the real
    # and all the fake articles and return a tuple where [0] are amount of real worlds
    # and [1] is amount of fake words.
    # len(re.findall(r'\w+', article)) - this is not a cleaned "text" though regex should remove punctioation as well
    def totalNumberOfWordsInRealAndFakeArticles(self, data):
        countReal = 0
        countFake = 0
        translator = str.maketrans('', '', punctuation)

        for index, row in data.iterrows():
            article = str(row['text'])
            if str(row['label']) == '0':
                countReal += len(re.findall(r'\w+', article))
            else:
                countFake += len(re.findall(r'\w+', article))
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

    #Count how many times a word appears in a given article
    def countWordInAnArticle(self, article, wordToCount):
        translator = str.maketrans('', '', punctuation)
        cleanedArticle = article.translate(translator).lower().split()
        return cleanedArticle.count(wordToCount)

    #Returns probability P(A) if an article is fake or not judging by all the articles
    def probabilityOfRealAndFakeArticlesFromTheDataset(self, data):

        realAndFakeArticleNumber = self.numberOfArticlesRealAndFake(data)
        total = realAndFakeArticleNumber[0] + realAndFakeArticleNumber[1]
        return realAndFakeArticleNumber[0]/total, realAndFakeArticleNumber[1]/total

    #Counting how many real and fake articles there are. Counting labels and returning a touple where
    # [0] is amount of real articles and [1] is amount of fake articles. 
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

    #This function write data to a file
    def writeToFile(self, data, fileName):
        data.to_csv(fileName)

    #This function returns a dictionary of probabilities for features in real articles
    def getProbabilitiesForRealArticles(self, data):
        realArticleDict = {}
        for index, row in data.iterrows():
            realArticleDict[row['words']] = row['probabilityInRealArticles']
        return realArticleDict

    #This function returns a dictionary of probabilities for features in fake articles
    def getProbabilitiesForFakeArticles(self, data):
        fakeArticleDict = {}
        for index, row in data.iterrows():
            fakeArticleDict[row['words']] = row['probabilityInFakeArticles']
        return fakeArticleDict

    def wordOccurancesOfFeaturesInANewArticle(self, article):
        words = []
        translator = str.maketrans('', '', punctuation)
        cleanedArticle = article.translate(translator).lower().split()
        for w in self.words:
            if w in cleanedArticle:
                words.append(w)
        return words
    
    




