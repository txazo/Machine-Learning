#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 集成学习

import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report

titanic = pd.read_csv('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')

X = titanic[['pclass', 'age', 'sex']]
y = titanic['survived']

X['age'].fillna(X['age'].mean(), inplace=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)

vec = DictVectorizer(sparse=False)
X_train = vec.fit_transform(X_train.to_dict(orient='record'))
X_test = vec.transform(X_test.to_dict(orient='record'))

# 决策树分类器
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
dtc_y_predict = dtc.predict(X_test)
dtc_score = dtc.score(X_test, y_test)
dtc_report = classification_report(y_test, dtc_y_predict, target_names=['died', 'survived'])
print('DecesionTree Classifier Score: {}'.format(dtc_score))
print('DecesionTree Classifier Report: \n{}'.format(dtc_report))

# 随机森林分类器
rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)
rfc_y_predict = rfc.predict(X_test)
rfc_score = rfc.score(X_test, y_test)
rfc_report = classification_report(y_test, rfc_y_predict, target_names=['died', 'survived'])
print('RandomForest Classifier Score: {}'.format(rfc_score))
print('RandomForest Classifier Report: \n{}'.format(rfc_report))

# 梯度提升决策树
gbc = GradientBoostingClassifier()
gbc.fit(X_train, y_train)
gbc_y_predict = gbc.predict(X_test)
gbc_score = gbc.score(X_test, y_test)
gbc_report = classification_report(y_test, gbc_y_predict, target_names=['died', 'survived'])
print('GradientBoosting Classifier Score: {}'.format(gbc_score))
print('GradientBoosting Classifier Report: \n{}'.format(gbc_report))
