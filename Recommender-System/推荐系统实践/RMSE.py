#!/usr/bin/python3
# -*- coding: utf-8 -*-

# RMSE

import math

def RMSE(data):
    return math.sqrt(sum([(x - y) * (x - y) for x, y in data]) / float(len(data)))

def MAE(data):
    return sum([abs(x - y) for x, y in data]) / float(len(data))

data = [[1, 6], [2, 5], [3, 4]]
rmse = RMSE(data)
mae = MAE(data)
print('rmse={}'.format(rmse))
print('mae={}'.format(mae))
