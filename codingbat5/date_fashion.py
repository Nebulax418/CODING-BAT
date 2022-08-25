# ~ > . > ~

def date_fashion(you, date):
    
    '''order of the statements matter. 0 comes first'''
    
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2 
    else:
        # do this if none if statements passed
        return 1

