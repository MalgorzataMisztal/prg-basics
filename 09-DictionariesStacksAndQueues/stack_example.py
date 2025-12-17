import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put('2')
cards.put('3')
cards.put('7')
cards.put('4')
cards.put('1')
cards.put('9')
cards.put('8') 

last_one = int(cards.get())
second_last = int(cards.get())
sum = last_one + second_last
print(f'Sum of the last two numbers of the stack equals {sum}')

# removes and prints elements from the top of the stack
remaining_sum = 0
while not cards.empty():
    card = int(cards.get())
    remaining_sum += card

print(f'Sum of remainig stack elements equals {remaining_sum}')
"""
Note the order of the printed elements.
The last added element is printed first.
"""
