# -*- coding:utf-8 -*-
import math

def check_intersect(x1,y1,r1,x2,y2,r2):
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)    

    if d > r1+r2:
        print('0')
    elif d < math.sqrt((r1-r2)**2):
        if r1 > r2:
            print('2')
        else:print('-2')
    else:
        print('1')
        
n = int(input())
for i in range(n):
    x1,y1,r1,x2,y2,r2 = map(float,input().split())
    check_intersect(x1,y1,r1,x2,y2,r2)
