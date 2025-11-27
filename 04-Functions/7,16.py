def f(n):
    if n <= 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    a = 0
    b = 1
    for i in range(3, n + 1):
        next = a + b
        a = b
        b = next
    return b

print(f(5))
print(f(9))