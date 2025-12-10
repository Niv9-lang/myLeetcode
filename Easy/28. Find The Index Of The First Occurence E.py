def strStr( haystack: str, needle: str) -> int:
    n = len(haystack)
    m= len(needle)
    lettre = needle[0]
    for i in range(n):
        if haystack[i]==lettre and haystack[i:i+m] == needle:
            return i

    return -1

print(strStr(haystack = "butsady", needle = "sady"))