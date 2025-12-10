def reverseBits(n: int) -> int:
        from collections import deque
        L = deque()
        m = n

        #Conversion en binaire
        while m >=1 :
            reste = m%2
            L.appendleft(reste)
            m = int(m/2)

        #Inversion et reconversion en décimal
        L.reverse()
        S = 0
        length = len(L)
        for i in range(length):
            S+=L[i]*2**(32-i-1)

        return S

print(reverseBits(2147483644))


# Pour les professionnels 

def reverseBits( n: int) -> int:
    res = 0
    pos = 31
    while n > 0:
        x = n & 1
        res += (x << pos)
        n >>= 1
        pos -= 1
    
    return res

""" 
Explication de la boucle while :

Ligne 1 :
L'opérateur & ici est l'opérateur AND binaire (multplication bit à bit) -> Cela permet d'extraire le bit le plus à droite (on voit que n est automatiquement 
converti en binaire par cette opération)

Ligne 2 :
On ajoute  à "res" au bit de position "pos" (31 puis 30 etc.) le bit "x" qu'on a extrait de 'n' juste avant

Ligne 3 et 4 :
On enlève le bit de poids le plus faible de 'n' puis on recommence les opérations précédentes (on se décale vers la gauche dans la lecture de "n" bit à bit)
pos -= 1 car on va remplir le bit de position pos-1 ensuite

Finalement, on retourne "res" qui est bien en décimal


"""

