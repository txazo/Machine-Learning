#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import nltk
import urllib2
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

response = urllib2.urlopen('http://python.org')
html = response.read()
clean = BeautifulSoup(html, 'html.parser').get_text()
tokens = [tok for tok in clean.split()]

freq_dist_nltk = nltk.FreqDist(tokens)
for k, v in freq_dist_nltk.items():
    print(str(k), ": ", str(v))

freq_dist_nltk.plot(50, cumulative=False)
