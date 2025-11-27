def f(detector):
    inside = 0
    outside = 0
    for i in detector:
        if i == '+':
            inside += 1
        elif i == '-':
            outside -= 1
        

    