# python 3 solution {codingbat uses python2}

def cigar_party(cigars, is_weekend):
    conditions = [
        
        # either of these conditions have to be true
        is_weekend and cigars >= 40,
        not is_weekend and cigars >= 40 and cigars <= 60        
        
    ]
    
    return True if any(conditions) else False

# 50 cigars and it is the weekend
print(cigar_party(50, True))

# 30 cigars and weekend is true {return False}
print(cigar_party(30, True))