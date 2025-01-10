string = "HELLOWORLD!"

def countv(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count = count+1
    return count
print(countv(string))



    
    
