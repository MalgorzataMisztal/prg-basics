a = int(input("Enter distance in km: "))
b = int(input("Enter number of travel hours: "))
c = int(input("Enter number of travel minutes: "))

avg_speed = lambda distance,hours,minutes: distance / (hours + minutes/60)

result = avg_speed(a, b, c)

print(f"Average speed: {result: .1f} km/h")
