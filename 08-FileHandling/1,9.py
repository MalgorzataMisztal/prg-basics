###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'
counter = 0

with open(file_name, 'r') as file:
   for line in file:
      cleaned_line = line.strip()
      if job_title in cleaned_line:
        counter += 1
        print (f'{counter}. {cleaned_line}')