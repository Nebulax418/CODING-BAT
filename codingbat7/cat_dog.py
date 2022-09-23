def cat_dog(str):
    
    cat_count = 0
    dog_count = 0
    
    for i in range(len(str)):
        if str[i:i+3].casefold() == "cat":
            cat_count += 1
            
        if str[i:i+3].casefold() == "dog":
            dog_count += 1
            
    
    return cat_count == dog_count

print(cat_dog("catdogcat"))