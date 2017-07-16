#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import numpy as np

# 信息熵

def comentropy(array):
    array = np.float32(array / np.sum(array))
    return - np.sum([i * math.log(i) for i in array])

num = 1000
print(comentropy(np.arange(5, num, 1)))
print(comentropy(np.arange(5, num, 5)))
print(comentropy(np.abs(np.random.rand(num))))
