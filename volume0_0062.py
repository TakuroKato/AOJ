# -*- coding:utf-8 -*-
s = []
while True:
    try:
        s.append(str(input()))
    except EOFError:
        break

def func(x):
    array = []
    if len(x) == 1:
        return x[0]
    for i in range(len(x)-1):
        array.append((x[i] + x[i+1]) % 10)
    return func(array)

for i in range(len(s)):
    arr = list(s[i])
    for j in range(len(arr)):
        arr[j] = int(arr[j])
    print(func(arr))
        
