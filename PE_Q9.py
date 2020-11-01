# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:25:17 2019

@author: charl
"""

def pythagtrip(a,b):
    from math import sqrt
    if sqrt(a**2 + b**2) == int(sqrt(a**2 + b**2)):
        return int(sqrt(a**2 + b**2))
    else:
        return False
    
for a in range(1,300):
    for b in range(1,1000):
        if not(pythagtrip(a,b) == False):
            if a+b+pythagtrip(a,b) == 1000:
                print(a*b*pythagtrip(a,b))
                