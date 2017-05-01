# -*- coding: UTF-8 -*-

f = file('data.txt','w')
f.write("我们都是好孩子")
f.close()

f2 = file('data.txt')
while True:
    line = f2.readline()
    if(len(line) == 0):
        break;
    print line
f2.close()