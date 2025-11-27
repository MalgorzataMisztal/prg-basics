def f(number, even):
    sum = 0
    number_str = str(number)
    for i in number_str:
        digit = int(i)
        if even == True:
            if digit % 2 == 0:
                sum += digit
        else:
            if digit % 2 == 1:
                sum += digit
    return sum

print(f(3124, True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))