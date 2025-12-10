
from fractions import Fraction
def smallestRepunitDivByK(k: int) -> int:
    for i in range(1,10500):
        #if int((10**i-1)//9) % k == 0:
        if Fraction(10**i-1,9) % k == 0:
            return i
    return -1

print(smallestRepunitDivByK(99989))

"""
La note indique que n est inférieur ou égal à 2**64 -1
En écrivant n comme une somme de puissance de 1à, on aboutit à n = (10**i -1)/9
pour i inférieur à 21 pour ne pas dépasser 2**64 -1


TOUTEFOIS, si on choisit (10**i - 1) / 9, on a des problèmes pour des valeurs de i trop grande
Typiquement, pour i == 17, Python renvoie 1.1111111111111112e+16 au lieu de 1.111111111111111e+16
car 11111111111111111 est trop grand pour être représenté exactement en float.

Le code ci-dessous ne peut pas fonctionner
"""

#Solution proposée par ChatGPT

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        r = 0
        for i in range(1, k+1):     # le cycle doit boucler avant k itérations
            r = (r * 10 + 1) % k    # ajoute un « 1 » en base 10
            if r == 0:
                return i
        return -1


"""
On utilise la relation R(i+1) = (10*Ri + 1) % k

Donc les restes r sont toujours inférieurs à k

Le cycle doit boucler avant k itérations selon le principe des tiroires (pigeonhole principle) :
r appartient à {0,1,...,k-1}
Si on tombe sur 0, on a gagné
Si on suppose qu'on fait plus de k itérations, alors on va nécessairement retomber sur un reste auparavant et alors une boucle apparaît
et dans cette boucle, on ne tombe jamais sur 0 sinon le programme se serait arrêté.

"""