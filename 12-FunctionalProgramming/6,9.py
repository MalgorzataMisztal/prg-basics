temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

positive_cities = list(
    map(lambda item: item[0],
        filter(lambda item: item[1] > 0, temperatures.items())))

print("Cities with positive temperatures:", " ".join(positive_cities))