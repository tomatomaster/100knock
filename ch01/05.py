#!/usr/bin/env python
# -*- coding: utf-8 -*-

sentence = raw_input()
words = sentence.split()

n = 2
n_gram_senten = []
n_gram_word = []

for i in range(len(words)):
    n_gram_senten.append(words[i:i+n])

print n_gram_senten

for i in range(len(sentence)):
    n_gram_word.append(sentence[i:i+n])

print n_gram_word
