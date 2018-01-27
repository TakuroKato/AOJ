# -*- coding:utf-8 -*-
cup = {'A':1,'B':0,'C':0}
while True:
    try:
        d = list(input().split(','))
        tmp = cup[d[0]]
        cup[d[0]] = cup[d[1]]
        cup[d[1]] = tmp
    except EOFError:
        break
for c in 'ABC':
    if cup[c] == 1:
        print(c)
