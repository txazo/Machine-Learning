#!/usr/bin/python
# -*- coding: utf-8 -*-

# 高斯朴素贝叶斯

import numpy as np
from sklearn.naive_bayes import GaussianNB

# 训练特征数据集
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# 训练标签数据集
Y = np.array([1, 1, 1, 2, 2, 2])

clf = GaussianNB()
clf.fit(X, Y)
# 分类预测
print(clf.predict([[-0.8, -1]]))
