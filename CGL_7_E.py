# -*- coding:utf-8 -*-
x1,y1,r1 = map(float,input().split())
x2,y2,r2 = map(float,input().split())
a,b = x2-x1,y2-y1
d = (a**2+b**2+r1**2-r2**2)/2
x = (d*a+b*(((a**2+b**2)*r1**2 - d**2)**0.5))/(a**2+b**2)
y = (d*b-a*(((a**2+b**2)*r1**2 - d**2)**0.5))/(a**2+b**2)

z = (d*a-b*(((a**2+b**2)*r1**2 - d**2)**0.5))/(a**2+b**2)
w = (d*b+a*(((a**2+b**2)*r1**2 - d**2)**0.5))/(a**2+b**2)
if x < z:
    print(x1+x,y1+y,end=' ')
    print(x1+z,y1+w)

elif x > z:
    print(x1+z,y1+w,end=' ')
    print(x1+x,y1+y)
elif y < w:
    print(x1+x,y1+y,end=' ')
    print(x1+z,y1+w)
else:
    print(x1+z,y1+w,end=' ')
    print(x1+x,y1+y)
