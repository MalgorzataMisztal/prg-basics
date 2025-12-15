matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

number = 0
for row in matrix:
    row[number] = 1
    print(*row)
    number += 1
