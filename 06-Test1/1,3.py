def f(product_code):
    sum = 0
    fourth = int(product_code[3])
    for i in range(3):
        i = int(product_code[i])
        sum += i
    if sum % 7 == fourth:
        return True
    else:
        return False
    
print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))