import pandas as pd
from langdetect import detect
from DataSetCleaner import DataSetCleaner
from vocabulary import Vocabulary

dataSetCleaner = DataSetCleaner

""" #Clean the train.csv dataset 
data = pd.read_csv('train.csv', delimiter=',')
data = dataSetCleaner.removeLanguage(DataSetCleaner, data, 'en')
data = dataSetCleaner.removeHTML(DataSetCleaner, data)
dataSetCleaner.writeToFile(DataSetCleaner, data, 'train.csv') """

""" #Counting the words from the vocabulary fn.csv in the articles.
vocabulary = Vocabulary('fn.csv')
totalWords = vocabulary.countWordsTotal(data)
dataSetCleaner.writeToFile(dataSetCleaner, totalWords, 'words.csv')
print(totalWords) """

#Counting words in real and fake news and doing the probabilities
vocabulary = Vocabulary('fn.csv')
data = pd.read_csv('trainEnglish.csv', delimiter=',')
#print(vocabulary.probabilityOfRealAndFakeArticlesFromTheDataset(data))

amountOfRealAndFakeArticles = vocabulary.numberOfArticlesRealAndFake(data)
wordsInArticles = vocabulary.countWordsTotalFakeOrRealArticle(data)
wordsInArticles = vocabulary.calculateTheProbabilityOfWordOccurancesAndAddColumns(data, wordsInArticles, amountOfRealAndFakeArticles)
dataSetCleaner.writeToFile(dataSetCleaner, wordsInArticles, 'wordsInArticles.csv')


#print(vocabulary.totalNumberOfWordsInRealAndFakeArticles(data))