
def selfDividingNumbers( left: int, right: int):
    L = []
    for i in range(left, right+1):
        i_str = str(i)
        compteur = 0
        for j in i_str:
            if int(j)!=0 and i%int(j)==0 :
                compteur+=1
            else:
                break
        
        L.append(i)
    
    return L     