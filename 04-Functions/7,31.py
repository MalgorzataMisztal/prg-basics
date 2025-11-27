def power(x, n):
    if n == 0:
        return 0
    else:
        return x*(x**(n - 1))
    
print(power(5, 3))