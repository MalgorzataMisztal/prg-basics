names = ['James','Emily','William','Olivia','Benjamin','Sophia','Henry']
print('Unsorted list: ')
print(names)

names_sorted  = sorted(names, key = lambda name: len(name))

print('Sorted list: ')
print(names_sorted)