def f(amount_to_pay):
    piatki = amount_to_pay // 5
    change5 = amount_to_pay % 5
    dwojki = change5 // 2
    change2 = change5 % 2
    jedynki = change2 // 1
    return piatki + dwojki + jedynki


print(f(23))
print(f(8))