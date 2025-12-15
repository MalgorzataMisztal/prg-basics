file_name = 'it_company.csv'


with open(file_name, 'r', encoding='utf-8') as file:
    counter = 0
    for line in file:
        print(line, end = '')
        counter += 1
        if counter == 5:
            input('Press Enter key...')
            counter = 0