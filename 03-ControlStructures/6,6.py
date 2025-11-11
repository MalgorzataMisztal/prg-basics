parking_hours = int(input('Enter the number of hours of parking: '))

if parking_hours <= 2:
    print('The parking fee is 5 PLN.')
elif parking_hours <= 6:
    print('The parking fee is 15 PLN.')
else:
    print('The parking fee is 20 PLN.')