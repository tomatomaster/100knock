#!/bin/python3
# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
import collections

counter = collections.defaultdict(int)
for line in open('hightemp.txt'):
    counter[line.split()[0]] += 1
       
sorted_list = []
for k,v in sorted(counter.items(), key=lambda x: -x[1]):
    sorted_list.append('{0}:{1}'.format(k,v))

print(sorted_list)