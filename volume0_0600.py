# -*- coding:utf-8 -*-
#まだ解けていない
#処理に時間がかかりすぎ？
import math
def norm(a,b):
    if a > b:
        return math.sqrt(a**2-b**2)
    else:
        return math.sqrt(b**2-a**2)

n = int(input())
a = [0]*n
for i in range(n):
    a[i] = int(input())

m = 0
opt = [0,0,0]
count = 0
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(j+1,n):
            g1,g2,g3 = 0,0,0
            if i != 0:
                for x in range(i+1,j):
                    g1 += a[x]
            else:
                for x in range(i,j):
                    g1 += a[x]
                    
            for x in range(j,k):
                g2 += a[x]
                
            if i == 0:
                for x in range(k,n):
                    g3 += a[x]
            elif k == n:
                for x in range(i+1):
                    g3 += a[x]
            else:
                for x in range(k,n):
                    g3 += a[x]
                for x in range(i+1):
                    g3 += a[x]
            count +=1
            l = min(g1,g2,g3)
            if m < l:
                m = l
                opt = [i,j,k]

print(m)
