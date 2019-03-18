import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from vocabulary import Vocabulary
from DataSetCleaner import DataSetCleaner
#todo - clean data set again and check if its weird or not
# Figure out the math of what needs doing
# Hassle with python
# Check if results is between 0 and 1
# What is the machine learning part of this?

##Our cleaned train dataset is weird, so using the uncleansed one.
df = pd.read_csv('train.csv', delimiter=',')
vocabulary = Vocabulary('fn.csv')
""" 
#P(A) this is a touple with p[0] is real article, p[1] fake article
probabilityOfArticleBeingRealOrFake = vocabulary.probabilityOfRealAndFakeArticlesFromTheDataset(df) """

y = df.label
X = df.drop('label', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=69)



