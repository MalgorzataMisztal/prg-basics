def f(array2D):
    n = len(array2D)
    for i in range(n):
        row_sum = sum(array2D[i])
        column_sum = 0
        for j in range(n):
            column_sum += array2D[j][i]
        if row_sum != column_sum:
            return False
    return True

if __name__ == "__main__":
    print(f([[3,7,2],[4,2,5],[5,2,1]]))
    print(f([[3,7,2],[4,2,5],[9,2,1]]))