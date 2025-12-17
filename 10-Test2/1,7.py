def f(array):
    number = 0
    for i in array:
        if len(i) >= 4 and len(i) <= 12:
            is_valid = True
            for j in i:
                if not(j.isalnum() or j.islower() or j == "_"):
                        is_valid = False
                        break
            if is_valid:
                number += 1
    return number
                

if __name__ == "__main__":
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))