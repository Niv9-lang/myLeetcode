def searchInsert( nums: list[int], target: int) -> int:
    n = len(nums)
    a = 0
    b = n-1
    m = (a+b)//2

    #Test des conditions aux limites
    if target == nums[a]:
        return a
    if target == nums[b]:
        return b
    
    #Raisonnement par dichotomie qui nous assure une complexité en O(log n)
    while b != a+1 and b!= a :
        if nums[m] > target:
            b = m
            m = (a+b)//2

        if nums[m] < target:
            a = m
            m = (a+b)//2

        if nums[m] ==target:
            return m
    
    # 3 cas de figures s'imposent à la fin de la boucle :

    if target > nums[a] and target < nums[b]:
        return a +1
    if target < nums[a]:
        return a
    else: # target > nums[b]
        return b + 1
    

print(searchInsert(nums = [1,3,5,6], target = 3))