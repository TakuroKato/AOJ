# -*- coding:utf-8 -*-
d = []
while True:
    try:
        d.append(float(input()))
    except EOFError:
        break
print(max(d)-min(d))
