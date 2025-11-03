###
# Calculation of circle area and circumference 
#

# determine radius and PI values
pi = 3.14159
radius = int(input('Enter the radius of circle: '))
# calculate area
area = pi * radius**2
# calculate circumference
circumference = 2 * pi * radius
# print results
print(f'When the circle has radius = {radius}, then area = {area: .2f} and circufenrence is {circumference: .2f}')