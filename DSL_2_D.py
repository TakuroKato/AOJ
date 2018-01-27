#! -*- coding:utf-8 -*-
n,q = map(int,input().split())
query = [0] * q
for i in range(q):
    query[i] = input()
arr = [2**31 - 1] * n

for i in range(q):
    tmp = list(query[i].split())    
    if len(tmp) == 4:

        s = int(tmp[1])
        t = int(tmp[2])
        for i in range(s,t+1):
            arr[i] = tmp[3]
    else:
        print(arr[int(tmp[1])])
