def sum2(nums):
    
    # return the sum of the first two elements
    
    if len(nums) == 0:
        return 0
    
    # sum function for an iterable
    
    
    return nums[0] + nums[len(nums) - 1] if len(nums) > 2 else sum(nums)

print(sum2([1, 2]))