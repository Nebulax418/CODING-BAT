def lucky_sum(a, b, c):
    
    # apply the same method as before
    
    ssum = 0
    
    if a == 13:
        return 0
    else:
        ssum += a
    
    if b == 13:
        return ssum
    else:
        ssum += b
    
    if c == 13:
        return ssum
    else:
        ssum += c
    
    # if all conditions pass, then just return the sum
    return ssum