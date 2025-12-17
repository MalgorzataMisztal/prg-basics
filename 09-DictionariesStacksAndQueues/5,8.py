# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Calculate total cost
total_cost = 0
for product in cart:
    if product in prices:
        total_cost += prices[product] * cart[product]

print("the total cost of a shopping cart: ", total_cost)