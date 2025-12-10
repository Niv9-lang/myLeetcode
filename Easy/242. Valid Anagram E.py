from collections import Counter
def isAnagram(s: str, t: str) -> bool:
    d1 = {letter :  0 for letter in s}
    d2 = {letter : 0 for letter in t}
    for i in range(len(s)):
        d1[s[i]]+=1
        d2[t[i]]+=1
    
    return d1 == d2

    
print(isAnagram(s = "rat", t = "car"))

"""
La fonction Counter() du module collections permet exactement de faire ce que j'ai fais à la main
Counter(s)= d1 ici
"""

