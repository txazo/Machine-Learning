#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# 结巴中文分词

import jieba

sentence = "小明是一个云计算专家"

# 精确模式分词
words = jieba.cut(sentence, cut_all=False)
print(", ".join(words))

# 自定义词典
jieba.load_userdict("./userdict.txt")
words = jieba.cut(sentence, cut_all=False)
print(", ".join(words))

import jieba.analyse

content = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"

# 基于TF-IDF算法的关键词抽取
for k, w in jieba.analyse.extract_tags(content, topK=10, withWeight=True):
    print("%s: %s" % (k, w))

# 基于TextRank算法的关键词抽取
for k, w in jieba.analyse.textrank(content, topK=10, withWeight=True):
    print("%s: %s" % (k, w))

import jieba.posseg as pseg

# 词性标注(参考汉语词性标注集)
for k, w in pseg.cut("我爱北京天安门"):
    print("%s: %s" % (k, w))

# 并行分词
jieba.enable_parallel(4)
