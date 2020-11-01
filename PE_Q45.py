trinums = [int(i*(i+1)/2) for i in range(1,200000)]
pentnums = [int(i*(3*i - 1)/2) for i in range(1,70000)]
hexnums = [int(i*(2*i - 1)) for i in range(1,40000)]


for num in trinums[285:]:
    if num in pentnums and num in hexnums:
        print(num)
        break