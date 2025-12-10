

def smallestRepunitDivByK( k: int) -> int:
    for i in range(22):
        if (10**i -1)/9 % k==0:
            return 10**i -1
    
    return False

print()