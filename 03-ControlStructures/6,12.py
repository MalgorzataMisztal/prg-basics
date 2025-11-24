number_of_products = int(input('Enter the number of purchased products: '))
product_price = int(input('Enter the product price: '))
if number_of_products > 2:
    amount_to_pay = (2 * product_price) + (number_of_products - 2) * product_price * 0.75
    print(f'Amount to pay: {amount_to_pay: .2f}')
else:
    amount_to_pay = number_of_products * product_price
    print(f'Amount to pay: {amount_to_pay}')