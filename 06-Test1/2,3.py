def f(password):
    counter = {}
    if len(password) < 6:
        return False
    for i in password:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    for count in counter.values():
        if count > 1:
            return False
    return True
    


print(f('ax15'))
print(f('book123'))
print(f('A2water3'))
print(f('qwerty'))
print(f(''))