# -*- coding:utf-8 -*-
#Write a program which solve a simultaneous equation:
#ax+by=c
#dx+ey=f
#The program should print x and y for given a, b, c, d, e and f (-1,000 ≤ a,b,c,d,e,f ≤ 1,000). You can suppose that given equation has a unique solution. 
import sys

def solve_eq(a,b,c,d,e,f):
    x = ((e*c)-(b*f))/((a*e)-(b*d))
    y = ((a*f)-(c*d))/((a*e)-(b*d))
    if x == -0:
        x = 0
    if y == -0:
        y = 0
        
    sol = [x,y]
    return sol

array = []
for i in sys.stdin:
    array.append(i)

a = [0]*6
for i in range(len(array)):
    x = array[i].split()
    for i in range(len(x)):
        a[i] = float(x[i])

    ans = solve_eq(a[0],a[1],a[2],a[3],a[4],a[5])
    print("{0:0.3f}".format(ans[0]), "{0:0.3f}".format(ans[1]))
