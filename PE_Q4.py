# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def paltest(n):
    num = str(n)
    for r in range(int(len(num)/2)):
        if not(num[r] == num[len(num)-r-1]):
            return False
    return True
    
a = 0
for i in range(100,1000):
    for j in range(100,1000):
        if i*j > a and paltest(i*j) == True:
            a = i*j
print(a)