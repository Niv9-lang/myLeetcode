def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = m-1
    j = -1
    index = -1                             
    while j >= -n:
        if i < 0:
            nums1[:n+j+1] = nums2[:n+j+1]
            return nums1
        
        elif nums2[j] > nums1[i]:
            nums1[index]=nums2[j]
            j-=1
            index-=1
        

        elif nums2[j] < nums1[i]:
            nums1[i],nums1[index] = nums1[index],nums1[i]
            index-=1
            i-=1

        else:
            nums1[index]=nums2[j]
            j-=1
            index-=1

    return nums1

print(merge([4,5,6,0,0,0],  3, [-3,-2,-1], 3)) 
print(merge([1,2,3,0,0,0],  3,  [2,5,6], 3))   
print(merge([1,0],  1,  [2],1))

"""
Commentaires du code qui paraît compliqué à première vue :

L'idée principale est de remplir la liste nums1 de la droite vers la gauche en commençant par ranger les plus grands nombres : 
on commence par le dernier element de la liste nums2 (ou l'élément d'indice j plus généralement)
et on le compare à l'élément d'indice m-1 (ou i plus généralement) de nums1.

La partie sous le else est choisie arbitrairement entre les deux elif précédent

ATTENTION : il s'agit bien de ELIF ici car sinon la boucle WHILE teste tous les if. Or, à chaque itération, on veut que seul un des if soit exécuté.

La variable index permet de suivre le premier 0 de la liste nums1 en partant de la droite et sera décrémenté de 1 à chaque fois que nums1
est modifié

Si i < 0: c'est qu'on a rangé tous les nombres de nums 1 et une partie de nums2 à droite dans l'ordre donc il ne reste plus qu'à rajouter
les éléments qui restent de nums2 (i.e nums2[:n+j+1] )
"""