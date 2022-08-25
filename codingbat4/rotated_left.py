def rotated_left(nums):
    br = list(nums[1:])    
    br.append(nums[0])
    return br

print(rotated_left([7, 0, 0]))
 