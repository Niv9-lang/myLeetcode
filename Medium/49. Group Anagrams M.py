def groupAnagrams(strs):
 
    def myCounter(str):
        d1 = {letter :  0 for letter in str}
        for i in range(len(str)):
            d1[str[i]]+=1
        return d1

    dico = {}
    for s in strs:
        comptage = myCounter(s)
        for j in dico:
            if comptage==dico[j][0]:
                dico[j][1].append(s)
                break

        else:
            dico[s] = (comptage,[s])
    
    return [dico[s][1] for s in dico] 
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


"""
Cette solution n'est carrément pas efficace car elle me force à utiliser une fonction myCounter lente puis à parcourir mon dico pour 
chaque itération de la boucle sur strs

Fonction defaultdict() du module Collections cf. Anytype
"""

from collections import defaultdict
def groupAnagrams2(strs):
            
    resDict = defaultdict(str)

    for s in strs:
        key = ''.join(sorted(s))

        if not resDict[key]:    #si la clé n'existe pas, pour un dico classique, on ne peut pas écrire if not resDict[key]
            resDict[key] = [s]
        else:       
            resDict[key].append(s)
        
    return list(resDict.values())
