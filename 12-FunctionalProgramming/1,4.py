n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))

res = lambda x: x * 3.6

result1 = res(n1)
result2 = res(n2)

print(f"{n1}m/s converted equals {result1}km/h")
print(f"{n2}m/s converted equals {result2}km/h")