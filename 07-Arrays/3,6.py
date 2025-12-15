arr = [15, 8, 31, 47, 2, 19]

i = 0
sum = 0
count = len(arr)

while i < count:
    sum += arr[i]
    i += 1

mean = sum / count

print(f"Arithmetic mean off array values: {mean: .2f}")