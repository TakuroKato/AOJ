# -*- coding:utf-8 -*-
def judge(data):
    num = list(map(int,data.split()))
    a,b = 0,0
    for i in range(10):
        if a <= num[i]:
            a = num[i]
        elif b <= num[i]:
            b = num[i]
        else:
            print('NO')
            return 0
    print('YES')
    return 0
            
n = int(input())
array = [0]*n
for i in range(n):
    array[i] = input()

for i in range(n):
    judge(array[i])

