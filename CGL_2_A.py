# -*- coding:utf-8 -*-
def judge(x):
    x0,y0,x1,y1,x2,y2,x3,y3 = map(float,x.split())
    if x1 - x0 == 0:
        if x3 -x2 == 0:
            print('2')
        elif y3 - y2 == 0:
            print('1')
        else:
            print('0')
    elif x3 - x2 == 0:
        if y1 - y0 == 0:
            print('1')
        else:
            print('0')
    elif y1 - y0 == 0:
        if y3 - y2 == 0:
            print('2')
        elif x3 - x2 == 0:
            print('1')
        else:
            print('0')
    elif y3 - y2 == 0:
        if x1 - x0 == 0:
            print('1')
        else:
            print('0')
    else:
        a1 = (y1-y0)/(x1-x0)
        a2 = (y3-y2)/(x3-x2)
        if a1 * a2 == -1:
            print('1')
        elif a1 == a2 or a1 == -a2:
            print('2')
        else:
            print('0')
n = int(input())            
q = ['']*n
for i in range(n):
    q[i] = input()
for i in range(n):        
    judge(q[i])
