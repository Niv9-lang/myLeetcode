def singleNumber(nums):
    a = nums[0]
    n = len(nums)
    for i in range(1,n):
        a = a ^ nums[i]         #XOR Operations

    return a

print(singleNumber([4,1,2,1,2,4,5]))

"""
La sortie d'un XOR à n entrées sera 1 quand le nombre d'entrées actives sera impair et 0 sinon
Le XOR est commutatif
Colonne de bit par colonne de bit, il y aura toujours un nombre pair de 0 et de 1 sans compter le bit du nombre seul. 
En ajoutant le bit de ce nombre seul, soit c'est 0 est dans ce cas le nombre de 1 reste pair donc la sortie vaut 0.
Soit le bit est 1 et dans ce cas le nombre de 1 est impair donc la sortie 1.

Bref, à la fin du processus, on retombe sur notre nombre seul dans la liste.
"""