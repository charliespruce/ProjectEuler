#takes a little too long, will optimise at later date
def d(n):
    total = 0
    from math import sqrt
    if n%2==0:
        if not(int(sqrt(n))==sqrt(n)):
            for i in range(2,int(sqrt(n))):
                if n%i == 0:
                    total = total + i + n//i
        if int(sqrt(n))==sqrt(n):
            for i in range(2,int(sqrt(n))+1):
                if n%i == 0:
                    total = total + i + n//i
            total = total - int(sqrt(n))
    if not(n%2==0):
        if not(int(sqrt(n))==sqrt(n)):
            for i in range(3,int(sqrt(n)),2):
                if n%i == 0:
                    total = total + i + n//i
        if int(sqrt(n))==sqrt(n):
            for i in range(3,int(sqrt(n))+1,2):
                if n%i == 0:
                    total = total + i + n//i
            total = total - int(sqrt(n))
    return total+1
total2 = 0
for i in range(1,10000):
    for j in range(1,10000):
        if d(i)==j and d(j)==i and not(i==j):
            total2 = total2+i+j
print(total2//2)