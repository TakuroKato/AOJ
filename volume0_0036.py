# -*- coding:utf-8 -*-
def judge(array):
    count = [[0 for i in range(8)] for i in range(8)]
    for i in range(8):
        x = 0
        for j in array[i]:
            if int(j) == 1:
                count[i][x] += 1
            x += 1

    a = 0
    p = []
    for i in range(8):
        for j in range(8):
            if count[i][j] != 0:
                p.append(a)
            a += 1

    if p[0]+1 != p[1]:
        if p[0] + 8*3 == p[3]:
            print('B')
        else:
            if p[0] + 8*2 + 1 == p[3]:
                print('F')
            else:
                print('D')
    else:
        if p[0]+1 == p[1] and p[1]+1 == p[2]:
            print('C')
        else:
            if p[0] + 8 == p[2] and p[1] + 8 == p[3]:
                print('A')
            else:
                if p[0]+8 == p[3]:
                    print('G')
                else:
                    print('E')
                    
while True:
    try:
        array = []
        for i in range(8):
            array.append(input())
        judge(array)
        input()
    except:
        break
