def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius = 25
fahrenheit = 77

converted_to_fahrenheit = celsius_to_fahrenheit(celsius)
converted_to_celsius = fahrenheit_to_celsius(fahrenheit)

print(f"{celsius}°C is equal to {converted_to_fahrenheit:.2f}°F")
print(f"{fahrenheit}°F is equal to {converted_to_celsius:.2f}°C")
