
def summaryRanges( nums: list[int]) -> list[str]:
    n = len(nums)
    if n == 0:
        return nums

    
    a = nums[0]
    b = nums[0]
    output = []

    if n == 1:
        return [str(a)]
    
    for i in range(1,n):
        if nums[i] !=nums[i-1] + 1:
            if a >= b:
                output.append(str(a))               # a est supérieur à b donc on a nums[i-2] + 1 < nums[i-1] +1 < nums[i]
                a = nums[i]

            else:
                output.append(f"{a}->{b}")
                a = nums[i]

            if i == n-1:                           # Cas à prendre en compte lorsque on a nums[-1] > nums[-2], il faut ajouter nums[-1] tout seul
                output.append(str(a))
        else:
            b = nums[i]                            # Tant qu'on a une progression arithmétique de raison 1, on continue à augmenter la range a->b
            if i == n-1:                           # Lorsqu'on arrive au bout de la liste, il faut ajouter a->b
                output.append(f"{a}->{b}")

        
    return output
print(summaryRanges([0,2,3,4,6,8,9]))


"""
Cette exercice présente bcp de problèmes au niveau des bords de la liste nums, il faut bien les gérer
"""