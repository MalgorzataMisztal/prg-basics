price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

value1 = 0
value2 = 0

print("LIST OF PRODUCTS AND THEIR PRICES BEFORE THE DISCOUNT")
for item, price in price_list.items():
    print(f"{item}: {price}")
    value1 += price

print(f"Total value of the products before the discount: {value1: .2f}")
print()
print("LIST OF PRODUCTS AND THEIR PRICES AFTER THE DISCOUNT")
for item, price in price_list.items():
    new_price = 0.9 * price
    print(f"{item}: {new_price: .2f}")
    value2 += new_price

print(f"Total value of the products after the discount: {value2: .2f}")