countries = [
{"name":"Poland", "population":38000000},
{"name":"Tokaleu", "population":1900},
{"name":"Niue", "population":1935},
{"name":"Nauru", "population":10800},
{"name":"Andorra", "population":87500}
]

print(f"{'COUNTRY':<15} {'POPULATION'}")
for country in countries:
    print(f"{country['name']:<15} {country['population']}")