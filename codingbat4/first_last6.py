def first_last6(nums):
    
    return True if len(nums) > 1 and nums[0] == 6 or nums[len(nums) - 1] == 6 else False


print(first_last6([6]))