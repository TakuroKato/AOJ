# -*- coding:utf-8 -*-
n,k = map(int,input().split())
w = [0]*n
sum = 0
for i in range(n):
    w[i] = int(input())
    sum += w[i]

def func(p):
    return k*p

p = 1
while True:
    if func(p) >= sum:
        print(p)
        break
    else:
        p += 1
