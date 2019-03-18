from DataSetCleaner import DataSetCleaner
from vocabulary import Vocabulary
import pandas as pd


#Creating the helper classes, used for counting words, probabilities and writing to file.
dataSetCleaner = DataSetCleaner
vocabulary = Vocabulary('fn.csv')
data = pd.read_csv('trainEnglish.csv', delimiter=',')

#Counting the words from the vocabulary fn.csv in the articles.
totalWords = vocabulary.countWordsTotal(data)
dataSetCleaner.writeToFile(dataSetCleaner, totalWords, 'words.csv')
print(totalWords) 

#Counting words in real and fake news and doing the probabilities

amountOfRealAndFakeArticles = vocabulary.numberOfArticlesRealAndFake(data)
wordsInArticles = vocabulary.countWordsTotalFakeOrRealArticle(data)
wordsInArticles = vocabulary.calculateTheProbabilityOfWordOccurancesAndAddColumns(data, wordsInArticles, amountOfRealAndFakeArticles)
#dataSetCleaner.writeToFile(dataSetCleaner, wordsInArticles, 'wordsInArticles.csv')


#print(vocabulary.totalNumberOfWordsInRealAndFakeArticles(data))