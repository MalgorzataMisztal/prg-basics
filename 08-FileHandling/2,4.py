###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(position_file, 'w') as new:   
    with open(employees_file, 'r') as file:
        for line in file:
            cleaned_line = line.strip()
            if job_title in cleaned_line:
                new.write(cleaned_line + '\n')
            if cleaned_line == '':
                continue

print('success.') 