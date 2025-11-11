###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Verify PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    requires_pin = ['1', '2', '3', '5']
    if choice in requires_pin:
        user_pin = input('Enter the PIN: ')
        if user_pin == pin:
            print('PIN verified')
        else:
            print('Incorrrect PIN. Access denied.')
            continue


    if choice == '1':
        print(f"Your current balance is: €{balance}")

    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")

    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")

    elif choice == '4':
        print('PIN checked. Proceed with transactions.')

    elif choice == '5':
        new_pin = input('Enter your new 4-digit PIN: ')
        if len(new_pin) == 4 and new_pin.isdigit():
            pin = new_pin
            print('PIN successfully changed!')
        else:
            print('Invalid PIN format. The PIN must consist of exactly 4 digits.')

    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break
    else:
        print("Invalid option. Please try again.")    
