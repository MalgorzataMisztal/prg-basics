def f(array):
    min_value = array[0][0]
    min_row = 0
    min_col = 0
    for row_index, row in enumerate(array):
        for col_index, value in enumerate(row):
            if value < min_value:
                min_value = value
                min_row = row_index
                min_col = col_index
    if min_row == min_col:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f([[7,8],[5,3],[9,4]]))
    print(f([[7,8,5,3],[9,4,2,6]]))