
def climbStairs( n: int) -> int:
    from math import comb
    S = 0
    p = int(n/2)
    for k in range(0,p+1):
        nb_de_1 = n - 2*k 
        places = k + nb_de_1
        S+= comb(places,k)
    return S

print(climbStairs(3))

#Cette algo est lent à cause du comb()