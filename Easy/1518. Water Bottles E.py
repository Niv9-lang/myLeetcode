def numWaterBottles(numBottles: int, numExchange: int) -> int:
    ans = numBottles
    nb_bouteilles_vides = numBottles
    while nb_bouteilles_vides - numExchange >=0:
        nb_bouteilles_vides -=numExchange
        nb_bouteilles_vides+=1
        ans+=1
    
    return ans

print(numWaterBottles(15,4))