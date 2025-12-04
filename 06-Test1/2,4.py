def f(hours,minutes,seconds):
    if minutes / 60 == hours or seconds / 3600 == hours:
        return True
    else:
        return False

print(f(1,60,3600))
print(f(2,120,7200))
print(f(4,220,14400))
print(f(3,180,10600))