def f(binary_number):
    for i in binary_number:
        if i != '1' and i != '0':
            return False
    return True

print(f("101101"))
print(f("1311a10100"))