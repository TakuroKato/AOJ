# -*- coding:utf-8 -*-
NIL = -1

class Node:
    parent = NIL
    left = NIL
    right = NIL

def getDepth(u):
    d = 0
    while T[u].parent != NIL:
        u = T[u].parent
        d += 1
    return d

def getChildren(u):
    c = T[u].left
    result = []
    while c != NIL:
        result.append(c)
        c = T[c].right
    return result

n = int(input())
T = [0]*n
for i in range(n):
    T[i] = Node()
    
for i in range(n):
    tmp = list(map(int,input().split()))
    id = tmp.pop(0)
    k = tmp.pop(0)
    c = tmp
    if k != 0:
        for j in range(len(c)):
            T[c[j]].parent = id
        T[id].left = c[0]
        for j in range(len(c)-1):
            T[c[j]].right = c[j+1]
            
for i in range(n):
    d = getDepth(i)
    c = getChildren(i)
    if d == 0:
        t = 'root'
    elif c == []:
        t = 'leaf'
    else:
        t = 'internal node'
    print('node ',i,': ','parent = ',T[i].parent,', depth = ',d,', ',t,', ',c,sep = '')
