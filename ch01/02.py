#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

word1 = u'パトカー'
word2 = u'タクシー'
for i in range(len(word2)):
    sys.stdout.write(word1[i]+word2[i])
