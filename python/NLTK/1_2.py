#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen('http://python.org')
html = response.read()
clean = BeautifulSoup(html, 'html.parser').get_text()
tokens = [tok for tok in clean.split()]

freq_dist_nltk = nltk.FreqDist(tokens)
for k, v in freq_dist_nltk.items():
    print(str(k), ": ", str(v))

freq_dist_nltk.plot(50, cumulative=False)
