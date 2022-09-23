def count_hi(str):
    
    # if any substring of length 2 is in the string then return the count
    
    count = 0
    
    for i in range(len(str)):
        if str[i:i+2] == "hi":
            count+=1
            
    
    return count

print(count_hi("abc hi ho hi"))

        