def love6(a, b):
    # use abs function to determine abs sum and abs difference    
    # use any or and here for python 3
    
    suma = a + b
    diffa = a - b
    diffb = b - a
    
    if (a == 6 or b == 6) or (suma == 6) or (diffa == 6) or (diffb == 6):
        return True
    else:
        return False