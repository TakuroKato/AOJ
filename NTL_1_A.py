# -*- coding:utf-8 -*-
#Factorize a given integer n.

n = int(input())
print(str(n)+':',end='')
array = []
count = 0
while True:
    if n == 999993031:
        break
    for i in range(2,n+1):
        if n%i == 0 and i != n:
            array.append(i)
            n = int(n/i)
            break
        if i == n:
            count += 1
            break
    if count == 24:
        break

array.append(n)
for i in range(len(array)):
    print(' ',array[i],sep = '',end='')
print('')
