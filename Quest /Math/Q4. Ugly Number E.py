
def isUgly(n: int) -> bool:
    if n <= 0:
        return False
    while n > 5 and (n%2==0 or n%3 == 0 or n%5 == 0):
        if n %2==0:
            n=n/2
        if n %5==0:
            n=n/5
        if n %3==0:
            n=n/3

    return n <=5

"""
La consigne n'admettait pas les nombres négatifs.

https://leetcode.com/problems/ugly-number/?envType=problem-list-v2&envId=maths-m2-divisibility-modular-arithmetic
"""