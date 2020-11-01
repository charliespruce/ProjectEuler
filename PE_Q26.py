def divrem(n,i):
    return n//i,n-(n//i)*i

def twofivediv(n):
    twos = 0
    fives = 0
    while n % 2 == 0:
        n = n//2
        twos +=1
    while n % 5 == 0:
        n = n//5
        fives += 1
    return max(twos,fives)

def reclooplen(n):
    rem = divrem(10**twofivediv(n),n)[1]
    if not(rem == 0):
        num = rem
        i = 0
        while True:
            rem = divrem(10*rem,n)[1]
            if rem == num:
                return i+1
            i += 1
    else:
        return 0
    
highest = 0
cor_num = 1
for i in range(1,1000):
    new = reclooplen(i)
    if new > highest:
        highest = new
        cor_num = i
        
print(cor_num)