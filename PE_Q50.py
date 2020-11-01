import numpy
def primesfrom2to(n):
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

primes = primesfrom2to(10**6)

highest = 0
corr_num = 0

for i in range(len(primes)//2+1):
    count = 1
    newtotal = primes[i]
    while newtotal < 1000000:
        newtotal,oldtotal = sum(primes[i:i+count+1]),newtotal
        if not(newtotal in primes):
            if oldtotal in primes and count > highest:
                highest = count
                corr_num = oldtotal
        count += 1
# takes ages bear with it, like 2-3 mins
print(corr_num)