decimal_number = int(input('Enter decimal number: '))
quotient = 1
if decimal_number > 0:
    while quotient > 0:
        quotient = decimal_number % 2
        print(quotient)
    