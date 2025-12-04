def f(x, y):
    if x == 0 or y == 0:
        return 'Error'
    elif x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 4
    elif x < 0 and y < 0:
        return 3
    elif x < 0 and y > 0:
        return 2
    
print(f(5, 2))
print(f(-5, 2))
print(f(5, -2))