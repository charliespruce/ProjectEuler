def fact(n):
    total = 1
    for i in range(2,n+1):
        total*=i
    return total
        
def curcheck(n):
    string = str(n)
    total = 0
    for char in string:
        total += fact(int(char))
    if total == n:
        return True
    else:
        return False

total = 0
for i in range(10,3500000):
    if curcheck(i):
        total += i
print(total)