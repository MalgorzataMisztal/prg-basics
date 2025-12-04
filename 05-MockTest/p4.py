def f(card_number):
    return card_number[0:2] + '**********' + card_number[12:16]


print(f("5290312400019022"))