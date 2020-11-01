numberstring = ''
for i in range(1,186000):
    numberstring = numberstring + str(i)

ans = 1
for i in range(7):
    ans *= int(numberstring[10**i - 1])
print(ans)