hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    names = ""
    for i in hotels:
        names += i["name"] + ", "
    return names[:-2]

def avg_price(hotels):
    sum = 0
    counter = 0
    for i in hotels:
        sum += i["price"]
        counter += 1
    return sum / counter

def cheaper(average1, average2):
    if average1 > average2:
        return 'Sopot'
    elif average1 < average2:
        return "Kraków"
    else:
        return "Ceny są równe"

krakow = hotel_list(hotels_in_Krakow)
average1 = avg_price(hotels_in_Krakow)
sopot = hotel_list(hotels_in_Sopot)
average2 = avg_price(hotels_in_Sopot)
cheaper_hotel = cheaper(average1, average2)

print('Hotels in Krakow: ', krakow)
print('Average hotel price in Krakow: ', average1)
print('Hotels in Sopot: ', sopot)
print('Average hotel price in Sopot: ', average2)
print('Cheaper hotels in: ', cheaper_hotel)

