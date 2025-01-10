def power(base,exponent):
    if exponent == 0:
        return 1
    else:
        return base*power(base,exponent-1)
    
base = float(input("ENTER THE BASE NUMBER:"))
exponent = int(input("ENTER THE EXPONENT:"))
result = power(base,exponent)

print(f"{base} raised to the power of {exponent} is {result}")
