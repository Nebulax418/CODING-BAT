def string_sploison(str):
    built_string = ""
    
    for i in range(len(str)):
        # [0:i+1]
        built_string += str[:i+1]        
    
    return built_string

print(string_sploison("abc"))
            