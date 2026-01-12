import random

class Thermometer:
    def __init__(self):
        self.temperature = None
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Now the thermometer is on")

    def turn_off(self):
        self.is_on = False
        print("Now the thermometer is off")

    def measure_temperature(self):
        if self.is_on == False:
            print("Firstly turn on the thermometer")
        else: 
            self.temperature = round(random.uniform(34.0, 42.0), 1)
    
    def display(self):
        if self.is_on == False:
            print("Thermometer is off")

        if self.temperature == None:
            print("No temperature measured.")
            return
        
        if self.temperature >= 41.0:
            print(f"Temperature: {self.temperature}C (CRITICAL TEMPERATURE!!)")
        elif self.temperature >= 37.0:
            print(f"Temperature: {self.temperature}C (Fever)")
        else:
            print(f"Temperature: {self.temperature}C (healthy)")

