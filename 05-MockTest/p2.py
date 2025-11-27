def f(n1, n2, n3):
    if n1 != n2 and n2 != n3 and n1 != n3:
        return True
    else:
        return False
    
print(f(4, 8, 5))
print(f(2, 9, 2))