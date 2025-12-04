class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    
    def print_receipt(self):
        print("Taxi ride: ")
        print(f'Distance: {self.distance} km')
        print(f'Rate per kilometer: €{self.rate_per_km}')
        print(f"Fare: {self.fare}")




def main():
    taxi1 = TaxiRide(2.0)
    taxi1.calculate_fare(4)
    taxi1.print_receipt()
    
    taxi2 = TaxiRide(3.0)
    taxi2.calculate_fare(7)
    taxi2.print_receipt()

if __name__ == "__main__":
    main()
