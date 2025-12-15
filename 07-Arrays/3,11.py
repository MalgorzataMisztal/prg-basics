array1 = [64, 34, 25, 12, 22, 11, 90]
array2 = [5, 1, 4, 2, 8]
array3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
        
print("Original: ", array1)
print("Sorted: ", bubblesort(array1))
print("=" * 30)

print("Original: ", array2)
print("Sorted: ", bubblesort(array2))
print("=" * 30)

print("Original: ", array3)
print("Sorted: ", bubblesort(array3))
print("=" * 30)