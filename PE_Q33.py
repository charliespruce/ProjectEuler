def curiouscheck(p,q):
    string_q = str(q)
    string_p = str(p)
    if p%10 == 0 and q%10 == 0:
        return False
    for char in string_p:
        if not(string_q.find(char) == -1):
            string_p,string_q = string_p.replace(char,'',1),string_q.replace(char,'',1)
    if not(string_p == '') and not(string_q == ''):
        if not(int(string_q)==0):
            if not(int(string_p)==p) and p/q == int(string_p)/int(string_q):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

num = 1
den = 1
for p in range(10,100):
    for q in range(p+1,100):
        if curiouscheck(p,q):
            num *= p
            den *= q

for i in range(2,num+1)[::-1]:
    if num%i==den%i==0:
        num = num//i
        den = den//i
print(den)
            
                
