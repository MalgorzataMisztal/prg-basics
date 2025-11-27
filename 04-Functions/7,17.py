def f(palindrome):
    backward = palindrome[::-1]
    if palindrome == backward:
        return True
    else:
        return False
    
print(f("radar"))
print(f("12-11-21"))
print(f("book"))