def front_times(str, n):
    front = str[:3]
    
    if len(str) < 3:
        return str * n
    else:
        return front * n
    

print(front_times("Hello", 5))