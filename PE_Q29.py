def dupremover(array):
    array.sort()
    newarray = []
    for element in array:
        if not(element in newarray):
            newarray.append(element)
    return(newarray)

array = []
for a in range(2,101):
    for b in range(2,101):
        array.append(a**b)

print(len(dupremover(array)))