# -*- coding:utf-8 -*-
d = []
while True:
    try:
        n,b = input().split(',')
        d.append(b)
    except EOFError:
        break

A,B,O,AB = [],[],[],[]
for i in range(len(d)):
    if d[i] == 'A':
        A.append(i)
    elif d[i] == 'B':
        B.append(i)
    elif d[i] == 'AB':
        AB.append(i)
    elif d[i] == 'O':
        O.append(i)
    else:
        print('error')
print(len(A))
print(len(B))
print(len(AB))
print(len(O))
