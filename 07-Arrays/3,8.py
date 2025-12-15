arr = [2, 6, 4, 9, 7]

def star(n):
    return "*" *n

for n in arr:
    print(f"{n}: {star(n)}")