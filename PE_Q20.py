number = 1
total = 0
for i in range(2,100):
    number = number * i
number = str(number)
for i in range(len(number)):
    total = total + int(number[i])
print(total)
