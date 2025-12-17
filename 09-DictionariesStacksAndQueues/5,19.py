import json

with open("reservations.json", 'r', encoding="utf-8") as file:
    dictionary = json.load(file)

number_of_paid_reservations = 0
number_of_unpaid_reservations = 0
value_of_paid_reservations = 0
value_of_unpaid_reservations = 0

reservation_list = dictionary["reservations"]
number_of_rooms = len(reservation_list)
for room in reservation_list:
    if room["paid"] == True:
        number_of_paid_reservations += 1
        value_of_paid_reservations += (room["price_per_night"] * room["nights"])
    else:
        number_of_unpaid_reservations += 1
        value_of_unpaid_reservations += (room["price_per_night"] * room["nights"])

print("Number of rooms: ", number_of_rooms)
print("Number of paid reservations: ", number_of_paid_reservations)
print("Number of unpaid reservations: ", number_of_unpaid_reservations)
print(f"Total value of paid reservations: {value_of_paid_reservations: .2f}")
print(f"Total value of unpaid reservations:  {value_of_unpaid_reservations: .2f}")