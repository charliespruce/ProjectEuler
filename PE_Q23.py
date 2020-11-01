def perf_test(n):
    divisors = [1]
    from math import sqrt
    if int(sqrt(n)) == sqrt(n):
        divisors.append(int(sqrt(n)))
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            if not(i == sqrt(n)):
                divisors.append(i)
                divisors.append(n//i)
    divisorsum = 0
    for number in divisors:
        divisorsum += number
    if divisorsum > n:
        return 'abundant'
    elif divisorsum < n:
        return 'deficient'
    else:
        return 'perfect'
total = 0
abundants = []
#needs to be optimised
for k in range(2,28123):
    if perf_test(k) == 'abundant':
        abundants.append(k)
for j in range(1,28124):
    sumtest = False
    for element in abundants:
        if element > j:
            break
        if j-element in abundants:
            sumtest = True
            break
    if sumtest == False:
        total += j
    
print(total)