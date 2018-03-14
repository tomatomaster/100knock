#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

sentence = u"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
sentence = sentence.split()
chem_map = {}

list = [0,4,5,6,7,8,14,15,18]
for i in range(len(sentence)):
    if i in list:
        chem_map[sentence[i][:1]] = sentence[i]
        list.remove(i)
    else:
        chem_map[sentence[i][:2]] = sentence[i]

for key in chem_map.keys():
    print('{0} = {1}'.format(key, chem_map[key]))
    
