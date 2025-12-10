def removeDuplicates(nums: list[int]) -> int:
    n = len(nums)
    indice_changement = 1
    a = nums[0]
    for i in range(1,n):
        if nums[i]!=a:
            nums[indice_changement]=nums[i]
            indice_changement+=1
            a = nums[i]
    print(nums)
    return indice_changement

print(removeDuplicates([1,1,2,3,4,4,5,6,6]))