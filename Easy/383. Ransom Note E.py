def canConstruct(ransomNote: str, magazine: str) -> bool:

    for lettre in ransomNote:
        if lettre in magazine:
            magazine = magazine.replace(lettre,'_',1)
        else:
            return False

    return True

print(canConstruct('aa','ab'))

########################################################################################################################################################################
# Mauvaise version ci-dessous
# La méthode str.replace() ne modifie pas les string mais en produit un nouveau donc la ligne 27 est ineffective

def canConstruct(ransomNote: str, magazine: str) -> bool:

    for lettre in ransomNote:
        if lettre in magazine:
            magazine.replace(lettre,'_',1)
        else:
            return False

    return True

print(canConstruct('aa','ab'))