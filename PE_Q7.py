# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:07:23 2019

@author: charl
"""

def isprime(n):
    from math import sqrt
    for r in range(2,int(sqrt(n))+1):
        if n % r == 0:
            return False
    return True

prime = 0
i = 0
while prime < 10002:
    i += 1
    if isprime(i) == True:
        prime +=1
print(i)