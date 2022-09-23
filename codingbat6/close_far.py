def close_far(a, b, c):
    
    diffab = abs(a - b)
    diffac = abs(a - c)
    diffbc = abs(b - c)
    
    if diffab <= 1 and diffac >= 2 and diffbc >= 2:
        return True
    
    if diffac <= 1 and diffab >= 2 and diffbc >= 2:
        return True
    
    return False 

print(2, 1, 4)
    