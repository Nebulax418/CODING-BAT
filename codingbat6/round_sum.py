def round_sum(a, b, c):
    
    # Condition 1
    
    '''
    Round an int value up to the next multiple of 10 
    if --> rightmost digit is 5 or more, so 15 rounds up to 20
    '''
    
    aa = round10(a)
    bb = round10(b)
    cc = round10(c)
    
    return aa + bb + cc

def round10(n):
    
    # get the last digit of the number -> n % 10
    lsdigit = n % 10
    
    # add 10 to the rounded if its greater than 5
    rnd = ((n / 10) * 10) + 10
    
    # digit less than 5 = 10
    # digit greater than 5 is the next multiple of 10
    
    return (n / 10) * 10 if lsdigit < 5 else rnd