# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 21:48:40 2019

@author: charl
"""

total1 = 0
for r in range(101):
    total1 += r
total2 = 0
for r in range(101):
    total2 += r**2
print(total1**2-total2)