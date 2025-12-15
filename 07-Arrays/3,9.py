def compare(array1, array2):
    print("Array1: ", *array1)
    print("Array2: ", *array2)

    if len(array1) != len(array2):
        return False

    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    
    return True
            
    
one = ["water","book","sky"]
two = ["water","book","sky"]

jeden = [True,False]
dwa = [True,False,True]

ein = [5,3,1]
zwei = [5,3,1]

uno = [3,2,1]
dos = [3,2]

testy = [(one, two), (jeden, dwa), (ein, zwei), (uno, dos)]

for a, b in testy:
    if compare(a, b) == True:
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are not the same")
    print()

