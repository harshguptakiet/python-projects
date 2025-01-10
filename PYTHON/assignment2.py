def extract_pattern(s):
    result =[]
    lenth=len(s)
    
    for i in range(lenth-3):
        if s[i]==s[i+3-1]:
           result.append(s[i:i+3])
    return result

s = input("enter the string:")
result = extract_pattern(s)
print(result)
   
    