# -*- coding:utf-8 -*-
def dist(ax,ay,bx,by):
    return ((bx-ax)**2 + (by-ay)**2)**0.5

x1,y1,r1 = map(float,input().split())
x2,y2,r2 = map(float,input().split())

d = dist(x1,y1,x2,y2)
if d > r1 + r2:
    print(4)
elif d == r1+r2:
    print(3)
elif d + r1 == r2 or d + r2 == r1:
    print(1)
elif d + r1 < r2 or d + r2 < r1:
    print(0)
else:
    print(2)
