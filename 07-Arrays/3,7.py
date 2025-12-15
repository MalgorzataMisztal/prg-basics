names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
print(names)

longest_name = names[0]
for i in names:
    if len(i) > len(longest_name):
        longest_name = i

print("Longest name: ", longest_name)