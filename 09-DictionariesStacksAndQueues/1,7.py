data = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

print("LIST OF PROODUCTS AND THE QUANTITY")
print("========================")
counter = 0
for product, quantity in data.items():
    print(f"{product}: {quantity}")
    counter += quantity

print()
print("The toal number of products in the store: ", counter)

