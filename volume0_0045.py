# -*- coding:utf-8 -*-
x = []
y = []
while True:
    try:
        tmp = list(input().split(','))
        x.append(int(tmp[0]))
        y.append(int(tmp[1]))
    except EOFError:
        break
    
sum = 0
for i in range(len(x)):
    sum += x[i]*y[i]
total = 0
for i in range(len(y)):
    total += y[i]
print(sum)
print(int(total / len(y) + 0.5))
