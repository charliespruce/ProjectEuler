def powerdigsum(n):
    n = str(n)
    total = 0
    for i in range(len(n)):
        total += int(n[i])**5
    return total

ans = 0

for i in range(2,1000000):
    if powerdigsum(i) == i:
        ans += i

print(ans)