name = input('Enter the name: ')

if name and name.endswith('a'):
    print(f'{name} -- Polish female name')
else:
    print(f'{name} -- Not classified as a typical Polish female name')