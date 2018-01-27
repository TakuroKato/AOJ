# -*- coding:utf-8 -*-
array = []
while True:
    try:
        a = int(input())
        array.append(a)
    except EOFError:
        break

data = [0]*101
for i in range(len(array)):
    data[array[i]] += 1
    
m = [i for i,j in enumerate(data) if j == max(data)]
for i in range(len(m)):
    print(m[i])
