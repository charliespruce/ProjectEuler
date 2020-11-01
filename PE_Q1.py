# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:13:16 2019

@author: charl
"""
total = 0
for r in range(1000):
    if r % 3 == 0 or r % 5 == 0:
        total += r
print(total)