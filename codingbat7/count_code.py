def count_code(str):
    
    count = 0
    
    for i in str:
        if str[i+1] == "co" and str[i+3] == "e":
            count+=1 

print(count_code("codexxxcopecoce"))   

            