import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   stack = []
   pairs = {
      ')': '(',
      '}': '{',
      ']': '['
   }
   for i in expression:
        if i in "({{":
            stack.append(i)
        elif i in ")}]":
            if not stack:
                return False
            top_element = stack.pop()
            if top_element != pairs[i]:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
         
         
   return #True if brackets in expression are ok of False otherwise

if brackets_ok(expression1):
   print(f"Expression 1 is valid: {expression1}")
else:
   print(f"Expression 1 is Invalid: {expression1}")

if brackets_ok(expression2):
    print(f"Expression 2 is valid: {expression2}")
else:
    print(f"Expression 2 is Invalid: {expression2}")

if brackets_ok(expression3):
    print(f"Expression 3 is valid: {expression3}")
else:
    print(f"Expression 3 is Invalid: {expression3}")