def isHappy( n: int) -> bool:
    L = set()
    S = n
    while S !=1:
            
        S2 = 0
        for digit in str(S):
            S2+=int(digit)**2
        S = S2
        if S in L:
            return False
        L.add(S)
    return True
        
print(isHappy(19))

"""
Enormément de choses à apprendre dans cette exercice :

- Utiliser des formules pour extraire les chiffres qui composent n est impossible à faire avec des formules mathématiques car
il y a plein d'erreurs d'arrondis

- Utiliser une chaine de caractères est bien plus simple

- L'utilisation d'un set permet d'avoir une fonction S in L en O(1) plutôt qu'une opération avec une liste qui serait plus long (O(n))
"""