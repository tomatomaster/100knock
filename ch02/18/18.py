#!/bin/python3

sort_seed_dict = {}
for line in open('hightemp.txt'):
    splitedLine = line.split()
    sort_seed_dict[line] = float(splitedLine[2])

sorted_list= []
for k, v in sorted(sort_seed_dict.items(), key=lambda x: x[1]):
    sorted_list.append(k)

for line in sorted_list:
    print(line)
    


