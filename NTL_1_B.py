# -*- coding:utf-8 -*-
def mpow(x,n,mod):
    if n == 0:
        return 1
    if n % 4 == 0:
        return mpow((x**4)%mod,int(n/4),mod)
    elif n%4 == 1:
        return (mpow(x,int(n-1),mod)*x)%mod
    elif n%4 == 2:
        return (mpow(x,int(n-2),mod)*(x**2))%mod
    elif n%4 == 3:
        return (mpow(x,int(n-3),mod)*(x**3))%mod
n,m = map(int,input().split())
mod = 1000000007
print(mpow(n,m,mod))
