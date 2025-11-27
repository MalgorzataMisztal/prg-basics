def f(number1,number2,number3):
    if number3 == '+':
        return number1 + number2
    elif number3 == '-':
        return number1 - number2
    elif number3 == '*':
        return number1 * number2
    elif number3 == '**':
        return number1 ** number2
    elif number3 == '%':
        return number1 % number2
    
print(f(2,3, "+"))
print(f(2,3, "%"))
print(f(2,3, "**"))
print(f(2,3, "*"))
print(f(2,3, "-"))