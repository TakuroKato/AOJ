# -*- coding:utf-8 -*-
def partition(A, p, r):
    x, i = A[r], p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

n = int(input())
A = list(map(int,input().split()))
s = partition(A,0,n-1)
print(*A[:s],end = ' ')
print([A[s]],end = ' ')
print(*A[s+1:])
