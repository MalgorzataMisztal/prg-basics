def f(subjects):
    averages = {}
    for subject_name, grades_list in subjects.items():
        average = sum(grades_list) / len(grades_list)
        averages[subject_name] = average
    return max(averages, key=averages.get)
    
if __name__ == "__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))