format24 = input('Enter time (24-hour format): ')
hours = int(format24[0:2])
minutes = format24[3:5]

if hours >= 1 and hours <= 11:
    print(f'Time in 12-hour format: {hours}:{minutes}am')
elif hours == 0:
    hours += 12
    print(f'Time in 12-hour format: {hours}:{minutes}am')
elif hours == 12:
    print(f'Time in 12-hour format: {hours}:{minutes}pm')   
elif hours >= 13 and hours <= 23:
    hours = hours - 12
    print(f'Time in 12-hour format: {hours}:{minutes}pm')

