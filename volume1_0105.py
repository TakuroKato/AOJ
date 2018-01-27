# -*- coding:utf-8 -*-
data = []
while True:
    try:
        data.append(input())
    except EOFError:
        break

d = {}
for i in range(len(data)):
    i,n = data[i].split()
    if i in d:
        d[i].append(n)
    else:
        d[i] = [n]
d = sorted(d.items(), key = lambda x:x[0])
for i in range(len(d)):
    i,n = d[i]
    n = map(int,n)
    print(i)
    n = sorted(n)
    for i in range(len(n)-1):
        print(n[i], end = ' ')
    print(n[-1])
