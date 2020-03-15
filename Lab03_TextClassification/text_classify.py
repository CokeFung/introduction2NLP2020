import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Text Preprocessing
import nltk
# nltk.download("all")
from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize
from nltk import NaiveBayesClassifier, classify

def normalization(text_list):
	features = {}
	word_list = [word.lower() for word in text_list]
	for word in word_list:
		features[word] = True
	return features


def tokenization(text):
	tokenize = word_tokenize(text)
	return normalization(tokenize)

def train(features, proportion):
	train_size = int(len(features) * proportion)
	train_set, test_set = features[:train_size], features[train_size:]
	print("Training set size = " + str(len(train_set)) + " emails")
	print("Testing set size = " + str(len(test_set)) + " emails")
	print()
	classifier = NaiveBayesClassifier.train(train_set)
	return train_set, test_set, classifier

def evaluate(train_set, test_set, classifier):
	print("Accuracy on the training set = " + str(classify.accuracy(classifier, train_set)))
	print("Accuracy on the testing set = " + str(classify.accuracy(classifier, test_set)))
	print()
	classifier.show_most_informative_features(50)

def main():
	#read data from .csv file and change columns name
	messages = pd.read_csv("./spam.csv", encoding="latin-1")
	messages = messages.drop(labels = ["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis = 1)
	messages.columns = ["category", "text"]

	all_features = []
	ind = 0
	data_len = len(messages)
	for row in messages.itertuples():
		#build features
		all_features.append((tokenization(row.text), row.category))
	

	train_set, test_set, classifier = train(all_features, 0.8)
	evaluate(train_set, test_set, classifier)


main()