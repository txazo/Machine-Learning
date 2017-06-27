#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# 语料库

from nltk.corpus import gutenberg

print gutenberg.fileids()

from nltk import FreqDist

fd = FreqDist()
for word in gutenberg.words("austen-persuasion.txt"):
    fd.inc(word)

print fd.N()
print fd.B()

for word in fd.keys()[:10]:
    print("%s: %s" % (word, fd[word]))
