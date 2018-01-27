# -*- coding:utf-8 -*-

import sys

array = []
for i in sys.stdin:
    if int(i) == 0:
        break
    array.append(int(i))

for i in range(len(array)):
    print('Case ',i+1,': ',array[i],sep='')
