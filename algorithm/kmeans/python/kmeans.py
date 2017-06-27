#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# K-Means

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1],
              [0, 0.8], [0.4, 0.9], [0.7, 0.5], [1.1, 1.3],
              [1.8, 1.6], [2.1, 2.5], [2.6, 2.4], [2.8, 3.2],
              [2, 2], [2, 3], [3, 2], [3, 3],
              [0.2, 2.6], [0.5, 2.2], [0.5, 3.3], [0.6, 2.8]])

res = KMeans(n_clusters=3).fit(X)
# 聚类标签
tag = res.labels_
# 聚类中心
center = res.cluster_centers_
# 画数据点
plt.scatter(X[:, 0], X[:, 1], c=tag)
# 画聚类中心点
plt.scatter(center[:, 0], center[:, 1], c=('red', 'green', 'blue'))
plt.title("KMeans")
plt.show()
