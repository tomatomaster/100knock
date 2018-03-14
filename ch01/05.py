#!/usr/bin/env python
# -*- coding: utf-8 -*-

sentence = "test test1 test2 test3"
words = sentence.split()

n = 2
lists = []

for i in range(len(words)):
    lists.append(words[i:i+n])

print lists
