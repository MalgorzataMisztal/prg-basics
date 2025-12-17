with open('data.csv', 'r', encoding='utf=8') as file:
    data = file.read()

def f(value):
    lines = data.splitlines()
    count = 0
    for line in lines[1:]:
        columns = line.split(',')
        salary = float(columns[-1])
        if salary >= value:
            count += 1
    return count

if __name__ == "__main__":
    print(f(9200))
    print(f(11640))