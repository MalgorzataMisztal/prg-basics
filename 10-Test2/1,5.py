with open("data.txt", 'r', encoding = 'utf-8') as file:
    data = file.read()

def f(first_letter, last_letter):
    words = data.lower().split()
    counter = 0
    for i in words:
        i = i.strip(".,?!:;")
        if len(i) > 0:    
            if i[0] == first_letter and i[len(i) - 1] == last_letter:
                counter += 1
    return counter

if __name__ == "__main__":
    print(f("w", "d"))