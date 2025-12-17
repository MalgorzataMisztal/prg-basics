def reverse(text):
    stack = []
    for i in text:
        stack.append(i)
    reversed = ""
    while len(stack) > 0:
        reversed += stack.pop()
    return reversed

if __name__ == "__main__":
    user_input = input("Enter text to reverse: ")
    result = reverse(user_input)
    
    print("-" * 20)
    print(f"Original: {user_input}")
    print(f"Reversed: {result}")
    print("-" * 20)