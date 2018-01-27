# -*- coding:utf-8 -*-
m = 1046527
n = int(input())
s = []
v = []
for i in range(n):
    tmp = input().split()
    s.append(str(tmp[0]))
    v.append(str(tmp[1]))

def h1(key):
    return key % m
def h2(key):
    return 1 + key % (m - 1)
def h(key,i):
    return ((h1(key) + i * h2(key))) % m

def insert(T,key):
    i = 0
    while True:
        j = h(key,i)
        if T[j] == -1:
            T[j] = key
            return j
        else:
            i += 1

def search(T,key):
    i = 0
    while True:
        j = h(key,i)
        if T[j] == key:
            return j
        elif T[j] == -1 or j >= m:
            return -1
        else:
            i += 1

def getChar(ch):
    if(ch == 'A'):
        return 1
    elif(ch == 'C'):
        return 2
    elif(ch == 'G'):
        return 3
    elif(ch == 'T'):
        return 4
    else:
        return 0

def getKey(string):
    sum = 0
    p = 1
    for i in range(len(string)):
        sum += p*getChar(string[i])
        p *= 5
    return sum

T = [-1]*m

for i in range(n):
    val = list(v[i])
    key = getKey(val)
    if s[i] == 'insert':
        insert(T,key)
    if s[i] == 'find':
        result = search(T,key)
        if result < 0:
            print('no')
        else:
            print('yes')
