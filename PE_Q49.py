from itertools import permutations
from sympy import isprime

digits = [0,1,2,3,4,5,6,7,8,9]

for i in digits:
    for j in digits:
        for k in digits:
            permarray = []
            perms = permutations([2,i,j,k])
            for perm in perms:
                num = ''
                for l in range(4):
                    num = num + str(perm[l])
                permarray.append(int(num))
            for num1 in permarray:
                for num2 in permarray:
                    if num2 > num1:
                        num3 = 2*num2 - num1
                        if num3 in permarray:
                            if isprime(num1) and isprime(num2) and isprime(num3):
                                print(str(num1)+str(num2)+str(num3))
                                exit()