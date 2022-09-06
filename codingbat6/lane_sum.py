def lone_sum(a, b, c):
    
    
    # using the set method
    
    
    # using brute force    
    # if a == b == c:
    #     return 0
    # elif a == b and a != c:
    #     return c
    # elif a == c and a != b:
    #     return b
    # elif a != b and a != c:
    #     return a + b + c
    
    # just add the numbers through logic
    
    ssum = 0
    
    # three conditions
    
    # number one
    if a != b and a != c: ssum += a
    
    
    # number two
    if b != a and b != c: ssum += b
    
    
    # number 3
    if c != a and c != b: ssum += c
    
    return ssum
        

print(lone_sum(1, 3, 3))
    
    
            