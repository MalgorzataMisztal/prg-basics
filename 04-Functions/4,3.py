###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
print(f'The area of ​​a triangle with sides {a}, {b} and {c} is {triangle_area(a,b,c)}' )
