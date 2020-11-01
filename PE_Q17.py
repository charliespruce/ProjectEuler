singledigits = 3+3+5+4+4+3+5+5+4
teens = 3+6+6+8+8+7+7+9+8+8
tens = 10*(6+6+5+5+5+7+6+6)+singledigits*8
totalsmall = singledigits+teens+tens
total = 900*7+100*singledigits+891*3+10*totalsmall+11
print(total)
