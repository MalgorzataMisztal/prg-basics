import math

def f(tree_circumference):
    diameter = tree_circumference / math.pi
    if diameter >= 50:
        return True
    else:
        return False
    
print(f(200))
print(f(100))