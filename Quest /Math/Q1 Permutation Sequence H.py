
from itertools import permutations
from math import factorial
def getPermutation(n: int, k: int) -> str:
    L = [i for i in range(1,n+1)]
    N = list(permutations(L))

    Perm = N[k-1]

    S = []
    for j in L:
        S.append(Perm[j-1]*10**(n-j))

    return sum(S)

"""
Problème de cette algo : pour des valeurs n grandes, on calcule toutes les combinaisons possibles avec la fonction permutation d'où une 
complexité en O(n!)


"""

def getPermutationBetter(n: int, k: int) -> str:
    


