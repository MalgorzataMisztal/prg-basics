def avg_speed(distance, hours, minutes):
    res = distance / (hours + minutes/60)
    return res

a = int(input("Enter distance in km: "))
b = int(input("Enter number of travel hours: "))
c = int(input("Enter number of travel minutes: "))
result = avg_speed(a, b, c)

print(f"Average speed: {result: .1f} km/h")