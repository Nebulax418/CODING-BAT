def left2(str):
    
    return str[2:]+str[:2] if len(str) > 2 else str


print(left2("Hello"))