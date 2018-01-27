# -*- coding:utf-8 -*-
a = []
while True:
    try:
        a.append(float(input()))
    except EOFError:
        break

for i in range(len(a)):
    count = 0
    x = a[i]
    sum = a[i]
    for j in range(9):
        if count % 2 == 0:
            x *= 2
            sum += x
        else:
            x /= 3
            sum += x
        count += 1
    print(sum)
