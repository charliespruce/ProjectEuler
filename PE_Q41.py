def pandigcheck(n):
    digits = ''
    n = str(n)
    for i in range(1,len(n)+1):
        digits = digits + str(i)
    for char in n:
        if char in n.replace(char,''):
            return False
        else:
            for dig in digits:
                if not(dig in n):
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

#increased power of 10 until it worked, don't ask.
primearray = primesfrom2to(10**7)

highest = 0
for num in primearray:
    if pandigcheck(num):
        highest = num
print(highest)