amount_string = input('Enter the amount: ')
amount = float(amount_string)
VAT = 0.23
vat_amount = amount * VAT
finish = amount + vat_amount
print(f'The amount is {amount: .2f}, ')
print(f'the vat equals {vat_amount: .2f}')
print(f'so total gross amount is {finish: .2f}')