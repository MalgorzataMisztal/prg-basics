class Bank:
    def __init__(self, no_account):
        self.no_account = no_account
        self.balance = 0

    def deposit(self, amount1):
        self.amount1 = amount1
        self.balance += amount1

    def withdraw(self, amount2):
        self.amount2 = amount2

        if amount2 > self.balance:
            print("Insufficient funds on the account")
            print("-" * 30)
        else:
            self.balance -= amount2

    def display_balance(self):
        print(f"Balance: {self.balance: .2f}PLN")
        print("-" * 30)

    def display_informations(self):
        print(f"Bank Account No: {self.no_account}")
        print(f"Balance: {self.balance: .2f}PLN")
        print("-" * 30)


if __name__ == ("__main__"):
    bank_account = Bank("12 3456 5555 9090 1111 0000 7722")
    bank_account.display_balance()
    bank_account.deposit(25.30)
    bank_account.display_balance()
    bank_account.withdraw(31.70)
    bank_account.display_balance()
    bank_account.withdraw(14)
    bank_account.display_informations()