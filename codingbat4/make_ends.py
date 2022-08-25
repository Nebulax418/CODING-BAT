def make_ends(nums):
    
    return [nums[0], nums[len(nums) - 1]] if len(nums) > 2 else 0

print(make_ends([1, 2, 3, 4, 5]))