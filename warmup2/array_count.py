def array_count9(nums):
    count = 0
    
    for number in nums:
        if number == 9:
            count+=1
            
    return count

print(array_count9([1, 2, 9, 9, 5]))    