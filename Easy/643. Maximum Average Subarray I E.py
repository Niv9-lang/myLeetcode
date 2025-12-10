
def findMaxAverage( nums: list[int], k: int) -> float:
    n = len(nums)
    S = 0
    for i in range(n):
        S1 = sum(nums[j] for j in range(i,i+k))  
        if S1 > S:
            S = S1


    return S / k

print(findMaxAverage([1,12,-5,-6,50,3],4))
##L'algortihme n'est pas performant car on recalcule les sommes à chaque fois à la ligne 6


def findMaxAverage1( nums: list[int], k: int) -> float:
    n = len(nums)
    S = sum(nums[j] for j in range(0,k))
    a = S
    for i in range(n-k):
        S1 = a  - nums[i] + nums[i+k]
        if S1 > S:
            S = S1
            a = S
        else:
            a = S1
    return S/k

"""
L'idée magique était d'utiliser une autre variable nommée 'a' pour stocker les valeurs déjà calculées et faire des opérations dessus
sans toucher à la valeur de S qu'on retournera en fin de programme
Cette solution semble être optimale selon Leetcode (top 10 %)
"""