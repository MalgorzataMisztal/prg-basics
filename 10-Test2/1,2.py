def f(arr):
    different = {}

    for i in arr:
        if i in different:
            different[i] +=1
        else:
            different[i] = 1

    for number, count in different.items():
        if count == 1:
            return number
        
if __name__ == "__main__":
    print(f([7,7,7,7,7,5,7,7]))