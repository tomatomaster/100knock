#!/usr/bin/env python
# -*- coding: utf-8 -*-

sentence1 = "paraparaparadise"
sentence2 = "paragraph"

#和集合
sum = sentence1 + sentence2
print sum

#積集合
mul_dic = {}
mul = []
for i in range(len(sentence1)):
    mul_dic[sentence1[i]] = True

for i in range(len(sentence2)):
    if mul_dic.get(sentence2[i], False) :
        mul.append(sentence2[i])
print mul

#差集合
diff = []
for i in range(len(sentence2)):
    if not(mul_dic.get(sentence2[i], False)) :
        diff.append(sentence2[i])
print diff


check = "se"
for i in range(len(sentence1) - 1):
    if sentence1[i:i+2] == check:
        print("{0} contains {1}".format(sentence1, check))
    
for i in range(len(sentence2) - 1):
    if sentence1[i:i+2] == check:
        print("{0} contains {1}".format(sentence2, check))
