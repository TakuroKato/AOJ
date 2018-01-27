# -*- coding:utf-8 -*-
rh = 0
rect = 0
while True:
    try:
        a,b,c = map(int,input().split(','))
        if a == b:
            rh += 1
        elif a**2 + b**2 == c**2:
            rect += 1
    except EOFError:
        break
print(rect)
print(rh)
