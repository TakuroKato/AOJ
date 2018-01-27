# -*- coding:utf-8 -*-
while True:
    n = int(input())
    x = []
    if n == 0:
        break
    d = [0]*4000
    for i in range(n):
        e,p,q = map(int,input().split())
        d[e] += p*q
    flag = 0
    for i in range(4000):
        if d[i] >= 1000000:
            print(i)
            flag = 1
    if flag == 0:
        print('NA')
