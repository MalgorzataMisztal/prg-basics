def ms_to_kmh (ms):
    result = ms * 3.6
    return result

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
abc = ms_to_kmh(a)
cde = ms_to_kmh(b)

print(f"{a}m/s contverted equals {abc}km/h")
print(f"{b}m/s contverted equals {cde}km/h")