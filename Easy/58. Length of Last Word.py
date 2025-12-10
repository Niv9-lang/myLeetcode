def lengthOfLastWord(self, s: str) -> int:
    n = len(s)
    s = s[::-1]
    compteur = 0
    for i in range(n):
        if s[i]!=' ':
            compteur+=1
        elif compteur > 0 and s[i]==' ':
            return compteur

    return compteur   