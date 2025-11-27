def f(amount_to_pay):
    sum = 0
    fifth = amount_to_pay // 5
    sum += fifth
    second = (amount_to_pay % 5) // 2
    sum += second
    change = (amount_to_pay % 5) % 2
    first = change // 1
    sum += first
    return sum

print(f(23))
print(f(8))
print(f(2))
print(f(0))