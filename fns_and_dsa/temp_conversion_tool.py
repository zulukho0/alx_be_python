FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = float(input("Enter the temperature to convert: "))
conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

def convert_to_celsius(fahrenheit):
    fahrenheit = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit-32)
    print(f"{temp}°F is {fahrenheit}°C")

def convert_to_fahrenheit(celsius):
    celsius = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) +32
    print(f"{temp}°C is {celsius}°F")


if conversion.upper() == "F":
    convert_to_celsius(temp)
elif conversion.upper() == "C":
    convert_to_fahrenheit(temp)
else:
    print("Invalid temperature. Please enter a numeric value.")