# -*- coding:utf-8 -*-
N = int(input())
data1 = []
data2 = []
for i in range(N):
    data1.append(int(input()))
    data2.append(int(input()))

for i in range(N):
    if data1[i] > 10**80-1 or data2[i] > 10**80-1 or data1[i]+data2[i] > 10**80-1:
        print('overflow')
    else:
        print(data1[i]+data2[i])
