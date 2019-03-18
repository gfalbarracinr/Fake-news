import pandas as pd
from langdetect import detect
from DataSetCleaner import DataSetCleaner
from vocabulary import Vocabulary
from sklearn.model_selection import train_test_split 
import re
import math 
import sys



""" #Clean the train.csv dataset 
data = pd.read_csv('train.csv', delimiter=',')
data = dataSetCleaner.removeLanguage(DataSetCleaner, data, 'en')
data = dataSetCleaner.removeHTML(DataSetCleaner, data)
dataSetCleaner.writeToFile(DataSetCleaner, data, 'train.csv') """

dataSetCleaner = DataSetCleaner
vocabulary = Vocabulary('fn.csv')

def test(data):
    count = 0
    countotal = 0
    for index, row in data.iterrows():

        article = str(row['text'])
        prediction = predict(article)
        label = row['label']
        if label == prediction:
            count += 1
        countotal += 1 

    return count/countotal
def train(data):

    #Calculating word probabilities P(A)
    probabilityOfArticleBeingRealOrFake = vocabulary.probabilityOfRealAndFakeArticlesFromTheDataset(data)
    probabilityFakeOrRealArticle = open("probabilityFakeOrRealArticle.txt", "w+")
    probabilityFakeOrRealArticle.write(str(probabilityOfArticleBeingRealOrFake[0])+"\n")
    probabilityFakeOrRealArticle.write(str(probabilityOfArticleBeingRealOrFake[1]))

    probabilityFakeOrRealArticle.close()

    #Counting the amount of words there are in real and fake articles all together
    totalNumberOfWordsInRealAndFakeArticles = vocabulary.totalNumberOfWordsInRealAndFakeArticles(data)

    #counting the total amount of features in fake and real articles
    wordsInArticles = vocabulary.countWordsTotalFakeOrRealArticle(data)

    #Calculating the probability of a feature being present in fake and real articles
    wordsInArticles = vocabulary.calculateTheProbabilityOfWordOccurancesAndAddColumns(data, wordsInArticles, totalNumberOfWordsInRealAndFakeArticles)

    #Writing all the calculations to a file
    vocabulary.writeToFile(wordsInArticles, 'wordsInArticles.csv')

def predict (article):
    #Features that are in the article
    features = vocabulary.wordOccurancesOfFeaturesInANewArticle(article)

    #Dicts with feature probabilities
    realProbabilityDict = vocabulary.getProbabilitiesForRealArticles(pd.read_csv('wordsInArticles.csv', delimiter=','))
    fakeProbabilityDict = vocabulary.getProbabilitiesForFakeArticles(pd.read_csv('wordsInArticles.csv', delimiter=','))

    #P(A) probability of article being fake or real, getting that from a file
    probabilityOfArticleBeingRealOrFake = []
    fileWithProbabilities = open("probabilityFakeOrRealArticle.txt")
    for line in fileWithProbabilities:
        probabilityOfArticleBeingRealOrFake.append(line)
    
    # PI(P(wi | y = 0)) = probabilityReal and PI(P(wi | y = 1))  = probabilityFake
    probabilityReal = likelihoodProbabilityReal(features, realProbabilityDict)
    probabilityFake = likelihoodProbabilityFake(features, fakeProbabilityDict)
    #Multiplying likelihood probability with probability of article being real
    probabilityReal *= float(probabilityOfArticleBeingRealOrFake[0])
    probabilityFake *= float(probabilityOfArticleBeingRealOrFake[1])

    #dividing with  PI(P(wi | y = 1))P(A) + PI(P(wi | y = 0))P(A)
    probabilityReal /= probabilityReal + probabilityFake
    probabilityFake /= probabilityReal + probabilityFake

    # #doing the logarithm part from the forumala
    #probabilityFake = math.log(probabilityFake)
    #probabilityReal = math.log(probabilityReal)

    #We'll use the probabilities without the log here for the time being
    #Returns the label, 1 for fake and 0 for real

    # probabilityFake = math.log(probabilityFake)
    # probabilityReal = math.log(probabilityReal)

    #We'll use the probabilities without the log here for the time being
    #Returns the label, 1 for fake and 0 for real
    if probabilityFake > probabilityReal:
        return 1
    else:
        return 0
    
# PI(P(wi | y = 0))
def likelihoodProbabilityReal(featureList, realProbabilities):

    featureProbabilitiesMultiplied = 1
    #multiplying all the feature probabilities found in article. Likelihood probabilities.
    for w in featureList:
        featureProbabilitiesMultiplied *= realProbabilities[w]
    
    return featureProbabilitiesMultiplied

#PI(P(wi | y = 1))
def likelihoodProbabilityFake(featureList, fakeProbabilities):

    featureProbabilitiesMultiplied = 1
    #multiplying all the feature probabilities found in article. Likelihood probabilities.
    for w in featureList:
        featureProbabilitiesMultiplied *= fakeProbabilities[w]

    return featureProbabilitiesMultiplied

# df = pd.read_csv('trainEnglish.csv', delimiter=',')
# y = df.label
# X = df
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=69)

# #train(X_train)
# dataset = X_test.append(y_test)
# #Example on how the prediction can work
# articleReal = " words words words more lalala such is life only potato"
# articleFake = "just writing my article very articulate " 
# print(test(dataset))

#Prints out the prediction where 0 is for real article and 1 is for a fake one.
print(predict(sys.argv[1]))



