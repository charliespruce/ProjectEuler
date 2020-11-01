numberlist = [0,1,2,3,4,5,6,7,8,9]

def permtest(n):
    n = str(n)
    if len(n) == 10:
        if '0' in n and '1' in n and '2' in n and '3' in n and '4' in n and '5' in n and '6' in n and '7' in n and '8' in n and '9' in n:
            return True
        else:
            return False
    elif len(n) == 9:
        if '1' in n and '2' in n and '3' in n and '4' in n and '5' in n and '6' in n and '7' in n and '8' in n and '9' in n:
            return True
        else:
            return False
    else:
        return False

permnumber = 0

for i in range(10000000000000):
    if permtest(i) == True:
        permnumber += 1
        currperm = i
    if permnumber == 1000000:
        print(currperm)
        break