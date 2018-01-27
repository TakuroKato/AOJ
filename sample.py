# -*- coding:utf-8 -*-

print('test program of loop process')
while True:
    try:
        n = input()
        print(n)
    except EOFError:
        print('EOFError end')
        break

# 整数Nと空白区切りの整数リストを受け取る
print('----------------------------')
print('test program of input process')
n = int(input())
print(n)
A = list(map(int,input().split()))

# ３つの整数からなるカンマ区切りのリストを受け取る
while True:
    try:
        x,y,s = map(int,input().split(','))
        ink(x,y,s)
    except EOFError:
        break

# 整数を標準入力から行ごとに受けとり，リストに追加
while True:
    try:
        a = int(input())
        array.append(a)
    except EOFError:
        break

# 任意の個数の整数を受け取り，リストにする
a = list(map(int,input().split()))
    
# 最大公約数，最小公倍数を求める
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)
