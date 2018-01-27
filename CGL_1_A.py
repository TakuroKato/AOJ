# -*- coding:utf-8 -*-
x1,y1,x2,y2 = map(float,input().split())
q = int(input())
x,y = [],[]
for i in range(q):
    x_t,y_t = map(float,input().split())
    x.append(x_t)
    y.append(y_t)

if x1 == x2:
    for i in range(q):
        print(x1,y[i])
elif y1 == y2:
    for i in range(q):
        print(x[i],y1)
else:
    a = (y2-y1)/(x2-x1)
    b = y1-a*x1
    for i in range(q):
        d = y[i]+(1/a)*x[i]
        px = (d-b)/(a+1/a)
        py = a*px+b
        print(px,py)
