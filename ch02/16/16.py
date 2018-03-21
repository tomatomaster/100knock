#!/bin/python3

n = input("Please input number you like:")
n = int(n)
num_lines = sum(1 for lines in open('hightemp.txt','r'))

if num_lines < n:
    exit("Input number is too big !! Please in put number is below " + str(num_lines))

w_files = []
for i in range(n):
    print("Create File" + str(i))
    w_files.append(open("File"+str(i),'w'))

w_line = num_lines/n

f_count = 0
for i,line in enumerate(open('hightemp.txt','r')):
    w_files[f_count].write(line)
    if (i+1)%w_line == 0:
        f_count += 1
