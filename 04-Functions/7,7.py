def f(amount_to_pay):
    for i in amount_to_pay:
        if i != '0' and i != '1':
            return False
    return True

print(f("101101"))
print(f("1311a10100"))