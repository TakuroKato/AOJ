# -*- coding:utf-8 -*-
# 良い解放が思いつかなかったので放置
x0,y0,x1,y1 = map(float,input().split())

def inc(a0,b0,a1,b1):
    det = a0 - a1
    if det != 0:
        a = (b0 - b1) / det
        b = (-(b0 * a1) + b1 * a0) / det
        return a

q = int(input())
x,y = [],[]
for i in range(q):
    x_t,y_t = map(float,input().split())
    x.append(x_t)
    y.append(y_t)

for i in range(len(x)):
    print(i)
    if x[i] != x0:
        if x[i] <= x0 <= x1 or x1 <= x0 <= x[i]:
            print('ONLINE_BACK')
        elif x0 <= x1 <= x[i] or x[i] <= x1 <= x0:
            print('ONLINE_FRONT')
        else:
            print('ON_SEGMENT')
        
