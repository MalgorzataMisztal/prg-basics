def f(sentence):
    sum = 0
    for i in sentence:
        i = ord(i)
        i - int(i)
        sum += i
    if sum % 3 == 0:
        return True
    else:
        return False
        
print(f("hello world"))
print(f("university"))
print(f("student"))