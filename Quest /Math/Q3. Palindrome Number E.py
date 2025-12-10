

def isPalindrome(x: int) -> bool:
        xs = str(x)
        return xs==xs[::-1]

print(isPalindrome(121))