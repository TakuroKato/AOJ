# -*- coding:utf-8 -*-

import sys

def func(x):
    return x**2

def rec(x,d):
    return d*func(x)

array = []
for i in sys.stdin:
    array.append(int(i))

for i in range(len(array)):
    d = array[i]
    k = int(600/d)
    result = 0
    for j in range(k):
        result += rec(j*d,d)

    print(result)
