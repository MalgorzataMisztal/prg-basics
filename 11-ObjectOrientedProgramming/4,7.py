class Statistics:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)
    
    def display(self):
        print("Numbers:", " ".join(str(n) for n in self.numbers))

    def max(self):
        return max(self.numbers)

    def min(self):
        return min(self.numbers)

    def mean(self):
        return sum(self.numbers) / len(self.numbers)
    
    def median(self):
        sorted_numbers = sorted(self.numbers)
        mid = len(sorted_numbers) // 2

        if len(sorted_numbers) % 2 == 1:
            return sorted_numbers[mid]
        else:
            return (sorted_numbers[mid - 1] + sorted_numbers[mid + 1]) / 2
        
    def print_statistics(self):
        print("Minimum: ", self.min())
        print("Maximum: ", self.max())
        print("Arithmetic Mean:", self.mean())
        print("Median:", self.median())


statistics = Statistics()
data = [12, 37, 6, 9, 17]

for num in data:
    statistics.add_number(num)

statistics.display()
statistics.print_statistics()