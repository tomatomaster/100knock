#coding:utf-8

f=open('./hightemp.txt','r')

count_line = 0
for row in f:
    count_line+=1

print count_line
