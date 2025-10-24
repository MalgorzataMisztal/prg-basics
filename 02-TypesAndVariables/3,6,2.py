import math

height = float(input('Enter your height in meters: '))
d = 3.57 * math.sqrt(height + 20)
print('Your distance to the horizon in kilometers: ', d)
