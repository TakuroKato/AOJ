# -*- coding:utf-8 -*-
import sys

w = int(input())
n = int(input())

array = []
for i in range(n):
    array.append(input())

a, b = [], []
for i in range(n):
    s = array[i]
    a.append(s[0])
    b.append(s[1])
    a[i], b[i] = int(a[i]), int(b[i])

lines = []
k = 0
for i in range(w):
    lines.append(k)
    k += 1 

for i in range(n):
    tmp1 = lines[a[i]-1]
    tmp2 = lines[b[i]-1]
    lines[a[i]-1] = tmp2
    lines[b[i]-1] = tmp1

for i in range(len(lines)):
    print(lines[i]+1)
