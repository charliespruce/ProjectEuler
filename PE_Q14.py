# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 00:46:16 2019

@author: charl
"""

def collatz(n):
    r = 1
    while not(n == 1):
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        r += 1
    return r

a = 0
for i in range(1,1000001):
    if collatz(i) > a:
        a = collatz(i)
        num = i
print(num)