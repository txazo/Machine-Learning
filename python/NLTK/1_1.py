#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
import operator
import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen('http://python.org')
html = response.read()
clean = BeautifulSoup(html, 'html.parser').get_text()
tokens = [tok for tok in clean.split()]

freq_dis = {}
for tok in tokens:
    if tok in freq_dis:
        freq_dis[tok] += 1
    else:
        freq_dis[tok] = 1

sorted_freq_dis = sorted(freq_dis.items(), key=operator.itemgetter(1), reverse=True)
for word in sorted_freq_dis:
    print(word[0], ': ', word[1])
