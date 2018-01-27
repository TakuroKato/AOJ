# -*- coding:utf-8 -*-

w = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
w.reverse()
def weight(x):
    res = []
    for i in range(len(w)):
        if w[i] <= x:
           res.append(i)
           x = x-w[i]
    return res
while True:
    try:
        x = int(input())
        res = weight(x)
        res.reverse()
        print(w[res[0]],end = '')
        for i in range(1,len(res)):
            print(' ',w[res[i]],sep = '',end = '')
        print('')
    except EOFError:
        break
