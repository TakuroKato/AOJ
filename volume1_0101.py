# -*- coding:utf-8 -*-
n = int(input())
arr = ['']*n
for i in range(n):
    arr[i] = list(input().split())

for i in range(n):
    for j in range(len(arr[i])):
        if arr[i][j] == 'Hoshino':
            arr[i][j] = 'Hoshina'
for i in range(n):
    for j in range(len(arr[i])-1):
        print(arr[i][j],end = ' ')
    print(arr[i][-1])
