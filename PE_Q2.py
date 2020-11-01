# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:18:19 2019

@author: charl
"""
fF = 1
fS = 1
total = 0

while fS < 4000001:
    fF, fS = fS, fF + fS
    if fS % 2 == 0:
        total = total + fS
print(total)