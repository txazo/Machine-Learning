#!/usr/bin/python
# -*- coding: utf-8 -*-

# 最小二乘法

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

def real_func(x):
    return x ** 2 - x * 4 + 5

def func(p, x):
    a, b, c = p
    return a * (x ** 2) + b * x + c

def error(p, x, y):
    return func(p, x) - y

Xi = np.linspace(0, 4, 10)
Yi = [np.random.normal(0.1, 0.5) + y for y in real_func(Xi)]
p0 = [1, 1, 1]

res = leastsq(error, p0, args=(Xi, Yi))
a, b, c = res[0]
print("a = %s, b = %s, c = %s" % (a, b, c))

plt.scatter(Xi, Yi, color="green", label="Sample Data", linewidth=1)

x = np.linspace(0, 5, 100)
y = a * (x ** 2) + b * x + c
plt.plot(x, y, color="red", label="Straight Line", linewidth=1)
plt.legend()
plt.show()
