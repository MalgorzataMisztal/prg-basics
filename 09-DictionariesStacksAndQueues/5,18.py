import json

with open("dogs.json", 'r', encoding='utf-8') as file:
    dogs = json.load(file)

for i in dogs:
    if i["age"] < 5:
        print("Name: ", i["name"], "\nbreed; ", i["breed"], "\nage: ", i["age"], "\nweight_kg: ", i["weight_kg"], "\nowner: ", i["owner"], "\nvaccinated: ", i["vaccinated"])
        print()