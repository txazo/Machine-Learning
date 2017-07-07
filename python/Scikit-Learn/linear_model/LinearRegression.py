#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 普通最小二乘法线性回归

import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

diabetes = load_diabetes()

X = diabetes.data[:, np.newaxis, 2]
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)

lr = LinearRegression(normalize=True)
lr.fit(X_train, y_train)
print('coef: {}, intercept: {}'.format(lr.coef_, lr.intercept_))

plt.scatter(X_test, y_test, color='red')
plt.plot(X_test, lr.predict(X_test), color='green', linewidth=2)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
