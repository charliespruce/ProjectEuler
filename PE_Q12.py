# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:38:04 2019

@author: charl
"""

def trinum(n):
    return n*(n+1)/2

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

from itertools import count
for r in count(2,):
    if len(list(divisorGenerator(trinum(r)))) > 500:
        print(trinum(r))
        break