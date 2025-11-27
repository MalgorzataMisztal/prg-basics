def f(sentence):
    sum = 0
    for i in sentence:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y':
            sum += 1
    return sum

print(f("water"))
print(f("hello world"))