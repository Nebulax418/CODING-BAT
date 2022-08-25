def last2(str):
    last_two_of_string = str[-2:]
    
    # neccessary for programming in java or any other language
    if len(str) <= 2:
        return 0
    
    # reading frames str[i:some relation to i]
    
    count = 0
    
    # the range will be within 0 to len(str) - 2
    for i in range(len(str)-2):
        
        # check each reading frame
        string_to_check = str[i:i+2]
        
        if string_to_check == last_two_of_string:
            # increase the number of times it is found (not including the last 2)
            count+=1
    
    return count

print(last2("HixxxHi"))