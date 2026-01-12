from functools import reduce

numbers = [2, 4, 6, 3, 7, 5]

# Filter even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Sum the even numbers using reduce
sum_of_evens = reduce(lambda a, b: a + b, even_numbers)

print(sum_of_evens)