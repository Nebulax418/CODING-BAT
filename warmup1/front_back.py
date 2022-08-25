def front_back(str):
    
    # code for switching
    front = str[0]
    back = str[len(str)-1]
    middle = str[1:len(str)-1]
    
    # only one character
    if len(str) == 1:
        return str
    else:
        new_string = back + middle + front
        return new_string    

print(front_back("aavj"))