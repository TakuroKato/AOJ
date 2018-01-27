# -*- coding:utf-8 -*-
n = []
while True:
    try:
        tmp = int(input())
        if tmp == 0:
            break
        else:
            n.append(tmp)
    except EOFError:
        break

for i in range(len(n)):
    c = 0
    d = 5
    for j in range(1,n[i]+1):
        while d <= n[i]:
            c += (n[i]//d)
            d *= 5
    print(c)
