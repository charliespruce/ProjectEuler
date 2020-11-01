from sympy import isprime
def lefttrunc(n):
    n = str(n)
    for i in range(len(n)):
        if not(isprime(int(n[i:]))):
            return False
    return True

def righttrunc(n):
    n = str(n)
    for i in range(len(n)):
        if not(isprime(int(n[:len(n)-i]))):
            return False
    return True

import numpy
def primesfrom2to(n):
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

primes = primesfrom2to(1000000)[4:]
total = 0
numof = 0

for num in primes:
    if lefttrunc(num) and righttrunc(num):
        total += num
        numof += 1

print(total)