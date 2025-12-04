def f(student1, student2):
    student1 = student1.replace(',', '')
    student2 = student2.replace(',', '')
    sum1 = 0
    sum2 = 0
    counter1 = 0
    counter2 = 0
    for i in student1:
        i = int(i)
        sum1 += i
        counter1 += 1
    first = sum1 / counter1
    
    for i in student2:
        i = int(i)
        sum2 += i
        counter2 += 1
    second = sum2 / counter2
    
    if first > second:
        return '1'
    elif second > first:
        return '2'
    elif first == second:
        return '0'
    
print(f("3,4,5", "4,3"))
print(f("3,4,5", "5,5,4,5"))
print(f("3,4,5,4", "4,4"))