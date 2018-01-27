# -*- coding:utf-8 -*-

S = int(input())

h = S//(60*60)
S = S%(60*60)
m = S//60
S = S%60
s = S
print(h,m,s,sep=':')
