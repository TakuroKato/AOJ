# -*- coding:utf-8 -*-
n = int(input())
arr = []
for i in range(n):
    c = input()
    try:
        tmp = c.split()
        com = str(tmp[0])
        num = int(tmp[1])
    except:
        com = str(c)
        num = -1

    if num != -1:
        if com == 'insert':
            arr.insert(0,num)
        if com == 'delete':
            ind = arr.index(num)
            arr.pop(ind)
    else:
        if com == 'deleteFirst':
            arr.pop(0)
        if com == 'deleteLast':
            arr.pop(-1)
if len(arr) != 1:
    for i in range(len(arr)-1):
        print(arr[i], end = ' ')
    print(arr[-1])
else:
    print(arr[0])
