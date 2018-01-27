# -*- coding:utf-8 -*-
def get_data():
    data = input().split(',')
    l = []
    for i in range(10):
        l.append(int(data[i]))
        v1,v2 = int(data[10]),int(data[11])
    return v1,v2,l

def meet_point(v1,v2,l):
    l_total = 0
    for i in range(10):
        l_total += l[i]
    t = l_total/(v1+v2)
    p = v1*t
    res = 0
    for i in range(10):
        res += l[i]
        if p <= res:
            return i+1

while True:
    try:
        v1,v2,l = get_data()
        print(meet_point(v1,v2,l))
    except EOFError:
        break
