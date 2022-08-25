def front3(str):
    front = str[:3]
    
    if len(str) < 3:
        return 3 * str
    else:
        return front * 3

print(front3("Hello"))
    