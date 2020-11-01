total = 1
curr = 1

#build up array of odd numbers (dim of squares surrounding 1)
array = [2*n-1 for n in range(2,502)]

#starts at 1 in the middle, and moves to the corners of each dim x dim square surrounding, adding to total each time
for dim in array:
    for i in range(1,5):
        curr += (dim-1)
        total += curr

print(total)