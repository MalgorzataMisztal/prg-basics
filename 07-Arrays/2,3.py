# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements

#total expenses for each category
total_monthly_expenses_food = 0
for row in monthly_expenses:
    total_monthly_expenses_food += row[0]

total_monthly_expenses_transport = 0
for row in monthly_expenses:
    total_monthly_expenses_transport += row[1]

total_monthly_expenses_utilities = 0
for row in monthly_expenses:
    total_monthly_expenses_utilities += row[2]

#total expenses for each week
week_1 = 0
for i in monthly_expenses[0]:
    week_1 += i

week_2 = 0
for i in monthly_expenses[1]:
    week_2 += i

week_3 = 0
for i in monthly_expenses[2]:
    week_3 += i

week_4 = 0
for i in monthly_expenses[3]:
    week_4 += i

#total expenses for a month
total_month = 0
for row in monthly_expenses:
    for i in row:
        total_month += i

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',total_monthly_expenses_food)
print('Transport:',total_monthly_expenses_transport)
print('Utilities:',total_monthly_expenses_utilities)
print('Week 1:',week_1)
print('Week 2:',week_2)
print('Week 3:',week_3)
print('Week 4:',week_4)
print('---------------')
print('TOTAL:',total_month)