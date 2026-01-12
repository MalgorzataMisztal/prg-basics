class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        first_letter = self.name[0]
        result = f"{self.surname}{first_letter}{self.seniority}"
        if self.age >= 18:
            return result.upper()
        else:
            return result.lower()
        
print(C("Anna","May",17,7))
print(C("George","Brown",21,4))