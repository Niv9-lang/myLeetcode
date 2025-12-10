

def longestCommonPrefix(strs: list[str]) -> str:
    n = len(strs)
    mot = strs[0]
    m = min([len(k) for k in strs])
    index = 0
    while index<m:
        lettre = mot[index]
        j = 0
        for i in range(1,n):    
            if strs[i][index]==lettre:
                if i == n-1 :
                    index+=1
                    j=1

        if j==0:
            break
    
    if index ==0:
        return ""
    return mot[:index]

print(longestCommonPrefix(["dog","racecar","car"]))

"""
Le code ci-dessus ne fonctionne pas pour la liste ["a","acc","ccc"] car les lignes 12 et 13 s'exécute
"""

def longestCommonPrefix2(strs: list[str]) -> str:
    n = len(strs)
    if n ==1:
        return strs[0]

    mot = strs[0]
    m = len(mot)
    index = 0
    while index<m:
        lettre = mot[index]
        j = False
        compteur = 0
        try:
            for i in range(1,n):    
                if strs[i][index]==lettre:
                    compteur +=1
                    if i ==n-1==compteur:
                        index+=1
                        j=True
            if not j:
                break
        except IndexError:
            return mot[:index-1]

    if index==0:
        return ""
    return mot[:index]

print(longestCommonPrefix2(["flower","flow","flight"]))

"""
Plus efficace car on n'utilise pas la fonction min()
"""
###################################################################################################
def longestCommonPrefix3( strs: list[str]) -> str:
    pref = strs[0]
    pref_len = len(pref)

    for s in strs[1:]:
        while pref != s[0:pref_len]:    #euh problème de taille pour certains éléments de s ? on est obligé de faire un try / except
            pref_len -= 1
            if pref_len == 0:
                return ""
            
            pref = pref[0:pref_len]
    
    return 

"""
J'adore, le problème de taille est réglé puisque si on trouve un préfixe commun alors n'importe quel mot l'a donc on n'a pas besoin de try et except
mais simplement de partir du premier mot et de tester pref != s[0:pref_len] puis de décrémenter pref_len de 1
"""