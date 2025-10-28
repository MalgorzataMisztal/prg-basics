product_string = input('Enter product price: ')
product_discount_string = input('Enter the discount in %:')
product_price = float(product_string)
product_discount = float(product_discount_string)

discount = product_discount / 100
print(f'The product price: {product_price: .2f}, \n')
print(f'the discount is {discount: .2f}%, \n')
print(f'discounted product price {discount*product_price: .2f} ')
print(f'difference between the product price before and after the discount: {product_price - discount*product_price: .2f} ')