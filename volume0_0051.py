# -*- coding:utf-8 -*-
def join_num(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[i] * 10**(7-i)
    return result
    
n = int(input())
x = [0] * n
for i in range(n):
    x[i] = str(input())

for i in range(n):
    d = []
    for c in x[i]:
        d.append(int(c))
    d.sort()
    a = join_num(d)
    d.reverse()
    b = join_num(d)
    print(b-a)
