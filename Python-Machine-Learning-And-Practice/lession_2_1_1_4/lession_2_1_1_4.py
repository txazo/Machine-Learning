#!/usr/bin/python3
# -*- coding: utf-8 -*-

# K近邻

from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state=33)

ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

# K近邻分类器
knc = KNeighborsClassifier()
knc.fit(X_train, y_train)
y_predict = knc.predict(X_test)
score = knc.score(X_test, y_test)
report = classification_report(y_test, y_predict, target_names=iris.target_names)
print('KNeighbors Classifier Score: {}'.format(score))
print('KNeighbors Classifier Report: \n{}'.format(report))
