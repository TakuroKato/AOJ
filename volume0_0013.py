# -*- coding:utf-8 -*-
array = []
while True:
    try:
        n = int(input())
        array.append(n)
    except EOFError:
        break
data = []
for i in range(len(array)):
    if array[i] == 0:
        elm = data.pop()
        print(elm)
    else:
        data.append(array[i])
