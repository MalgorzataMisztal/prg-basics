arr = [15, 8, 31, 47, 2, 19]

sum = 0
count = len(arr)

for i in arr:
    sum += i

mean = sum / count

print(f"Arithmetic mean off array values: {mean: .2f}")