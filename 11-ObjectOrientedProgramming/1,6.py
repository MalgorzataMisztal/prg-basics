class Phone:
    def __init__(self, brand, battery_level):
        self.brand = brand
        self.battery_level = battery_level
        self.is_on = False

    def power_on(self):
        if self.battery_level > 0:
            self.is_on = True
            print("The phone is now ON.")
        else:
            print("Battery is empty. Cannot power on.")

    def make_call(self):
        if self.is_on and self.battery_level > 0:
            self.battery_level -= 10
            print("Making a call...")
        else:
            print("Cannot make a call. Phone is off or battery is empty.")

    def charge_phone(self, amount):
        self.battery_level += amount
        if self.battery_level > 100:
            self.battery_level = 100
        print("Phone is charging...")


# Create a smartphone object
my_phone = Phone("Samsung", 50)

# Call methods
my_phone.power_on()
my_phone.make_call()
my_phone.charge_phone(30)

# Display object properties
print("\nPhone properties:")
print("Brand:", my_phone.brand)
print("Battery level:", my_phone.battery_level)
print("Is phone on?", my_phone.is_on)