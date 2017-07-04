#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sklearn.datasets import fetch_20newsgroups
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

news = fetch_20newsgroups(subset='all')

X_train, X_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25, random_state=33)

vec = CountVectorizer()
X_train = vec.fit_transform(X_train)
X_test = vec.transform(X_test)

mnb = MultinomialNB()
mnb.fit(X_train, y_train)
y_predict = mnb.predict(X_test)
score = mnb.score(X_test, y_test)
report = classification_report(y_test, y_predict, target_names=news.target_names)
print('Naive Bayes Classifier Score: {}'.format(score))
print('Naive Bayes Classifier Report: {}'.format(report))