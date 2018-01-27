# -*- coding:utf-8 -*-

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)

n = int(input())
a = list(map(int,input().split()))
p = lcm(a[0],a[1])
for i in range(n):
    p = lcm(p,a[i])
print(int(p))
