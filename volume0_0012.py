# -*- coding:utf-8 -*-
import sys
import math

def norm(x1,y1,x2,y2):
    r = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return r

def judge(x1,y1,x2,y2,x3,y3,xp,yp):
    r1 = norm(x1,y1,x2,y2)
    r2 = norm(x2,y2,x3,y3)
    r3 = norm(x3,y3,x1,y1)

    d1 = norm(xp,yp,x1,y1)
    d2 = norm(xp,yp,x2,y2)
    d3 = norm(xp,yp,x3,y3)

    if d1 > r1 or d1 > r3:
        print('NO')
    elif d2 > r1 or d2 > r2:
        print('NO')
    elif d3 > r3 or d3 > r2:
        print('NO')
    else:
        print('YES')

array = []
for i in sys.stdin:
    array.append(i)

for i in range(len(array)):
    tmp = array[i]
    x1,y1,x2,y2,x3,y3,xp,yp = map(float,tmp.split(' '))
    judge(x1,y1,x2,y2,x3,y3,xp,yp)
