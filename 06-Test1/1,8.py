def f(speed1, speed2):
    if speed2 == speed1 * 1000 / 3600:
        return True
    else:
        return False
    
print(f(36, 10))
print(f(20, 20))