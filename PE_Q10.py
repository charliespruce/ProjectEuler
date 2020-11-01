# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:47:02 2019

@author: charl
"""

def isprime(n):
    from math import sqrt
    for r in range(2,int(sqrt(n))+1):
        if n % r == 0:
            return False
    return True

total = 0
for i in range(2,2000000):
    if isprime(i) == True:
        total += i
print(total)