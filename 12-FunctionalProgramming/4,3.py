grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

grades1 = list(filter(lambda i: i > 2.0, grades))
total_sum = sum(grades1)
count = len(grades1)

if count > 0:
    mean = total_sum / count
    result = f"Arithmetic mean for grades <> 2.0 is {mean:.2f}"
else:
    result = 'You do not have grades'

print(result)