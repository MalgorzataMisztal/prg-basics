x = int(input('Enter the x of a point on the plane: '))
y = int(input('Enter the y of a point on the plane: '))

if x == 0 and y == 0:
    print(f'Point P({x},{y} is located in the position (0,0)')
elif x == 0:
    print(f'Point P({x},{y} is located on x-axis')
elif y == 0:
    print(f'Point P({x},{y} is located on y-axis')
elif x > 0 and y > 0:
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')
elif x > 0 and y < 0:
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')
elif x < 0 and y < 0:
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')
elif x < 0 and y > 0:
    print(f'Point P({x},{y}) is in the forth quadrant of the coordinate system')

