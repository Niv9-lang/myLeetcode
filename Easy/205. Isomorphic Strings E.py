
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        new_s = ""                    #j'ai décidé de créer une nouvelle variable new_s car on ne peut pas modifier les lettres de s (les string sont IMMUTABLES)
        dico = {}
        for v in range(len(s)):
    
            if s[v] in dico:                   #On a déja rencontré cette valeur précédemment
                new_s += dico[s[v]]
            else:
                if t[v] not in dico.values():   #On n'a pas rencontré cette valeur précédemment. Le (not in) assure la bijectivité
                    dico[s[v]]=t[v]
                    new_s+= t[v]
                else:                           #une lettre de t admet deux antécédents dans s donc on renvoie un False
                    return False

        return new_s == t

##########################################################################################################################################################

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1,dic2={},{}
        for s1,t1 in zip(s,t):
            if (s1 in dic1 and dic1[s1]!=t1) or (t1 in dic2 and dic2[t1]!=s1):
                return False
            dic1[s1]=t1
            dic2[t1]=s1
        return True
        