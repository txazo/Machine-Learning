#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import numpy as np
import pandas as pd

# 基于物品的协同过滤推荐

# 初始化
def init(ratings, movies):
    print('---------- 基于物品的协同过滤推荐 ----------')
    print('---------- 初始化 ----------')
    # {用户:{物品:评分}}
    userMap = {}
    # {物品:[物品名,[用户]]}
    itemMap = {}
    for index, row in ratings.iterrows():
        if row[0] not in userMap:
            userMap[row[0]] = {}
        if row[1] not in itemMap:
            itemMap[row[1]] = ['', []]
        userMap[row[0]][row[1]] = row[2]
        itemMap[row[1]][1].append(row[0])
    for index, row in movies.iterrows():
        if row[0] in itemMap:
            itemMap[row[0]][0] = row[1]
    print('---------- 初始化完成 ----------')
    return userMap, itemMap

# 同现相似度
def cooccurrence_similarity(itemMap, itemId1, itemId2):
    users1 = itemMap[itemId1][1]
    users2 = itemMap[itemId2][1]
    sameUsers = [userId for userId in users1 if userId in users2]
    if len(sameUsers) == 0:
        return 0
    return len(sameUsers) / math.sqrt(len(users1) * len(users2))

# top-N相似物品
def topNSimItem(itemMap, itemId, n=20):
    sims = [(cooccurrence_similarity(itemMap, itemId, other), other) for other in itemMap if other != itemId]
    sims.sort()
    sims.reverse()
    return sims[:n]

# 生成top-N相似物品集
def generateTopNItems(itemMap, n=20):
    topNItemMap = {}
    for index, item in enumerate(itemMap.items()):
        if index % 100 == 0:
            print('---------- {} {}'.format(len(itemMap), index))
        topNItemMap[item[0]] = topNSimItem(itemMap, item[0], n)
    return topNItemMap

# 基于物品的top-N推荐
def topNRecommendByItemCF(userMap, itemMap, topNItemMap, userId, n=10):
    predictScores = {}
    userItems = userMap[userId]
    for itemId, score in userMap[userId].items():
        for sim, other in topNItemMap[itemId]:
            if other not in userItems:
                if other not in predictScores:
                    predictScores[other] = 0
                predictScores[other] += sim * score
    sortPredictScores = [(score, itemMap[itemId][0]) for itemId, score in predictScores.items()]
    sortPredictScores.sort()
    sortPredictScores.reverse()
    return [(name, score) for score, name in sortPredictScores[:n]]

k = 10
ratings = pd.read_csv('./data/ratings.csv')
movies = pd.read_csv('./data/movies.csv')
userMap, itemMap = init(ratings, movies)
topNItemMap = generateTopNItems(itemMap)
for userId in userMap:
    print('用户{}的Top-N推荐: {}'.format(userId, topNRecommendByItemCF(userMap, itemMap, topNItemMap, userId, k)))
