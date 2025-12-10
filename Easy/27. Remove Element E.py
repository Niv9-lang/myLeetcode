def removeElement(nums, val: int) -> int:
    n = len(nums)
    k = 0

    for i in range(n):
        
        if nums[i] == val:
            for j in range(i+1,n):
                if nums[j]!=val:
                    nums[i],nums[j]=nums[j],nums[i]
                    k+=1
                    break
                elif j == n-1:
                    nums[k:]=['_' for _ in range(n-k)]
                    return k   
        else:
            k+=1

    nums[k:]=['_' for _ in range(n-k)]
    return k

print(removeElement([0,1,2,2,3,0,4,2],2))
       