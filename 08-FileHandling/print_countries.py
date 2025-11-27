###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    line_number = 0
    for line in file:
        line_number += 1
        print(line_number, '. ', line, end="")