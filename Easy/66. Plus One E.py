
def plusOne(digits):
    n = len(digits)
    if digits[-1]!=9:
        digits[-1]+=1
        return digits
    index = -1
    digits[index]+=1
    while digits[index]==10:
        if index ==-n:
            digits.insert(0,1)
            digits[index]=0
            return digits
        digits[index]=0
        index -=1
        digits[index]+=1


    return digits
        
print(plusOne([9,8]))

#Remarque : la fonction .insert() a une complexité en O(n) donc notre programme a une complexité au pire de O(n^2). Il semblerait qu'il n'y ait pas 
# de meilleure complexité 