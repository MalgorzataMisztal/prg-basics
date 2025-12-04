def f(size1, size2):
    if size1 == 'S':
        size1 = 1
    elif size1 == 'M':
        size1 = 2
    elif size1 == 'L':
        size1 = 3

    if size2 == 'S':
        size2 = 1
    elif size2 == 'M':
        size2 = 2
    elif size2 == 'L':
        size2 = 3
    
    if size1 > size2:
        return 1
    elif size1 < size2:
        return 2
    elif size1 == size2:
        return 0
    
print(f("L","S"))
print(f("M","L"))
print(f("S","S"))