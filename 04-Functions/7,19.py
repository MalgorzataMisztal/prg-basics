def f(number):
    number_str = str(number)
    counter = {}
    for i in number_str:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    sum = 0
    for i, numerator in counter.items():
        if numerator > 1:
            value = int(i)
            sum += value * (numerator - 1)
    return sum

print(f(1027))
print(f(230335))
print(f(513553007))