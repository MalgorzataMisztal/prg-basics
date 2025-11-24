first = input('SURVEY Are you interested in computer science? (y/n): ')
second = input('Do you like playing computer games? (y/n): ')
third = input('Do you have an Instagram account? (y/n): ')
print ()

if first == 'y':
    first = 'Yes'
elif first == 'n':
    first = 'No'
    
print(f'SURVEY RESULTS Interested in computer science: {first}')

if second == 'y':
    second = 'Yes'
elif second == 'n':
    second = 'No'

print('Playing computer games: ', second)

if third == 'y':
    third = 'Yes'
elif third == 'n':
    third = 'No'

print('Has an Instagram account: ', third)
