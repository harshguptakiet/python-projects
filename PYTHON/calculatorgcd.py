import math

def compute_gcd(x, y):
    return math.gcd(x, y)

def compute_lcm(x, y):
    return (x * y) // compute_gcd(x, y)

num1 = 54
num2 = 24

gcd = compute_gcd(num1, num2)
lcm = compute_lcm(num1, num2)

print(f"The GCD of {num1} and {num2} is {gcd}")
print(f"The LCM of {num1} and {num2} is {lcm}")
