total = 0
for pounds in range(3):
    for fifties in range(5):
        if pounds*100+fifties*50>200:
            continue
        for twenties in range(11):
            if pounds*100+fifties*50+twenties*20>200:
                continue
            for tens in range(21):
                if pounds*100+fifties*50+twenties*20+tens*10>200:
                    continue
                for fives in range(41):
                    if pounds*100+fifties*50+twenties*20+fives*5+tens*10>200:
                        continue
                    for twos in range(101):
                        if pounds*100+fifties*50+twenties*20+tens*10+fives*5+twos*2>200:
                            continue
                        for ones in range(201):
                            if pounds*100+fifties*50+twenties*20+tens*10+fives*5+twos*2+ones==200:
                                total+=1

print(total+1)
