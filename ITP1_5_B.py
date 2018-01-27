# -*- coding:utf-8 -*-

def frame(H,W):
    for i in range(W):
        print('#',end='')
    print('')
    for j in range(1,H-1):
        for i in range(W):
            if i == 0 or i == W-1:
                print('#',end='')
            else:
                print('.',end='')
        print('')
    for i in range(W):
        print('#',end='')
    print('')

import sys
for i in sys.stdin:
    H,W = map(int,i.split())
    if H == 0 and W == 0:
        break
    print('')
    frame(H,W)
    #if H == 0 and W == 0:
    #    break

