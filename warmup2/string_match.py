def string_match(a, b):
    # game plan
    
    count = 0
    
    '''
    Run for loop each time
    --> to check if a[i:i+1] == b[i:i+1] and index(a[i]) == index(b[i])
    and index(a[i+1]) == index(b[i+1])
    #'''
    
    # len(str) - 1 when using range and i
    
    '''
    
    Surprisingly python allows you to use more than one
    variable inside a for loop clause using the and keyword
    
    #'''
    for i in range(len(a)-1 and len(b) - 1):
      if a[i:i+2] == b[i:i+2]:
          count+=1
          
        
    return count  


print(string_match('xxcaazz', 'xxbaaz'))        