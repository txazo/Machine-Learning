#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import numpy as np
import pandas as pd

# 基于用户的协同过滤推荐

# 初始化
def init(ratings, movies):
    print('---------- 基于用户的协同过滤推荐 ----------')
    print('---------- 初始化 ----------')
    # {用户:{物品:评分}}
    userMap = {}
    for index, row in ratings.iterrows():
        if row[0] not in userMap:
            userMap[row[0]] = {}
        userMap[row[0]][row[1]] = row[2]
    # {物品:物品名}
    itemMap = {}
    for index, row in movies.iterrows():
        itemMap[row[0]] = row[1]
    print('---------- 初始化完成 ----------')
    return userMap, itemMap

# 同现相似度
def cooccurrence_similarity(userMap, userId1, userId2):
    items1 = userMap[userId1]
    items2 = userMap[userId2]
    sameItems = [itemId for itemId in items1 if itemId in items2]
    if len(sameItems) == 0:
        return 0
    return len(sameItems) / math.sqrt(len(items1) * len(items2))

# top-N相似用户
def topNSimUser(userMap, userId, n=20):
    sims = [(cooccurrence_similarity(userMap, userId, other), other) for other in userMap if other != userId]
    sims.sort()
    sims.reverse()
    return sims[:n]

# 基于用户的top-N推荐
def topNRecommendByUserCF(userMap, itemMap, userId, n=10):
    simUsers = topNSimUser(userMap, userId)
    userItems = userMap[userId]
    predictScores = {}
    for sim, userId in simUsers:
        for itemId, score in userMap[userId].items():
            if itemId not in userItems:
                if itemId not in predictScores:
                    predictScores[itemId] = 0
                predictScores[itemId] += sim * score
    sortPredictScores = [(score, itemMap[itemId]) for itemId, score in predictScores.items()]
    sortPredictScores.sort()
    sortPredictScores.reverse()
    return [(name, score) for score, name in sortPredictScores[:n]]

k = 10
ratings = pd.read_csv('./data/ratings.csv')
movies = pd.read_csv('./data/movies.csv')
userMap, itemMap = init(ratings, movies)
for userId in userMap:
    print('用户{}的Top-N推荐: {}'.format(userId, topNRecommendByUserCF(userMap, itemMap, userId, k)))
