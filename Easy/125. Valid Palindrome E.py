from string import ascii_letters

def isPalindrome(s: str) -> bool:

    ascii_with_digits =ascii_letters
    ascii_with_digits = ascii_with_digits + '0123456789'
    news = ''.join(c for c in s if c in ascii_with_digits)  

    return (news.lower() == news[::-1].lower())
    
print(isPalindrome(s = "0P"))

"""
We could have check if all the elements in s were alphanumerical according to the defintion of Leetcode by using
the method text.isalnum() that returns True if 'text' contains only alphanumerical characters and False otherwise
"""