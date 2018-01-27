# -*- coding:utf-8 -*-
import math

def walk(d,angle):
    x = d*math.cos(angle)
    y = d*math.sin(angle)
    p = [x,y]
    return p

x,y,angle = 0,0,90
while True:
    d, a = map(int, input().split(","))
    p = walk(d,math.radians(angle))
    x += p[0]
    y += p[1]
    angle -= a
    if d == a == 0:
        break

print(int(x))
print(int(y))
