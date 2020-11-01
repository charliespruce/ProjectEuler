def permutation(lst): 
    if len(lst) == 0: 
        return []
    if len(lst) == 1: 
        return [lst] 
    l = []
    for i in range(len(lst)): 
       m = lst[i] 
       remLst = lst[:i] + lst[i+1:] 
       for p in permutation(remLst): 
           l.append(m + p) 
    return l
  
perms = [int(num) for num in permutation('123456789')]

# just guessed that it would only use 1 & 2 and it worked don't ask me.
highest = 0
for i in range(5000,10000):
    num = int(str(i)+str(2*i))
    if num in perms:
        highest = num
print(highest)