def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

print("Temperature Conversion Program")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
choice = int(input("Enter your choice (1-3): "))
if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(c)
    print("Temperature in Fahrenheit:", result)
elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(f)
    print("Temperature in Celsius:", result)
elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    result = celsius_to_kelvin(c)
    print("Temperature in Kelvin:", result)
else:
    print("Invalid choice!")