number = 0
for i in range(1,1001):
    number += i**i
numberstring = str(number)
print(numberstring[len(numberstring)-10:])