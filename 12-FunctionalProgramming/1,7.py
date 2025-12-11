is_even = lambda number: number % 2 

a = int(input("Enter the number: "))

if is_even(a) == 0:
    print('Number is even')
else:
    print('Number is odd')