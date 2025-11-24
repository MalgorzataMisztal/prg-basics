current_price = float(input('Enter the current price: '))
previous_price = float(input('Enter the previous price: '))
reduction = current_price / previous_price
reduction_percentage = (1 - reduction) * 100
if reduction <= 0.90:
    print('Buy the product!')
    print(f'Product price reduced by {reduction_percentage: .0f}%')
else :
    print("You shouldn't buy this product ")