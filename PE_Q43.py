numarray = [2,3,5,7,11,13,17]

def propertycheck(n):
    n = str(n)
    for i in range(2,9):
        if not(int(n[i-1:i+2])%numarray[i-2] == 0):
            return False
    return True

from itertools import permutations
pandigarray = []
perms = permutations([0,1,2,3,4,5,6,7,8,9])
for perm in perms:
    num = ''
    for i in range(10):
        num = num + str(perm[i])
    pandigarray.append(int(num))

ans = 0
for num in pandigarray:
    if propertycheck(num):
        ans += num
print(ans)