def factorial(n):
    if n == 0 or n ==1:
        return 1 
    else:
        return n * factorial(n-1)
    
number  = int(input("ENTER A NUMBER:"))
print(f"Factorial of {number } is {factorial(number)}")