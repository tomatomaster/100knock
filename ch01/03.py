#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
sentence = sentence.replace(",","").replace(".","")
wordList =  sentence.split()
for word in wordList:
    print len(word),

