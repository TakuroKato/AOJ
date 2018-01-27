# -*- coding:utf-8 -*-
#Your friend who lives in undisclosed country is involved in debt. He is borrowing 100,000-yen from a loan shark. The loan shark adds 5% interest of the debt and rounds it to the nearest 1,000 above week by week.

x = 100000
n = int(input())

for i in range(n):
    x = x + x*0.05
    a = x // 1000
    r = x % 1000
    if r != 0:
        x = 1000*a + 1000
    else:
        x = 1000*a
        
print(int(x))
