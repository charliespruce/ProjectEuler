from sympy import isprime
from sympy import prime

squarearray = [i**2 for i in range(1,10001)]
comparray = [2*i - 1 for i in range(5,5001) if not(isprime(2*i - 1))]

def proptest(n):
    for square in squarearray:
        if square < n//2 - 2:
            if isprime(n - 2*square):
                return True
    return False

for num in comparray:
    if not(proptest(num)):
        print(num)
        break