#!/usr//bin/python3
# -*- coding: utf-8 -*-

# NumPy: 同种元素的多维数组

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)

a = np.arange(0, 20, 3)
a = np.arange(24).reshape(2, 3, 4)

a = np.linspace(0, 10, 21)

a = np.random.rand(2, 4)

a = np.random.randn(2, 4)
