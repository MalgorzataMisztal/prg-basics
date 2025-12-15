rec_values =[48,47,54,50,42,68,39,46]

speed = list(filter(lambda v: v > 50, rec_values))

print('Recorder values : ', rec_values)
print('Speed too high: ', speed)