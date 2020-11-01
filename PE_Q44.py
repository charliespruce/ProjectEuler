pentnums = [int(i*(3*i - 1)/2) for i in range(1,3000)]

for num1 in pentnums:
    for num2 in pentnums[pentnums.index(num1):]:
        if num1 + num2 in pentnums and num2 - num1 in pentnums:
            print(num2-num1)
            exit()