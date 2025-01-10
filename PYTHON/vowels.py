string = "HELLOWORLD!"

def count(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

print (f"THE NUMBER OF VOWELS ARE:" ,{count(string)})
    
