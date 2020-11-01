import math

def primefactors(n): 
    array = []
    while n % 2 == 0: 
        array.append(2), 
        n = n // 2      
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            array.append(i), 
            n = n//i 
    if n > 2: 
        array.append(n)
    newarray = []
    while not(array == []):
        num = array[0]
        newarray.append(num**array.count(num))
        array = list(filter(lambda i: i != num,array))
    return newarray

def consecprimefactors(n):
    [list1,list2,list3,list4] = [set(primefactors(i)) for i in range(n,n+4)]
    if list1.intersection(list2,list3,list4) == set():   
        return True
    else:    
        return False

count = 10
while True:
    if len(primefactors(count))==len(primefactors(count+1))==len(primefactors(count+2))==len(primefactors(count+3))==4:
        if consecprimefactors(count):
            print(count)
            break
    count += 1