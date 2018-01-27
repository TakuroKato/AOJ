# -*- coding:utf-8 -*-

string = input()
array = string.split()
a,b,c = int(array[0]),int(array[1]),int(array[2])

if a < b and b < c:
    print('Yes')
else:
    print('No')
    
