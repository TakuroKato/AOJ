# -*- coding:utf-8 -*-
import sys

array = []
x,y = [],[]
for i in sys.stdin:
    array.append(i)
    if i == '0 0\n':
        break
    
for i in range(len(array)):
    x,y = array[i].split()
    if int(x) == 0 and int(y) == 0:
        break
    elif x > y:
        y,x = x,y
    print(x,y)
