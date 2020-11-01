from sympy import prime
primearray = [prime(i) for i in range(1,300)]
miniprimearray = primearray[:168]
def primestreak(a,b):
    i = 0
    while True:
        quad = i**2 + a*i + b
        if not(quad in primearray):
            return i
        i += 1

highest = 0
corr_ab = [0,0]
for b in miniprimearray:
    for a in range(-1000,1000):
        temp = primestreak(a,b)
        if temp > highest:
            highest = temp
            corr_ab = [a,b]

print(corr_ab[0]*corr_ab[1])