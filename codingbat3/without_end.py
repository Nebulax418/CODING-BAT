def without_end(str):
    
    if len(str) < 2:
        return 0
    
    return str[1:len(str)-1]

print(without_end("Hello"))