def palcheck(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

def dectobin(n):
    ans = bin(n)
    return int(ans[2:])

total = 0
for i in range(1,1000001):
    if palcheck(i) and palcheck(dectobin(i)):
        total += i
print(total)