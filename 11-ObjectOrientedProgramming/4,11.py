class C:
    def __init__(self, data):
        self.data = data

    def m1(self, s, n):
        self.data[s] = n

    def m2(self, s):
        total = 0
        for sector in s:
            if sector in self.data:
                total += self.data[sector]
        return total
    
obj = C({"A":120, "D":150, "G":90, "K":110})

obj.m1("G", 130)

print(obj.m2("GD"))
print(obj.m2("KEJ"))