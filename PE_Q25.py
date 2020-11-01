fib1 = 1
fib2 = 1
fibnumber = 2
while len(str(fib2)) < 1000:
    fib1, fib2 = fib2, fib1+fib2
    fibnumber += 1
    
print(fibnumber)