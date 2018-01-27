# -*- coding:utf-8 -*-
# 最小回数になっていない
n,m = map(int,input().split())
c = list(input().split(' '))
count = 0
for i in range(m):
    c[-1-i] = int(c[-1-i])
    if n == 0:
        break
    if n//c[-1-i] != 0:
        count += n//c[-1-i]
        n -= (n//c[-1-i])*c[-1-i]
        print(n)
        print(count)
print(count)
