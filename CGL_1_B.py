# -*- coding:utf-8 -*-
x1,y1,x2,y2 = map(float,input().split())
det = x1 - x2
if det != 0:
    a = (y1 - y2) / det
    b = (-(y1 * x2) + y2 * x1) / det

q = int(input())
x,y = [],[]
for i in range(q):
    x_t,y_t = map(float,input().split())
    x.append(x_t)
    y.append(y_t)

if det == 0:
    for i in range(q):
        print(-x[i],y[i])
elif y2 == y1:
    for i in range(q):
        print(x[i],-y[i])
else:
    for i in range(q):
        k = y[i] + 1/a * x[i]
        s = (k - b)/(a + 1/a)
        print(s+(s-x[i]),-1/a * (s+(s-x[i])) + k)
