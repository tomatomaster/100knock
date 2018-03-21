#!/bin/python3

n = input("Please input number you like:")
n = int(n)

f = open('hightemp.txt','r')
count = 0
for line in f:
    if n == count:
        break
    else:
        print(line)
        count += 1
