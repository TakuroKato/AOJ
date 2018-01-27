# -*- coding:utf-8 -*-
data = input()
a,b,c = data.split()

count = 0
for n in range(int(a),int(b)):
    if int(b) == 1:
        count = 0
    elif int(c)%n == 0:
        count += 1

print(count)
