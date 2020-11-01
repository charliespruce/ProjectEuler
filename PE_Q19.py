total = 0
day = 1
for i in range(1901,2001):
    for j in range(1,13):
        if j in [1,3,5,7,8,10,12]:
            daysinmonth = 31
        if j in [9,4,6,11]:
            daysinmonth = 30
        if j == 2 and i%4 == 0:
            daysinmonth = 29
        if j == 2 and not(i%4 == 0):
            daysinmonth = 28
        for k in range(1,daysinmonth+1):
            if day%7 == 6 and k == 1:
                total += 1
                print('FOUND:'+str(k)+'/'+str(j)+'/'+str(i))
            day +=1
print(total)
