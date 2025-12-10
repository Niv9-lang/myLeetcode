

def canMakeArithmeticProgression(arr: list[int]) -> bool:
    n = len(arr)
    if n == 1 or n ==0 or not any(arr[i]!=arr[i-1] for i in range(1,n)):
        return True

    minimum = min(arr)
    maximum = max(arr)
    r = int((maximum-minimum)/(n-1)) #On sait que si on peut ordonner les éléments, la raison r est nécessairement (maximum-minimum)/(n-1)
    arr_set = set(arr)

    if len(arr_set)!=n: #Présence de doublons sauf si arr[k,k,k,k..,k], cas traité plus haut
        return False
    
    while minimum in arr_set:
        if minimum == maximum:
            return True
        minimum = minimum + r

    return False

print(canMakeArithmeticProgression([0,0,0]))

"""
On aurait aussi pu penser à trier la liste dans l'ordre croissant ou décroissant et étudier la différence
entre chaque membre mais cela aurait donné une complexité en O(n*log n)

Ici, trouver max et min se fait en O(n) et l'utilisation d'un set donne une complexité en O(n)
"""