# -*- coding:utf-8 -*-
#There is a data which provides heights (in meter) of mountains. The data is only for ten mountains.Write a program which prints heights of the top three mountains in descending order.

import sys

data = []
count = 0
for i in sys.stdin:
    data.append(int(i))
    count = count+1
    if count == 10:
        break

N = len(data)
m = 100

for i in range(m):
    for n in range(N-1):
        a = data[n]
        b = data[n+1]
        if a <= b:
            data[n] = b
            data[n+1] = a
        else:
            pass
for i in range(3):
    print(data[i])
