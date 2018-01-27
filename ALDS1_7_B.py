# -*- coding:utf-8 -*-
NIL = -1
class Node:
    parent = NIL
    left = NIL
    right = NIL
    type = NIL
    depth = NIL
    sibling = NIL
    degree = NIL
    height = NIL
    
def setHeight(u):
    h1 = h2 = 0
    if T[u].right != NIL:
        h1 = setHeight(T[u].right) + 1
    if T[u].left != NIL:
        h2 = setHeight(T[u].left) + 1
    if h1 == h2 == NIL:
        return NIL
    else:
        return max(h1,h2)

def getDepth(u):
    d = 0
    while T[u].parent != NIL:
        u = T[u].parent
        d += 1
    return d

def getSibling(u):
    if T[u].parent == NIL:
        return NIL
    if T[T[u].parent].left != u and T[T[u].parent].left != NIL:
        return T[T[u].parent].left
    if T[T[u].parent].right != u and T[T[u].parent].right != NIL:
        return T[T[u].parent].right
    return NIL

def getDegree(u):
    deg = 0
    if T[u].left != NIL:
        deg += 1
    if T[u].right != NIL:
        deg += 1
    return deg

n = int(input())
T = [0]*n

for i in range(n):
    T[i] = Node()
for i in range(n):
    id,l,r = map(int,input().split())
    T[id].left = l
    T[id].right = r
    
for i in range(n):
    if T[i].left != NIL:
        T[T[i].left].parent = i
    if T[i].right != NIL:
        T[T[i].right].parent = i

for i in range(n):
    if T[i].parent == NIL:
        T[i].type = 'root'
    elif T[i].parent != NIL and (T[i].left != NIL or T[i].right != NIL):
        T[i].type = 'internal node'
    else:
        T[i].type = 'leaf'

for i in range(n):
    T[i].depth = getDepth(i)
    T[i].sibling = getSibling(i)
    T[i].degree = getDegree(i)
    T[i].height = setHeight(i)
for i in range(n):
    print('node ',i,': parent = ',T[i].parent,', sibling = ',T[i].sibling,', degree = ',T[i].degree,', depth = ',T[i].depth,', height = ',T[i].height,', ',T[i].type,sep = '')
