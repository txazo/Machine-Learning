#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# 分句

import collections
from nltk.tokenize import sent_tokenize

str = "It was one of the worst movies I've seen, despite good reviews. \
    Unbelievably bad acting!! Poor direction. VERY poor production. \
    The movie was bad. Very bad movie. VERY bad movie. VERY BAD movie. VERY BAD movie!"
sentences = sent_tokenize(str)
print(sentences)
