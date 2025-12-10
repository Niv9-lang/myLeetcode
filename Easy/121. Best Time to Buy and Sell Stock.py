def maxProfit( prices: list[int]) -> int:
    n = len(prices)
    m = prices[0]
    maximum = prices[0]
    for i in range(1,n):
        m = min (m,prices[i-1])
        if prices[i] - m > maximum:
            maximum = prices[i] - m

    if maximum <=0:
        return 0
    return maximum

"""
Il est plus intéressant de réfléchir à l'envers, pour maximiser le profit, on prend l'élément i et on regarde 
le minimum des éléments de prices d'indices 0 à i-1
Cela nous donne une complexité en O(n) parfaite
"""