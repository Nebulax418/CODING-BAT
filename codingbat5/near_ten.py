def near_ten(num):
    
    # within 2 of a multiple of 10
    
    # the difference between the division of num and 10 should be in 2 digits
    remainder = num % 10

    return remainder <= 2 or remainder >= 8

print(near_ten(19))    

  
