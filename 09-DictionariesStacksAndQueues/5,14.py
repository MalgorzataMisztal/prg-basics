# Write a program that supports customer service in an office. Use the
# queue. Each new customer receives a ticket with an automatically
# assigned consecutive number and is added to the end of the queue.
# The next customer to be served is taken from the beginning of the
# queue.

import queue

current_queue = queue.Queue()
new_customer = 1

def add_customer():
    global new_customer
    ticket = new_customer
    current_queue.put(ticket)
    print(f"-> Your ticket number: {ticket}. (Added to queue)")
    
    new_customer += 1

def customer():
    if not current_queue.empty():
        current_number = current_queue.get()
        print(f"<- Customer with ticket number: {current_number}")
    else:
        print("Queue is empty")

if __name__ == "__main__":
    add_customer()
    add_customer()
    print("Customer is to be served")
    customer()
    print("New customers")
    add_customer()
    print("Customer is to be served")
    customer()
    customer()
    customer()