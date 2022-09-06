def no_teen_sum(a, b, c):

    # if any value is in 13 - 19, then it value = 0
    # except if the value is 15 or 16 - value stays intact
    
    aa = fix_teen(a)
    bb = fix_teen(b)
    cc = fix_teen(c)
    
    return aa + bb + cc
    

# helper function to determine the fixed value for the teen
# stops from writing the code all the time {decomposition}
# return the value if the value is in conditions
def fix_teen(n):
    return 0 if n >= 13 and n <= 19 and n != 15 and n != 16 else n



print(no_teen_sum(12, 1, 13))
print(no_teen_sum(1, 1, 16))
