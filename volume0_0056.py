# -*- coding:utf-8 -*-
def mark(s, x):
    for i in range(x + x, len(s), x):
        s[i] = False

def sieve(n):
    s = [True] * n
    for x in range(2, int(n**0.5) + 1):
        if s[x]: mark(s, x)
    return [i for i in range(0,n) if s[i] and i > 1]

p = sieve(

def goldbach(n):
    
n = []
while True:
    try:
        n.append(int(input()))
    except EOFError:
        break
    
