#!/usr/bin/python3
# -*- coding: utf-8 -*-

#### SVM

from sklearn.svm import SVC

X = [[0, 0], [1, 1]]
y = [0, 1]
clf = SVC(kernel='linear')
clf.fit(X, y)
pred = clf.predict([[2., 2.]])
print(pred[0])
