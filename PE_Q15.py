def fact(n):
    total = 1
    for i in range(2,n+1):
        total *= i
    return total

# we have to go down 20 and across 20, and compute the number of waus of doing this
# this is the same as ordering 20 red balls and 20 blue balls.

print(fact(40)//fact(20)**2)