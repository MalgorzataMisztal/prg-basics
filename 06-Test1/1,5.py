def f(a, b):
    sum = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            sum += i
        else:
            continue
    return sum

print(f(1, 6))
print(f(2, 10))