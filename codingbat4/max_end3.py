def max_end3(nums):
    
    # Use the max funtion
    great = max(nums[0], nums[len(nums) - 1])
    
    # multiply [] list by many numbers
    return [great] * len(nums)

print(max_end3([1, 2, 3, 4, 5]))    
    