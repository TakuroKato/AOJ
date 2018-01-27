# -*- coding:utf-8 -*-

string = input()
array = string.split()
x = [int(array[0]),int(array[1]),int(array[2])]
y = sorted(x)

for value in y:
    print(value, end=' ')
print('')
