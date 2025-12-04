# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.studentid_number = 0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.studentid_number = 123456
    student2.name = "Olivia"
    student2.age = 21
    student2.studentid_number = 987654
    student3.name = 'Basia'
    student3.age = 23
    student3.studentid_number = 123789

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, student id number: {student1.studentid_number}')
    print(f'{student2.name}, {student2.age} years old, student id number: {student2.studentid_number}')
    print(f'{student3.name}, {student3.age} years old, student id number: {student3.studentid_number}')

