# -*- coding:utf-8 -*-
def rec(x1,q):
    return x1-((x1**3-q)/(3*(x1**2)))

q = []
while True:
    try:
        tmp = int(input())
        if tmp == -1:
            break
        q.append(tmp)
    except EOFError:
        break
for i in range(len(q)):
    x1 = float(q[i]/2)
    while True:
        x1 = rec(x1,q[i])
        if abs(x1**3 - q[i]) < 0.00001*q[i]:
            break
    print(x1)
