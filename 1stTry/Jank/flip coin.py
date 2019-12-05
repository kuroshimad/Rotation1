##flip coin
import random 

def flip_coin():
    total = 0
    for i in range (0,10):
        chance = random.randint(0,1)
        if chance ==0:
            total = total - 1
        else:
            total = total + 1
    return total

##main
result = []
for i in range (0,100000):
    result.append(flip_coin())
    

