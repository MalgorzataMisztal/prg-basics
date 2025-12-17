winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}

sum = 0
for x, y in winter_semester.items():
    sum += y

print("The total number of hours in the winter semester is ", sum)