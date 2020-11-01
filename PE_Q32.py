from collections import OrderedDict
def remove_duplicate(str1):
  return "".join(OrderedDict.fromkeys(str1))

def disjoint(string1,string2):
    for char in string1:
        if not(string2.find(char) == -1):
            return False
    return True

def pandigcheck(a,b):
    if remove_duplicate(str(a)) == str(a) and remove_duplicate(str(b)) == str(b):
        string_a,string_b = str(a),str(b)
        if disjoint(str(a),str(b)) and string_a.find('0') == -1 and string_b.find('0') == -1:
            if remove_duplicate(str(a*b)) == str(a*b):
                digits = '123456789'
                for dig in str(a) + str(b):
                    digits = digits.replace(dig,'')
                temp = ''.join(sorted(str(a*b)))
                if temp == digits:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def dupremover(array):
    array.sort()
    newarray = []
    for element in array:
        if not(element in newarray):
            newarray.append(element)
    return(newarray)

array = []

for a in range(1,1000):
    for b in range(1,10000):
        if pandigcheck(a,b) == True:
            array.append(a*b)

array = dupremover(array)
total = 0
for num in array:
    total += num

print(total)