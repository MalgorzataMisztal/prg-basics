###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
temp = int(input('Enter the temperature in degrees Celsius: '))
k = temp + 273.15
f = temp * 9 / 5 + 32

print(f'Temperature in degrees Celsius: {temp}, in Kelvin: {k} and in Fahrenheit: {f}.')