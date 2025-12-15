results = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
   return lambda pts: pts>=limit

a = list(filter(min_pts(70), results))
b = list(filter(min_pts(40), results))
c = list(filter(min_pts(30), results))

print(f"Min 70 pts: {a}")
print(f"Min 40 pts: {b}")
print(f"Min 30 pts: {c}")