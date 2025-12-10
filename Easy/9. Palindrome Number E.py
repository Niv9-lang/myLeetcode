def isPalindrome(x: int) -> bool:
    mystr = str(x)
    return (mystr ==mystr[::-1])

print(isPalindrome(122))