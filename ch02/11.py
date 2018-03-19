read_f = open('./hightemp.txt', 'r')
write_f = open('replacedTab2Space.txt', 'w')

for line in read_f:
    write_f.write(line.expandtabs(1))

