import json

with open("data.json", 'r', encoding="utf-8") as file:
    students = json.load(file)

def  f(years, course, average_grade):
    count = 0
    for student in students:
        if(
            student.get("age", 0) >= years and
            course in student.get("grades", {}) and
            student["grades"][course] >= average_grade
        ):
            count += 1
    return count