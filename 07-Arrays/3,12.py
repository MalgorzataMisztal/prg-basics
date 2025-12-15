array = [2, 3, 2, 5, 8, 1, 9, 8]
print("Array:", *array)

unique_elements = []

for i in array:
    if array.count(i) == 1:
        unique_elements.append(i)

print("Unique elements:", *unique_elements)
