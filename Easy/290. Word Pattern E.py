def wordPattern(pattern: str, s: str) -> bool:
    d1,d2 = {},{}
    s_list = s.split()

    if len(pattern)!=len(s_list):
        return False
    
    for i in range(len(pattern)):
        if (pattern[i] in d1 and d1[pattern[i]]!=s_list[i]) or (s_list[i] in d2 and d2[s_list[i]]!=pattern[i]):
            return False
    
        d1[pattern[i]]=s_list[i]
        d2[s_list[i]]=pattern[i]


    return True


print(wordPattern( pattern = "aaaa", s = "dog cat cat dog"))

"""
Inspiré de l'exercice 205 sur les Isomorphic strings


La condition ligne 7 nous assure que l'on a bien une bijection (aucun élément de s_list aura deux antécédents dans d1)
"""