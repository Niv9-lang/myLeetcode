def isSubsequence( s: str, t: str) -> bool:
    
    if s =="":
        return True
    
    i_s = -1
    n = len(s)
    m = len(t)
    for j in range(m):
        if t[j]==s[i_s+1]:
            i_s+=1
        if i_s == n-1:
            return True
    return False
