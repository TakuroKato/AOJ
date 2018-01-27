# -*- coding:utf-8 -*-
#Write a program which reads an integer n and prints the number of prime numbers which are less than or equal to n. A prime number is a natural number which has exactly two distinct natural number divisors: 1 and itself. For example, the first four prime numbers are: 2, 3, 5 and 7.

import sys

# return the number of prime numbers smaller than n
def prime(n):
    l = range(0,n+1)
    i,k = 0,2
    result = 1

    if n >= 3:
        prime_nums = [2, 3]
    else:
        prime_nums = []

    while i <= n:
        while l[i] > k:
            result = l[i]%k
            k = k+1
            if result == 0:
                break
            if (l[i]-1 == k) and (result != 0):
                prime_nums.append(l[i])

        i, k = i+1, 2

    #return prime_nums
    return len(prime_nums)

while True:
    try:        
        psum = prime(int(input()))
        print(psum)
    except:
        break
    
