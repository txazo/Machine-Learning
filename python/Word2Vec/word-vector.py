#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sklearn.datasets import fetch_20newsgroups
from bs4 import BeautifulSoup
import nltk, re

news = fetch_20newsgroups(subset='all')
X, y = news.data, news.target

def news_to_sentences(news):
    news_text = BeautifulSoup(news, 'html5lib').get_text()
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    raw_sentences = tokenizer.tokenize(news_text)
    sentences = []
    for sent in raw_sentences:
        sentences.append(re.sub('[^a-zA-Z]', ' ', sent.lower().strip()).split())

sentences = []
for x in X:
    sentences += news_to_sentences(x)

print(sentences)
