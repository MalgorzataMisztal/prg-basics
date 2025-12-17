def f(number):
    stack = []
    if number == 0:
        return "0"
    while number > 0:
        reminder = number % 2
        stack.append(reminder)
        number = number // 2
    binary = ""
    while len(stack) > 0:
        binary += str(stack.pop())
    return binary

num = 18
converted_num = f(num)
print("Natural number: ", num)
print("Binary number: ", converted_num)