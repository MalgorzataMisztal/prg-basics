array1 = [4,36,12,28,9,44,5]
array2 = [5,1,36]

print("Numbers from array1 that are not in array2:")

for number in array1:
    if number not in array2:
        print(number)