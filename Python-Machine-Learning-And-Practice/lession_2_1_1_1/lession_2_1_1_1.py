#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report

column_names = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'Class']

# 读取数据
data = pd.read_csv(
        'http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',
        names=column_names)

# 数据预处理
data = data.replace(to_replace='?', value=np.nan)
data = data.dropna(how='any')

# 数据集切分
X_train, X_test, y_train, y_test = train_test_split(data[column_names[1:10]], data[column_names[10]], test_size=0.25,
                                                    random_state=33)

ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

lr = LogisticRegression()
# 训练模型
lr.fit(X_train, y_train)
# 模型预测
lr_y_predict = lr.predict(X_test)
# 评分
lr_score = lr.score(X_test, y_test)
lr_report = classification_report(y_test, lr_y_predict, target_names=['良性', '恶性'])
print(lr_y_predict)
print("LR Classifier Score: {}".format(lr_score))
print("LR Classifier Score Report: {}".format(lr_report))

sgdc = SGDClassifier()
sgdc.fit(X_train, y_train)
sgdc_y_predict = lr.predict(X_test)
sgdc_score = sgdc.score(X_test, y_test)
sgdc_report = classification_report(y_test, sgdc_y_predict, target_names=['良性', '恶性'])
print("SGD Classifier Score: {}".format(sgdc_score))
print("LR Classifier Score Report: {}".format(sgdc_report))
