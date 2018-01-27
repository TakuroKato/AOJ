# -*- coding:utf-8 -*-
import itertools

def cal(n,s):
    l = list(itertools.combinations(range(10),n))
    count = 0
    for i in l:
        if sum(i) == s:
            count += 1
    return count

while True:
    n,s = map(int,input().split())
    if n == 0 and s==0:
        break
    else:
        print(cal(n,s))
