# ever other character starting with the first

def string_bits(str):
    
    built_string = ""
    
    for i in range(0, len(str), 2):
        built_string+=str[i]
    
    return built_string

print(string_bits("Hello"))
    