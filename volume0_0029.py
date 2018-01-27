# -*- coding:utf-8 -*-

string = list(str(input()).split(' '))
l = [0]*len(string)
k = 0
r = 0
for i in range(len(string)):
    if len(string[i]) > k:
        k = len(string[i])
        r = i
    for j in range(len(string)):
        if string[i] == string[j]:
            l[i] += 1
m = l.index(max(l))
print(string[m],string[r],sep = ' ')
