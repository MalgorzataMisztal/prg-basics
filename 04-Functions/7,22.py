def f(name):
    words = name.split()
    acronym = ""
    for i in words:
        acronym += i[0]
    return acronym

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))