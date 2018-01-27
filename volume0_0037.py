# -*- coding:utf-8 -*-
hor = []
var = []
for i in range(5):
    hor.append(input().split())
    if i == 4:
        break
    else:
        var.append(input().split())

h = []
for i in range(len(hor)):
    h[i] =  list(hor[i])

print(h)
i,j = 0,0
