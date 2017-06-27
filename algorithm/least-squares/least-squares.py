#!/usr/bin/python
# -*- coding: utf-8 -*-

# 最小二乘法

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

def func(p, x):
    k, b = p
    return k * x + b

def error(p, x, y):
    return func(p, x) - y

Xi = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Yi = np.array([10, 12, 21, 23, 29, 33, 42, 43, 50, 53])
p0 = [1, 20]

res = leastsq(error, p0, args=(Xi, Yi))
k, b = res[0]
print("k = %s, b = %s" % (k, b))

plt.scatter(Xi, Yi, color="green", label="Sample Data", linewidth=2)

x = np.linspace(0, 12, 100)
y = k * x + b
plt.plot(x, y, color="red", label="Straight Line", linewidth=2)
plt.legend()
plt.show()
