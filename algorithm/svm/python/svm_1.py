#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 支持向量机

from sklearn.datasets import load_boston
from sklearn.cross_validation import train_test_split
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

boston = load_boston()
X = boston.data
y = boston.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.25)

ss_X = StandardScaler()
ss_y = StandardScaler()

X_train = ss_X.fit_transform(X_train)
X_test = ss_X.fit_transform(X_test)
y_train = ss_y.fit_transform(y_train)
y_test = ss_y.fit_transform(y_test)

# 使用线性核函数配置的支持向量机进行回归训练
linear_svr = SVR(kernel='linear')
linear_svr.fit(X_train, y_train)
linear_svr_y_predict = linear_svr.predict(X_test)

# 使用多项式核函数配置的支持向量机进行回归训练
poly_svr = SVR(kernel='poly')
poly_svr.fit(X_train, y_train)
poly_svr_y_predict = poly_svr.predict(X_test)

# 使用径向基核函数配置的支持向量机进行回归训练
rbf_svr = SVR(kernel='rbf')
rbf_svr.fit(X_train, y_train)
rbf_svr_y_predict = rbf_svr.predict(X_test)

# 对三种核函数进行测评
print('R-squared value of linear SVR is ', linear_svr.score(X_test, y_test))
print('R-squared value of poly SVR is ', poly_svr.score(X_test, y_test))
print('R-squared value of rbf SVR is ', rbf_svr.score(X_test, y_test))
