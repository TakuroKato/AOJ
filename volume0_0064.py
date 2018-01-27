# -*- coding:utf-8 -*-
# 連番，例えば100を個別に1,0,0と解釈してしまう
arr = []
while True:
    try:
      s = list(input())
      arr += s
    except EOFError:
        break
table = [0,1,2,3,4,5,6,7,8,9]
for i in range(len(table)):
    table[i] = str(table[i])
    
sum = 0
for i in range(len(arr)):
    if arr[i] in table:
        sum += int(arr[i])
print(sum)
