def calculate(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.lstrip('-').replace('.', '', 1).isdigit():
            stack.append(float(token))
        elif token in ['+', '-', '*', '/', '-']:
            if len(stack) < 2:
                return "Error: Not enough values in stack"
            val2 = stack.pop()
            val1 = stack.pop()
            result = 0
            if token == '+':
                result = val1 + val2
            elif token == '-' or token == '-':
                result = val1 - val2
            elif token == '*':
                result = val1 * val2
            elif token == '/':
                if val2 == 0:
                    return "Error: Division by zero"
                result = val1 / val2
            stack.append(result)
        elif token == '=':
            if len(stack) > 0:
                return stack.pop()
            else:
                return "Empty Stack"
    return stack[-1] if stack else "Empty"


if __name__ == "__main__":
    expressions = [
        "2 3 + =",
        "2 4 1 + * =",
        "2 3 + 4 5 + * =",
        "8 3 1 + / 3 2 – 4 + * ="]
    print(f"{'RPN Expression':<30} | {'Result'}")
    print("-" * 45)
    
    for exp in expressions:
        clean_exp = exp.replace('–', '-') 
        result = calculate(clean_exp)
        print(f"{exp:<30} | {result}")