# -*- coding:utf-8 -*-
import math
#lin関数にて，y軸に並行な直線を処理できない課題
def get_data():
    xa,ya,xb,yb,xc,yc,xd,yd = map(float,input().split(','))
    return xa,ya,xb,yb,xc,yc,xd,yd

def dist(x1,y1,x2,y2):
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return d

def lin(x1,y1,x2,y2):
    if x1 == x2:
        m = 10000000000    ac = dist(xa,ya,xc,yc)
    bd = dist(xb,yb,xd,yd)
    
    m1,n1 = lin(xb,yb,xd,yd)
    d1 = p_l(xa,ya,m1,n1)
    if ac < d1:
        print('NO')
        return 0
    
    m2,n2 = lin(xb,yb,xd,yd)
    d2 = p_l(xc,yc,m2,n2)
    if ac < d2:
        print('NO')
        return 0

    m3,n3 = lin(xa,ya,xc,yc)
    d3 = p_l(xb,yb,m3,n3)
    if bd < d3:
        print('NO')
        return 0
    
    m4,n4 = lin(xa,ya,xc,yc)
    d4 = p_l(xd,yd,m4,n4)
    if bd < d4:
        print('NO')
        return 0
    
    print('YES')
    return 0

while True:
    try:
        xa,ya,xb,yb,xc,yc,xd,yd = get_data()
        convex(xa,ya,xb,yb,xc,yc,xd,yd)
    except EOFError:
        break
