initials = lambda name,surname: name[0] + surname[0]

name = input('Enter your name: ')
surname = input('Enter your surname: ')

print(f"Initials: {initials(name, surname)}")