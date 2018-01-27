# -*- coding:utf-8 -*-
def solve(i,m):
    if m == 0:
        return True
    if i >= n:
        return False
    res = solve(i+1,m) or solve(i+1,m - A[i])
    return res

n = int(input())
A = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

for j in range(q):
    if solve(0,m[j]):
        print('yes')
    else:
        print('no')
