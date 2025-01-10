def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  
        n = n // 10    
    return total


number = int(input("enter the number:"))
print(f"Sum of digits of {number} is {sum_of_digits(number)}")
