amount = int(input('Enter the amount in PLN: '))
fifth = 0
second = 0
first = 0
if amount >= 5:
    fifth = amount // 5
    rest = amount % 5
 rest >= 2:
        second = rest // 2
        rest = rest % 2
        while rest >= 1:
            first = rest / 1

print(f'The amount of PLN {amount} in coins:')
print(f'5 PLN coins: {fifth}')
print(f'2 PLN coins: {second}')
print(f'1 PLN coins: {first}')