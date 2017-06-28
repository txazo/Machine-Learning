#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# 原始数据集
dataSet = list(csv.reader(open("./pima-indians-diabetes.csv", "rb")))
# 训练数据集
trainDataSet = dataSet[:500]
# 测试数据集
testDataSet = dataSet[500:]

train_X = np.array([trainDataSet[i][:8] for i in range(0, len(trainDataSet))]).astype(np.float)
train_Y = np.ravel([trainDataSet[i][8:] for i in range(0, len(trainDataSet))]).astype(np.float)
test_X = np.array([testDataSet[i][:8] for i in range(0, len(testDataSet))]).astype(np.float)
test_Y = np.ravel([testDataSet[i][8:] for i in range(0, len(testDataSet))]).astype(np.float)

clf = GaussianNB()
# 模型训练
clf.fit(train_X, train_Y)
# 模型预测
pred = clf.predict([[4, 205, 23, 56, 500, 5, 0.1, 20]])
print("Predict: %d" % pred)
pred = clf.predict(test_X)
# 评估精度
accuracy = accuracy_score(pred, test_Y)
print("Accuracy Score: %f" % accuracy)
