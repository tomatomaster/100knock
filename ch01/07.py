#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import sys 

sys.stdin = codecs.getreader('shift_jis')(sys.stdin)
stdin = raw_input()
in_list = stdin.split()
print in_list
print(u"{0}時の{1}は{2}".format(in_list[0], in_list[1], in_list[2]))