arr = [15, 38, 7, 23, 14]
a = int(input("Number: "))
print("Array: ", *arr)

def occurs(number, array):
    if number in array:
        return f"Result: number {number} appears in the array"
    else:
        return f"Result: number {number} does not appear in the array"
    
print(occurs(a, arr))