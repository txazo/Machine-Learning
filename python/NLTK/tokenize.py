#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# 分词

sentence = "Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\n\nThanks."

# \w+|[^\w\s]+
from nltk.tokenize import WordPunctTokenizer

words1 = WordPunctTokenizer().tokenize(sentence)

# 正则分词
from nltk.tokenize import RegexpTokenizer

words2 = RegexpTokenizer('\w+|\$[\d\.]+|\S+').tokenize(sentence)
