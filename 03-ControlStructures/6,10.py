dog_age = int(input("Enter you dog's age in human years: "))

if dog_age <= 2:
    dog_age = dog_age * 10.5
else:
    dog_age = (dog_age - 2) * 4 + 2 * 10.5

print(f"The dog's age in dog's years is {dog_age} years")