def f(palindome):
    backward = palindome[::-1]
    if palindome == backward:
        return True
    else:
        return False
    
print(f("radar"))
print(f("12-11-21"))
print(f("book"))