# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:32:53 2019

@author: charl
"""

def isprime(n):
    from math import sqrt
    for r in range(2,int(sqrt(n))+1):
        if n % r == 0:
            return False
    return True

def largestfactor(n):
    from math import sqrt
    for r in range(2,int(sqrt(n))+1):
        if n % r == 0:
            return n//r
    print('Prime')
    
def ansfunc(n):
    if isprime(largestfactor(n)) == True:
        return largestfactor(n)
    else:
        return ansfunc(largestfactor(n))
