def singleNumber(nums):
    a = nums[0]
    n = len(nums)
    for i in range(1,n):
        a = a ^ nums[i]

    return a

print(singleNumber([4,1,2,1,2,4,5]))