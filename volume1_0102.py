# -*- coding:utf-8 -*-
while True:
    n = int(input())
    if n == 0:
        break
    arr = [[0] * n] * n
    for i in range(n):
        arr[i] = list(map(int,input().split()))

    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += arr[i][j]
        arr[i].append(tmp)

    last_line = []
    for j in range(n):
        tmp = 0
        for i in range(n):
            tmp += arr[i][j]
        last_line.append(tmp)

    tmp = 0
    for i in range(n):
        tmp += last_line[i]
    last_line.append(tmp)

    for i in range(len(arr[i])-1):
        for j in range(len(arr[i])):
            print('{0:5d}'.format(arr[i][j]),end = '')
        print('')
    for i in range(len(last_line)):
        print('{0:5d}'.format(last_line[i]),end = '')
    print('')
