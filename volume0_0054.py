# -*- coding:utf-8 -*-
a = []
b = []
n = []
while True:
    try:
        tmp = list(input().split())
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))
        n.append(int(tmp[2]))
    except EOFError:
        break

for i in range(len(a)):
    s = 0
    for j in range(n[i]):
        f = a[i]*(10**(j+1))
        s += (f//b[i])%10
    print(s)
