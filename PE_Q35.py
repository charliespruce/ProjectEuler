def rotations(n):
    n = str(n)
    array = []
    for i in range(len(n)):
        rotation = n[i:len(n)]+n[0:i]
        array.append(rotation)
    return array

from sympy import isprime

import numpy
def primesfrom2to(n):
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

primes = primesfrom2to(1000000)

def circprimecheck(n):
    for num in rotations(n):
        if not(isprime(int(num))):
            return False
    return True

total = 0
for i in primes:
    if circprimecheck(i):
        total += 1
print(total)