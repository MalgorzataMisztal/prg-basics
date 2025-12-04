def f(number):
    if number == 0:
        return True
    if number == 1:
        return True
    if number == 2:
        return True
    a = 0
    b = 1
    new = 0
    while b < number:
        new = a + b
        a = b
        b = new
    if b == number:
        return True
    else:
        return False
    
print(f(5))
print(f(4))