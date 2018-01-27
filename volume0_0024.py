# -*- coding:utf-8 -*-

def experiment(v):
    n = 1
    k = 4.9
    while True:
        y = 5*n-5
        v_ex = 2*4.9*(y/k)**0.5
        if v_ex >= v:
            return n
            break
        else:
            n += 1

while True:
    try:
        v = float(input())
        print(experiment(v))
    except EOFError:
        break
