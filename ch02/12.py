#!/usr/bin/env python
# -*- coding: utf-8 -*-

data_f = open('./hightemp.txt','r')
col1 = open('./col1.txt','w')
col2 = open('./col2.txt','w')

lines = []
for line in data_f:
    lines = line.split()
    col1.write(lines[0]+'\n')
    col2.write(lines[1]+'\n')

