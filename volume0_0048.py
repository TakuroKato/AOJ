# -*- coding:utf-8 -*-
def weigh(w):
    if w <= 48.0:
        print('light fly')
    elif w > 48.0 and w <= 51.0:
        print('fly')
    elif w > 51.0 and w <= 54.0:
        print('bantam')
    elif w > 54.0 and w <= 57.0:
        print('feather')
    elif w > 57.0 and w <= 60.0:
        print('light')
    elif w > 60.0 and w <= 64.0:
        print('light welter')
    elif w > 64.0 and w <= 69.0:
        print('welter')
    elif w > 69.0 and w <= 75.0:
        print('light middle')
    elif w > 75.0 and w <= 81.0:
        print('middle')
    elif w > 81.0 and w <= 91.0:
        print('light heavy')
    else:
        print('heavy')
    return 0

d = []
while True:
    try:
        d.append(float(input()))
    except EOFError:
        break

for i in range(len(d)):
    weigh(d[i])
