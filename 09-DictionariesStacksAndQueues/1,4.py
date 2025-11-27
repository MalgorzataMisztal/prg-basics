person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print("Name: ", person["name"])

print("Hobby: ", person["hobby"])

print(person)
print("\n")

person['surname'] = 'Nowak'
print("New surname: ", person["surname"])

person["married"] = False
print("Married: ", person["married"])

person["Gender: "] = "male"
print("Gender: ", person["Gender: "])

person["hobby"].append("bicycle")
print("Hobby: ", person["hobby"])

person["phone"]["work"] = '313131444'

print("\n")
for first, second in person.items():
    print(f"{first}: {second}")