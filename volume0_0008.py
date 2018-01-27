# -*- coding:utf-8 -*-
#Write a program which reads an integer n and identifies the number of combinations of a,b,c and d (0 ≤ a,b,c,d ≤ 9) which meet the following equality:
#a+b+c+d=n
import sys

x = [0]*51
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                x[a+b+c+d] += 1

array = []
for i in sys.stdin:
    array.append(i)

for k in range(len(array)):
    n = array[k]
    print(x[int(n)])
    
