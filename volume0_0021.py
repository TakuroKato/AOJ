# -*- coding:utf-8 -*-
def check_para(x1,y1,x2,y2,x3,y3,x4,y4):
    if x1 == x2 and x4 == x3:
        print('YES')
        return 0
    elif x1 == x2 or x3 == x4:
        print('NO')
        return 0
    k1 = (y2-y1)/(x2-x1)
    k2 = (y4-y3)/(x4-x3)
    if abs(k1-k2) < 1e-10:
        print('YES')
    else:
        print('NO')

n = int(input())
for i in range(n):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(float,input().split())
    check_para(x1,y1,x2,y2,x3,y3,x4,y4)

