name = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),("Jackson","Peter"),("Johnson","Rick"),("Lewis","Terry"),("Clarke","Robin")]

last_name = list(map(lambda x: f"{x[0].upper()}, {x[1]}", name))
for i in last_name:
    print(i)