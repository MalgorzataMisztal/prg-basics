from contact import Contact

class Contact_List:
    def __init__(self):
        self.contacts = []

    def add_contact(self, number):
        self.contacts.append(number)

    def display(self):
        print("Contact List")
        for contact in self.contacts:
            print(contact)