# -*- coding:utf-8 -*-

def hit_blow(a,b):
    hit = 0
    blow = 0
    for i in range(4):
        if a[i] == b[i]:
            hit += 1
    for i in range(4):
        for j in range(4):
            if a[i] == b[j]:
                blow += 1
    blow -= hit
    print(hit,blow)
    return 0

while True:
    try:
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        hit_blow(a,b)
    except EOFError:
        break
