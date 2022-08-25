def string_times(str, n):
    
    # convert the int to a non-negative int even if negative int is passed
    abs_n = abs(n)
    
    return str * abs_n

print(string_times("Hi", 5))