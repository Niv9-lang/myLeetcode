def hammingWeight( n) -> int:
    res = 0
    while n > 0:
        x = n & 1
        if x == 1:
            res+=1
            
        n >>=1
    return res

print(hammingWeight(11))