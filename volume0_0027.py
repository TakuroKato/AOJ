# -*- coding:utf-8 -*-
from datetime import date
LIST=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

while True:
    m, d = map(int,input().split())
    if m == 0:
        break
    print(LIST[date(2004,m,d).weekday()])
