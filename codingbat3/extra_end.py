def extra_end(str):
    
    if len(str) < 2:
        return 0
    
    return str[-2:] * 3

print(extra_end("Hello"))