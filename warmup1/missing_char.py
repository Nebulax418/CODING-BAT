def missing_char(str, n):
    # we cannot modify the string itself because it is immutable
    before_n = str[:n]
    after_n = str[n+1:]
    return before_n + after_n

# entire length of the string is 5 
# but we count up to 4 because it is 0 to 4
print(missing_char("Hello", 5))