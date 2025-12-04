def f(a, b):
    sum = 0
    c = 0
    d = 1
    new = 0
    for i in range(a, b + 1):
        if i == 0:
            continue
        if i == 1:
            continue
        if i == 2:
            sum +=1
        if i > 2:
            new = c + d
            sum += new
            c = d
            d = new
    return sum

print(f(1, 5))
print(f(6, 21))