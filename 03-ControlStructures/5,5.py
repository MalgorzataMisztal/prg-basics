###
# Sums numbers entered by user
#
total_sum = 0
count_of_numbers = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    count_of_numbers += 1

    if count_of_numbers > 0:
        arithmetic = total_sum / count_of_numbers
    else:
        arithmetic = 0

print(f"The total sum of the numbers is: {total_sum}, and arithemetic means equals {arithmetic}")